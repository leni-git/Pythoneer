import socket
import struct
from time import sleep

HOST = ''
PORT = 5555
ADDR = (HOST, PORT)

timeout = 2

are_you_send_off = False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(ADDR)
sock.listen(5)
client, ip = sock.accept()

client.settimeout(1)
#
# sec = 0
# usec = 500000
# timeval = struct.pack('ll', sec, usec)
# client.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeval)

while True:
    try:
        data = client.recv(1024)
        data = data.decode()
        print('data >> {}'.format(data))
        if data == 'end':
            break
        sleep(5)
        data = client.send('here_off'.encode())
    except socket.timeout as e:
        if not are_you_send_off:
            print('off 보냄 >> {}'.format(e))
            client.send('off'.encode())
            are_you_send_off = True

    if are_you_send_off:
        try:
            data = client.recv(1024)
            data = data.decode()
            print('data >> {}'.format(data))

        except:
            print('이거 안됨')
        else:
            print('try가 참일 경우 동작')
            are_you_send_off = False