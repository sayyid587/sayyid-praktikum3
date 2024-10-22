# Inisialisasi  max dengan nilai 0
max = int(0)

# Loop untuk menerima input bilangan dari pengguna
while True:
    # Input bilangan dari pengguna
    num = int(input("Masukkan bilangan (0 untuk berhenti): "))
    
    # Periksa apakah bilangan yang dimasukkan adalah 0 jika ya maka pengulangan akan berhenti
    if num == 0:
        break
    
    # Periksa apakah bilangan yang dimasukkan lebih besar dari max
    if num > max:
        max = num

# Tampilkan bilangan terbesar yang ditemukan
print("Bilangan terbesar adalah:", max)
