import turtle

turtle = turtle.Turtle()
turtle.shape('turtle')
a = 200
for i in range(2):
    turtle.forward(2*a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)