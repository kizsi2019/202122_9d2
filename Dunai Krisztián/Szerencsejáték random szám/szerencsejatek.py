import random
import math

# Legkisebb és legnagyobb szám megadása / input
legkisebb = int(input("Legkisebb szám: "))
nagyobb = int(input("Legnagyobb szám: "))

# Esély kiszámolása a legkisebb és legnagyobb összeadásával / math
x = random.randint(legkisebb, nagyobb)
print("Csak",
	round(math.log(nagyobb + legkisebb)),
	" szám van hogy kitaláld")

# Próbálkozások száma változó és annak alapértéke / változó
probalkozascount = 0

# Tippelés kiszámolása és próbálkozások hozzáadása
while probalkozascount < math.log(nagyobb + legkisebb):
	probalkozascount += 1

	tipp = int(input("Tippelj egy számot: "))

	if x == tipp:
		print("Siker! Megcsináltad ennyi próbálkozásból!: ",
			probalkozascount, " próbálkozás")

# Ha túl nagy vagy túl kicsi a megadott szám 
		break
	elif x > tipp:
		print("A megadott szám túl kicsi!")
	elif x < tipp:
		print("A megadott szám túl nagy!")

# A random legenerált szám eredeménye és a tippelt szám

if probalkozascount >= math.log(nagyobb + legkisebb):
	print("\nA szám ez volt: %d" % x)

