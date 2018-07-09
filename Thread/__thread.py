if __name__ == "__main__":
    import socket
    from _thread import start_new_thread

    from __function import *

    HOST = ''
    PORT = 10003
    ADDR = (HOST, PORT)
    BUFF_SIZE = 1024

    serverSocket = socket.socket()
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(ADDR)
    serverSocket.listen(5)

    print("""
        Thread data Sharing Test
        
            * 메소드 동작을 진행 중일 때 프로그램을 종료하고 싶으시면 강제 종료해 주세요.
            * 리눅스에서 강제종료 동작( 설정 변경 안 했을 경우 ): Ctrl + C
            * 파이참에서 강제종료 동작( 설정 변경 안 했을 경우 ): Ctrl + F2
            
            1. 메소드에서 지역변수를 사용할 때
            2. 매번 클래스를 새로 생성하여 매개변수로 전달 할 때 ( 인스턴스 변수, 인스턴스 지역 변수 )
            3. 최초 1회 클래스 생성 후 생성한 클래스를 매개변수로 전달 할 때 ( 인스턴스 변수, 인스턴스 지역 변수 )
            
            0. 종료
    """)
    choice = input(' >> ')

    if choice == '0':
        exit(0)

    elif choice == '1':
        print("\n\tlocal_value_thread start")

        while True:
            clientSocket, addr = serverSocket.accept()
            start_new_thread(local_value_thread, (clientSocket, addr,))

    elif choice == '2':
        print("\n\tclass_value_thread start")

        num = 10
        while True:
            clientSocket, addr = serverSocket.accept()
            client = ClientInfo(clientSocket, addr[1], num)
            client_test = ClassTest()

            print("Connected from inside port << {} >>".format(addr[1]))
            start_new_thread(class_value_thread, (client, client_test, ))

    elif choice == '3':
        print("\n\tclass_value_thread start")

        num = 10
        client_test = ClassTest()
        while True:
            clientSocket, addr = serverSocket.accept()
            client = ClientInfo(clientSocket, addr[1], num)

            print("Connected from inside port << {} >>".format(addr[1]))
            start_new_thread(class_value_thread, (client, client_test,))

    else:
        print('\n\t★ You can choose only from 0 to 3 ★')

