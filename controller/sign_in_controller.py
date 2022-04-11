from service.sign_in_service import SignInService


class CredentialsException:
    pass


class SignInController:
    def __init__(self, service: SignInService, view = None):
        self.service = service
        self.view = view

    def sign_in(self, username, password):
        self.service.sign_in(username, password)

    def get_signed_user(self):
        self.service.get_signed_user()

