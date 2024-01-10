print('=== DATA PENJUALAN ===')
print('=== Jenis Transaksi ===')
print('1. Belanja 2. Bayar Tagihan')

namapembeli = input('Input Nama Pembeli = ')
pilihanTrs = input('Silahkan Pilih jenis transaksi(belanja/transaksi) = ')

if pilihanTrs == 'belanja':
    print('=== LIST BARANG ===')
    print('1. le mineral 2. buah')
    belanjaApa = input('Mau Belanja Apa = ')

    if belanjaApa == 'le mineral':
        hargaBrg = 5000
        jumlahBrg = int(input('Mau Beli Berapa = '))

        totalBelanja = hargaBrg * jumlahBrg
    
    elif belanjaApa == 'buah':
        hargaBrg = 10000
        jumlahBrg = int(input('Mau Beli Berapa = '))

        totalBelanja = hargaBrg * jumlahBrg
    else:
        print(f'Barang {belanjaApa} tidak tersedia..')

    #output
    print('=== STRUKT BELANJA ===')
    print(f'Nama Pembeli = {namapembeli}')
    print(f'Jenis Transaksi = {pilihanTrs}')
    print(f'Nama Barang = {belanjaApa}')
    print(f'Harga Barang = {hargaBrg}')
    print(f'Jumlah Barang = {jumlahBrg}')
    print(f'Total Belanja = {totalBelanja}')

elif pilihanTrs == 'transaksi':
    print('=== Jenis Tagihan ===')
    print('1. pln 2. pulsa 3.pdam')
    belanjaApa = input('Silihakan Pilih Jenis Tagihan = ')

    if belanjaApa == 'pln':
        tagihan = 400000
        print(f'Total Tagihan = {tagihan}')
        bayartagihan = int(input('Nominal Pembayaran = '))
        hasil = bayartagihan - tagihan

    elif belanjaApa == 'pulsa':
        tagihan = 150000
        print(f'Total Tagihan = {tagihan}')
        bayartagihan = int(input('Nominal Pembayaran = '))
        hasil = bayartagihan - tagihan

    elif belanjaApa == 'pdam':
        tagihan = 200000
        print(f'Total Tagihan = {tagihan}')
        bayartagihan = int(input('Nominal Pembayaran = '))
        hasil = bayartagihan - tagihan

    else:
        print(f'Jenis Tagihan {belanjaApa} tidak tersedia..')

    #output
    print('=== STRUKT BELANJA ===')
    print(f'Nama Pembeli = {namapembeli}')
    print(f'Jenis Transaksi = {pilihanTrs}')
    print(f'Jenis Tagihan = {belanjaApa}')
    print(f'Tagihan = {tagihan}')
    print(f'Nominal Bayar = {bayartagihan}')
    print(f'Kembalian = {hasil}')
else:
    print(f'Transaksi{pilihanTrs} tidak ada..')


