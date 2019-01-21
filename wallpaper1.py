import turtle
from util import *
from math import sqrt
from random import random


def getfillcolor():
    base_color = (1, 0.65, 0)
    s = random()
    return (s*x for x in base_color)


if __name__ == "__main__":

    (t, s) = init_objects()

    WIN_WIDTH = s.window_width()
    WIN_HEIGHT = s.window_height()
    XMAX = WIN_WIDTH / 2
    XMIN = -XMAX
    YMAX = WIN_HEIGHT / 2
    YMIN = -YMAX
    TSIZE = 100
    THEIGHT = sqrt(3)/2 * TSIZE
    NROWS = int(WIN_HEIGHT / THEIGHT) + 1
    NCOLS = int(WIN_WIDTH / TSIZE) + 1

    for row in range(NROWS):

        move_turtle(t, XMIN, YMIN + row*THEIGHT)

        for col in range(NCOLS):
            t.fillcolor(getfillcolor())
            t.begin_fill()
            (x, y) = t.pos()
            draw_triangle(t, TSIZE)
            t.forward(TSIZE)
            t.end_fill()

        move_turtle(t, XMIN - TSIZE/2, YMIN + (row+1)*THEIGHT)

        for col in range(NCOLS):
            t.fillcolor(getfillcolor())
            t.begin_fill()
            (x, y) = t.pos()
            draw_inv_triangle(t, TSIZE)
            t.forward(TSIZE)
            t.end_fill()

    s.exitonclick()
