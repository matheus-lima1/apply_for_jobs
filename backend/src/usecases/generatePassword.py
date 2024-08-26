from src.usecases.errors.invalidPasswordError import InvalidPasswordError
from src.usecases.errors.nonExistsPasswordError import NonExistsPasswordError

class GeneratePassword:

    def __init__(self, userPasswordRepository, generatePasswordValueService, encryptionService, validatePasswordService):
        self.userPasswordRepository = userPasswordRepository
        self.generatePasswordValueService = generatePasswordValueService
        self.encryptionService = encryptionService
        self.validatePasswordService = validatePasswordService

    def perform(self, remaingQueries, expirationTime, policies, minLength, passwordAlreadyGenerated):
        if passwordAlreadyGenerated:
            if self.validatePasswordService.validatePolicies(passwordAlreadyGenerated, policies, minLength):
                value = passwordAlreadyGenerated
            else:
                raise InvalidPasswordError() 
        else:
            value = self.generatePasswordValueService.generate(policies, minLength)

        cryptPassword = self.encryptionService.encrypt(value)
        newPassword = self.userPasswordRepository.create(remaingQueries, expirationTime, cryptPassword)
        if not newPassword:
            raise NonExistsPasswordError()

        return newPassword
