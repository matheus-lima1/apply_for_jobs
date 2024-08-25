from flask import Flask, jsonify, make_response, request
from src.usecases.getPassword import GetPassword
from src.usecases.generatePassword import GeneratePassword
from src.usecases.ports.userPasswordRepository import UsersPasswordRepository
from src.usecases.ports.validatePasswordService import ValidatePasswordService
from src.usecases.ports.generatePasswordValueService import GeneratePasswordValueService
from src.usecases.ports.manipulatePasswordService import ManipulatePasswordService


app = Flask(__name__)

@app.route('/password/<string:id>')
def getPassword(id):
    userPasswordRepository = UsersPasswordRepository()
    validatePasswordService = ValidatePasswordService(userPasswordRepository)
    manipulatePasswordService = ManipulatePasswordService(userPasswordRepository)
    getPassword = GetPassword(userPasswordRepository, validatePasswordService, manipulatePasswordService)
    try:
        password = getPassword.perform(id)

        return make_response(jsonify({
            'data': password
        }), 200)
    except Exception as error:
        return make_response(jsonify({
            "message": str(error)
        }), 400)

@app.route('/password', methods=['POST'])
def generatePassword():
    data = request.get_json()

    userPasswordRepository = UsersPasswordRepository()
    generatePasswordValueService = GeneratePasswordValueService()
    generatePassword = GeneratePassword(userPasswordRepository, generatePasswordValueService)
    try:
        newPassword = generatePassword.perform(data)

        return make_response(jsonify({
            'data': newPassword
        }), 200)
    except Exception as error:
        return make_response(jsonify({
            "message": str(error)
        }), 400)




@app.route('/teste/<string:name>')
def teste(name):
    return make_response(jsonify(
        {
            'message': 'Hello ' + name
        }), 200)

@app.route('/teste', methods=['POST'])
def create():
    name = request.json.get('name')

    if not name:
        return make_response(jsonify({
            'message': 'Campo "name" é obrigatório'
        }), 400)

    return make_response(jsonify({
        'message': 'Hello ' + name
    }), 200)



@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)