from service.user_service import UserService

class UserController:
    def __init__(self, service: UserService, view: None):
        self.service = service
        self.view = view



