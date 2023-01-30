#1
'''
def osszegzo(x,y):
    return osszegzo(x,y)
print(osszegzo(x+y))
'''

#2
'''
paros = False
def parose(x,y,z):
    paros = False
    if parose()/2 == 0:
        paros = True
    else:
        paros = False
    print(paros)
'''

#3
'''
def harommal_oszthato():
    lista=[]
    lista2=[]
    szam = int(input('Adj meg egy számot, ha ki akar lépni, írjon egy negatív számot'))
    while szam >= 0:
        lista.append(szam)
        if szam / 3 == 0 and szam >= 0:
            lista2.append(szam)
        szam = int(input('Adj meg egy számot, ha ki akar lépni, írjon egy negatív számot'))

    if szam < 0:
        return lista
        print("Ezeket adta meg:", lista)
        print("Ebből ezek oszthatóak 3mal", lista2)
        print("Ennyi érték osztható 3mal", lista2.count())
'''

#4



#5
'''
lista = []
szam = int(input("Adj meg egy pozitív egész számot"))
while szam > 0:
    lista.append(szam)
    szam = int(input("Adj meg egy pozitív egész számot"))
def min(lista):
    min = lista[0]
    for item in lista:
        if item < min:
            min = item
    return min
print(min(lista))
print(lista)
'''
