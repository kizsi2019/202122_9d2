import turtle
window = turtle.Screen()
shapeboi = turtle.Turtle()

sides = int(input("sides?"))
for i in range(sides):
    if sides <= 30:
        shapeboi.forward(50)
    else:
        shapeboi.forward(2)
    shapeboi.left(360/sides)

window.mainloop()