 
import random
randomvalasz = random.randint(0,1)
szam = int(input('Adj meg egy számot!'))

if szam >5:
	print('A megadott szám túl nagy!')
elif szam <0:
	print('A megadott szám túl alacsony!')
else:
	print('')

if szam == randomvalasz:
    print('Az gondolt szám egyezik, gratulálok!')
else:
    print('A gondolt szám nem egyezik, próbáld újra!')


    
