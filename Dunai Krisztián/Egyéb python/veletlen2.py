import random

veletlen_szam = random.randint(1,2)
if veletlen_szam == 1:
    penz = "fej"
else:
    penz = "iras"

    szam =input("Fej vagy írás?")

if szam == penz:
        print ("Eltaláltad!")
else:
     print ("Nem találtad el!")
    
