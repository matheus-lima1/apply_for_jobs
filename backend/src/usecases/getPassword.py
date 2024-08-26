from src.usecases.errors.invalidPasswordError import InvalidPasswordError
from src.usecases.errors.nonExistsPasswordError import NonExistsPasswordError

class GetPassword:

    def __init__(self, userPasswordRepository, validatePasswordService, manipulatePasswordService, encryptionService):
        self.userPasswordRepository = userPasswordRepository
        self.validatePasswordService = validatePasswordService
        self.manipulatePasswordService = manipulatePasswordService
        self.encryptionService = encryptionService

    def perform(self, passwordId):
        password = self.userPasswordRepository.findById(passwordId)
        
        if not password:
            raise NonExistsPasswordError()

        if not self.validatePasswordService.checkHealth(password):
            self.manipulatePasswordService.destroy(passwordId)
            raise InvalidPasswordError()

        
        self.manipulatePasswordService.decrement(passwordId)
        return self.encryptionService.decrypt(password.get('value').get('S'))
