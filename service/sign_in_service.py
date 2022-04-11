from dao.user_repository import UserRepository
from entity.registered_user import RegisteredUser
from exception.credentials_exception import CredentialsException


class CredentialsException:
    pass


class SignInService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self._singed_user = None


    def sign_in(self, username: str, password: str) :
        #load
        self.user_repository.load()
        user = self.user_repository.find_by_username(username)
        if user is not None and user.password == password:
            self._singed_user = user
            return user
        raise CredentialsException("Invalid username or password. Try again.")

    def sign_out(self) -> RegisteredUser:
        self._singed_user = None

    def get_signed_user(self) -> RegisteredUser | None:
        return self._singed_user

