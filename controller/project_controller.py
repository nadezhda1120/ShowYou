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

    def create_project(self, project: Project):
        # TODO validation
        project.author = self._current_user.username
        self._project_repository.create(project)
        self._project_repository.save()

    def edit_project(self, project: Project, updated_project: Project):
        #self._project_repository.find_by_id(project.id)
        project.description = updated_project.description
        project.title = updated_project.title
        project.images = updated_project.images
        project.tags = updated_project.tags
        project.subject =updated_project.subject
        self._project_repository.update(project)
        self.save_project()

    def delete_project(self, project: Project):
        self._project_repository.load()
        self._project_repository.delete_by_id(project.id)
        self.save_project()

    #should implement delete_project by title, author

    def add_comment(self, comment: Comment):
        pass
        comment.authorID = self._current_user.id
        #comment.projectID =


    def edit_comment(self):
        pass

    def delete_comment(self):
        pass


    def print_all_projects(self):
        for project in self._project_repository.find_all():
            print(project)
        #self._project_repository.load()

    def save_project(self):
        self._project_repository.save()



