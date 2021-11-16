from tkinter import *
import sqlite3
from tkcalendar import Calendar
import datetime as datee

class MenuUtama:

    db_name = 'catering.db' 





    def __init__(self,root):

        self.root = root
        root.title('Menu Utama')
        bg1 = PhotoImage(file='Menu1.png')
        label11 = Label(root, image = bg1)
        label11.place(x = 0, y = 0)

        #Function

        paket = IntVar
        x = datee.datetime.now().strftime(f"%d - %b - %Y")

        cal = Calendar(root, selectmode = 'day')

        cal.grid(row=2,rowspan = 7, column = 3)

        def grad_date():
            dateTtl.config(text ="Tanggal yang dipilih : "+ cal.get_date())       

        #Tombol Data Baru
        
        nama = Label(root, text = 'Masukan Nama Anda ').grid(row=0, column=0,sticky=W)
        namaEntry = Entry(root,width =30).grid(row=0, column=1,sticky=W)
        paket = Label(root, text = 'Pilih Paket Anda ').grid(row=1, column=0,sticky=W)
        r1 = Radiobutton(root,text='Pernikahan',variable=paket,value=1).grid(row=1, column=1,sticky=W)
        r2 = Radiobutton(root,text='Ulang Tahun',variable=paket,value=2).grid(row=2, column=1,sticky=W)
        r3 = Radiobutton(root,text='Hajatan',variable=paket,value=3).grid(row=3, column=1,sticky=W)
        porsi = Label(root, text = 'Porsi ').grid(row=4, column=0,sticky=W)
        porsiEntry = Entry(root,width =30).grid(row=4, column=1,sticky=W)
        alamat = Label(root,text = 'Alamat').grid(row=5, column=0,sticky=W)
        alamatEntry = Entry(root).grid(row=5,column=1,sticky=W)
        tanggal = Label(root,text = 'Tanggal Pemesanan').grid(row=6, column=0,sticky=W)
        tanggalEntry = Label(root,text = x ).grid(row=6, column=1,sticky=W)
        gapMaker = Label(root,text ="     ").grid(row=0,rowspan=10,column=2)
        ttglkirim = Label(root,text = 'Tanggal Kirim').grid(row=0, column=3)
        saveBuxtton = Button(root,text='Pilih Tanggal',command=grad_date).grid(row=9,column=3)
        dateTtl = Label(root,text ="Tanggal yang dipilih : ")
        dateTtl.grid(row=1,column=3)

        #Table View SQLite









if __name__ == '__main__':

    root = Tk()
    root.title('Menu Utama')
    bg = PhotoImage(file='Menu.png')
    label1 = Label(root, image = bg)
    label1.place(x = 0, y = 0)
    application = MenuUtama(root)
    root.mainloop()