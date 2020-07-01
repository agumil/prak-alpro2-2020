def hitungLuasLingkaran(r):
    luas = 22 / 7 * r * r
    return luas

def hitungNilaiMin(deret):
    paling_kanan = (len(deret) - 1)
    minimal = deret[paling_kanan]
    for i in range(len(deret) - 1):
        if deret[i] < minimal:
            minimal = deret[i]
    return minimal

def hitungRataRata(deret_lain):
    jumlah_angka = len(deret_lain)
    rerata = 0
    for i in range(len(deret_lain) - 1):
        rerata += deret_lain[i] / jumlah_angka
    return rerata

r = 7
print('Luas lingkaran dengan jari-jari', r, 'adalah', hitungLuasLingkaran(r))

A = [56, 23, 10, 22, 12]
print('Nilai minimal dalam deret', A, 'adalah', hitungNilaiMin(A))

B = [12, 1, 3, 10, 5]
print('Nilai rata-rata dari deret', B, 'adalah', hitungRataRata(B))
