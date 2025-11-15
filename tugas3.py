# Kelas induk
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def perkenalan(self):
        print(f"Halo, nama saya {self.nama}, umur saya {self.umur} tahun.")

# Kelas turunan pertama
class Mahasiswa(Orang):
    def __init__(self, nama, umur, nim, jurusan):
        super().__init__(nama, umur)  # memanggil konstruktor kelas induk
        self.nim = nim
        self.jurusan = jurusan

    def info_mahasiswa(self):
        print(f"Saya mahasiswa dengan NIM {self.nim} dari jurusan {self.jurusan}.")

# Kelas turunan kedua
class Dosen(Orang):
    def __init__(self, nama, umur, nidn, mata_kuliah):
        super().__init__(nama, umur)
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def info_dosen(self):
        print(f"Saya dosen dengan NIDN {self.nidn}, mengajar {self.mata_kuliah}.")

# Program utama
mhs = Mahasiswa("Ahmad Arsyi Sazali", 21, "24241119", "Pendidikan teknologi informasi")
dsn = Dosen("Dr. pinkiboy", 40, "0123456", "Pemrograman Berorientasi Objek")

print("=== Data Mahasiswa ===")
mhs.perkenalan()
mhs.info_mahasiswa()

print("\n=== Data Dosen ===")
dsn.perkenalan()
dsn.info_dosen()
