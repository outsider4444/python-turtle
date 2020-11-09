import turtle


turtle.shape('turtle')
x = 0
y = 0
a = 10
for i in range(10):
    turtle.penup()
    turtle.goto(x,y)
    for i in range(4):
        turtle.pendown()
        turtle.forward(a)
        turtle.left(90)
    a = a +20
    x -= 10
    y -=10
