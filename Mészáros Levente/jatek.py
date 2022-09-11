import random



chance = 0


szam = random.randint(1, 5)

szam2 = int(input("Adj meg egy véletlen számot"))
chance += 1



while szam2 > szam and chance < 3:
    szam2 = int(input("Az általad megadott szám nagyobb"))
    chance += 1

while szam2 < szam and chance < 3:
    szam2 = int(input("Az általad megadott szám kisebb"))
    chance += 1

if szam2 == szam:
    print("talált")

if chance == 3 and szam2 != szam:
    print("Vesztettél")










