from controller.sign_in_controller import SignInController
from controller.user_controller import UserController
from dao.user_repository import UserRepository
from dao.project_repository import ProjectRepository
from entity.project import Project
from entity.admin import Admin
from entity.registered_user import RegisteredUser
from service.sign_in_service import SignInService
from service.user_service import UserService
from service.project_service import ProjectService

if __name__ == '__main__':
    user1 = RegisteredUser('Nadezhda', 'Pandelieva', 'nadezhda1106', 'nadezhdapa@gmail.com', '15264', 'image.png')
    user2 = RegisteredUser('Ivan', 'Popov', 'iv5941', 'ipopopv@abv.bg', '154896', 'image.png')
    user3 = RegisteredUser('Georgi', 'Georgiev', 'gg_2051', 'gg_200@gmail.com', '6384VCGHJK', 'image.png')
    user4 = RegisteredUser('Ivo', 'Georgiev', 'ivo_2051', 'ivo_5200@gmail.com', '638CGHJK', 'image.png')
    users = [user1, user2, user3]

    users_repo = UserRepository("user.json", RegisteredUser)
    user_service = UserService(users_repo)
    user_controller = UserController(user_service)
    user_controller.create_account(user1)
    user_controller.create_account(user4)
    user_service.print_all_users()
    #user_controller.delete_user(user1)


    print("Test sign in")
    sign_in_service = SignInService(users_repo)
    sign_in_controller = SignInController(sign_in_service)
    sign_in_service.sign_in('nadezhda1106', '15264')
    sign_in_controller.get_signed_user()



    print("After deleting")
    user_service.print_all_users()

    print("Changing user data")
    user1_edited = RegisteredUser('Nadya', 'Pandelieva', 'nadezhda1106', 'nadezhdapandelieva@gmail.com', '1234', 'image.png')
    user_service.edit_user_data(user1_edited)
    user_service.print_all_users()

    # admin - self, first_name, last_name, username, email,  password, id = None, role=Role.ADMIN
    print("admin")
    admin1 = Admin('Nadezhda', 'Pandelieva', 'nadezhda1106', 'nadezhdapa@gmail.com', '15few264')
    admin2 = Admin('Ivan', 'Popov', 'iv5941', 'ipopopv@abv.bg', '154fw896')
    admin3 = Admin('Georgi', 'Georgiev', 'ggf_2051', 'gg_200@gmail.com', '6384VCGfweHJK')
    admins = [admin1, admin2, admin3]

    admins_repo = UserRepository("admin.json", Admin)
    admins_service = UserService(admins_repo)

    for admin in admins:
        admins_service.add_user(admin)

    admins_service.print_all_users()


    p4 = Project('Day in Paris', 'These are pictures of my Erasmus project in Paris.', ['image1.png', 'image2.png', 'image3.png'], 'landscape',['Paris', 'sun', 'friends', 'feeling','image', 'good'])
    p1 = Project('Rare Ware', 'Photo Session of Rare Ware sunglasses', ['image1.png', 'image2.pg', 'imageo3.pngf'],
                 'Sunglasses', ['sunglasses', 'friends', 'product', 'red', 'image'])
    p3 = Project('Lord of the Ring', 'Sceens of the film', ['image1.png', 'image2.pg', 'imageo3.png'], 'Film',
                 ['film', 'ring', 'lord', 'awesome'])

    #projects = [p1, p3, p4, p2, p5,p6,p7,p8,p9,p10,p11]

    project_repo1 = ProjectRepository("projects_user1.json", Project)
    project_repo2 = ProjectRepository("projects_user2.json", Project)
    pr_service1 = ProjectService(user1, project_repo1)
    pr_service2 = ProjectService(user2, project_repo2)

    # TODO add more projects into the repo
    # for p in projects:
    #     pr_service1.create_project(p)
    #
    # print("Projects")
    # pr_service1.create_project(p1)
    # pr_service1.create_project(p3)
    # pr_service1.create_project(p4)
    # pr_service2.create_project(p3)
    # pr_service2.create_project(p4)
    #
    # pr_service1.print_all_projects()
    #
    #
    # print("After deleting")
    #
    # # pr_controller1.delete_project(p3)
    # # pr_controller1.print_all_projects()
    #
    # print("Project: ", p1)
    # print("Add like")
    # user_service.add_like(p1, project_repo1)
    # user_service.add_like(p1, project_repo1)
    # user_service.add_like(p1, project_repo1)
    # user_service.add_like(p1, project_repo1)
    # print(p1)
    #


    print("Top 10")
    # pr_service1 += pr_service2
    # pr_service1.print_all_projects()
    #project_repo1 += project_repo2
    # for p in project_repo1.find_all():
    #     print(p.likes)
    pr_service1.view_top_10()


    # print("Found by tag")
    # for project in project_repo1.find_by_tag("image"):
    #     print(project)
    #
    # print("Before editing")
    # pr_controller2.print_all_projects()
    # print("After editing")
    # p3_edit = Project('Lord of the Ring', 'Magical night with the Lord of the Ring', ['image1.png', 'image2.pg', 'image4.png'], 'Film',
    #              ['film', 'ring', 'lord', 'awesome'])
    # pr_controller2.edit_project(p3,p3_edit)
    # pr_controller2.print_all_projects()
    #
    # print("Add comment")
    # c1 = Comment("Very Nice details of the logo")
    # c2 = Comment("Good job")
    # pr_controller1.add_comment(user3, c1, p3)
    # pr_controller1.add_comment(user3, c2, p3)
    # pr_controller1.print_all_project_comments(p3)
    # c1_edit = Comment("Very neat work")
    # print("Edited comment")
    # pr_controller1.edit_comment(c1, c1_edit)
    # pr_controller1.print_all_project_comments(p3)
    # print("Remove comment")
    # #print(c1_edit)
    # pr_controller1.delete_comment(user3, c1_edit)
    # pr_controller1.print_all_project_comments(p3)
    # ###, title, description,  images, subject = None, tags = None, likes = None,author = None

