import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Eszti = turtle.Turtle()
Eszti.shape("triangle")

Eszti.penup()
meret = 20
color = ["ho"]
for i in range(30):
    Eszti.stamp() 
    meret = meret + 3 
    Eszti.forward(meret) 
    Eszti.right(24)

ablak.mainloop()