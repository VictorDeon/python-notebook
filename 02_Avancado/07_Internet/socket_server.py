"""
Lado do servidor abre um TCP/IP em uma porta, espera uma mensagem de um cliente, e manda essa mensagem de volta como resposta. Esse é uma simples ouve/responde conversação por cliente, mas percorre um loop infinito para ouvir por mais clientes enquanto o script do servidor estiver rodando. O cliente pode rodar em outra máquina ou no mesmo computador se usa o localhost como servidor.


"""

# Importa tudo do modulo socket
from socket import *

# Criar o nome do host (servidor que recebe os pedidos do cliente)
# String vazia diz que o endereço do servidor é o localhost ou 0.0.0.0 ou 127.0.0.1
server_host = 'localhost'

# Criar o número da porta
server_port = 5000

# 1° argumento: Equivale a família de endereços, no caso AF_INET é o protocolo de endereço IP
# 2° argumento: É o protocolo de transferência TCP, no caso temos a stream (SOCK_STREAM) e o datagram (SOCK_DGRAM)
# IP: Tem uma rede que equivale ao CEP da rua e o host que equivale ao predio
# TCP: É o número do apartamento do predio especificado no IP, temos também o UDP
# Uma requisição(carta) precisa do IP(CEP, predio) e do TCP(número do apartamento) para chegar ao cliente(destinatário).
# Objecto socket com a combinação servidor TCP/IP
server_socket = socket(AF_INET, SOCK_STREAM)

# Vincula o servidor ao endereço e o número da porta
server_socket.bind((server_host, server_port))

# O socket/servidor começa a esperar por clientes limitando a 5 conexões por vez
server_socket.listen(5)

def receive():
    while True:
        # Aceita uma conexão quando encontrada e devolve a
        # um novo socket(conexão) e o endereço do cliente conectado
        conection, address = server_socket.accept()
        print('Server conectado por', address)
    
        while True:
            # Recebe dados enviada pelo cliente (1024 bytes de informação)
            data = conection.recv(1024)
            
            # Se não receber nada paramos o loop
            if not data: break
                
            # O servidor manda de volta um resposta
            conection.send(b'Resposta => ' + data)
            
        # Fecha a conexão criada depois de responder o cliente
        conection.close()
        
if __name__ == '__main__':
    receive()