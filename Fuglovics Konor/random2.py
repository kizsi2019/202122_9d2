import random

random_number = random.randint(1,2)
if random_number == 1:
    penz = "fej"
else:
    penz = "irás"
number2 =(input("Fej vagy írás? (fej/irás)"))
if number2 == penz:
    print("Eltaláltad!")
else:
    print("Nem találtad el!")