from src.usecases.errors.invalidPasswordError import InvalidPasswordError
from src.usecases.errors.nonExistsPasswordError import NonExistsPasswordError

class GeneratePassword:

    def __init__(self, userPasswordRepository, generatePasswordValueService, encryptionService):
        self.userPasswordRepository = userPasswordRepository
        self.generatePasswordValueService = generatePasswordValueService
        self.encryptionService = encryptionService

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

        cryptPassword = self.encryptionService.encrypt(value)
        newPassword = self.userPasswordRepository.create(remaingQueries, expirationTime, cryptPassword)
        if not newPassword:
            raise NonExistsPasswordError()

        # if not self.validatePasswordService.check(password):
        #     raise InvalidPasswordError()

        return newPassword