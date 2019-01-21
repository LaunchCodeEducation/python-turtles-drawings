import turtle
from util import *


"""
Adapted from https://docs.python.org/3/library/turtle.html
"""
if __name__ == "__main__":

    (t, s) = init_objects()

    DIAMETER = 150
    ANGLE = 150
    NSIDES = 3

    t.color('dark green', 'orchid')
    s.bgcolor('light gray')
    t.begin_fill()
    for i in range(int(360/(180 - ANGLE))):
        draw_reg_poly(t, NSIDES, DIAMETER)
        t.left(ANGLE)
    t.end_fill()

    t.ht()
    s.exitonclick()
