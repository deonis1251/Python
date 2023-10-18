import turtle

n = 500
pen = turtle.Turtle()

for i in range(n * 3):
    pen.forward(i * 30)
    pen.left(120)

turtle.done()