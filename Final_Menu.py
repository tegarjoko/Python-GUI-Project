from tkinter import *
import sqlite3
from tkinter.ttk import Treeview
from tkcalendar import Calendar
import datetime as datee

class MenuUtama:

    db_name = 'catering.db' 

    def __init__(self,root):

        self.root = root
        root.title('Menu Utama Catering')
        root.geometry("700x500")
        bg1 = PhotoImage(file='Menu1.png')
        label11 = Label(root, image = bg1)
        wrapper1 = LabelFrame(root,text = "Form Pesanan Baru",bg="#a6cfd5")
        wrapper1.pack(fill=BOTH,padx=15,pady=(15,0))
        wrapper2 = LabelFrame(root,text = "Data Pesanan",bg="#0f084b",fg="white")
        wrapper2.pack(fill=BOTH,expand=True,padx=15,pady=(0,15))
        

        #Function

        paket = IntVar
        x = datee.datetime.now().strftime(f"%d - %b - %Y")

        cal = Calendar(wrapper1, selectmode = 'day')
        cal.grid(row=2,rowspan = 7, column = 3)

        def grad_date():
            dateTtl.config(text ="Tanggal yang dipilih : "+ cal.get_date())       

        #Tombol Form Pesanan
        nama = Label(wrapper1, text = 'Masukan Nama Anda ').grid(row=0, column=0,sticky=W)
        namaEntry = Entry(wrapper1,width =30).grid(row=0, column=1,sticky=W)
        paket = Label(wrapper1, text = 'Pilih Paket Anda ').grid(row=1, column=0,sticky=W)
        r1 = Radiobutton(wrapper1,text='Pernikahan',variable=paket,value=1).grid(row=1, column=1,sticky=W)
        r2 = Radiobutton(wrapper1,text='Ulang Tahun',variable=paket,value=2).grid(row=2, column=1,sticky=W)
        r3 = Radiobutton(wrapper1,text='Hajatan',variable=paket,value=3).grid(row=3, column=1,sticky=W)
        porsi = Label(wrapper1, text = 'Porsi ').grid(row=4, column=0,sticky=W)
        porsiEntry = Entry(wrapper1).grid(row=4, column=1,sticky=W)
        alamat = Label(wrapper1,text = 'Alamat').grid(row=5, column=0,sticky=W)
        alamatEntry = Entry(wrapper1,width=30).grid(row=5,column=1,sticky=W)
        tanggal = Label(wrapper1,text = 'Tanggal Pemesanan').grid(row=6, column=0,sticky=W)
        tanggalEntry = Label(wrapper1,text = x ).grid(row=6, column=1,sticky=W)
        gapMaker = Label(wrapper1,text ="     ").grid(row=0,rowspan=10,column=2)
        ttglkirim = Label(wrapper1,text = 'Tanggal Kirim').grid(row=0, column=3)
        saveBuxtton = Button(wrapper1,text='Pilih Tanggal',command=grad_date).grid(row=9,column=3)
        dateTtl = Label(wrapper1,text ="Tanggal yang dipilih : ")
        dateTtl.grid(row=1,column=3)

        #Table View SQLite
        trv = Treeview(wrapper2,columns=(1,2,3,4,5,6,7),show='headings',padding=10)
        trv.column(1,width=15)
        trv.column(2,width=100)
        trv.column(3,width=100)
        trv.column(4,width=50)
        trv.column(5,width=200)
        trv.column(6,width=100)
        trv.column(7,width=100)

        trv.heading(1, text ="ID")
        trv.heading(2, text ="Nama")
        trv.heading(3, text ="Paket")
        trv.heading(4, text ="Porsi")
        trv.heading(5, text ="Alamat")
        trv.heading(6, text ="TGL Pesan")
        trv.heading(7, text ="TGL Kirim")
        trv.pack()
        









if __name__ == '__main__':

    root = Tk()
    root.title('Menu Utama')
    bg = PhotoImage(file='Menu.png')
    label1 = Label(root, image = bg)
    label1.place(x = 0, y = 0)
    application = MenuUtama(root)
    root.mainloop()