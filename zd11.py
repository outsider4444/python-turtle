import turtle

n = 1
a = 30
x = -100
y = 0
turtle.shape('turtle')
turtle.left(90)
for i in range(8):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(360):
        turtle.left(1)
        turtle.forward(n/4)
    for i in range(360):
        turtle.right(1)
        turtle.forward(n / 4)

    n+=0.5
turtle.mainloop()
