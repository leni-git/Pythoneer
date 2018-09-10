import struct
from utils_socket import *

if __name__=="__main__":
    accepted_client = socket_connect()
    if accepted_client:
        print("socket_connect succed")
        print("")

        if socket_read(accepted_client):
            print("socket_read succeed")
            print("")

            if socket_write(accepted_client, "Here is Server, socket_read"):
                print("socket_write succeed")
            else:
                print("socket_write false")

            print("")

        else:
            print("socket_read false")
            print("")

        if socket_read_struct(accepted_client):
            print("socket_read_struct succeed")
            print("")

            if socket_write(accepted_client, "Here is Server, socket_read_struct"):
                print("socket_write succeed")
            else:
                print("socket_write false")

            print("")

        else:
            print("socket_read_struct false")
            print("")

        if socket_close(accepted_client):
            print("socket_close succeed, program exit")
        else:
            print("socket_close false, program exit")

    else:
        print("socket_connect false")
