from dao.project_repository import ProjectRepository
from dao.user_repository import UserRepository
from entity.project import Project
from entity.registered_user import RegisteredUser


class UserController:

    def __init__(self):
        self._user_repository = UserRepository()


    #about admin
    def add_user(self, user: RegisteredUser):
        pass

    def edit_user_data(self):
        pass

    def delete_user(self):
        pass

    def add_like(self, project: Project):
        project.likes += 1


