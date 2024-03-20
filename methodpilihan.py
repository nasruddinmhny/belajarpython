def tambah():
    a = input("Input Nilai A = ")
    b = input("Input Nilai B = ")

    hasil = a + b

    print(f'Hasil nilai {a} + nilai {b} = {hasil}')

def perkalian():
    a = input("Input Nilai A = ")
    b = input("Input Nilai B = ")

    hasil = a * b

    print(f'Hasil nilai {a} + nilai {b} = {hasil}')

def pengurangan():
    a = input("Input Nilai A = ")
    b = input("Input Nilai B = ")

    hasil = a - b

    print(f'Hasil nilai {a} + nilai {b} = {hasil}')

def pembagian():
    a = input("Input Nilai A = ")
    b = input("Input Nilai B = ")

    hasil = a // b

    print(f'Hasil nilai {a} + nilai {b} = {hasil}')

def tambah_bilangan(nilaiA,nilaiB,nilaiC):
    hasil = nilaiA + nilaiB + nilaiC
    return hasil

def biodata(nama,jeniskelamin,nohp):
    print(f"nama saya adalah {nama}")
    print(f"Jenis Kelamin saya adalah {jeniskelamin}")
    print(f"no telpon saya {nohp}")