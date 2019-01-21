import turtle
from util import *


"""
Adapted from https://docs.python.org/3/library/turtle.html
"""
if __name__ == "__main__":

    (t, s) = init_objects()

    DIAMETER = 200
    ANGLE = 170

    move_turtle(t, -DIAMETER/2, 0)
    t.color('red', 'yellow')
    t.begin_fill()
    for i in range(int(360/(180 - ANGLE))):
        t.forward(DIAMETER)
        t.left(ANGLE)
    t.end_fill()

    s.exitonclick()
