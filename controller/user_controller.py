from service.user_service import UserService

class UserController:
    def __init__(self, service: UserService, view = None):
        self.service = service
        self.view = view


    def create_account(self, user):
        self.service.create_account(user)

    def delete_account(self, user):
        self.service.delete_user(user)

    def edit_user_data(self, user):
        self.service.edit_user_data(user)

    def show_user_profile(self, user):
        pass
        #self.view.user_profile()

