from dao.json_repository import JsonRepository
#from entity.registered_user import RegisteredUser
from util.fun_util import find
from entity.project import Project

class ProjectRepository(JsonRepository):
    #do I need it or is the same as find_by_username
    #in json I'm saving only the username of the creator
    #i'm wondering won't it be better to save the whole information about the user
    # to be like in the DB to have connection between User and Project
    def find_by_user(self, username: str) -> list[Project] | None:
        project_list = self.find_all()
        results = find(lambda project: project.author == username, project_list)
        return results
        #if none raise ProjectNotFound

    def find_by_tag(self, searched_tag) -> Project | None:
        lower_tag = searched_tag.lower()
        project_list = self.find_all()
        results = []
        for project in project_list:
            for tag in project.tags:
                if lower_tag in tag.lower():
                    results.append(project)
                    break
        return results

    def find_by_section(self, section) -> list[Project]:
        pass

    def find_by_title(self, title) -> list[Project]:
        title_to_lower = title.lower()
        projects_list = self.find_all()
        results = find(lambda project: title_to_lower in project.title.lower(), projects_list)
        return results
        #raise exception









