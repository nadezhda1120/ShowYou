from dao.idGenerator import IdGeneratorUuid
from dao.json_repository import JsonRepository
from dao.repository import Repository
from entity.registered_user import RegisteredUser
from util.fun_util import find


class UserRepository(JsonRepository):

    def find_by_username(self, username: str) -> RegisteredUser | None:
        users_list = self.find_all()
        results = find(lambda user: user.username == username, users_list)
        return results

    def find_by_email(self, email) -> RegisteredUser | None:
        users_list = self.find_all()
        results = find(lambda user: user.email == email, users_list)
        return results

    #we have find_by_id




