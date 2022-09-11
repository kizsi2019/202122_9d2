import random
szam1 = int(input('Adja meg egy számot'))
szam2 = random.randint(1, 5)
if szam1 == szam2:
 print('egyenlő')
else:
    if szam1 < szam2:
     print('Az ön száma Kisebb')
    else:
        print('Az ön száma Nagyobb')