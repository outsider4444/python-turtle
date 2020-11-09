import turtle

turtle.shape('turtle')
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(150)
turtle.end_fill()
# глазики
turtle.penup()
turtle.goto(-60,200)
turtle.fillcolor('blue')
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
turtle.penup()
turtle.goto(60,200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()
#нос
turtle.penup()
turtle.goto(0,180)
turtle.pendown()
turtle.pensize(8)
turtle.right(90)
turtle.forward(50)
#рот
turtle.penup()
turtle.goto(70,90)
turtle.color('red')
turtle.pendown()
turtle.circle(-70,180,100)








turtle.mainloop()