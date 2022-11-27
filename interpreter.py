# instruction decode
from instruction_decode import decode
# debugger
from debugger.print_register_memory import print_register_memory

file_masukan = input("Masukkan nama file input: ")
file_masukan = "asm_files/"+file_masukan

# Melakukan pengetesan error, akan error saat tidak file masukan
try:
    # Membaca text yang masuk ke dalam operasi
    file_input = open(file_masukan)
    isi_file = file_input.read() 
    file_input.close()

    # Mengecek setiap line instruksi
    for line in isi_file.split("\n"):
        decode(line)

    # Mengecek register memory   
    print_register_memory()

# Ketika try di atas error maka tidak ada file yang dipanggil
except FileNotFoundError:
    print("file tidak ada")
