import random

nice = 0
x = int(input('small')) 
y = int(input('big')) 
while nice < 10:
    sus = random.randint(x,y)
    answer = int(input('Adj meg le számot'))   

    if answer < x:
        print('small')
    elif answer > y:
        print('big')
    else:
        print('')

    if answer == sus:
        print('good job')
        nice += 1
        print(nice)
    else:
        print('loser')

