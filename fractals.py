import turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def draw_koch(t, depth, length):
    t.speed("fastest")
    t.pd()
    if depth == 1:
        t.fd(length)
    if depth > 1:
        draw_koch(t, depth - 1, length)
        t.lt(60)
        draw_koch(t, depth - 1, length)
        t.rt(120)
        draw_koch(t, depth - 1, length)
        t.lt(60)
        draw_koch(t, depth - 1, length)      
    t.pu()

def new_koch(t, depth, length):
    t.speed("fastest")
    t.pd()
    if depth == 1:
        t.fd(length)
    if depth > 1:
        new_koch(t, depth - 1, length)
        t.color("red")
        t.lt(80)
        new_koch(t, depth - 1, length)
        t.color("gray")
        t.rt(160)
        new_koch(t, depth - 1, length)
        t.color("blue")
        t.lt(80)
        new_koch(t, depth - 1, length)        
    t.pu()


def tree(t, depth, length, angle):
    t.pd()
    t.speed("fastest")
    if depth == 1:
        t.fd(length)
        t.backward(length)
    else:
        t.fd(length)
        t.rt(angle)
        tree(t, depth - 1, length, angle)
        t.lt(angle * 2)
        tree(t, depth - 1, length, angle)
        t.rt(angle)
        t.backward(length)

def tree_new(t, depth, length, angle):
    t.pd()
    t.speed("fastest")
    if depth == 1:
        length = depth * 10
        t.pensize(3)
        t.color('green')
        t.fd(length)
        t.backward(length)
        t.color('brown')
    else:
        length = depth * 10 + random.randrange(40)
        t.color('brown')
        t.pensize(depth * 2)
        t.fd(length)
        t.rt(angle)
        tree_new(t, depth - 1, length, angle)
        t.lt(angle * 2)
        tree_new(t, depth - 1, length, angle)
        t.rt(angle)
        t.backward(length)

def draw_sierpinski(t, depth, length):
    t.speed("fastest")
    t.pd()
    if depth == 1:
        t.lt(60)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(180)
    else:
        draw_sierpinski(t, depth - 1, length/2)
        t.fd(length / 2)
        draw_sierpinski(t, depth - 1, length/2)
        t.lt(120)
        t.fd(length / 2)
        t.rt(120)
        draw_sierpinski(t, depth - 1, length/2)
        t.rt(120)
        t.fd(length / 2)
        t.lt(120)

def draw_sierpinski_new(t, depth, length):
    t.speed("fastest")
    t.pu()
    if depth == 1:
        t.fillcolor(colors[random.randrange(7)])
        t.begin_fill()
        t.lt(60)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(120)
        t.fd(length)
        t.rt(180)
        t.end_fill()
    else:
        draw_sierpinski_new(t, depth - 1, length/2)
        t.fd(length / 2)
        draw_sierpinski_new(t, depth - 1, length/2)
        t.lt(120)
        t.fd(length / 2)
        t.rt(120)
        draw_sierpinski_new(t, depth - 1, length/2)
        t.rt(120)
        t.fd(length / 2)
        t.lt(120)


 
