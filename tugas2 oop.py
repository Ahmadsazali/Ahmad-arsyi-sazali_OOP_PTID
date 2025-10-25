class Mahasiswa:
    # Class variable -> sama untuk semua objek
    universitas = "Universitas Mandalika"

    def __init__(self, nama, nim, jurusan):
        # Instance variable -> unik untuk setiap objek
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print(f"Nama      : {self.nama}")
        print(f"NIM       : {self.nim}")
        print(f"Jurusan   : {self.jurusan}")
        print(f"Universitas: {Mahasiswa.universitas}")
        print("-" * 30)


# Membuat beberapa objek mahasiswa
mhs1 = Mahasiswa("Arsyi", "24241119", "Teknologi Informasi")
mhs2 = Mahasiswa("Ahmad", "242433", "Pendidikan Teknologi Informasi")

# Menampilkan data
mhs1.tampilkan_info()
mhs2.tampilkan_info()

# Mengubah class variable (berlaku untuk semua)
Mahasiswa.universitas = "Universitas Mandalika"

print("Setelah universitas diubah:\n")
mhs1.tampilkan_info()
mhs2.tampilkan_info()
    