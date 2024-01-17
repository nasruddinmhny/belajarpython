jawab = 'y'
namateman = []#diawali index 0
while True:
    nama = input('Input nama teman : ')
    namateman.append(nama)

    jawab = input('Masih mau nambah teman [y/t] :')

    if jawab == 't':
        break

print('== Nama Teman Saya ==')
for nama in range (len(namateman)):
    print(f'index[{nama}] Nama = {namateman[nama]}')



    