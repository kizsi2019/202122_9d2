# Made by Mészáros Levente
import random

MIN = 1 # változó 1
MAX = 5 # változó 2
sikeres = 0 
sikertelen = 0
újra = True  # A játék újrakezdéséhez kapcsolódó változó
kitalálta = False # kitalálásváltozó


while újra:
 random_szam = random.randint(MIN,MAX)
 próbálkozás = 0 # próbálkozásváltozó
  # Amíg a kitalálta változó nem True(azaz False), addig kérje be a számot,
  # addig, ameddig a próbálkozásváltozó kisebb mint 3

 while not kitalálta and próbálkozás < 3: # a ciklus kezdődjön újra 
     tipp =input('Melyik számra gondoltam ' +str(MIN) + ' és ' +str(MAX)+ ' között?') # Írja ki a kérdést, melyik számra gondoltam. A MIN és Max változók modosíthatók. Ha modósítjuk őket, a mondatban megváltoznak.
     tipp =int(tipp)
     próbálkozás += 1 # Jó vagy rossz, ha tippelünk, a próbálkozás változó változzon + 1-et
     if tipp == random_szam: # Ha eltaláltuk, az érték legyen True
      kitalálta = True
     if kitalálta:
       print("ügyes") # Ha eltaláltuk, írja ki hogy ügyes
       sikeres +=1
     else:
       print("nem jó") # Ha nem találtuk el, írja ki hogy nem jó
       sikertelen += 1
 válasz = None
 while válasz != "i" and válasz != "n":
     válasz =input("Akarsz játszani még egyet (i/n) ? ") # Megkérdezi a program, hogy akarunk e még egyet játzani
 
 if válasz == "n": # Ha válasz n, akkor ne ismétlődjön meg a ciklus 
    újra = False   

 print("Ennyi sikeres válaszod volt:" ,sikeres)
 print("Ennyi sikertelen válaszod volt:" ,sikertelen)
   
   # (c) Made by Mészáros Levente





    


