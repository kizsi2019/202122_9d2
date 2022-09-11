from random import random


from random import randrange
randomszam = randrange(1, 5)
print(" Adj meg egy számot!" )
bemenet = int (input())

if bemenet == randomszam:
    print( " A két szám egyezik. " )
elif bemenet > randomszam:
    print(" Az általad adott szám nagyobb, mint a random szám. ")
else:
    print (" Az általad adott szám kisebb, mint a random szám. ")