class gempa:
    def __init__(self,lokasi,skala):
        self.lokasi= lokasi
        self.skala = skala
    def dampak(self):
        if self.skala < 2:
         print(f"Gempa tidak berasa{self.skala}")
        elif 2 <= self.skala <  4:
           print(f"Bangunan retak-retak{self.skala}")
        elif 4 <= self.skala < 6:
           print(f"Bangunan Roboh{self.skala}")
        elif self.skala > 6:
           print(f"Bangunan Roboh dan Berdampak Tsunami")

lokasi_pertama = "Inggris"
skala_gempa = 1.2
gempa_pertama= gempa(lokasi_pertama,skala_gempa)

gempa_pertama.dampak()

lokasi_kedua = "Amerika"
skala_gempa2 = 6.1
gempa_kedua = gempa(lokasi_kedua,skala_gempa2)
gempa_kedua.dampak()


lokasi_ketiga = "Australia"
skala_gempa3 = 3.3
gempa_ketiga = gempa(lokasi_ketiga,skala_gempa3)
gempa_ketiga.dampak()

lokasi_keempat = "Israel"
skala_gempa4 = 5.6
gempa_keempat = gempa(lokasi_keempat,skala_gempa4)
gempa_keempat.dampak()

lokasi_kelima = "Rusia"
skala_gempa5 = 4.0
gempa_kelima = gempa(lokasi_kelima,skala_gempa5)
gempa_kelima.dampak()
