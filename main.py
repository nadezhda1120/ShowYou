from controller.project_controller import ProjectController
from dao.user_repository import UserRepository
from dao.project_repository import ProjectRepository
from entity.project import Project
from entity.registered_user import RegisteredUser
from view.comment import Comment

if __name__ == '__main__':
    user1 = RegisteredUser('Nadezhda', 'Pandelieva', 'nadhioe', 'nadezhdapa@gmail.com', '15264', 'image.png')
    user2 = RegisteredUser('Ivan', 'Popov', 'iv5941', 'ipopopv@abv.bg', '154896', 'image.png')
    user3 = RegisteredUser('Georgi', 'Georgiev', 'gg_2051', 'gg_200@gmail.com', '6384VCGHJK', 'image.png')
    users = [user1, user2, user3]

    users_repo = UserRepository("user.json", RegisteredUser)
    #user_controller = UserController(user1, users_repo)
    # for u in users:
    #     users_repo.create(u)
    #
    # for user in users_repo.find_all():
    #     print(user)
    #
    # users_repo.save()
    #print('Found')
    users_repo.load()
    users_repo.delete_by_id('ad15ad9f-b4f2-11ec-805d-900f0c431cac')
    # print(users_repo.find_by_username('nadhioe'))
    # print(users_repo.find_by_email("ipopopv@abv.bg"))
    #print(users_repo.find_by_id("ad15ad9d-b4f2-11ec-830b-900f0c431cac"))


    p4 = Project('Day in Paris', 'These are pictures of my Erasmus project in Paris.', ['image1.png', 'image2.png', 'image3.png'], 'landscape',['Paris', 'sun', 'friends', 'feeling','image', 'good'])
    p1 = Project('Rare Ware', 'Photo Session of Rare Ware sunglasses', ['image1.png', 'image2.pg', 'imageo3.pngf'],
                 'Sunglasses', ['sunglasses', 'friends', 'product', 'red', 'image'])
    p3 = Project('Lord of the Ring', 'Sceens of the film', ['image1.png', 'image2.pg', 'imageo3.png'], 'Film',
                 ['film', 'ring', 'lord', 'awesome'])
    p = [p1, p3, p4]
    project_repo1 = ProjectRepository("projects_user1.json", Project)
    project_repo2 = ProjectRepository("projects_user2.json", Project)
    pr_controller1 = ProjectController(user1, project_repo1)
    pr_controller2 = ProjectController(user2, project_repo2)

    print("Projects")
    pr_controller1.create_project(p1)
    pr_controller1.create_project(p3)
    pr_controller1.create_project(p4)
    pr_controller2.create_project(p3)
    pr_controller2.create_project(p4)

    pr_controller1.print_all_projects()


    print("After deleting")
    pr_controller1.delete_project(p1)
    pr_controller1.print_all_projects()

    print("Found by tag")
    for project in project_repo1.find_by_tag("image"):
        print(project)

    print("Before editing")
    pr_controller2.print_all_projects()
    print("After editing")
    p3_edit = Project('Lord of the Ring', 'Magical night with the Lord of the Ring', ['image1.png', 'image2.pg', 'image4.png'], 'Film',
                 ['film', 'ring', 'lord', 'awesome'])
    pr_controller2.edit_project(p3,p3_edit)
    pr_controller2.print_all_projects()

    print("Comment test ")
    c1 = Comment("Very Nice details of the logo")
    pr_controller1.add_comment(c1)
    print(c1)
    # ###, title, description,  images, subject = None, tags = None, likes = None,author = None

