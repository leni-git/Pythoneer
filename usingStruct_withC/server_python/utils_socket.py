import socket
import struct

# from typing import NamedTuple
#
# class STRUCT_VALUE(NamedTuple):
#   int_value: int
#   string_value: str

HOST = ''
PORT = 4000
BUFF_SIZE = 1024
ADDR = (HOST, PORT)

def socket_connect():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(ADDR)
    server_socket.listen(10)

    try:
        accepted_client, ip = server_socket.accept()
        print("accpted client: {}".format(ip))
    except:
        return False

    return accepted_client

def socket_write(accepted_client, text):
    try:
        accepted_client.send(text.encode())
    except:
        return False

    return True

def socket_read(accepted_client):
    try:
        text = accepted_client.recv(BUFF_SIZE)
        print("client text: {}".format(type(text)))
        print("client text: {}".format(text.decode()))
    except:
        return False

    return True

def socket_read_struct(accepted_client):
    try:
        temp = accepted_client.recv(BUFF_SIZE)
        print("client temp struct text: {}".format(temp))
        print("client temp struct text size: {}".format(len(temp)))

        print("")

        test_leni = struct.unpack('I20s',temp)
        print("client struct int: {}".format(test_leni[0]))
        print("client struct string: {}".format(test_leni[1]))
        # unicode_test = str(test_leni[1], 'ascii').encode('utf-8')
        # print("client struct string decode: {}".format(unicode_test.decode()))
        print("client struct string decode: {}".format(test_leni[1].decode()))
        # str = unicode(test_leni[1], errors='ignore')
        print("client struct int: {}".format(str))
        #
        # int_text = struct.unpack('I', temp[:4])
        # print("client struct int: {}".format(int_text[0]))
        # print("client int_text struct text size: {}".format(len(temp[:4])))
        #
        # print("")
        #
        # # string_text = struct.unpack('fmt', temp[5:])
        # print("client s struct size: {}".format(len(temp[4:])))
        # print('client s: {}'.format(temp[4:]))
        # string_text = struct.unpack('20s', temp[4:])
        # print("client struct type: {}".format(type(string_text[0])))
        # print("client struct text: {}".format(string_text[0].decode()))

    except Exception as e:
        print("error:::: {}".format(e))
        return False

    return True

def socket_close(accepted_client):
    try:
        accepted_client.close()
    except:
        return False

    return True
