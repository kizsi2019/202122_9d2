while True:
    import random

    number2 = random.randint(1, 5)
    number = int(input('Give me a number. '))

    if number == number2:
        print('The number is correct!')
        print('[END_OF_PROGRAM]')
        break
    elif number < number2:
        print('The number is smaller than my number')
        continue
    elif number > number2:
        print('The number is bigger than my number')
        continue