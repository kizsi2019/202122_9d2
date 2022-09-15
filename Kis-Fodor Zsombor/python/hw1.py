import random

numba = random.randint(-5, 5)

guess = int(input("give numba"))

if guess == numba:
    print("correct")
else:
    print("wrong")