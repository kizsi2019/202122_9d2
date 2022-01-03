szam =int(input("Adj meg egy számot!"))
if szam > 0 and szam % 2 == 0:
    print("pozitív páros")
elif szam <0 and szam % 2 == 1:
    print("negatív páratlan")