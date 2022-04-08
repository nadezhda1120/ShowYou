from dao.user_repository import UserRepository
from entity.registered_user import RegisteredUser
from exception.credentials_exception import CredentialsException


class CredentialsException:
    pass


class LoginService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self._logged_user = None


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

