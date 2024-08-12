import turtle
from turtle import Turtle,Screen

tom=Turtle()
screen=Screen()

def move_for():
    tom.forward(5)
def move_bac():
    tom.backward(5)

def left():
    tom.left(10)

def right():
    tom.right(10)

def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.listen()
screen.onkeypress(key="w",fun=move_for)
screen.onkeypress(key="s",fun=move_bac)
screen.onkeypress(key="a",fun=left)
screen.onkeypress(key="d",fun=right)
screen.onkey(key="c",fun=clear)

screen.exitonclick()