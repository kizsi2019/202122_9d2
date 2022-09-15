x = int(input("give numba"))
y = int(input("give numba again"))

if x < 0 and y < 0:
    print("both are negative")
elif x < 0 or y < 0:
    print("one is negative")
else:
    print("both are positive")