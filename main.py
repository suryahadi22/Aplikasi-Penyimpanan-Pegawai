import Tkinter as tk
import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('data.db')
q = conn.cursor()
q.execute('CREATE TABLE IF NOT EXISTS \
           karyawan(nama TEXT)')
q.close()

def tambah():
    print('Tambah ditekan')

    tambahApps = tk.Tk()
    tambahApps.title('Tambah Pegawai')

    size = tk.Canvas(tambahApps, width=200, height=50)
    size.pack()

    label = tk.Label(tambahApps, text='Masukkan Nama Pegawai')
    label.pack()

    pegawai_baru = tk.StringVar(tambahApps)
    entry = tk.Entry(tambahApps, text="Nama Pegawai ", bd=5, textvariable = pegawai_baru)
    entry.pack()

    def prosesTambah():
        data = pegawai_baru.get()

        print('diproses', data)
        with conn:
            q = conn.cursor()
            q.execute("INSERT INTO karyawan (nama) VALUES (?);", (data,))
            conn.commit()

        tambahApps.destroy()
    
    # click1 = tk.Button(tambahApps, text="Simpan", command=lambda: prosesTambah(pegawai_baru))
    click1 = tk.Button(tambahApps, text="Simpan", command=prosesTambah)
    click1.pack(padx=5, pady=5)

    tambahApps.mainloop()


def lihat():
    appsLihat = tk.Tk()
    appsLihat.title('Lihat Pegawai')

    size = tk.Canvas(appsLihat, width=200, height=25)
    size.pack()

    title = tk.Label(appsLihat, text="Daftar Karyawan", font="bold")
    title.pack(padx=5, pady=5)

    with conn:
        q = conn.cursor()
        q.execute("SELECT * FROM karyawan")

        if q.fetchone() is None:
            print('kosong')
            kosong = tk.Label(appsLihat, text='Data Kosong')
            kosong.pack()
        else:
            for row in q.fetchall():
                print(row)

                label = tk.Label(appsLihat, text=row)
                label.pack()
                spasi = tk.Label(appsLihat, text='========')
                spasi.pack()

    appsLihat.mainloop()

def hapus():
    print('hapus clicked')

    hapusApps = tk.Tk()
    hapusApps.title('Hapus Pegawai')

    size = tk.Canvas(hapusApps, width=200, height=50)
    size.pack()

    label = tk.Label(hapusApps, text='Masukkan Nama Pegawai')
    label.pack()

    hapus_pegawai = tk.StringVar(hapusApps)
    entry = tk.Entry(hapusApps, text="Nama Pegawai ", bd=5, textvariable = hapus_pegawai)
    entry.pack()

    def prosesHapus():
        data = hapus_pegawai.get()

        print('diproses', data)
        with conn:
            q = conn.cursor()
            q.execute("DELETE FROM karyawan WHERE nama = (?);", (data,))
            conn.commit()

        hapusApps.destroy()
    
    # click1 = tk.Button(tambahApps, text="Simpan", command=lambda: prosesTambah(pegawai_baru))
    click1 = tk.Button(hapusApps, text="Hapus", command=prosesHapus)
    click1.pack(padx=5, pady=5)

    hapusApps.mainloop()

def keluar():
    print('Keluar')
    conn.close()
    exit()

###################################################################################
apps = tk.Tk()
apps.title('Aplikasi Penyimpanan Pegawai')

size = tk.Canvas(apps, width=200, height=25)
size.pack()

click1 = tk.Button(apps, text="Tambah Data Pegawai", command=tambah)
click1.pack(padx=5, pady=5)

click2 = tk.Button(apps, text="Lihat Data Pegawai", command=lihat)
click2.pack(padx=5, pady=5)

click3 = tk.Button(apps, text="Hapus Data Pegawai", command=hapus)
click3.pack(padx=5, pady=5)

click4 = tk.Button(apps, text="Keluar", command=keluar)
click4.pack(padx=5, pady=5)

copyr = tk.Label(apps, text="Copyright(C) 2019 Suryahadi Eko Hanggoro | Suryahadi.com | UPJ")
copyr.pack()

apps.mainloop()