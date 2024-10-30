import math

bil1 = int(input("bilangan 1  : "))
bil2 = int(input("bilangan 2  : "))
pangkat1 = math.pow(bil1,4)
pangkat2 = math.pow(bil2,2)
jumlah = pangkat1 + pangkat2
akar = math.sqrt(jumlah)

print()
print(f"pangkat1 = {pangkat1}")
print(f"pangkat2 = {pangkat2}")
print(f"hasil jumlah  : {jumlah}")
print(f"akar = {akar}")
