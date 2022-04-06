from dao.idGenerator import IdGeneratorUuid
from dao.project_repository import ProjectRepository
from entity.project import Project
from entity.registered_user import RegisteredUser
from view.comment import Comment

class ProjectController:
    comment_id_generator = IdGeneratorUuid()

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

    def edit_project(self, current_project: Project, edited_project: Project):
        current_project.description = edited_project.description
        current_project.title = edited_project.title
        current_project.images = edited_project.images
        current_project.tags = edited_project.tags
        current_project.subject =edited_project.subject
        self._project_repository.update(current_project)
        self.save_project()

    def delete_project(self, project: Project):
        self._project_repository.load()
        self._project_repository.delete_by_id(project.id)
        self.save_project()

    #should implement delete_project by title, author

    def add_comment(self, user: RegisteredUser, comment: Comment, project: Project):
        comment.creator = user.username
        comment.commentID = self.__class__.comment_id_generator.get_next_id()
        project.comments.append(comment)
        self._project_repository.update(project)
        self.save_project()

    def edit_comment(self, current_comment: Comment, edited_comment: Comment):
        #self._project_repository.load()
        def find_project_by_id_comment(c_id):
            for project in self._project_repository.find_all():
                for comment in project.comments:
                    if c_id == comment.commentID:
                        comment.content = edited_comment.content
                        self._project_repository.update(project)
                        self.save_project()
        find_project_by_id_comment(current_comment.commentID)


    def delete_comment(self):
        pass


    def print_all_projects(self):
        for project in self._project_repository.find_all():
            print(project)

    def print_all_project_comments(self, project: Project):
        project.print_comments()

    def save_project(self):
        self._project_repository.save()



