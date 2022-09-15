import random

numba = random.randint(1, 3)

guess = int(input("give numba between 1 and 3"))

if guess == numba:
    print("correct")
else:
    print("wrong")