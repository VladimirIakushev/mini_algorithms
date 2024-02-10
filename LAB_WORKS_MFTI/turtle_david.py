import turtle


def david():
    for step in range(6):
        turtle.begin_fill()
        for i in range(6):
            turtle.forward(60)
            turtle.left(120)
            turtle.end_fill()
        turtle.forward(60)
        turtle.right(60)


turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('green', 'yellow')
turtle.speed(100)

david()
turtle.backward(200)
david()
