from enum import Enum

class Role(Enum):
    USER = 1
    ADMIN = 2
    UNREGISTERED_USER = 3

    @classmethod
    def from_json(cls, prop_dict):
        return cls[prop_dict['name']]

    def to_json(self):
        return self.name

class PersonalInfo:
    def __init__(self, id = None, first_name = None, last_name = None, username = None, email = None,  password = None, role = None):
        self.id = id
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.role = role


    # def __repr__(self):
    #     repr = f'|{str(self.id)} | {self.first_name} |  {self.last_name } | { self.username } | { str(self.role )} | '
    #     return repr

    def __str__(self):
        return f'|{str(self.id):10s} | {self.first_name:10s} |  {self.last_name:10s} | { self.username:15s} | {self.password:20s} | {str(self.role):5s}'


