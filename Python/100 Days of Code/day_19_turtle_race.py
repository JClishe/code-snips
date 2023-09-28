"""This is the turtle racing exercise for the Day 19 lesson"""
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "green"]
Y_positions = [150, 75, 0, -75, -150]

for turtle_index in range(0, 5):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.goto(x=-230, y=Y_positions[turtle_index])
    timmy.color(colors[turtle_index])











screen.exitonclick()
