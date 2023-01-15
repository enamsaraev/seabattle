import socket
import threading


PORT = 5050
HOST = socket.gethostbyname(socket.gethostname())


class Client:

    def __init__(self, host, port) -> None:
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        self.__header = 64
        self.__format = 'utf-8'

    
    def connect(self):

        threading.Thread(target=self.sending_msg, args=(self.client,)).start()
        threading.Thread(target=self.recieving_msg, args=(self.client,)).start()

    def sending_msg(self, client):
        """"""

        while True:
            message = input("")
            client.send(message.encode(self.__format))
            print("You: " + message)


    def recieving_msg(self, client):
        """"""

        while True:
            print(client.recv(self.__header).decode(self.__format))


cli = Client(HOST, PORT)
cli.connect()
