jawab = 'y'
namaPenyumbang = []
sidonasi = []
biayaButuh = 10000000
while True:
    nama = input('Nama Penyumbang : ')
    namaPenyumbang.append(nama)

    donasi = int(input('Donasi = '))
    sidonasi.append(donasi)

    jawab = input('Masi mau input [y/t] : ')
    if jawab == 't':
        break

print('=== Data Donasi ===')
totaldonasi = 0
for i in range (len(namaPenyumbang)):
    print(f'Nama : {namaPenyumbang[i]} -> jum. Donasi = {sidonasi[i]}')
    totaldonasi += sidonasi[i]

hasil = biayaButuh - totaldonasi

if totaldonasi >= biayaButuh:
    keterangan = 'Baiaya mencukupi'
else:
    keterangan = f'Masi butuh Donasi sebesar = {hasil}'

print(f'Total Donasi = Rp. {totaldonasi}')
print(f'Biaya Yang Dibutuhkan = Rp. {biayaButuh}')
print(f'Keterangan = {keterangan}')
