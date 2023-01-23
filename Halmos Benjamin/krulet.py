def kerulet(x, *args):
    if len(args) == 0:
        return 4 * x
    if len(args) == 1:
        return (x + args[0]) * 2
    if len(args) == 2:
        return x + args[0] + args[1]
    else:


idom = None
print("kerülete" + kerulet(2))
print("kerülete" + kerulet(2,3))
print("kerülete" + kerulet(2,3,4))
print("kerülete" + kerulet(2,3,4,5))
