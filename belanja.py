
jawab = 'y'

listNamaBarang = []
listHargaBarang = []
listJumlahBarang = []
while(True):
    namabarang = input('Input nama barang = ')
    listNamaBarang.append(namabarang)

    hargabarang = float(input('Input Harga Barang = Rp. '))
    listHargaBarang.append(hargabarang)

    jumlahbarang = int(input('Input Jumlah Barang = '))
    listJumlahBarang.append(jumlahbarang)

    jawab = input('Masih Mau Belanja [y/t]= ')

    if jawab == 't':
        break


print('=== OUTPUT ===')
totalbayar = 0
for i in range (len(listNamaBarang)):
    #rumus mencari total bayar

    total = listHargaBarang[i] * listJumlahBarang[i]
    totalbayar += total
    print(f'=== ITEM {[i]} ===')
    print(f'Nama Barang = {listNamaBarang[i]}')
    print(f'Harga Barang =Rp. {listHargaBarang[i]}')
    print(f'Jumlah Barang = {listJumlahBarang[i]}')
    print(f'Total = Rp. {total}')

print(f'== Total Bayar = Rp. {totalbayar}')
cekmember = input('apakah anda member [y = member / t = non member]= ')

if cekmember == 'y':
    diskon = 0.02
    totaldiskon = totalbayar * diskon
    totalbayarsetelahdiskon = totalbayar - totaldiskon
else:
    diskon = 0
    totaldiskon = totalbayar * diskon
    totalbayarsetelahdiskon = totalbayar - totaldiskon
    
print(f'Member = {cekmember}')
print(f'Diskon = {diskon}')
print(f'Total Diskon = Rp. {totaldiskon}')
print(f'== Total Pembayaran Setelah Diskon = Rp. {totalbayarsetelahdiskon}')
