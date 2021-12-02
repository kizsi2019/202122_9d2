# Made by Krisztian
import random
import math

# Legkisebb és legnagyobb szám megadása / input
print("Add meg a legkisebb és legnagyobb számokat amelyek benne lesznek a játékban.")
legkisebb = int(input("Legkisebb szám a játékban: "))
nagyobb = int(input("Legnagyobb szám a játékban: "))

# Maximum próbálkozások számának kiszámolása / math
x = random.randint(legkisebb, nagyobb)
print("Csak",
	round(math.log(nagyobb + legkisebb)),
	"próbálkozásod lehet, hogy kitaláld a számot!")

# Próbálkozások száma változó és annak alapértéke / változó
probalkozascount = 0

# Tippelés kiszámolása és próbálkozások hozzáadása
while probalkozascount < math.log(nagyobb + legkisebb):
	probalkozascount += 1

	tipp = int(input("Tippelj egy számot: "))

	if x == tipp:
		print("Gratulálunk! Sikerült kitalálnod a számot! Próbálkozások száma: ",
			probalkozascount, "")

# Ha túl nagy vagy túl kicsi a megadott szám 
		break
	elif x > tipp:
		print("A megadott szám túl kicsi, próbálkozz tovább!")
	elif x < tipp:
		print("A megadott szám túl nagy, próbálkozz tovább!")

# A random legenerált szám eredeménye és a tippelt szám

if probalkozascount >= math.log(nagyobb + legkisebb):
	print("\nA szám ez volt: %d" % x)

# (c) Dunai Krisztian 