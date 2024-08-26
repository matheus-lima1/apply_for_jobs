from flask import Flask
from flask_cors import CORS

from src.interfaces.controllers.passwordController import PasswordController

from src.usecases.getPassword import GetPassword
from src.usecases.generatePassword import GeneratePassword

from src.repositories.userPasswordRepository import UsersPasswordRepository
from src.services.validatePasswordService import ValidatePasswordService
from src.services.generatePasswordValueService import GeneratePasswordValueService
from src.services.manipulatePasswordService import ManipulatePasswordService
from src.services.encryptionService import EncryptionService


app = Flask(__name__)
CORS(app)

userPasswordRepository = UsersPasswordRepository()
validatePasswordService = ValidatePasswordService(userPasswordRepository)
generatePasswordValueService = GeneratePasswordValueService(validatePasswordService)
manipulatePasswordService = ManipulatePasswordService(userPasswordRepository)
encryptionService = EncryptionService()

getPasswordUseCase = GetPassword(userPasswordRepository, validatePasswordService, manipulatePasswordService, encryptionService)
generatePasswordUseCase = GeneratePassword(userPasswordRepository, generatePasswordValueService, encryptionService, validatePasswordService)

passwordController = PasswordController(getPasswordUseCase, generatePasswordUseCase)

@app.route('/password/<string:id>', methods=['GET'])
def get_password(id):
    return passwordController.getPassword(id)

@app.route('/password', methods=['POST'])
def generate_password():
    return passwordController.generatePassword()