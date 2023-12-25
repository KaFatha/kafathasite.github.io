class orang:
    def __init__(self, fnama, lnama):
        self.fnama =  fnama
        self.lnama = lnama

    def jalan(self):
        print("Saya bisa jalan")

    def cetak(self):
        print("nama saya ", self.fnama, self.lnama)

class mahasiswa(orang):
    def __init__(self, fnama, lnama, prodi, angkatan):
        super().__init__(fnama, lnama)
        self.prodi = prodi
        self.angkatan =  angkatan

    def print(self):
        super().cetak()
        print("Prodi saya ",self.prodi)
        print("Saya angkatan ",self.angkatan)

class karyawan(orang):
    def __init__(self, fnama, lnama, jabatan):
        super().__init__(fnama, lnama)
        self.jabatan = jabatan

    def tampil(self):
        super().cetak()
        print("Jabatan saya ", self.jabatan)

# Objek Orang 
x = orang("Bagus", "Maulana")
x.cetak()

# Objek Mahasiswa 
y = mahasiswa("Gilang", "Dirga", "Teknik Informatika", "2023")
y.print()
y.jalan()

# Objek Karyawan
a = karyawan("Agus", "Gumilang", "Supervisor")
a.tampil()
a.cetak()