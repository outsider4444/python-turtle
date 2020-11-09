import turtle

turtle.shape('turtle')
n = 5
n1 = 11
turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
def star(n):
    turtle.left(180 - (180/n))
    turtle.forward(200)
x = 1
while x <= n:
    star(n)
    x += 1
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
def star2(n1):
    turtle.left(180 - (180/n1))
    turtle.forward(200)
x = 1
while x <= n1:
    star2(n1)
    x += 1
turtle.mainloop()