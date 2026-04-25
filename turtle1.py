import turtle

from numpy import character

screen=turtle.Screen()
screen.title("DRAW")
screen.bgcolor("black")
screen.screensize(1700,600)

character=turtle.Turtle()
character.shape("turtle")
character.color("white")
character.shapesize(2)

def foward_func():
    character.forward(10)
def back_func():
    character.back(10)
def right_func():
    character.right(5)
def left_func():
    character.left(5)

screen.onkey(foward_func, "w")
screen.onkey(back_func,"s")
screen.onkey(right_func,"d")
screen.onkey(left_func,"a")

screen.listen()

while True:
    screen.update()