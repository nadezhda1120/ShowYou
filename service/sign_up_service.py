from dao.user_repository import UserRepository
from entity.registered_user import RegisteredUser


class SignUpService:
    def __init__(self, account_repository: UserRepository):
        """ @type account_repository AccountRepository """
        self._account_repository = account_repository

    def create_account(self, user: RegisteredUser) -> RegisteredUser:
        # when user.json is empty and I try to add new user it raise error because of self._user_repository.load()
        self.user_repository.load()
        if self._user_repository.find_by_username(user.username) == None:
            created = self._user_repository.create(user)
            self._user_repository.save()
            return created
        else:
            print("User with this username already exist")
            # raise UserAlreadyExist(self._user_repository.find_by_username(user.username))