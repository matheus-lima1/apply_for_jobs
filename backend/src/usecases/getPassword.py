from src.usecases.errors.invalidPasswordError import InvalidPasswordError
from src.usecases.errors.nonExistsPasswordError import NonExistsPasswordError

class GetPassword:

    def __init__(self, userPasswordRepository, validatePasswordService, decrementRemainingQueriesService):
        self.userPasswordRepository = userPasswordRepository
        self.validatePasswordService = validatePasswordService
        self.decrementRemainingQueriesService = decrementRemainingQueriesService

    def perform(self, passwordId):
        password = self.userPasswordRepository.findById(passwordId)
        if not password:
            raise NonExistsPasswordError()

        if not self.validatePasswordService.check(password):
            raise InvalidPasswordError()

        self.decrementRemainingQueriesService.decrement(passwordId)
        return password.get('value').get('S')
        # return self.userPasswordRepository.decryptPassword(password)