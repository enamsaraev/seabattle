import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050

HEADER = 64 #the length of first client's message
FORMAT = 'utf-8'


class Server:

    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        
        self.__header = 1024
        self.__format = 'utf-8'

        self.user_data = {'user': 'pass', 'haha': 'pass'}

        self.rooms = {1: [], 2: []}


    def runserver(self):
        """Startring server"""

        self.server.listen()
        print('Running')

        while True:
            client, _ = self.server.accept()

            thread = threading.Thread(target=self.__auth_a_client, args=(client,))
            thread.start()
        
        self.server.close()

    
    def __auth_a_client(self, client):
        """CLient authorization"""

        res, username = self.__check_login(client)

        if res:
            self.__show_client_to_active_room(client, username)

    def __send_login_info(self, client):

        client.send('<server> Введите username: unique'.encode(self.__format))
        username = client.recv(self.__header).decode(self.__format)

        client.send('<server> Введите password: unique'.encode(self.__format))
        password = client.recv(self.__header).decode(self.__format)

        return username, password

    def __check_login(self, client):

        res = False

        while res == False:
            username, password = self.__send_login_info(client)

            # res = rd.check_login(username, password)
            if username in self.user_data and self.user_data[username] == password:
                res = True

        return True, username

    def __show_client_to_active_room(self, client, username: str):

        rooms = [f'<server> Room {key} - {value}' for key, value in self.rooms.items()]
        client.send('\n'.join(rooms).encode(self.__format))

        room = int(client.recv(self.__header).decode(self.__format))

        client_data = {client: username}
        self.rooms[room].append(client_data)
        
        self.__create_room_connection(room, client_data, client)
    
    def __create_room_connection(self, room: int, client_data: dict, client):

        room_curr = len(self.rooms[room])

        if room_curr == 1:
            client.send('<server> Waiting for other connections'.encode(self.__format))

        if room_curr> 1:
            for val in self.rooms[room]:
                for cli_key, _ in val.items():
                    cli_key.send('<server> Chat started'.encode(self.__format))

                    thread = threading.Thread(target=self.__start_chatting, args=(room, cli_key,))
                    thread.start()
                
    def __start_chatting(self, room: int, client):
        while True:
            msg_to_client = client.recv(self.__header).decode(self.__format)

            print(self.rooms[room])

            for val in self.rooms[room]:
                for cli_key, cli_value in val.items():
                    if cli_key != client:
                        cli_key.send(f'<{cli_value}> {msg_to_client}'.encode(self.__format))



ser = Server(HOST, PORT)
ser.runserver()