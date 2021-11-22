import sqlite3

con = sqlite3.connect('catering.db')
c = con.cursor()
'''c.execute("""CREATE TABLE datapesananbarubaru (
    nama text,
    paket text,
    porsi integer,
    alamat text,
    tgl_psn text,
    tgl_krm text,
    total_harga integer,
    notlp integer
)""")'''


#c.execute("INSERT INTO datapesananbarubaru VALUES ('Tegar','Ulang Tahun','100','Jl.Swadaya 2,Kec.Tambun Selatan,Kab.Bekasi','21/11/2021','25/11/2021','2000000','08122304844')")
#c.execute("DELETE FROM datapesananbarubaru WHERE nama = 'Dosen 3'")
c.execute("SELECT * FROM datapesananbarubaru")
print(c.fetchall())
con.commit()
con.close()

