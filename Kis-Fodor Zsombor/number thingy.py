import random

#lowest number
x = int(input("lowest number?"))
#highes number
y = int(input("highest number?"))
#number we want to find
z = int(input("number you want?"))

#misc
guess = None
tries = 0

#guessing code
while guess != z:
    guess = random.randint(x,y)
    print(guess)
    tries += 1
    if guess == z:
        print("I found the number it took me this many tries:", tries)