from datetime import datetime


class Comment:
    now = datetime.now()
    def __init__(self,content, commentID=None, creator=None):
        self.commentID = commentID
        self.creator = creator
        self.content = content
        self._date = self.__class__.now.strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f'|{self.commentID}|{self.creator}|{self._date}|{self.content}|'