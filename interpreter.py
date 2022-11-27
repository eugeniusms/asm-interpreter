file_masukan = input("Masukkan nama file input: ")
file_masukan = "asm_files/"+file_masukan

# Melakukan pengetesan error, akan error saat tidak file masukan
try:
    # Membaca text yang masuk ke dalam operasi
    file_input = open(file_masukan)
    isi_file = file_input.read() 
    file_input.close()

    for i in isi_file:
        print(i, end=" ")

# Ketika try di atas error maka tidak ada file yang dipanggil
except FileNotFoundError:
    print("file tidak ada")
