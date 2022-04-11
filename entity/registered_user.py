import imghdr
from entity.personal_info import PersonalInfo, Role


class RegisteredUser(PersonalInfo):
    def __init__(self, first_name = None, last_name = None,
                 username = None, email = None, password = None, profile_picture = None, id = None, active=True, role= Role.USER):
        super().__init__(id, first_name, last_name, username, email, password, role)
        self.image = profile_picture
        self.active = active

        #self.following = following

        # created
        #modified
        # list of followed users
        # list of projects
        # should have the ability to manage it own personal data
        # change their password


    def __str__(self):
        return f'{super().__str__()} | {str(self.image)} | {self.active} |'






