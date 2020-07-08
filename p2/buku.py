from IPython.display import clear_output

buku = []
kl=1

def show_data():
    if len(buku) <= 0:
        print ("BELUM ADA DATA")
    else:
        for indeks in buku: 
            print(indeks)

def insert_data(): 
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)
    

def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks > len(buku)): 
        print ("ID SALAH")
    else: 
        judul_baru = input("Judul Baru: ")
        buku[indeks] = judul_baru
        

def delete_data():
    show_data()
    indeks = int(input("inputkan ID buku: "))
    if(indeks > len(buku)): 
        print("ID SALAH")
    else: 
        buku.remove(buku[indeks])
        

def show_menu(): 
    global Tr
    Tr = 1
    print ("\n")
    print ("------------ MENU ------------")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
    
    menu = int(input("PILIH MENU: "))
    print ("\n")
    clear_output(wait=True)
    if (menu == 1):
        show_data()
    elif (menu == 2):
        insert_data()
    elif (menu == 3):
        edit_data()
    elif (menu == 4):
        delete_data()
        Tr=0
    else:
        print ("Salah Pilih: ")
    return Tr

Tr=1
if __name__ == "__main__":
    while(Tr==1):
        Tr=show_menu()
        clear_output(wait=True)
