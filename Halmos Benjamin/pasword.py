szo = "lol"

incorrect = True
while incorrect:

    valasz = input('Adj meg a jelszavad! ')

    if not valasz == szo:
        print("Helytelen jelszó")
        int(input('Adj meg a jelszavad!'))

    else:
        incorrect = False

        print('Belépés megadva!')
