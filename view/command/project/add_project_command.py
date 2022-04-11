class AddProjectCommand:
    def __init__(self, project_controller):
        self.project_controller = project_controller

    def __call__(self, project):
        self.project_controller.add_project(project)