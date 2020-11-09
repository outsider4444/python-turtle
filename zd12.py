import turtle

turtle.shape('turtle')
n = 1
turtle.penup()
turtle.goto(-250,0)
turtle.pendown()
turtle.left(90)
for i in range(6):
    turtle.circle(-50,180,100)
    turtle.circle(-10,180,100)