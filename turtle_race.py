import turtle
from turtle import Turtle,Screen
import random

color=["red","orange","green","yellow","blue","purple"]

screen=Screen()
screen.setup(width=500,height=400)
is_race_on=False
x=-230
y=-100

all_turtles=[]

for item in color:
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(item)
    new_turtle.penup()
    new_turtle.goto(x,y)
    all_turtles.append(new_turtle)
    y=y+50


user_bet=turtle.textinput(title="make your bet",prompt="which turtle is going to win? Enter a color?")

if user_bet:
    is_race_on=True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You won the race,{winning_color} is the winner")
            else:
                print(f"You lost the race,{winning_color} is the winner")


        turtle.forward(random.randint(0,10))

screen.exitonclick()