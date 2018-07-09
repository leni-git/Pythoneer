import socket


HOST = ''
PORT = 10003
ADDR = (HOST, PORT)
BUFF_SIZE = 1024

clientSocket = socket.socket()
clientSocket.connect(ADDR)

for i in range(10):
    data = clientSocket.recv(BUFF_SIZE)
    print('{}'.format(data.decode()))

