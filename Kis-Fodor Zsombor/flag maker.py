import turtle

#
ablak = turtle.Screen()
Flag = turtle.Turtle()
Flag.shape("blank")

#parameters
number = 0
Flag.speed(10)
Flag.pensize(10)

#flag making
#lgbtq flag
for g in ["red","yellow","orange","green","blue","purple"]:
    Flag.color(g)
    Flag.forward(200)
    Flag.penup()
    number += 1
    if number % 2 == 0:
        Flag.left(90)
        Flag.forward(10)
        Flag.left(90)
    else:
        Flag.right(90)
        Flag.forward(10)
        Flag.right(90)
    Flag.pendown()

Flag.penup
Flag.right(90)
Flag.forward(50)
Flag.left(90)
Flag.pendown

ablak.mainloop()