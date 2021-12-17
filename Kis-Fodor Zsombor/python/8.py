import turtle
window = turtle.Screen()
shapeboi = turtle.Turtle()

shapeboi.speed(10)
shapeboi.pensize(3)
shapeboi.shape("triangle")
shapeboi.left(90)
for i in range(180):
    shapeboi.forward(1)
    shapeboi.right(1)
shapeboi.left(180)
for i in range(180):
    shapeboi.forward(1)
    shapeboi.right(1)

window.mainloop()