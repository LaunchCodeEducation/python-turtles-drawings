import turtle


def init_objects():
    t = turtle.Turtle()
    t.speed(0)
    return (t, t.getscreen())


def move_turtle(t, x, y):
    t.up()
    t.goto(x, y)
    t.down()


def getrowcolor(row):
    return (0, 0, (0.9 - row / 14) % 1)

if __name__ == '__main__':

    (t, s) = init_objects()

    WIN_WIDTH = s.window_width()
    WIN_HEIGHT = s.window_height()
    XMAX = WIN_WIDTH / 2
    XMIN = -XMAX
    YMAX = WIN_HEIGHT / 2
    YMIN = -YMAX
    PEAK_H = 50
    PEAK_W = 50

    for row in range(int(WIN_HEIGHT / PEAK_H) + 1):

        t.fillcolor(getrowcolor(row))

        move_turtle(t, XMIN, YMIN + (row-1)*PEAK_H)
        t.begin_fill()

        while(t.pos() < (XMAX, YMAX)):
            (x, y) = t.pos()
            t.goto(x + PEAK_W / 2, y + PEAK_H)
            t.goto(x + PEAK_W, y)

        (x, y) = t.pos()
        t.goto(x, y + PEAK_H)

        while(t.pos() > (XMIN, YMIN)):
            (x, y) = t.pos()
            t.goto(x - PEAK_W / 2, y + PEAK_H)
            t.goto(x - PEAK_W, y)

        (x, y) = t.pos()
        t.goto(x, y - PEAK_H)
        t.end_fill()

    s.exitonclick()
