def sqeSearch(data, key):
    pos = []
    for i in range(len(data)):
        if data[i] == key:
            pos.append(i+1)
    if len(pos) > 0:
        print('data', key, 'sebanyak', len(pos), 'ditemukan di posisi', pos)
        print('iterasi yang diperlukan', i+1)
    else:
        print('data tidak ditemukan')
    return pos


# no 1
a = 'iwan tri riyadiyanto'
res = ''.join(sorted(a))
sqeSearch(res, 'i')

# no 2
nim = '1900017034'
nim = ''.join(sorted(nim))
sqeSearch(nim, '0')

# no 3
prodi = 'sistem informasi'
prodi = ''.join(sorted(prodi))
sqeSearch(prodi, 'i')

# no 4
nama = 'agung gumilang'
nama = ''.join(sorted(nama))
sqeSearch(nama, 'a')
