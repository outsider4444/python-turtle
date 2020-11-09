import turtle
t = turtle.Turtle()
t.shape('turtle')

n = 6
x = 1
def flower(x):
    while x <= n:
        t.circle(50)
        t.left(360 / n)
        x += 1

flower (x)