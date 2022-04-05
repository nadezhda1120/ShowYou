from dao.project_repository import ProjectRepository
from entity.project import Project
from entity.registered_user import RegisteredUser
from view.comment import Comment

class ProjectController:
    def __init__(self, current_user: RegisteredUser, project_repo: ProjectRepository):
        self._current_user = current_user
        self._project_repository = project_repo

    # def create_project(self, title, description, images, subject=None, tags=None):
    #     project = Project(title, description, images, subject, tags)
    #     project.author = self.username
    #     self._project_repository.create(project)
    #     self._project_repository.save()
    #     # thinking about making list of projects represented by dictionary

    #how to connect project with author
    def create_project(self, project: Project):
        project.author = self._current_user.username
        self._project_repository.create(project)
        self._project_repository.save()

    def edit_project(self, project):
        pass

    def delete_project(self, project: Project):
        self._project_repository.delete_by_id(project.id)

    #should implement delete_project by title, author
    def add_comment(self, comment: Comment):
        pass

    def edit_comment(self):
        pass

    def delete_comment(self):
        pass

    def add_like(self):
        pass

    def print_all_projects(self):
        for project in self._project_repository.find_all():
            print(project)
        #self._project_repository.load()

    def save_project(self):
        self._project_repository.save()



