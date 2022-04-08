from dao.idGenerator import IdGeneratorUuid
from dao.project_repository import ProjectRepository
from entity.project import Project
from entity.registered_user import RegisteredUser
from view.comment import Comment

class ProjectService:
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
    def __add__(self, other):
        for project in other._project_repository:
            self.update_project(project)


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
        self.update_project(current_project)

    def delete_project(self, project: Project):
        self._project_repository.load()
        self._project_repository.delete_by_id(project.id)
        self.save_project()

    #should implement delete_project by title, author

    def add_comment(self, user: RegisteredUser, comment: Comment, project: Project):
        comment.creator = user.username
        comment.commentID = self.__class__.comment_id_generator.get_next_id()
        project.comments.append(comment)
        self.update_project(project)

    def edit_comment(self, current_comment: Comment, edited_comment: Comment):
        def update_project_comment(c_id):
            for project in self._project_repository.find_all():
                for comment in project.comments:
                    if c_id == comment.commentID:
                        comment.content = edited_comment.content
                        self.update_project(project)
        update_project_comment(current_comment.commentID)


    def delete_comment(self,user: RegisteredUser, comment: Comment):
        # TODO fix the error
        for project in self._project_repository.find_all():
            for c in project.comments:
                print(f'{type(comment.content)} |  {type(user.username)}')
                if str(comment.content) == str(c.content) & str(user.username) == str(c.creator):
                    project.comments.remove(c)
                    self.update_project(project)
                else:
                    print("not found")
                    #raise Exception


    def print_all_projects(self):
        self._project_repository.load()
        for project in self._project_repository.find_all():
            print(project)
            #return project

    def print_all_project_comments(self, project: Project):
        project.print_comments()

    def save_project(self):
        self._project_repository.save()

    def update_project(self, project):
        self._project_repository.update(project)
        self.save_project()


    def view_top_10(self):
        self._project_repository.load()
        sorted_projects = sorted(self._project_repository.find_all(), key = lambda i: i.likes, reverse=True)
        for index, p in enumerate(sorted_projects):
            if index != 10:
                print(p)
            else:
                break


