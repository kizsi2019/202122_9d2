<<<<<<< HEAD
import random
list =[]
szamlalo = 1
szamlalo2 = 0
while szamlalo <=20:
    szam = random.randint(1,12)
    if szam % 3 == 0:
     print(szam)
    szamlalo2 = szamlalo2 + 1
  szamlalo = szamlalo + 1
=======
import random
list =[]
szamlalo = 1
szamlalo2 = 0
while szamlalo <=20:
    szam = random.randint(1,12)
    if szam % 3 == 0:
     print(szam)
    szamlalo2 = szamlalo2 + 1
  szamlalo = szamlalo + 1
>>>>>>> cb175d114ff0dd5f46f86fff2d49a7ccae3709f8
print('Enyi hárommal osztható szám volt: ',szamlalo2 )