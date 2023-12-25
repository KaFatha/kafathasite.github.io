# class Animal
class Animal :
    def __init__(self, nama, makanan, hidup, kembangBiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.kembangBiak = kembangBiak

    def cetak(self):
        print("Nama Binatang ini adalah: ", self.nama)
        print("Binatang ini Memakan: ", self.makanan)
        print("Binatang ini hidup di: ", self.hidup)
        print("Cara Berkembang Biaknya adalah: ", self.kembangBiak)


# class Badak
class Badak(Animal):
    def __init__(self, nama, makanan, hidup, kembangBiak,cula, status):  
        super().__init__(nama, makanan, hidup, kembangBiak)
        self.cula = cula
        self.status = status
    

    # Method khusus Badak
    def cetak1(self):
        super().cetak()
        print("Binatang ini mempunyai ", self.cula)
        print("Status Binatang ini adalah: ", self.status)


# class Ikan
class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, kembangBiak, tipe, warna):
        super().__init__(nama, makanan, hidup, kembangBiak)
        self.tipe = tipe
        self.warna = warna

    # Method khusus Ikan
    def cetak2(self):
        super().cetak()
        print("Tipe Ikan ini adalah: ", self.tipe)
        print("Warna Ikan ini adalah: ", self.warna)


# Child class Ular
class Ular(Animal):
    def __init__(self, nama, makanan, hidup, kembangBiak, panjang, jenisUlar) : #berbisa atau ngga 
        super().__init__(nama, makanan, hidup, kembangBiak);
        self.panjang = panjang
        self.jenisUlar = jenisUlar

    # Method khusus Ular
    def cetak3(self):
        super().cetak()
        print("Panjang ular ini adalah: ", self.panjang)
        print("Ular ini adalah jenis ular: ", self.jenisUlar)


# Contoh penggunaan
a = Badak("Badak","Rumput","Darat","Beranak","Cula 2","Hampir Punah")
a.cetak1()

print("")

b = Ikan("Ikan","Pelet","Air","Bertelur","Hias","Emas")
b.cetak2()

print("")

c = Ular("Ular","Daging","Amfibi","Ovovivipar","1 Meter","Berbisa")
c.cetak3()