import redis
import json
import pickle


class RD:

    def __init__(self) -> None:
        
        self.available_rooms = {1: [], 2: []}
        self.client_data = {}


    def set_a_value(self, value: dict) -> None:
        """Set a data to rd"""

        self.client_data = value

    
    def get_a_value(self) -> dict:
        """Retrieve a value"""

        value = self.available_rooms
        return value

