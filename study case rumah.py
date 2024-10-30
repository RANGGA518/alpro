import math

bil1 = int(input("jumlah penggunaan daya lampu (dalam watt): "))
bil2 = int(input("waktu (jam): "))
harga = int(input("harga per kwh: "))

hasil = bil1 * bil2
kwh = hasil / 1000

harga_total1 = kwh * harga
print(f"harga total per hari: Rp {harga_total1:.2f}")

bulan = harga_total1 * 30
print(f"harga total per bulan: Rp {bulan:.2f}")


bil1 = int(input("jumlah penggunaan daya kipas (dalam watt): "))
bil2 = int(input("waktu (jam): "))
harga = int(input("harga per kwh: "))

hasil = bil1 * bil2
kwh = hasil / 1000

harga_total2 = kwh * harga
print(f"harga total per hari: Rp {harga_total2:.2f}")

bulan = harga_total2 * 30
print(f"harga total per bulan: Rp {bulan:.2f}")


bil1 = int(input("jumlah penggunaan daya tv (dalam watt): "))
bil2 = int(input("waktu (jam): "))
harga = int(input("harga per kwh: "))

hasil = bil1 * bil2
kwh = hasil / 1000

harga_total3 = kwh * harga
print(f"harga total per hari: Rp {harga_total3:.2f}")

bulan = harga_total3 * 30
print(f"harga total per bulan: Rp {bulan:.2f}")

jumlah_keseluruhan = harga_total1 + harga_total2 + harga_total3
print(f"jumlah_keseluruhan: Rp {bulan:.3f}")
