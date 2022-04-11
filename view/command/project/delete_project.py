from controller.project_controller import ProjectController


class DeleteProjectCommand:
    def __init__(self, project_controller: ProjectController):
        self.project_controller = project_controller

    def __call__(self, *args, **kwargs):
        #TODO show add book dialog
        #self.project_controller.delete_project()
        print("Showing 'Delete Books' dialog")
