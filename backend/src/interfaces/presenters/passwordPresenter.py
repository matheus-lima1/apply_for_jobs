from flask import jsonify, make_response

class PasswordPresenter:
    @staticmethod
    def presentGetPassword(password):
        return make_response(jsonify({'password': password}), 200)

    @staticmethod
    def presentGeneratedPassword(new_password):
        return make_response(jsonify({'id': new_password}), 200)

    @staticmethod
    def presentError(error):
        return make_response(jsonify({"message": str(error)}), 400)
    
    @staticmethod
    def presentCustomError(error, statusCode):
        response = {
            "message": str(error)
        }
        return make_response(jsonify(response), statusCode)
