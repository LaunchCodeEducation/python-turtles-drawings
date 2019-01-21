import turtle


def init_objects():
    t = turtle.Turtle()
    t.speed(0)
    return (t, t.getscreen())


def move_turtle(t, x, y):
    t.up()
    t.goto(x, y)
    t.down()
