def binSearch(data, key):
    awal = 1
    akhir = len(data) + 1
    ketemu = False
    i = 1
    while (awal <= akhir) and not ketemu:
        tengah = int((awal + akhir)/2)
        if key == data[tengah]:
            ketemu = True
            print('data', key, 'ditemukan di posisi', tengah, 'dari data setelah di urutkan')
            print('iterasi yang diperlukan', i)
        elif (key < data[tengah]):
            akhir = tengah - 1
        else:
            awal = tengah + 1
        i = i+1
    if ketemu == False:
        print('data tidak ditemukan')

# No 1
a = 'iwan tri riyadiyanto'
res = ''.join(sorted(a))
binSearch(res, 'i')

# No 2
nim = '1900017034'
nim = ''.join(sorted(nim))
binSearch(nim, '0')

# No 3
prodi = 'sistem informasi'
prodi = ''.join(sorted(prodi))
binSearch(prodi, 'i')

# No 4
nama = 'agung gumilang'
nama = ''.join(sorted(nama))
binSearch(nama, 'a')
