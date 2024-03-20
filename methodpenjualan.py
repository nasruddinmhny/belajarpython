#totalBayar = jumpesan * hargaBalok
#totalpajak = totalbayar * 0.11 = 44000
#totalsetelahpajak = totalbayr + totlapajak

def HitungTotalBayar(jpesan,hrgb):
    #hitung = jpesan * hrgb
    return jpesan * hrgb

def HitungPajak(totalbyr):
    return totalbyr * 0.11

def HitungTotalSetelahPajak(totalbyr,totalpjk):
    return totalbyr + totalpjk

def Cetak(jump,hb,totbyr,totpjk,totspjk):
    print("---- STRUK BELANJA ----")
    print(f'Jumlah Pemesanan = {jump}')
    print(f'Harga 1 Balok Batako = {hb}')
    print(f'Total Bayar = {totbyr}')
    print(f'Total Pajak = {totpjk}')
    print(f'Total Bayar + Pajak 11% = {totspjk}')

def inputData():
    jump = int(input("Mau pesan berapa balok = "))
    hb = int(input(" Harga 1 Balok Batako = "))
    #totalBayar = jumpesan * hargaBalok
    totalBayar = HitungTotalBayar(jump,hb)
    totalpajak= HitungPajak(totalBayar)
    totalSetelahPajak = totalBayar + totalpajak
    Cetak(jump,hb,totalBayar,totalpajak,totalSetelahPajak)

def mainUtama():
    
    inputData()
    

   
  
