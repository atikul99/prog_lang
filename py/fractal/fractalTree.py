import turtle
import random

t = turtle.Turtle(shape="turtle")

t.lt(90)

lv = 10
l = 120

t.width(lv)

t.penup()
t.bk(l)
t.pendown()
t.fd(l)

def draw_tree(l, level):
    s = random.choice(range(10, 30))

    width = t.width()  # save the current pen width

    t.width(width * 3.0 / 4.0)  # narrow the pen width

    l = 3.0 / 4.0 * l

    t.lt(s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.rt(2 * s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.lt(s)

    t.width(width)  # restore the previous pen width

t.speed(0)

draw_tree(l, 2)

turtle.done()
