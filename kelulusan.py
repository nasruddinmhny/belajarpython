
#nilai uts dan nilai uas
# nis, nama, kelas, mapel
# list [], tupple (), dict {key,value}
jawab = 'y'
nisList = []
namaList = []
kelasList = []
mapelList = []
nilaiutsList = []
nilaiuasList =[]
while True:
    
    nis = input('Nis : ')
    nisList.append(nis)

    nama = input('Nama : ')
    namaList.append(nama)

    kelas = input('Kelas : ')
    kelasList.append(kelas)

    mapel = input('Mata Pelajaran : ')
    mapelList.append(mapel)

    nilaiuts = int(input('Nilai UTS : '))
    nilaiutsList.append(nilaiuts)

    nilaiuas = int(input('Nilai UAS : '))
    nilaiuasList.append(nilaiuas)
    
    jawab = input('Masih mau input [y/t] : ')
    if jawab == 't':
        break





print('=== OUTPUT ===')

nilaiakhirList = []

for i in range(len(nisList)):
    nilaiakhir = (nilaiutsList[i] * 0.5) + (nilaiuasList[i] * 0.5)
    nilaiakhirList.append(nilaiakhir)

    if nilaiakhirList[i] < 50:
        keterangan = 'Gagal'
    else:
        keterangan = 'Lulus'
        

    print(f'Nis : {nisList[i]}')
    print(f'Nama : {namaList[i]}')
    print(f'Kelas : {kelasList[i]}')
    print(f'Mata Pelajaran : {mapelList[i]}')
    print(f'Nilai UTS : {nilaiutsList[i]}')
    print(f'Nilai UAS : {nilaiuasList[i]}')
    print(f'Nilai Akhir : {nilaiakhirList[i]}')
    print(f'Keterangan : {keterangan}')

