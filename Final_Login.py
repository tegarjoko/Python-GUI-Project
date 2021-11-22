from tkinter import *
from Final_Menu import *
from tkinter import messagebox

class loginForm:

    user = 'admin'

    def __init__(self,root):

        self.root = root
        self.root.title('LOGIN SCREEN')

        Label(text = ' Username ',font='Times 15').place(x = 200, y =175)
        self.username = Entry()
        self.username.place(x=200,y=200)

        Button(text='LOGIN',command=self.login_user).place(x=200,y=220)

    def login_user(self):
        if self.username.get() == self.user:
            root.destroy()
            #Open new window
            newroot = Tk()
            application = MenuUtama(newroot)
            newroot.mainloop()
        else:
            messagebox.showerror("ERROR","Username salah! Silahkan coba lagi")
            self.username.delete(0,END)

if __name__ == '__main__':

    root = Tk()
    root.geometry("700x500")
    bg = PhotoImage(file="Menu.png")
    label1 = Label(root, image = bg)
    label1.place(x = 0, y = 0)
    application = loginForm(root)
    root.mainloop()