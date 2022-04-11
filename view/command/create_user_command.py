class CreateUserCommand:
    def __init__(self, user_controller):
        self.user_controller = user_controller

    def __call__(self, user):
        self.user_controller.create_account(user)
