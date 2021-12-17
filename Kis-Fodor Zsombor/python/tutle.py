import turtle

#parameters
ablak = turtle.Screen()
Pain = turtle.Turtle()
Pain.shape("blank")

#shapes
#triangle
for i in range(3):
    Pain.forward(80)
    Pain.left(120)

#cube
for i in [0,1,2,3]:
    Pain.forward(70)
    Pain.left(90)

#circle
for i in range(360):
    Pain.forward(0.6)
    Pain.left(1)

#color changing
for sz in ["hotpink","purple","pink","red"]:
    Pain.color(sz)
    Pain.forward(70)
    Pain.left(90)

ablak.mainloop()