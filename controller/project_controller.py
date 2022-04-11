from entity.project import Project
from service.project_service import ProjectService


class ProjectController:
    def __init__(self, service: ProjectService, view=None):
        self.view = view
        self.service = service

    def print_all_projects(self):
        # TODO make it return
        self.service.print_all_projects()

    def save_project(self):
        self.service.save_project()

    def show_added_project(self):
        pass

    def create_project(self, project: Project):
        self.service.create_project(project)
        #self.view.refresh()

    def add_comment(self, comment):
        self.service.add_comment(comment)

    def delete_project(self, project):
        self.service.delete_project(project)








