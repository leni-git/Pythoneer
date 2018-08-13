import socket
from time import sleep

HOST = '127.0.0.1'
RECORDER_PORT = 5555

RECODER_ADDR = (HOST, RECORDER_PORT)

FILE_HEADER_SIZE = 44
FILE_READ_SIZE = 8192
BUF_SIZE = 1024

client_recoder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_recoder.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_recoder.connect(RECODER_ADDR)

while True:
    client_recoder.send('hi'.encode())
    sleep(10)
    send_data = client_recoder.recv(1024)
    print('{}'.format(send_data.decode()))
# f = open('1channel_mono.raw', 'rb')
# while True:
#     data = f.readline()
#     print("data type >> {}".format(data))
#
#     if len(data) == 0:
#         client_recoder.send('end'.encode())
#         break
#     client_recoder.send(data)