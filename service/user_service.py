from dao.project_repository import ProjectRepository
from dao.user_repository import UserRepository
from entity.project import Project
from entity.registered_user import RegisteredUser


class UserAlreadyExist(Exception):
    pass


class UserService:

    def __init__(self, user_repo: UserRepository):
        self._user_repository = user_repo

    #about admin functionality

    def add_user(self, user: RegisteredUser):
        # when user.json is empty and I try to add new user it raise error because of self._user_repository.load()
        self._user_repository.load()
        if self._user_repository.find_by_username(user.username) == None:
            self._user_repository.create(user)
            self._user_repository.save()
        else:
            print("User with this username already exist")
            #raise UserAlreadyExist(self._user_repository.find_by_username(user.username))


    def edit_user_data(self,user: RegisteredUser):
        # what if someone want to change his username
        self._user_repository.load()
        user_to_edit = self._user_repository.find_by_username(user.username)
        user.id = user_to_edit.id
        self._user_repository.update(user)
        self._user_repository.save()

    def delete_user(self, user: RegisteredUser):
        self._user_repository.load()
        user_to_be_deleted = self._user_repository.find_by_username(user.username)
        # TODO exception handeling for user not found
        self._user_repository.delete_by_id(user_to_be_deleted.id)
        self._user_repository.save()

    def add_like(self, project: Project, project_repo: ProjectRepository):
        # TODO by who is added the like
        # find_project_in_repo = project_repo.find_by_id(project.id)
        # find_project_in_repo.likes = find_project_in_repo.likes + 1
        project.likes = project.likes + 1
        project_repo.save()

    def print_all_users(self):
        self._user_repository.load()
        for user in self._user_repository.find_all():
            print(user)


