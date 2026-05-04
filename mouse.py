import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")

def explosion(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    for i in range(20):
        t.pencolor(random.random(), random.random(), random.random())
        t.forward(random.randint(20, 100))
        t.backward(random.randint(20, 100))
        t.right(18)

turtle.onscreenclick(explosion)

turtle.done()