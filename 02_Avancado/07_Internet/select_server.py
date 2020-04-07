"""
Threads não rodam realmente em paralelo a não ser que você tenha vários CPUs, o que realmente acontece é que o sistema operacional escolhe entre as tarefas a serem executadas aquela a ser executada, e vai trocando entre as threads. O seu sistema operacional faz isso tão rápido que você tem a ilusão de que as threads estão sendo executadas em paralelo. Esse processo é chamado de multiplexing

Porém podemos fazer o python selecionar as tarefas a serem executadas até todas serem completadas. Servidores podem aplicar essa técnica para lidar com múltiplos clientes ao mesmo tempo sem utilizar threads ou forks

Para fazer isso usamos o módulo select da biblioteca padrão, vamos realizar o multiplexing sem uso de nada do sistema operacional.

Esse servidor irá lidar com múltiplos clientes em paralelo com o select. Usar select para manualmente lidar com um conjunto de sockets: Socket principais que aceitam novas conexões, e sockets de input conectadas para aceitar clientes.
"""

# Importar o select e o socket
from select import select
from socket import socket, AF_INET, SOCK_STREAM
import time

def now():
    return time.ctime(time.time())

# Configurações do servidor
server_host = 'localhost'
server_port = 5000

# Número de sockets usados
socket_number = 2

# Lista de sockets criados por função de cada socket
main_socket = []
read_socket = []
write_socket = []

# Cria um socket pada cada função
for i in range(socket_number):
    # Configura um socket TCP/IP
    connection_socket = socket(AF_INET, SOCK_STREAM)
    
    # Configura o socket
    connection_socket.bind((server_host, server_port))
    connection_socket.listen(5)
    
    # Adiciona a lista de sockets principais e leitores
    main_socket.append(connection_socket)
    read_socket.append(connection_socket)
    
    # Aumenta o valor da porta para mudar o próximo socket
    server_port += 1
    
def run():
    print("Loop de seleção de socket iniciado!")
    
    while True:
        # Vemos todos os sockets legíveis e escrevíveis e os selecionamos
        readable_socket, writeable_socket, exceptions = select(read_socket, write_socket, [])
        
        # Para cada socket legível
        for socket_object in readable_socket:
            # Se ele é um socket principal
            if socket_object in main_socket:
                # Aceita o socket
                connection_socket, ip_address = socket_object.accept()
                # Imprime as conexões
                print("Conecta:", ip_address, id(connection_socket))
                # E o coloca no socket de leitura
                read_socket.append(connection_socket)
            else:
                # Lemos o que está no socket
                data = socket_object.recv(1024)
                
                # Imprime a mensagem recebida
                print("\tRecebeu", data, "em", id(socket_object))
                
                # Se não recebermos nada
                if not data:
                    # Fechamos o socket
                    socket_object.close()
                    # E o removemos do socket de leitura
                    read_socket.remove(socket_object)
                else:
                    # Preparamos uma resposta para ser enviado
                    answer = 'Resposta eco => %s as %s' % (data, now())
                    socket_object.send(answer.encode())

if __name__ == '__main__':
    run()