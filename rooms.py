import redis


class Room:

    def __init__(self) -> None:
        
        pass


    def get_all_rooms(self, rooms: dict) -> str:
        """Retrieve all rooms in chat"""

        available_rooms = [f'Room {key}: participiants - {value}' for key, value in rooms.items()]
        return ' '.join(available_rooms).encode('utf-8')
    

    def add_client_to_the_room(self, room_number: str, client: object, rooms: dict) -> None:
        """Add a client to the existing room"""

        lst = rooms.get(room_number)
        print(lst, type(lst))

        rooms[room_number] = [client]

        return rooms

    
    def return_a_clients_neighbour(self, current_room: int, rooms: dict):
        """Retrievind an client partner"""

        client = None

        for cli in rooms[current_room]:
            if cli != cli:
                client = cli

        return client
