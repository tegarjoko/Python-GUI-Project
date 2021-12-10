from tkinter import *
import Final_ADMManager as fa
import Final_Menu as fm
from tkinter import messagebox
import sqlite3
import datetime as datee

class loginForm:

    def __init__(self,rootLogin):
        self.rootLogin = rootLogin
        rootLogin.geometry("500x300")
        self.bg = PhotoImage(file="Menuu.png")
        self.label1 = Label(rootLogin, image = self.bg)
        self.label1.place(x = 0, y = 0)
        self.rootLogin.iconbitmap('key.ico')

        # Memanggil tanggal dan waktu sekarang
        self.startdate = datee.datetime.now().strftime(f"%d/%m/%y - %X")

        # Form untuk login username dan password
        global username
        self.rootLogin.title('LOGIN')
        Label(text = ' USERNAME ',font='Times 10',bg='#002233',fg='white').place(x = 220, y =45)
        self.username = Entry()
        self.username.place(x=200,y=70)
        Label(text = ' PASSWORD ',font='Times 10',bg='#002233',fg='white').place(x = 220, y =110)
        self.password = Entry(show='*')
        self.password.place(x=200,y=135)
        self.lala = Button(text='MASUK',command=self.login_userButton)
        self.lala.place(x=240,y=170)
        rootLogin.bind("<Return>",self.login_userEnter)
        self.dashboard = Button(text='Manage Admin',command=self.adminManager).place(x=400,y=250)

        # Membuat Toplevel() untuk membuat window diatas window (popup) , Toplvel iini untuk menampilkan login owner
    def adminManager(self):
        global admwindow
        admwindow = Toplevel()
        admwindow.title('MASUKAN PASSWORD OWNER')
        admwindow.geometry("300x70")
        global passOwnerEntry
        passOwnerEntry = Entry(admwindow,show='*')
        passOwnerEntry.grid(row=0,column=1, sticky=E)
        passOwnerButton = Button(admwindow,text='MASUK',command=self.loginADM).grid(rowspan=2)  
        passOwnerLabel = Label(admwindow,text='PASSWORD',padx=15).grid(row=0,column=0, sticky=W)
        admwindow.mainloop()
        
        # Function berisi logika untuk ketika login button di window login owner dipencet
    def loginADM(self):
        if passOwnerEntry.get() == 'rahasia':
            admwindow.destroy()
            self.rootLogin.destroy()
            newroot2 = Tk()
            application = fa.ADMManager(newroot2)
            newroot2.mainloop()
        else:
            messagebox.showerror("ERROR","Salah!")
            passOwnerEntry.delete(0,END)

        # Function berisi logika dan sql query execute ketika tombol login di pencet
    def login_userButton(self):
        con = sqlite3.connect('catering.db')
        c = con.cursor()
        c.execute(f"SELECT * FROM datakaryawan1 where nama = '{self.username.get()}' and password = '{self.password.get()}'")
        fetch = c.fetchone()
        if fetch:
            c.execute(f"INSERT INTO logadmin (nama,tglmasuk) VALUES ('{self.username.get()}','{self.startdate}')")
            con.commit()
            con.close()
            self.rootLogin.destroy()
            #Open new window (Final_Menu)
            newroot = Tk()
            application = fm.MenuUtama(newroot)
            newroot.mainloop()
        else:
            messagebox.showerror("ERROR","Username atau Password salah! Silahkan coba lagi")
            self.username.delete(0,END)
            self.password.delete(0,END)

        # Function berisi logika dan sql query execute ketika tombol ENTER di keyboard di pencet
    def login_userEnter(self,Event):
        con = sqlite3.connect('catering.db')
        c = con.cursor()
        c.execute(f"SELECT * FROM datakaryawan1 where nama = '{self.username.get()}' and password = '{self.password.get()}'")
        fetch = c.fetchone()
        if fetch:
            c.execute(f"INSERT INTO logadmin (nama,tglmasuk) VALUES ('{self.username.get()}','{self.startdate}')")
            con.commit()
            con.close()
            self.rootLogin.destroy()
            # Open new window (Final_Menu)
            newroot = Tk()
            application = fm.MenuUtama(newroot)
            newroot.mainloop()
        else:
            messagebox.showerror("ERROR","Username atau Password salah! Silahkan coba lagi")
            self.username.delete(0,END)
            self.password.delete(0,END)


if __name__ == '__main__':

    rootLogin = Tk()
    application = loginForm(rootLogin)
    rootLogin.mainloop()