import random

#stuff for code
numbers = 1
boiswith3 = 0

#code
while numbers <= 20:
    randomnumber = random.randint(1,12)
    numbers += 1
    if randomnumber % 3 == 0:
        print(randomnumber)
        boiswith3 += 1
print('I found this many numbers that can be divided by three:', boiswith3)
