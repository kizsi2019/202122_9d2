szam = 1
while szam <= 10:
    print(szam)
    szam = szam + 1

szamlalo = 1
while szamlalo <= 5:
    print('Programozni jó!')
    szamlalo = szamlalo + 1

folytatja = True
while folytatja:
    print('Vidd ki a szemetet!')
    valasz = input('Mondjam még egyszer? (i/n)')
    if valasz == 'n':
        folytatja = False




szam = int(input('Adj meg egy számot 5 és 10 között! '))

while not 5 <= szam <= 10:
    szam = int(input('Helytelen érték! Adj meg egy számot 5 és 10 között! '))

print('Rendben!')
print('>> Program vége! <<                                                   lol')