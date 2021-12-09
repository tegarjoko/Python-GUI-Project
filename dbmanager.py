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

'''c.execute("""CREATE TABLE datakaryawan1 (
    id integer,
    nama text,
    password text,
    notlp integer
)""")'''

'''c.execute("""CREATE TABLE logadmin (
    nama text,
    tglmasuk text,
    tglkeluar text
)""")'''


#c.execute("INSERT INTO logadmin VALUES ('Tegar','tegar0987','08122304844')")
#c.execute("DELETE FROM datapesananbarubaru WHERE nama = 'Dosen 3'")
c.execute("SELECT * FROM logadmin")
print(c.fetchall())
con.commit()
con.close()

