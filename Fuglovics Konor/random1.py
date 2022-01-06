import random

number = random.randint(1,3)
number2 =int(input("Adj meg egy számot 1 és 3 között! "))
if number == number2:
    print('eltaláltad!')
else:
    print("nem találtad el...")