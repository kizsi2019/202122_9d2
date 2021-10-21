import random
import math

kisebb = int(input("Add meg a legkisebb számot:- "))
nagyobb = int(input("Add meg a legnagyobb számot:- "))

randomszam = random.randint(kisebb, nagyobb)
print("Csak ",
	round(math.log(kisebb - nagyobb + 1, 2)),
	" esélyed van nyerni!")

probalkozasszam = 0

while probalkozasszam < math.log(kisebb - nagyobb + 1, 2):
	probalkozasszam += 1

	talalat = int(input("Írj egy számot!:  "))

	if randomszam == talalat:
		print("Sikerult! Probalkozasok szama: ",
			probalkozasszam, " probalkozas")
		break
	elif randomszam > talalat:
		print("Túl kicsi a megadott szám!")
	elif randomszam < talalat:
		print("Túl nagy a megadott szám!")

if probalkozasszam >= math.log(kisebb - nagyobb + 1, 2):
	print("\nA helyes szám: %d" % randomszam)

