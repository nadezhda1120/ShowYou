from dao.idGenerator import IdGeneratorUuid
from dao.json_repository import JsonRepository
from dao.repository import Repository
from entity.personal_info import Role
from entity.registered_user import RegisteredUser
from util.fun_util import find


class UserRepository(JsonRepository):

    def find_by_username(self, username: str) :
        users_list = self.find_all()
        results = find(lambda user: user.username == username, users_list)
        return results

    def find_by_email(self, email):
        users_list = self.find_all()
        results = find(lambda user: user.email == email, users_list)
        return results

    @staticmethod
    def is_admin(self, user):
        True if user.role == Role.ADMIN else False

    @staticmethod
    def is_user(self, user):
        True if user.role == Role.USER else False
    #we have find_by_id




