from tkinter import *
import Final_Login as fl
import sqlite3
from tkinter.ttk import Treeview
from tkcalendar import Calendar
import datetime as datee
from tkinter import messagebox


class MenuUtama:
    def __init__(self, root):
        self.root = root
        root.title("Menu Utama Catering")
        root.geometry("1020x600")
        root.config(bg="lightblue")
        root.iconbitmap("menu-ico.ico")
        self.wrapper1 = LabelFrame(root, text="Form Pesanan Baru")
        self.wrapper1.pack(fill=BOTH, padx=15, pady=(15, 0))
        self.wrapper2 = LabelFrame(
            root, text="Data Pesanan", bg="lightblue", fg="black"
        )
        self.wrapper2.pack(fill=BOTH, expand=True, padx=15, pady=(0, 15))

        # Function

        # Mengdeklarasi paket sebagai variabel integer

        paket = IntVar()

        # Memanggil tanggal sekarang

        x = datee.datetime.now().strftime(f"%d/%m/%y")

        # Function untuk Memilih tanggal

        cal = Calendar(self.wrapper1, selectmode="day")
        cal.grid(row=2, rowspan=7, column=3)

        # Mengambil data tanggal yang dipilih dari Calender

        def grad_date():
            dateTtl.config(text="Tanggal yang dipilih : " + cal.get_date())

        # Melihat isi table dari database sqlite3

        def DatabaseView():
            trv.delete(*trv.get_children())
            con = sqlite3.connect("catering.db")
            c = con.cursor()
            c.execute("SELECT * FROM datapesananbarubaru ORDER BY tgl_krm ASC")
            fetch = c.fetchall()
            for data in fetch:
                trv.insert(
                    "",
                    "end",
                    values=(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5],
                        data[6],
                        data[7],
                    ),
                )
            con.commit()
            con.close()

        # Tombol Form Pesanan

        nama = Label(self.wrapper1, text="Masukan Nama Anda ").grid(
            row=0, column=0, sticky=W
        )
        namaEntry = Entry(self.wrapper1, width=30)
        namaEntry.grid(row=0, column=1, sticky=W)
        paketLabel = Label(self.wrapper1, text="Pilih Paket Anda ").grid(
            row=1, column=0, sticky=W
        )
        myLabel = Label(self.wrapper1, text="")
        myLabel.grid(row=3, column=0, sticky=W)
        r1 = Radiobutton(self.wrapper1, text="Pernikahan", variable=paket, value=1)
        r1.grid(row=1, column=1, sticky=W)
        r2 = Radiobutton(self.wrapper1, text="Ulang Tahun", variable=paket, value=2)
        r2.grid(row=2, column=1, sticky=W)
        pilihPaket = Button(
            self.wrapper1, text="Pilih Paket", command=lambda: clicked(paket.get())
        )
        pilihPaket.grid(row=3, column=1, sticky=W)
        porsi = Label(self.wrapper1, text="Porsi (Min 150)").grid(
            row=4, column=0, sticky=W
        )
        porsiEntry = Entry(self.wrapper1)
        porsiEntry.grid(row=4, column=1, sticky=W)
        alamat = Label(self.wrapper1, text="Alamat").grid(row=5, column=0, sticky=W)
        alamatEntry = Entry(self.wrapper1, width=30)
        alamatEntry.grid(row=5, column=1, sticky=W)
        tanggal = Label(self.wrapper1, text="Tanggal Pemesanan").grid(
            row=6, column=0, sticky=W
        )
        tanggalEntry = Label(self.wrapper1, text=x)
        tanggalEntry.grid(row=6, column=1, sticky=W)

        # Menampilkan paket yang dipilih dari radiobutton

        def clicked(value):
            if value == 1:
                myLabel.config(text="Pernikahan")
            elif value == 2:
                myLabel.config(text="Ulang Tahun")

        # Menghitung Total dari harga paket dikali jumlah porsi

        def hitungTotal():
            global hargaakhir
            try:
                if paket.get() == 1 and int(porsiEntry.get()) >= 150:
                    porsi = int(porsiEntry.get())
                    hargaakhir = porsi * 25000
                    hargaCounter.config(text="Total Harga : " + str(hargaakhir))
                elif paket.get() == 2 and int(porsiEntry.get()) >= 150:
                    porsi = int(porsiEntry.get())
                    hargaakhir = porsi * 30000
                    hargaCounter.config(text="Total Harga : " + str(hargaakhir))
                else:
                    messagebox.showerror(
                        "ERROR", "Silahkan Pilih Paket dan Porsi diatas 150!"
                    )
            except:
                messagebox.showerror("ERROR", "Silahkan isi porsi!")

        # Function menghitung kembalian dari total harga dikurangi cash

        def hitungKembalian():
            try:
                cash = int(inputCash.get())
                kembaliannya = cash - hargaakhir
                kembalianOutput.config(text="" + str(kembaliannya))
            except:
                messagebox.showerror("ERROR", "Ada yang salah")

        # Lanjutan form Pesanan

        hargaCounter = Label(self.wrapper1, text="Total Harga : ")
        hargaCounter.grid(row=7, column=0, sticky=W)
        inputCashHolder = Label(self.wrapper1, text="Cash :").grid(
            row=7, column=1, sticky=W
        )
        inputCash = Entry(self.wrapper1, width=20)
        inputCash.grid(row=7, column=1, sticky=E)
        kembalianHolder = Button(
            self.wrapper1, text="Hitung Kembalian", command=hitungKembalian
        ).grid(row=8, column=1, sticky=W)
        kembalianOutput = Label(self.wrapper1, text="")
        kembalianOutput.grid(row=8, column=1, sticky=E)
        hargaButton = Button(
            self.wrapper1, text="Hitung Harga", command=hitungTotal
        ).grid(row=8, column=0, sticky=W)
        noLabel = Label(self.wrapper1, text="NO Telepon :").grid(
            row=9, column=0, sticky=W
        )
        noEntry = Entry(self.wrapper1)
        noEntry.grid(row=9, column=1, sticky=W)
        gapMaker = Label(self.wrapper1, text="       ").grid(
            row=0, rowspan=10, column=2
        )
        ttglkirim = Label(
            self.wrapper1, text="Tanggal Kirim ", bg="blue", fg="white"
        ).grid(row=0, column=3)
        saveBuxtton = Button(
            self.wrapper1,
            text="Pilih Tanggal",
            command=grad_date,
            bg="blue",
            fg="white",
        )
        saveBuxtton.grid(row=9, column=3, sticky=W)
        dateTtl = Label(self.wrapper1, text="Tanggal yang dipilih : ")
        dateTtl.grid(row=1, column=3)

        # Functions SQLITE

        # Function untuk memastikan form tidak kosong

        def validasi():
            return (
                namaEntry.get() != ""
                and paket.get() != ""
                and porsiEntry.get() != ""
                and alamatEntry.get() != ""
                and x != ""
                and cal.get_date() != ""
                and hargaakhir != ""
                and noEntry.get() != ""
            )

        # Function menambah data yang sudah di input ke dalam database sqlite3

        def tambahData():
            if validasi():
                try:
                    trv.delete(*trv.get_children())
                    con = sqlite3.connect("catering.db")
                    c = con.cursor()
                    if paket.get() == 1:
                        paket1 = "Pernikahan"
                    elif paket.get() == 2:
                        paket1 = "Ulang Tahun"
                    c.execute(
                        "INSERT INTO datapesananbarubaru VALUES (:nama, :paket, :porsi, :alamat, :tglpesan, :tglkirim, :harga, :notelp)",
                        {
                            "nama": namaEntry.get(),
                            "paket": paket1,
                            "porsi": porsiEntry.get(),
                            "alamat": alamatEntry.get(),
                            "tglpesan": x,
                            "tglkirim": cal.get_date(),
                            "harga": hargaakhir,
                            "notelp": noEntry.get(),
                        },
                    )
                    con.commit()
                    c.execute("SELECT * FROM datapesananbarubaru")
                    fetch = c.fetchall()
                    for data in fetch:
                        trv.insert(
                            "",
                            "end",
                            values=(
                                data[0],
                                data[1],
                                data[2],
                                data[3],
                                data[4],
                                data[5],
                                data[6],
                                data[7],
                            ),
                        )
                    con.commit()
                    con.close()
                    resetForm()
                    messagebox.showinfo("SUCCESS", "Data Berhasil Disimpan!")
                except ValueError:
                    messagebox.showerror("ERROR", "Silahkan Masukan data yang benar!")
            else:
                messagebox.showerror("ERROR", "Silahkan Isi semua data!")

        # Function mengupdate data yang sudah di pilih ke dalam database sqlite3

        def updateData():
            if validasi():
                try:
                    trv.delete(*trv.get_children())
                    con = sqlite3.connect("catering.db")
                    c = con.cursor()
                    if paket.get() == 1:
                        paket1 = "Pernikahan"
                    elif paket.get() == 2:
                        paket1 = "Ulang Tahun"
                    c.execute(
                        f"UPDATE datapesananbarubaru SET nama = :nama, paket = :paket, porsi = :porsi, alamat = :alamat, tgl_psn = :tglpesan, tgl_krm = :tglkirim, total_harga = :harga, notlp = :notelp WHERE nama = '{dataNama.get()}'",
                        {
                            "nama": namaEntry.get(),
                            "paket": paket1,
                            "porsi": porsiEntry.get(),
                            "alamat": alamatEntry.get(),
                            "tglpesan": x,
                            "tglkirim": cal.get_date(),
                            "harga": hargaakhir,
                            "notelp": noEntry.get(),
                        },
                    )
                    con.commit()
                    c.execute("SELECT * FROM datapesananbarubaru")
                    fetch = c.fetchall()
                    for data in fetch:
                        trv.insert(
                            "",
                            "end",
                            values=(
                                data[0],
                                data[1],
                                data[2],
                                data[3],
                                data[4],
                                data[5],
                                data[6],
                                data[7],
                            ),
                        )
                    con.commit()
                    con.close()
                    resetForm()
                    messagebox.showinfo("SUCCESS", "Data Berhasil Diupdate!")
                except ValueError:
                    messagebox.showerror("ERROR", "Silahkan Masukan data yang benar!")

            else:
                messagebox.showerror("ERROR", "Silahkan Isi semua data!")

        # Functions untuk memastikan data yang dipilih tidak kosong

        def validData():
            return len(dataNama.get()) != 0

        # Functions untuk menghapus data yang dipilih dari table

        def hapusData():
            if validData():
                try:
                    con = sqlite3.connect("catering.db")
                    c = con.cursor()
                    c.execute(
                        f"DELETE FROM datapesananbarubaru WHERE nama = '{dataNama.get()}'"
                    )
                    con.commit()
                    trv.delete(*trv.get_children())
                    c.execute("SELECT * FROM datapesananbarubaru")
                    fetch = c.fetchall()
                    for data in fetch:
                        trv.insert(
                            "",
                            "end",
                            values=(
                                data[0],
                                data[1],
                                data[2],
                                data[3],
                                data[4],
                                data[5],
                                data[6],
                                data[7],
                            ),
                        )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Data Berhasil Dihapus")
                    dataNama.delete(0, END)
                    resetForm()
                except ValueError:
                    messagebox.showerror("ERROR", "Isi data yang akan dihapus!")
            else:
                messagebox.showerror("ERROR", "Isi Data yang akan dihapus!")

        # Function untuk Mereset form pesanan agar kosong

        def resetForm():
            try:
                myLabel.config(text="")
                namaEntry.delete(0, END)
                paket.set(None)
                porsiEntry.delete(0, END)
                alamatEntry.delete(0, END)
                hargaCounter.config(text="Total Harga :")
                noEntry.delete(0, END)
                dateTtl.config(text="Tanggal yang dipilih : ")
                tanggalEntry.config(text=x)
                dataNama.delete(0, END)
                kembalianOutput.config(text="")
                inputCash.delete(0, END)
            except:
                messagebox.showerror("ERROR", "Data Sudah Kosong!")

        # Functin Exit MenuUtama

        def exitMenu():
            tglnya = datee.datetime.now().strftime(f"%d/%m/%y - %X")
            con = sqlite3.connect("catering.db")
            c = con.cursor()
            c.execute("SELECT * FROM logadmin ORDER BY tglmasuk DESC")
            fetchlog = c.fetchone()
            namanya = fetchlog[0]
            c.execute(
                f"UPDATE logadmin SET tglkeluar = '{tglnya}' WHERE nama = '{namanya}'"
            )
            con.commit()
            con.close()
            root.destroy()
            # Membuka window baru (Final_Login)
            rootLogin = Tk()
            fl.loginForm(rootLogin)
            rootLogin.mainloop()

        # Tombol Operasi SQLite

        exitButton = Button(
            self.wrapper2, text="Exit", bg="red", fg="white", command=exitMenu
        ).pack(side=BOTTOM)
        resetButton = Button(
            self.wrapper1, text="Reset Form", command=resetForm, bg="red", fg="white"
        ).grid(row=9, column=8)
        gapmaker2 = Label(self.wrapper1, text="   ").grid(rowspan=7, column=4)
        labelHapus = Label(self.wrapper1, text="Data yang Terpilih adalah : ").grid(
            row=8, column=6
        )
        refreshButton = Button(
            self.wrapper1, text="Update Data", bg="yellow", command=updateData
        ).grid(row=9, column=3, sticky=E)
        hapusButton = Button(
            self.wrapper1, text="Hapus Data", bg="red", fg="white", command=hapusData
        ).grid(row=9, column=7)
        dataNama = Entry(self.wrapper1)
        dataNama.grid(row=9, column=6)
        simpanButton = Button(
            self.wrapper1,
            text="Simpan Data",
            bg="green",
            fg="white",
            command=tambahData,
        ).grid(row=9, column=3)
        updateButton = Button(
            self.wrapper2,
            text="View Table",
            bg="green",
            fg="white",
            command=DatabaseView,
        ).pack()

        # Tampilan Menu Makanan

        menu1 = Label(
            self.wrapper1,
            text="PAKET PERNIKAHAN \n 1. Ayam Gulai \n 2. Sop Kambing \n 3. Asinan \n 4. AQUA \n\n Rp.25,000",
            bg="lightblue",
        ).grid(row=1, rowspan=6, column=6)
        menu2 = Label(
            self.wrapper1,
            text="PAKET ULANG TAHUN \n 1. Butter Cake \n 2. French Fries \n 3. Ice Cream \n 4. Fanta \n\n Rp.30,000",
            bg="lightblue",
        ).grid(row=1, rowspan=6, column=7)

        # Menampilkan Isi di table dari database

        tree_scrollbar = Scrollbar(self.wrapper2)
        tree_scrollbar.pack(side=RIGHT, fill=Y)
        trv = Treeview(
            self.wrapper2,
            columns=(1, 2, 3, 4, 5, 6, 7, 8),
            show="headings",
            yscrollcommand=tree_scrollbar.set,
        )
        tree_scrollbar.config(command=trv.yview)
        # Pembentukan kolom Table
        trv.column(1, width=100)
        trv.column(2, width=100)
        trv.column(3, width=50)
        trv.column(4, width=200)
        trv.column(5, width=100)
        trv.column(6, width=100)
        trv.column(7, width=150)
        trv.column(8, width=150)
        # Pemberian nama kolom table
        trv.heading(1, text="Nama")
        trv.heading(2, text="Paket")
        trv.heading(3, text="Porsi")
        trv.heading(4, text="Alamat")
        trv.heading(5, text="TGL Pesan")
        trv.heading(6, text="TGL Kirim")
        trv.heading(7, text="Total Harga")
        trv.heading(8, text="No Telp")
        trv.pack()

        # Function Memilih table agar muncul di form

        def selector(Event):
            resetForm()
            dataNama.delete(0, END)
            selected = trv.focus()
            values = trv.item(selected, "values")
            dataNama.insert(0, values[0])
            myLabel.config(text=values[1])
            if myLabel.cget("text") == "Pernikahan":
                paket.set(value="1")
                r1.invoke()
            elif myLabel.cget("text") == "Ulang Tahun":
                paket.set(value="2")
                r2.select()
            else:
                messagebox.showerror("ERROR", "Sesuatu ada yang salah")
            namaEntry.insert(0, values[0])
            porsiEntry.insert(0, values[2])
            alamatEntry.insert(0, values[3])
            tanggalEntry.config(text=values[4])
            dateTtl.config(text="Tanggal yang dipilih : " + values[5])
            hargaCounter.config(text="Total Harga : " + values[6])
            noEntry.insert(0, values[7])

        # Event Listener untuk mendengarkan double klik

        trv.bind("<Double-1>", selector)


if __name__ == "__main__":
    root = Tk()
    application = fl.loginForm(root)
    root.mainloop()
