import random

szam = random.randint(1, 5)
bekeres = int(input('Adj meg egy számot! '))
print("Random szám:",szam)
if bekeres == szam:
    print('A két szám megegyezik.')
elif bekeres > szam:
    print("A megadott szám nagyobb, mint a random szám.")
else:
    print("A megadott szám kisebb, mint a random szám.")