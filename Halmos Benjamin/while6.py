import random
szam = 1
db = 0
while szam <= 20:
    veletlen_szam = random.randint(1,12)
    if veletlen_szam % 3 == 0:
        print(veletlen_szam)
        db = db + 1
    szam = szam +1
print("ennyi db 3mal osztható számot találtam")