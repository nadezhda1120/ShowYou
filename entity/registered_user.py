import imghdr
from entity.personal_info import PersonalInfo, Role
from entity.project import Project
from dao.project_repository import *


class RegisteredUser(PersonalInfo):
    def __init__(self, first_name = None, last_name = None,
                 username = None, email = None, password = None, profile_picture = None, role = Role.USER, id = None, active=True):
        super().__init__(id, first_name, last_name, username, email, password, role)
        self.image = profile_picture
        self.active = active
        #self._project_repository = ProjectRepository("project.json", Project)
        # created
        #modified
        # list of commented projects
        # list of followed users
        # list of projects
        # should have the ability to manage it own personal data
        # change their password


    def __str__(self):
        #repr =  f'| {str(self.id):24s} | {self.first_name:15.15s} | {self.last_name:15.15s} | {self.username:15.15s} | {self.password:15.15s} | {self.role:15.15s} | {self.image:15.15s} | {self.active:} |'
        return f'{super().__str__()} | {str(self.image)} | {self.active} | '


    # def create_project(self,project: Project):
    #     #project = Project(title, description, images, subject, tags)
    #     project.author = self.username
    #     self._project_repository.create(project)
    #     self._project_repository.save()
    #     #thinking about making list of projects represented by dictionary


    # def print_all_projects(self):
    #     for project in self._project_repository.find_all():
    #         print(project)





