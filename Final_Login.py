from tkinter import *
from Final_Menu import *
from tkinter import messagebox

class loginForm:

    user = 'admin'

    def __init__(self,root):

        self.root = root
        self.root.title('LOGIN')
        root.iconbitmap('key.ico')
        Label(text = ' PASSWORD ',font='Times 15',bg='#002233',fg='white').place(x = 200, y =100)
        self.username = Entry(show='*')
        self.username.place(x=200,y=135)
 

        self.lala = Button(text='LOGIN',command=self.login_userButton)
        self.lala.place(x=240,y=170)
        root.bind("<Return>",self.login_userEnter)

    def login_userButton(self):
        if self.username.get() == self.user:
            root.destroy()
            #Open new window
            newroot = Tk()
            application = MenuUtama(newroot)
            newroot.mainloop()
        else:
            messagebox.showerror("ERROR","Username salah! Silahkan coba lagi")
            self.username.delete(0,END)

    def login_userEnter(self,Event):
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
    root.geometry("500x300")
    bg = PhotoImage(file="Menuu.png")
    label1 = Label(root, image = bg)
    label1.place(x = 0, y = 0)
    application = loginForm(root)
    root.mainloop()