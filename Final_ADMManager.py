from tkinter import *
from tkinter.ttk import Treeview
import sqlite3
from tkinter import messagebox
import Final_Login as fl

class ADMManager:
    
    def __init__(self,rootADM):
        self.rootADM = rootADM
        rootADM.geometry("1020x600")
        rootADM.title('Admin Manager')
        self.wrapper1 = LabelFrame(rootADM,text="Form Data Admin")
        self.wrapper1.pack(fill=BOTH,padx=15)
        self.wrapper2 = LabelFrame(rootADM,text="Daftar Data Admin ")
        self.wrapper2.pack(fill=BOTH,padx=15,pady=(0,15))
        self.wrapper3 = LabelFrame(rootADM,text="Riwayat Login / Masuk")
        self.wrapper3.pack(fill=BOTH,expand=True,padx=15,pady=(0,15))

        # Function Mengambil data dari database table datakaryawan1
    
        def DatabaseView():
            trv.delete(*trv.get_children())
            con = sqlite3.connect('catering.db')
            c = con.cursor()
            c.execute("SELECT * FROM datakaryawan1")
            fetch = c.fetchall()
            for data in fetch:
                trv.insert('', 'end', values=(data[0],data[1], data[2], data[3]))
            con.commit()
            con.close()

        # Function Mengambil data dari database table logadmin
    
        def DatabaseViewLog():
            trve.delete(*trve.get_children())
            con = sqlite3.connect('catering.db')
            c = con.cursor()
            c.execute("SELECT * FROM logadmin ORDER BY tglmasuk DESC")
            fetch = c.fetchall()
            for data in fetch:
                trve.insert('', 'end', values=(data[0],data[1], data[2]))
            con.commit()
            con.close()

        # Form Manajemen Admin

        idLabel = Label(self.wrapper1,text="ID Admin").grid(row=0,column=0)
        idEntry = Entry(self.wrapper1)
        idEntry.grid(row=0,column=1)
        namaLabel = Label(self.wrapper1,text ="Nama").grid(row=1,column=0)
        namaEntry = Entry(self.wrapper1)
        namaEntry.grid(row=1,column=1)
        gapMaker = Label(self.wrapper1,text ="       ").grid(row=0,rowspan=3,column=2)
        alamatLabel = Label(self.wrapper1,text="Password").grid(row=0,column=3)
        passwordEntry = Entry(self.wrapper1)
        passwordEntry.grid(row=0,column=4)
        noLabel = Label(self.wrapper1,text ="No TELP").grid(row=1,column=3)
        noEntry = Entry(self.wrapper1)
        noEntry.grid(row=1,column=4)
        gapMaker2 = Label(self.wrapper1,text ="          ").grid(row=0,rowspan=3,column=5)
        
        # Functions SQLITE

        # Function untuk memastikan form tidak kosong
        def validasi():
            return idEntry.get() != "" and namaEntry.get() != "" and passwordEntry.get() != "" and noEntry.get() != ""

        # Function menambah data yang sudah di input ke dalam database sqlite3
        def tambahData():
            if validasi():
                try:
                    trv.delete(*trv.get_children())
                    con = sqlite3.connect('catering.db')
                    c = con.cursor()
                    c.execute("INSERT INTO datakaryawan1 VALUES (:id, :nama, :password, :no)",
                            {
                                'id' : idEntry.get(),
                                'nama' : namaEntry.get(),
                                'password' : passwordEntry.get(),
                                'no' : noEntry.get()
                            } 
                            )
                            
                    con.commit()
                    c.execute("SELECT * FROM datakaryawan1")
                    fetch = c.fetchall()
                    for data in fetch:
                            trv.insert('', 'end', values=(data[0],data[1], data[2], data[3]))
                    con.commit()
                    con.close()
                    messagebox.showinfo("SUCCESS","Data Berhasil Disimpan!")
                    resetForm()
                except ValueError:
                    messagebox.showerror("ERROR","Silahkan Masukan data yang benar!")

            else:
                messagebox.showerror("ERROR","Silahkan Isi semua data!")

        # Function mengupdate data yang sudah di pilih ke dalam database sqlite3
        def updateData():
            if validasi():
                try:
                    trv.delete(*trv.get_children())
                    con = sqlite3.connect('catering.db')
                    c = con.cursor()
                    c.execute(f"UPDATE datakaryawan1 SET id = :id, nama = :nama, password = :password, notlp = :notlp WHERE id = '{hapusEntry.get()}'",
                            {
                                'id' : idEntry.get(),
                                'nama' : namaEntry.get(),
                                'password' : passwordEntry.get(),
                                'notlp' : noEntry.get()
                            }
                            )
                    con.commit()
                    c.execute("SELECT * FROM datakaryawan1")
                    fetch = c.fetchall()
                    for data in fetch:
                            trv.insert('', 'end', values=(data[0],data[1], data[2], data[3]))
                    con.commit()
                    con.close()
                    resetForm()
                    messagebox.showinfo("SUCCESS","Data Berhasil Diupdate!")
                except ValueError:
                    messagebox.showerror("ERROR","Silahkan Masukan data yang benar!")
            else:
                messagebox.showerror("ERROR","Silahkan isi data!")

        #Functions untuk memastikan data yang dipilih tidak kosong
        def validData():
            return len(hapusEntry.get()) != 0
        
        # Functions untuk menghapus data yang dipilih dari table
        def hapusData():
            if validData():
                try:
                    con = sqlite3.connect('catering.db')
                    c = con.cursor()
                    c.execute(f"DELETE FROM datakaryawan1 WHERE id = '{hapusEntry.get()}'")
                    con.commit()
                    trv.delete(*trv.get_children())
                    c.execute("SELECT * FROM datakaryawan1")
                    fetch = c.fetchall()
                    for data in fetch:
                        trv.insert('', 'end', values=(data[0],data[1], data[2], data[3]))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Data Berhasil Dihapus")
                    resetForm()
                except:
                    messagebox.showerror("ERROR","Ada yang Salah")
            else:
                messagebox.showerror("ERROR","Masukin ID Data!")

         # Function untuk Mereset form pesanan agar kosong
        def resetForm():
            try:
                idEntry.delete(0,END)
                namaEntry.delete(0,END)
                passwordEntry.delete(0,END)
                noEntry.delete(0,END)
                hapusEntry.delete(0,END)
            except:
                messagebox.showerror("ERROR","Data Kosong!")

        # Function Exit ADMManager
        def exitForm():
            rootADM.destroy()
            #Menampilkan window baru (Final_Login)
            rootLogin = Tk()
            fl.loginForm(rootLogin)
            rootLogin.mainloop()
            

        # Tombol untuk melaksanakan Function SQLITE
        exitButton = Button(self.wrapper3,text="EXIT",bg="red",fg="white",command=exitForm).pack(side=BOTTOM)
        hapusButton = Button(self.wrapper1,text ="Hapus",bg="red",fg="white",command=hapusData).grid(row=0,column=8)
        viewButtonLog = Button(self.wrapper3,text ="Lihat Riwayat Login",bg='green',fg="white",command=DatabaseViewLog).pack()
        viewButton = Button(self.wrapper2,text ="Lihat Data",bg='green',fg="white",command=DatabaseView).pack()
        resetButton = Button(self.wrapper1,text ="Reset Form",bg='green',fg="white",command=resetForm).grid(row=1,column=7)
        saveButton = Button(self.wrapper1,text ="Simpan",bg='green',fg="white",command=tambahData).grid(row=0,column=6)
        updateButton = Button(self.wrapper1,text="Update",bg='yellow',command=updateData).grid(row=1,column=6)
        hapusEntry = Entry(self.wrapper1)
        hapusEntry.grid(row=0,column=7,padx=(2,15))


        # Menampilkan Isi di table dari database Daftar Admin / daftarkaryawan1

        tree_scrollbar = Scrollbar(self.wrapper2)
        tree_scrollbar.pack(side=RIGHT,fill=Y)
        trv = Treeview(self.wrapper2,columns=(1,2,3,4),show='headings',yscrollcommand=tree_scrollbar.set)
        tree_scrollbar.config(command=trv.yview)
        
        trv.column(1,width=50)
        trv.column(2,width=150)
        trv.column(3,width=300)
        trv.column(4,width=200)
        trv.heading(1, text ="ID")
        trv.heading(2, text ="Nama")
        trv.heading(3, text ="Password")
        trv.heading(4, text ="No TELP")
        trv.pack()
        
        # Menampilkan Isi di table dari database Riwayat Login / logadmin

        tree_scrollbar = Scrollbar(self.wrapper3)
        tree_scrollbar.pack(side=RIGHT,fill=Y)
        trve = Treeview(self.wrapper3,columns=(1,2,3),show='headings',yscrollcommand=tree_scrollbar.set)
        tree_scrollbar.config(command=trve.yview)
        
        trve.column(1,width=150)
        trve.column(2,width=200)
        trve.column(3,width=200)
        trve.heading(1, text ="Nama")
        trve.heading(2, text ="Waktu Masuk")
        trve.heading(3, text ="Waktu Keluar")
        trve.pack()

        # Function Memilih table agar muncul di form
        def selector(Event):
            resetForm()
            hapusEntry.delete(0,END)
            selected = trv.focus()
            values = trv.item(selected,'values')
            hapusEntry.insert(0,values[0])
            idEntry.insert(0,values[0])
            namaEntry.insert(0,values[1])
            passwordEntry.insert(0,values[2])
            noEntry.insert(0,values[3])

        # Event Listener untuk mendengarkan double klik
        trv.bind("<Double-1>",selector)




if __name__ == '__main__':
    rootADM = Tk()
    application = fl.loginForm(rootADM)
    rootADM.mainloop()
