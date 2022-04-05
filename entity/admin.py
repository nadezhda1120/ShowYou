from entity.personal_info import PersonalInfo, Role
#should be able to manage all user's data except password
#should manage comments and projects with unappropriate content


class Admin(PersonalInfo):
    def __init__(self, first_name, last_name, username,email,  password, id = None, role=Role.ADMIN) :
        super.__init__(self, first_name, last_name, username,email, password, role, id)
        #self.org_number = org_number

    def edit_comment(self):
        pass

    def edit_project(self):
        pass

    def delete_comment(self):
        pass

    def delete_project(self):
        pass

    def add_section(self):
        pass

    def __str__(self):
        return f'{super.__str__()} {self.org_number} |'