from src.usecases.errors.invalidPasswordError import InvalidPasswordError
from src.usecases.errors.nonExistsPasswordError import NonExistsPasswordError

class GetPassword:

    def __init__(self, userPasswordRepository, validatePasswordService):
        self.userPasswordRepository = userPasswordRepository
        self.validatePasswordService = validatePasswordService

    def perform(self, passwordId):
        password = self.userPasswordRepository.findById(passwordId)
        if not password:
            raise NonExistsPasswordError()

        # if not self.validatePasswordService.check(password):
        #     raise InvalidPasswordError()

        return password
        # return self.userPasswordRepository.decryptPassword(password)