"""
Contextualizando, o servidor pode está em um aplicativo só escutando se o dispositivo (raspberry) envia algum sinal de alerta ou bateria. Assim que envia ele vai retornar para a rasp que recebeu a mensagem.
"""

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def connect():
    """
    Disparado assim que o lado cliente se conectar ao servidor.
    client.connect(url)
    """

    print('Cliente Conectado')
    
@socketio.on('alert')
def handle_message(message):
    """
    Disparado assim que o cliente envia
    uma mensagem para o servidor de "alert"
    """

    print('Mensagem recebida: ' + str(message))
    emit('feedback', {"retorno": True}, broadcast=True)
    
@socketio.on('batery')
def handle_batery(message):
    """
    Disparado assim que o cliente envia
    uma mensagem para o servidor de "batery"
    """

    print('Nível de bateria: ' + str(message))
    emit('feedback', {"retorno": True}, broadcast=True)
    
@socketio.on('disconnect')
def disconnect():
    """
    Disparado assim que o lado cliente se desconecta do servidor.
    cliente.disconnect()
    """

    print("Cliente Desconectado")
    
# Rodar o servidor
socketio.run(app, debug=True, host="0.0.0.0", port=3000)