from flask import Flask, jsonify, make_response, request

app = Flask(__name__)



@app.route('/teste/<string:name>')
def teste(name):
    return make_response(jsonify(
        {
            'message': 'Teste ' + name
        }), 200)

@app.route('/teste', methods=['POST'])
def create():
    name = request.json.get('name')

    if not name:
        return make_response(jsonify({
            'message': 'Campo "name" é obrigatório'
        }), 400)
    
    return make_response(jsonify({
        'message': 'Teste ' + name
    }), 200)