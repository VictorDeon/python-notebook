from flask import Flask, jsonify, request, render_template
from exception import CustomException
app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Mostra uma mensagem no navegador.
    """

    return 'Hello, World!'


@app.route('/template')
@app.route('/template/<context>')
def template(context=None):
    """
    Renderiza uma página html com o template passado.
    """
    
    return render_template('internet.html', context=context)


@app.route('/get', methods=['GET'])
def get_method():
    """
    Realiza uma requisição do tipo GET.
    """

    return jsonify([
        {"title": "C"},
        {"title": "C++"},
        {"title": "Java"},
        {"title": "Python"},
        {"title": "Javascript"},
    ])


@app.route('/data', methods=['POST', 'PUT', 'PATCH', 'DELETE'])
def data_method():
    """
    Realiza uma requisição do tipo POST.
    """
    
    data = request.get_json()

    if not data:
        raise CustomException("Não foi informado nenhum dado.")
        
    return jsonify(data)


@app.errorhandler(CustomException)
def handle_invalid_data(error):
    """
    Faz com que a requisição retorne
    uma exceção em formato JSON caso ocorra.
    """
    
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="8080")