from tkinter import *
import sqlite3
from tkinter.ttk import Treeview
from tkcalendar import Calendar
import datetime as datee

class MenuUtama:
    con = sqlite3.connect('catering.db')
    c = con.cursor()

    def __init__(self,root):
        self.root = root
        root.title('Menu Utama Catering')
        root.geometry("1020x500")
        root.config(bg='lightblue')
        self.wrapper1 = LabelFrame(root,text = "Form Pesanan Baru")
        self.wrapper1.pack(fill=BOTH,padx=15,pady=(15,0))
        self.wrapper2 = LabelFrame(root,text = "Data Pesanan",bg="#0f084b",fg="white")
        self.wrapper2.pack(fill=BOTH,expand=True,padx=15,pady=(0,15))



        #Function

        paket = IntVar()

        x = datee.datetime.now().strftime(f"%d - %m - %Y")

        cal = Calendar(self.wrapper1, selectmode = 'day')
        cal.grid(row=2,rowspan = 7, column = 3)

        def grad_date():
            dateTtl.config(text ="Tanggal yang dipilih : "+ cal.get_date())  

        def DatabaseView():
            trv.delete(*trv.get_children())
            con = sqlite3.connect('catering.db')
            c = con.cursor()
            c.execute("SELECT * FROM datapesananbarubaru")
            fetch = c.fetchall()
            for data in fetch:
                trv.insert('', 'end', values=(data[0],data[1], data[2], data[3],data[4],data[5],data[6],data[7]))
            con.commit()
            con.close()
        

        def clicked(value):
            if value == 1:
                myLabel=Label(self.wrapper1, text="Perikahan")
                myLabel.grid(row=3, column=0,sticky=W)
                #myLabel.delete(0,END)
            elif value == 2:
                myLabel =Label(self.wrapper1, text="Ulang Tahun")
                myLabel.grid(row=3, column=0,sticky=W)
                #myLabel.delete(0,END)


        #Tombol Form Pesanan
        nama = Label(self.wrapper1, text = 'Masukan Nama Anda ').grid(row=0, column=0,sticky=W)
        namaEntry = Entry(self.wrapper1,width =30)
        namaEntry.grid(row=0, column=1,sticky=W)
        paketLabel = Label(self.wrapper1, text = 'Pilih Paket Anda ').grid(row=1, column=0,sticky=W)
        r1 = Radiobutton(self.wrapper1,text='Pernikahan',variable=paket,value=1)
        r1.grid(row=1, column=1,sticky=W)
        r2 = Radiobutton(self.wrapper1,text='Ulang Tahun',variable=paket,value=2)
        r2.grid(row=2, column=1,sticky=W)
        pilihPaket = Button(self.wrapper1,text='Pilih Paket',command=lambda: clicked(paket.get()))
        pilihPaket.grid(row=3, column=1,sticky=W)
        porsi = Label(self.wrapper1, text = 'Porsi (Min 150)').grid(row=4, column=0,sticky=W)
        porsiEntry = Entry(self.wrapper1)
        porsiEntry.grid(row=4, column=1,sticky=W)
        alamat = Label(self.wrapper1,text = 'Alamat').grid(row=5, column=0,sticky=W)
        alamatEntry = Entry(self.wrapper1,width=30)
        alamatEntry.grid(row=5,column=1,sticky=W)
        tanggal = Label(self.wrapper1,text = 'Tanggal Pemesanan').grid(row=6, column=0,sticky=W)
        tanggalEntry = Label(self.wrapper1,text = x )
        tanggalEntry.grid(row=6, column=1,sticky=W)

        def hitungTotal():
            global hargaakhir
            if paket.get() == 1:
                porsi = int(porsiEntry.get())
                hargaakhir = porsi * 25000
                hargaCounter.config(text = 'Total Harga : '+str(hargaakhir))
                
            elif paket.get() == 2:
                porsi = int(porsiEntry.get())
                hargaakhir = porsi * 30000
                hargaCounter.config(text = 'Total Harga : '+str(hargaakhir))

        hargaCounter = Label (self.wrapper1,text = 'Total Harga : ')
        hargaCounter.grid(row=7, column=0,sticky=W)
        hargaButton = Button(self.wrapper1,text = "Hitung Harga", command=hitungTotal).grid(row=8,column=0,sticky=W)
        noLabel = Label(self.wrapper1,text ="Masukan NO Telpon :").grid(row=9,column=0,sticky=W)
        noEntry = Entry(self.wrapper1)
        noEntry.grid(row=9,column=1)
        gapMaker = Label(self.wrapper1,text = "       ").grid(row=0,rowspan=10,column=2)
        ttglkirim = Label(self.wrapper1,text = 'Tanggal Kirim ',bg="blue",fg="white").grid(row=0, column=3)
        saveBuxtton = Button(self.wrapper1,text='Pilih Tanggal',command=grad_date,bg="blue",fg="white")
        saveBuxtton.grid(row=9,column=3,sticky=W)
        dateTtl = Label(self.wrapper1,text ="Tanggal yang dipilih : ")
        dateTtl.grid(row=1,column=3)
        
        
        #Tombol Functions SQLITE
        
        def tambahData():
            trv.delete(*trv.get_children())
            con = sqlite3.connect('catering.db')
            c = con.cursor()
            if paket.get() == 1:
                paket1 = "Pernikahan"
            elif paket.get() == 2:
                paket1 = "Ulang Tahun"
            c.execute("INSERT INTO datapesananbarubaru VALUES (:nama, :paket, :porsi, :alamat, :tglpesan, :tglkirim, :harga, :notelp)",
                    {
                        'nama' : namaEntry.get(),
                        'paket' : paket1,
                        'porsi' : porsiEntry.get(),
                        'alamat' : alamatEntry.get(),
                        'tglpesan' : x,
                        'tglkirim' : cal.get_date(),
                        'harga' : hargaakhir,
                        'notelp' : noEntry.get(),
                    }
                    )
            con.commit()
            c.execute("SELECT * FROM datapesananbarubaru")
            fetch = c.fetchall()
            for data in fetch:
                    trv.insert('', 'end', values=(data[0],data[1], data[2], data[3],data[4],data[5],data[6],data[7]))

            con.commit()
            con.close()

        def hapusData():
            con = sqlite3.connect('catering.db')
            c = con.cursor()
            c.execute("DELETE FROM datapesananbarubaru WHERE notlp = "+dataNama.get())
            con.commit()
            trv.delete(*trv.get_children())
            c.execute("SELECT * FROM datapesananbarubaru")
            fetch = c.fetchall()
            for data in fetch:
                trv.insert('', 'end', values=(data[0],data[1], data[2], data[3],data[4],data[5],data[6],data[7]))
            con.commit()
            con.close()

        #Tombol Operasi
        #resetButton = Button(self.wrapper1,text="Reset Form",command=resetForm).grid(row=6,column=4)
        gapmaker2 = Label(self.wrapper1,text ="        ").grid(rowspan=9,column=5)
        labelHapus = Label(self.wrapper1,text ="Data yang akan dihapus adalah : ").grid(row=8,column=7)
        refreshButton = Button(self.wrapper1,text ="Refresh Table",bg="yellow",command=DatabaseView).grid(row=9,column=6)
        hapusButton = Button(self.wrapper1,text ="Hapus Data",bg="red",fg="white",command=hapusData).grid(row=9,column=8)
        dataNama = Entry(self.wrapper1)
        dataNama.grid(row=9,column=7)
        simpanButton = Button(self.wrapper1,text="Simpan Data",bg="green",fg="white",command=tambahData).grid(row=9,column=3,sticky=E)


        #Harga Menu
        menu1 = Label(self.wrapper1,text ="PAKET PERNIKAHAN \n 1. Ayam Gulai \n 2. Sop Kambing \n 3. Asinan \n 4. AQUA \n\n Rp.25,000",bg="lightblue").grid(row=1,rowspan=6,column=6)
        menu2 = Label(self.wrapper1,text ="PAKET ULANG TAHUN \n 1. Butter Cake \n 2. French Fries \n 3. Ice Cream \n 4. Fanta \n\n Rp.30,000",bg="lightblue").grid(row=1,rowspan=6,column=7)

        #Table View SQLite
        tree_scrollbar = Scrollbar(self.wrapper2)
        tree_scrollbar.pack(side=RIGHT,fill=Y)
        trv = Treeview(self.wrapper2,columns=(1,2,3,4,5,6,7,8),show='headings',yscrollcommand=tree_scrollbar.set)
        tree_scrollbar.config(command=trv.yview)
        
        trv.column(1,width=100)
        trv.column(2,width=100)
        trv.column(3,width=50)
        trv.column(4,width=200)
        trv.column(5,width=100)
        trv.column(6,width=100)
        trv.column(7,width=150)
        trv.column(8,width=150)

        trv.heading(1, text ="Nama")
        trv.heading(2, text ="Paket")
        trv.heading(3, text ="Porsi")
        trv.heading(4, text ="Alamat")
        trv.heading(5, text ="TGL Pesan")
        trv.heading(6, text ="TGL Kirim")
        trv.heading(7, text ="Total Harga")
        trv.heading(8, text ="No Telp")
        trv.pack()

        def selector(Event):
            dataNama.delete(0,END)
            selected = trv.focus()
            values = trv.item(selected,'values')
            dataNama.insert(0,values[7])
        
        #Event Listener
        trv.bind("<Double-1>",selector)

if __name__ == '__main__':
    root = Tk()
    application = MenuUtama(root)
    root.mainloop()