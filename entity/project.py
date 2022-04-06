#from entity.registeredUser import RegisteredUser
import imghdr
from datetime import datetime
from view.comment import Comment
# upload image
class Project:
    next_id = 1  # unique id sequence
    now = datetime.now()

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id

    def __init__(self,title= None, description = None,  images = None, subject = None, tags = None,author = None, id= None):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.dateCreated = self.__class__.now.strftime("%d/%m/%Y %H:%M:%S")
        self.subject = subject
        self.tags = tags
        self.images = images
        self.likes = 0
        self.comments = []
        #self._idProject = self.__class__.next_id
        #section
        #list of comments
        #when was created
        #when was last modified
        # every project should be able to be downloaded in printable format

    # add list of images

    def top_10(self):
        #sorted projects by likes (first 10)
        pass


    def __str__(self):
        return  f"| {self.id} | {str(self.title):20s} | {str(self.author):10s} | {self.description} | {str(self.images)} | {', '.join(self.tags)} |"

    def print_comments(self):
        for comment in self.comments:
            print(comment)