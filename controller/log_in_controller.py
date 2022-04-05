from dao.user_repository import UserRepository
from entity.registered_user import RegisteredUser
#from exception.credentials_exception import CredentialsException


class CredentialsException:
    pass


class LoginController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self._logged_user = None

    def register(self, user: RegisteredUser) -> RegisteredUser:
        # TODO validate user
        created = self.user_repository.create(user)
        self.user_repository.save()
        return created

    def login(self, username: str, password: str) -> RegisteredUser:
        user = self.user_repository.find_by_username(username)
        if user is not None and user.password == password:
            self._logged_user = user
            return user
        raise CredentialsException("Invalid username or password. Try again.")

    def logout(self) -> RegisteredUser:
        self._logged_user = None

    def get_logged_user(self) -> RegisteredUser | None:
        return self._logged_user


#class SignUpService:
#     def __init__(self, account_repository):
#         """ @type account_repository AccountRepository """
#         self._account_repository = account_repository
#
#     def create_account(self, username, email):
#         account = Account(username, email)
#         self._account_repository.add(account)