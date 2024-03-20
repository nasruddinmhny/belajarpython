from methodpilihan import tambah,perkalian,pengurangan,pembagian

print('==== PROGRAM SEDERHANA ====')
print('1. tambah 2. kurang 3. kali 4. bagi')

pilihan = input("Silahkan Pilih Operator = ")

if pilihan == "tambah":
    tambah()
elif pilihan == "kurang":
    pengurangan()
elif pilihan == "kali":
    perkalian()
elif pilihan == "bagi":
    pembagian()
else:
    print("pilihan tidak ada...")