numba = int(input("give numba"))

if numba % 3 == 0 and numba % 4 == 0:
    print("can be both divided by 3 and 4")
elif numba % 3 == 0:
    print("can only be divided by 3")
elif numba % 4 == 0:
    print("can only be divided by 4")
elif numba % 3 != 0 and numba % 4 != 0:
    print("can't be divided by 4 and 3")