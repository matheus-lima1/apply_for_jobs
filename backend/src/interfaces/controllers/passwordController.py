from flask import request
from src.interfaces.presenters.passwordPresenter import PasswordPresenter
from src.usecases.errors.nonExistsPasswordError import NonExistsPasswordError
from src.usecases.errors.invalidPasswordError import InvalidPasswordError
from src.usecases.errors.unavailablePasswordError import UnavailablePasswordError

class PasswordController:
    def __init__(self, getPasswordUsecase, generatePasswordUsecase):
        self.getPasswordUsecase = getPasswordUsecase
        self.generatePasswordUsecase = generatePasswordUsecase

    def getPassword(self, id):
        try:
            password = self.getPasswordUsecase.perform(id)
            return PasswordPresenter.presentGetPassword(password)
        
        except UnavailablePasswordError as error:
            return PasswordPresenter.presentCustomError(error, 404)
        except NonExistsPasswordError as error:
            return PasswordPresenter.presentCustomError(error, 404)
        except Exception as error:
            return PasswordPresenter.presentError(error)

    def generatePassword(self):
        data = request.get_json()
        remaingQueries = data.get('maxAttempts')
        expirationTime = data.get('availabilityTime')
        policies = data.get('policies')
        minLength = data.get('minLength')
        passwordAlreadyGenerated = data.get('password')

        print(data)
        try:
            newPassword = self.generatePasswordUsecase.perform(remaingQueries, expirationTime, policies, minLength, passwordAlreadyGenerated)
            return PasswordPresenter.presentGeneratedPassword(newPassword)
        
        except NonExistsPasswordError as error:
           return PasswordPresenter.presentCustomError(error, 404)
        
        except Exception as error:
            return PasswordPresenter.presentError(error)
