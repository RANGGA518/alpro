    # deklarasi function
def inputan(komentar):
    masukan = int(input(komentar +' = '))
    return masukan

def get_total_harga(harga, qty):
    # isi function
    total_harga = harga * qty
    print('total_harga = ' ,total_harga)
    # return value
    return total_harga

def get_kembalian(pembayaran,total_harga):
    kembalian = pembayaran - total_harga
    print('kembalian = ',kembalian)

    #pemanggilan function
harga = inputan('harga')
qty = inputan('qty')
total_harga = get_total_harga(harga,qty)
pembayaran = inputan('pembayaran')
get_kembalian(pembayaran,total_harga)