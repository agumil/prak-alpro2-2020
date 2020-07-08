class Hewan:
    jumlah = 0
    def setHewan(self, jenis, reproduksi, makanan):
        self.jenis = jenis
        self.reproduksi = reproduksi
        self.makanan = makanan
        Hewan.jumlah += 1

    def tampilJumlah(self):
        print("Jumlah hewan :", Hewan.jumlah, '\n')

    def tampilHewan(self):
        print("Jenis :", self.jenis, "golongan pemangsa :", self.makanan, "cara reproduksi :", self.reproduksi)

h = Hewan()
h.setHewan("Ular", "Ovovivipar", "Karnivora")
h.tampilHewan()
h.tampilJumlah()

h.setHewan("Sapi", "Vivipar", "Herbivora")
h.tampilHewan()
h.tampilJumlah()

h.setHewan("Ayam", "Ovipar", "Omnivora")
h.tampilHewan()
h.tampilJumlah()
