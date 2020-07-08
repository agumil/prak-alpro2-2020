import os

def bacaFile(nama_file):
    file = open(nama_file, "r")
    str = file.read()
    print(str)
    file.close()
    

def tulis(nama_file, teks, mode):
    file = open(nama_file, mode)
    file.writelines(teks)
    file.close()

def renameFile(old):
    new = None
    respon = input("Apakah anda ingin mengganti nama file (Y/N) : ")
    if respon == 'y' or respon == 'Y':
        new = input("Masukkan nama file baru : ")
        os.rename(old, new)
        print("File {} telah diubah menjadi {}.".format(nama_file, new), '\n')
    else:
        print("File closed")
    return new

def removeFile(nama_file):
    respon = input("Apakah anda ingin menghapus file {} (Y/N) : ".format(nama_file))
    if respon == 'y' or respon == 'Y':
        os.remove(nama_file)
        print("File {} telah dihapus.".format(nama_file))
    else:
        print("File closed")

nama_file = "IO_contoh.txt"
konten = ["Lorem ipsum dolor sit amet",
          "consectetur adipiscing elit",
          "Donec volutpat varius ligula",
          "vitae sollicitudin libero placerat a."]
konten_lain = ["Tulisan ini akan menggantikan",
               "semua teks pada file ini."]

print("========== BEFORE ==========")
bacaFile(nama_file)
print()

tulis(nama_file, konten, 'a')

print("========== AFTER APPENDED ==========")
bacaFile(nama_file)
print()

tulis(nama_file, konten_lain, 'w')

print("========== AFTER WRITED ==========")
bacaFile(nama_file)
print()

new = renameFile(nama_file)

if new != None:
    removeFile(new)
else:
    print("End program")
