import turtle
from util import *


"""
Adapted from https://docs.python.org/3/library/turtle.html
"""
if __name__ == "__main__":

    (t, s) = init_objects()

    DIAMETER = 100
    ANGLE = 170

    t.color('goldenrod', 'firebrick')
    t.begin_fill()
    for i in range(int(360/(180 - ANGLE))):
        draw_square(t, DIAMETER)
        t.left(ANGLE)
    t.end_fill()

    t.ht()
    s.exitonclick()
