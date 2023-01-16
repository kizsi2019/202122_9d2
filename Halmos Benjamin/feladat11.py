nevek = []

nev = None
while nev != '':
    nev = input('Adj meg egy a/A-val kezdődő szót! ')
    #print(nev[0])
    if nev != '' and (nev[0] =="a" or nev[0] =="A"):
        nevek.append(nev)

print(nevek)