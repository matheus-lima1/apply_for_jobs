from src.usecases.errors.invalidPasswordError import InvalidPasswordError
from src.usecases.errors.nonExistsPasswordError import NonExistsPasswordError

class GeneratePassword:

    def __init__(self, userPasswordRepository, generatePasswordValueService):
        self.userPasswordRepository = userPasswordRepository
        self.generatePasswordValueService = generatePasswordValueService

    def perform(self, data):
        remaingQueries = data.get('maxAttempts')
        expirationTime = data.get('availabilityTime')
        policies = data.get('policies')
        minLength = data.get('minLength')
        passwordAlreadyGenerated = data.get('password')

        if passwordAlreadyGenerated:
            value = passwordAlreadyGenerated
        else:
            value = self.generatePasswordValueService.generate(policies, minLength)

        newPassword = self.userPasswordRepository.create(remaingQueries, expirationTime, value)
        if not newPassword:
            raise NonExistsPasswordError()

        # if not self.validatePasswordService.check(password):
        #     raise InvalidPasswordError()

        return newPassword
        # return self.userPasswordRepository.decryptPassword(password)