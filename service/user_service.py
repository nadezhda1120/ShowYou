from dao.project_repository import ProjectRepository
from dao.user_repository import UserRepository
from entity.project import Project
from entity.registered_user import RegisteredUser


class UserAlreadyExist(Exception):
    pass


class UserService:

    def __init__(self, user_repo: UserRepository):
        self.user_repository = user_repo

    #about admin functionality

    #not needed
    def add_user(self, user: RegisteredUser):
        # when user.json is empty and I try to add new user it raise error because of self._user_repository.load()
        self.user_repository.find_all()
        if self.user_repository.find_by_username(user.username) == None:
            self.user_repository.create(user)
            self.user_repository.save()
        else:
            print("User with this username already exist")
            #raise UserAlreadyExist(self._user_repository.find_by_username(user.username))


    def edit_user_data(self,user: RegisteredUser):
        # what if someone want to change his username
        self.user_repository.load()
        user_to_edit = self.user_repository.find_by_username(user.username)
        user.id = user_to_edit.id
        self.user_repository.update(user)
        self.user_repository.save()

    def delete_user(self, user: RegisteredUser):
        self.user_repository.load()
        user_to_be_deleted = self.user_repository.find_by_username(user.username)
        # TODO exception handeling for user not found
        self.user_repository.delete_by_id(user_to_be_deleted.id)
        self.user_repository.save()

    def add_like(self, project: Project, project_repo: ProjectRepository):
        # TODO by who is added the like
        # find_project_in_repo = project_repo.find_by_id(project.id)
        # find_project_in_repo.likes = find_project_in_repo.likes + 1
        project.likes = project.likes + 1
        project_repo.save()

    def print_all_users(self):
        #self.user_repository.load()
        for user in self.user_repository.find_all():
            print(user)


