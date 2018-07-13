class ClientInfo:
    """
        Client Info Class
        It's not action class just Information
    """
    def __init__(self, sock, port, num):
        self.sock = sock
        self.port = port
        self.num = num

    def self_value_plus(self):
        self.num += 1


class ClassTest:
    """
        Thread data sharing Test Class
            1. Are the class values shared?
                - self.value
                - def self_value_plus(self): void
                - def get_value(self): self.value

            2. Are the local values in Class shared?
                - def class_local_value(num): void
    """
    def __init__(self):
        self.value = 0

    @staticmethod
    def class_local_value(num):
        # This class-method doesn't use self(Class)
        # So you can use this "@staticmethod"
        num -= 1
        return num

    def self_value_plus(self):
        self.value += 1

    def get_value(self):
        return self.value


def class_value_thread(client, client_test):
    """
        :param client: class ClientInfo()
        :param client_test: class ClassTest()
        :return: void

        Thread data sharing Test Method for Class
    """

    for i in range(10):
        client.sock.send(('{} 의 {} 번째 num={}, self.value={}'.format(client.port, i, client.num, client_test.get_value())).encode())
        get_num(client.port, client.num, client_test.get_value())
        client.num = client_test.class_local_value(client.num)
        client_test.self_value_plus()
        input(' >> ')

    print('end << {} >>'.format(client.port))


def local_value_thread(sock, addr):
    """
    :param sock: (main)clientSocket >> socket Instance
    :param addr: (main)addr >> dic(ip, port)
    :return: void

        Thread data sharing Test for Method
    """

    num = 0
    for i in range(10):
        sock.send(('{} 의 {} 번째 num={}'.format(addr[1], i, num)).encode())
        num += 1
        get_num(addr[1], num)
        input(' >> ')

    print('end << {} >>'.format(addr[1]))


def get_num(port, num, value=None):
    if not value:
        print('{} 의 num={}'.format(port, num))
    else:
        print('{} 의 num={}, value={}'.format(port, num, value))
