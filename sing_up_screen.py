from tkinter import *
from tkinter.ttk import Combobox
import ast
import tkinter.font as font
from PIL import ImageTk, Image
from tkinter import messagebox

class SignUp:
    def __init__(self, window):
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


        def sign_up(self):
            messagebox.showerror('SignUp', 'Successful registration')
            self.window.destroy()
        def sign(self):
            self.window.destroy()

        self.frame = Frame(c, width=430, height=600, bg="white") #,highlightbackground="#57a1f8", highlightthickness=2
        self.frame.place(x=270, y=30)
        self.frame.pack(padx=18, pady=30)
        heading = Label(self.window, text="Create your account", fg='#57a1f8', bg='white',
                        font=('Microsoft YaHei UI Light', 21, 'bold'))
        heading.place(x=320.5, y=30)

        # ----------------------------------------------------------------------------------
        def on_enter(e):
            username.delete(0, 'end')

        def on_leave(e):
            name = username.get()
            if name == '':
                username.insert(0, 'Username')

        first_name = Entry(self.frame, width=17, fg='grey', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
        first_name.place(x=70, y=60)
        first_name.insert(0, 'First name')

        last_name = Entry(self.frame, width=17, fg='grey', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
        last_name.place(x=220, y=60)
        last_name.insert(0, 'Last name')

        username = Entry(self.frame, width=36, fg='grey', border=1, bg='white', font=('Microsoft YaHei UI Light', 11))
        username.place(x=70, y=100)
        username.insert(0, 'Username')
        username.bind('<FocusIn>', on_enter)
        username.bind('FocusOut', on_leave)


#-----------------------------------------
        e_mail = Entry(self.frame, width=36, fg='grey', border=1, bg='white',
                       font=('Microsoft YaHei UI Light', 11))
        e_mail.place(x=70, y=140)
        e_mail.insert(0, 'E-mail')
        # Frame(frame, width=295,height=2,bg='black').place(x=40,y=107)
        # -----------------------------------------------------------------------------------

        def on_enter(e):
            entered_password.delete(0, 'end')

        def on_leave(e):
            name = entered_password.get()
            if name == '':
                entered_password.insert(0, 'Password')

        # hide password while entered
        entered_password = Entry(self.frame, width=36, fg='grey', border=1, bg='white',
                                 font=('Microsoft YaHei UI Light', 11))
        entered_password.place(x=70, y=180)
        entered_password.insert(0, 'Password')
        entered_password.bind('<FocusIn>', on_enter)
        entered_password.bind('FocusOut', on_leave)

        # Frame(frame, width=295,height=2,bg='black').place(x=40,y=177)

        # ---------------------------------------------------
        reentered_password = Entry(self.frame, width=36, fg='grey', border=1, bg='white',
                                   font=('Microsoft YaHei UI Light', 11))
        reentered_password.place(x=70, y=220)
        reentered_password.insert(0, 'Confirm Password')
        # -------------------------------------------------


        # role--------------------------------------------------------
        # date-birth -------------------------------------------------
        # hote town

        combo_box = Combobox(self.frame,
                             values=[
                                 "user",
                                 "admin"], width=45)

        combo_box.place(x=70, y=300)
        # self, first_name = None, last_name = None,
        # #username = None, email = None, password = None, profile_picture = None, role = Role.USER, id = None, active=True

        # -----------------------------------------------------------------------------
        # in button place command=validateLogIn
        # colour when mouse on button
        Button(self.frame, width=41, pady=7, text='Sign up', fg='white', bg='#57a1f8', border=0, command=sign_up).place(x=70,
                                                                                                                  y=340)
        label = Label(self.frame, text="Already have an account ?", fg='black', bg='white',
                      font=('Microsoft YaHei UI Light', 10))
        label.place(x=107, y=390)

        sign_up_button = Button(self.frame, width=6, text='Sign In', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                         command=sign)
        sign_up_button.place(x=270, y=393)

