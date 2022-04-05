from datetime import datetime

from entity.registered_user import RegisteredUser
from entity.admin import Admin
from entity.project import Project

class Comment:
    now = datetime.now()
    def __init__(self,content, commentID=None, authorID=None, projectID=None):
        self.commentID = commentID
        self.authorID = authorID
        self.projectID = projectID
        self.content = content
        self._date = self.__class__.now.strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f'|{self.commentID}|{self.authorID}|{self.projectID}|{self._date}|{self.content}|'