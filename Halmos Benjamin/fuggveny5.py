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

