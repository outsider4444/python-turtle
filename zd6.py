import turtle

n = 0
f = 100
grad = 30
turtle.shape('turtle')
for i in range(12):
    turtle.forward(f)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(f)
    turtle.left(180)
    turtle.left(grad)
turtle.mainloop()