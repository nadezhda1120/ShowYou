from idlelib import window
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

from sing_up_screen import SignUp
import ast

root= Tk()
root.title('Sign in')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def sign_in():
    username=user.get()
    password=code.get()

    if username == 'admin' and password == '1234':
        screen=Toplevel(root)
        screen.title('App')
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen,text= 'Hello EveryOne!', bg= '#fff',font=('Microsoft YaHei UI Light',50, 'bold')).pack(expand=True)
        #print('Successfully Logged In')

        screen.mainloop()
    elif username != 'admin' or password != '1234':
        messagebox.showerror('Invalid','Invalid username or password')


#---------------------------------------------------------------
def signup_command():
    window=Toplevel(root)
    # def signup()
    #window.destroy()
    w = SignUp(window)

#---------------------------------------------------------------------------
img = ImageTk.PhotoImage(Image.open("images/login.png"))
Label(root,image=img, bg = 'white').place(x=50,y=50,width=400,height=400)
frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

#frame['relief'] = 'sunken'
heading = Label(frame, text="Sign In", fg='#57a1f8',bg='white', font=('Microsoft YaHei UI Light',23, 'bold'))
heading.place(x=150,y=5)

#----------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name== '':
        user.insert(0, 'Username')

user = Entry(frame, width=25,fg='grey',border=0, bg= 'white', font=('Microsoft YaHei UI Light',11))
user.place(x=75,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('FocusOut',on_leave)

Frame(frame, width=270,height=2,bg='black').place(x=70,y=107)
#-----------------------------------------------------------------------------------

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name== '':
        code.insert(0, 'Password')

#hide password while entered
code = Entry(frame, width=25,fg='grey',border=0, bg= 'white', font=('Microsoft YaHei UI Light',11))
code.place(x=75,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('FocusOut',on_leave)

Frame(frame, width=270,height=2,bg='black').place(x=70,y=177)
#-----------------------------------------------------------------------------
#in button place command=validateLogIn
# colour when mouse on button
Button(frame,width=38,pady=7,text='Sign In',fg='white',bg='#57a1f8',border=0, command=sign_in).place(x=70,y=220)
label=Label(frame, text="Don't have an account ?", fg='black',bg='white', font=('Microsoft YaHei UI Light',10))
label.place(x=100,y=270)


sign_up= Button(frame, width=6,text='Sign Up', border=0, bg='white', cursor='hand2',fg= '#57a1f8', command=signup_command)
sign_up.place(x=257,y= 274)

sign_up= Button(frame, width=30,text='Continue without an account', border=0, bg='white', cursor='hand2',fg= '#57a1f8')
sign_up.place(x=100,y= 320)

root.mainloop()