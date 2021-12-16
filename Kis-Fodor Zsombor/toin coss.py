import random

coin = ["heads", "tail"]
coinflip = random.choice(coin)
leguess =input("heads or tail?")
if coinflip == leguess:
    print("gooud guess")