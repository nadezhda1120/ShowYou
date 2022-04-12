from tkinter import *
from tkinter.ttk import Combobox
import ast
import tkinter.font as font
from PIL import ImageTk, Image
from tkinter import messagebox

from controller.user_controller import UserController
from view.command.create_user_command import CreateUserCommand
from entity.registered_user import RegisteredUser


class SignUp:
    def __init__(self, window, sign_up_controller: UserController):
        self.sign_up_controller = sign_up_controller
        self.window = window
        self.window.title('Sign up')
        self.window.geometry('925x500+300+200')
        self.window.configure(bg='#fff')
        self.window.resizable(False, False)


        c = Canvas(self.window, height=925, width=500+300+200)
        background_image = ImageTk.PhotoImage(Image.open("images/b4.jpg").resize((900,700)))
        self.window.background_image = background_image
        c.pack(fill="both", expand=True)
        c.create_image(0, 0, image=background_image, anchor = "nw")
        c.pack()

        self.first_name = StringVar()
        self.last_name = StringVar()
        self.username = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()
        self.role = StringVar()


        self.frame = Frame(c, width=430, height=600, bg="white") #,highlightbackground="#57a1f8", highlightthickness=2
        self.frame.place(x=270, y=30)
        self.frame.pack(padx=18, pady=30)
        heading = Label(self.window, text="Create your account", fg='#57a1f8', bg='white',
                        font=('Microsoft YaHei UI Light', 21, 'bold'))
        heading.place(x=320.5, y=30)

        # ----------------------------------------------------------------------------------
        def on_enter(e):
            first_name_box.delete(0, 'end')

        def on_leave(e):
            if first_name_box.get() == '':
                first_name_box.insert(0, 'First name')

        first_name_box = Entry(self.frame, textvariable=self.first_name, width=17, fg='grey', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
        first_name_box.place(x=70, y=60)
        first_name_box.insert(0, 'First name')
        first_name_box.bind('<FocusIn>', on_enter)
        first_name_box.bind('<FocusOut>', on_leave)


        def on_enter(e):
            last_name_box.delete(0, 'end')

        def on_leave(e):
            name = last_name_box.get()
            if name == '':
                last_name_box.insert(0, 'Last name')

        last_name_box = Entry(self.frame,textvariable= self.last_name,  width=17, fg='grey', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
        last_name_box.place(x=220, y=60)
        last_name_box.insert(0, 'Last name')

        last_name_box.bind('<FocusIn>', on_enter)
        last_name_box.bind('<FocusOut>', on_leave)

        def on_enter(e):
            username_box.delete(0, 'end')

        def on_leave(e):
            name = username_box.get()
            if name == '':
                username_box.insert(0, 'Username')

        username_box = Entry(self.frame, width=36,textvariable= self.username, fg='grey', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
        username_box.place(x=70, y=100)
        #username_box.insert(0, 'Username')
        username_box.bind('<FocusIn>', on_enter)
        username_box.bind('FocusOut', on_leave)
        self.username.set('Username')


#-----------------------------------------

        def on_enter(e):
            email_box.delete(0, 'end')

        def on_leave(e):
            name = email_box.get()
            if name == '':
                email_box.insert(0, 'E-mail')

        email_box = Entry(self.frame,textvariable=self.email,  width=36, fg='grey', border=1, bg='white',
                       font=('Microsoft YaHei UI Light', 11))
        email_box.place(x=70, y=140)
        email_box.insert(0, 'E-mail')

        email_box.bind('<FocusIn>', on_enter)
        email_box.bind('FocusOut', on_leave)

        # Frame(frame, width=295,height=2,bg='black').place(x=40,y=107)
        # -----------------------------------------------------------------------------------

        def on_enter(e):
            entered_password_box.delete(0, 'end')

        def on_leave(e):
            name = entered_password_box.get()
            if name == '':
                entered_password_box.insert(0, 'Password')

        # hide password while entered
        entered_password_box = Entry(self.frame, textvariable= self.password, width=36, fg='grey', border=1, bg='white',
                                 font=('Microsoft YaHei UI Light', 11))
        entered_password_box.place(x=70, y=180)
        entered_password_box.insert(0, 'Password')
        entered_password_box.bind('<FocusIn>', on_enter)
        entered_password_box.bind('FocusOut', on_leave)

        # Frame(frame, width=295,height=2,bg='black').place(x=40,y=177)

        # ---------------------------------------------------
        def on_enter(e):
            confirm_password_box.delete(0, 'end')

        def on_leave(e):
            name = confirm_password_box.get()
            if name == '':
                confirm_password_box.insert(0, 'Confirm Password')

        confirm_password_box = Entry(self.frame, textvariable= self.confirm_password, width=36, fg='grey', border=1, bg='white',
                                   font=('Microsoft YaHei UI Light', 11))
        confirm_password_box.place(x=70, y=220)
        confirm_password_box.insert(0, 'Confirm Password')

        confirm_password_box.bind('<FocusIn>', on_enter)
        confirm_password_box.bind('<FocusOut>', on_leave)

        # -------------------------------------------------


        # role--------------------------------------------------------
        # date-birth -------------------------------------------------
        # home town

        # role_combo_box = Combobox(self.frame, textvariable=self.role,
        #                      values=[
        #                          "user",
        #                          "admin"], width=45)
        # role_combo_box.insert(0,'Role')
        # role_combo_box.place(x=70, y=300)

        # -----------------------------------------------------------------------------
        # in button place command=validateLogIn
        # colour when mouse on button
        Button(self.frame, width=41, pady=7, text='Sign up', fg='white', bg='#57a1f8', border=0,
               command=lambda: self.sign_up()).place(x=70,y=340)
        label = Label(self.frame, text="Already have an account ?", fg='black', bg='white',
                      font=('Microsoft YaHei UI Light', 10))
        label.place(x=107, y=390)

        sign_in_button = Button(self.frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                         command=lambda: self.sign)
        sign_in_button.place(x=270, y=393)


    # def sign_up_command(self, user):
    #     c = CreateUserCommand(self.sign_up_controller)
    #     c(user)

    def sign_up(self):
        user = RegisteredUser(self.first_name.get(), self.last_name.get(), self.username.get(), self.email.get(), self.password.get())
        self.sign_up_controller.create_account(user)
        messagebox.showinfo('SignUp', 'Successfully Sign up')
        self.window.destroy()

    def sign(self):
        self.window.destroy()

