from tkinter import *
from Final_Menu import *

class loginForm:

    user = 'admin'

    def __init__(self,root):

        self.root = root
        self.root.title('LOGIN SCREEN')

        Label(text = ' Username ',font='Times 15').place(x = 200, y =175)
        self.username = Entry()
        self.username.place(x=200,y=200)

        Button(text='LOGIN',command=self.login_user).place(x=200,y=220)
        Button(text='REGISTRASI',command=self.registerForm).place(x=250,y=220)

    def userBaru(self):
        self.userBaru = Toplevel(root)
        infoBaru = self.namaUser
        self.tambahUser = self.user.append(infoBaru)
        if infoBaru in self.user and self.passrahasia == '2001':
            Label(self.userBaru,text="Berhasil !").pack()
        else:
            Label(self.userBaru,text="Gagal!").pack()

    def registerForm(self):
        self.registerForm = Toplevel(root)
        self.registerForm.title('REGISTRASI')
        Label(self.registerForm,text="Masukan User Baru :").grid(row=0,column=0)
        self.namaUser = Entry(self.registerForm,width=50).grid(row=1,column=0)
        Label(self.registerForm,text="Password Admin :").grid(row=2,column=0)
        self.passrahasia = Entry(self.registerForm,width=50).grid(row=3,column=0)
        Button(self.registerForm,text='REGISTER',command=self.userBaru).grid(row=4,column=0)

    def login_user(self):
        if self.username.get() == self.user:
            root.destroy()
            #Open new window
            newroot = Tk()
            application = MenuUtama(newroot)
            newroot.mainloop()
        else:
            self.message = Label(text = 'Username or Password incorrect. Try again!',fg = 'Red')
            self.message.place(x=200,y=250)

if __name__ == '__main__':

    root = Tk()
    root.geometry("700x500")
    bg = PhotoImage(file="Menu.png")
    label1 = Label(root, image = bg)
    label1.place(x = 0, y = 0)
    application = loginForm(root)
    root.mainloop()