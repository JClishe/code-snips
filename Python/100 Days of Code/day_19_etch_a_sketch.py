"""This is the exercise for the Day 19 lesson"""
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def forward():
    """Move the turtle forward 10 spaces"""
    timmy.forward(10)

def backward():
    """Move the turtle backward 10 spaces"""
    timmy.backward(10)

def counter_clockwise():
    """Rotate the turtle 10 degrees to the left"""
    timmy.left(10)

def clockwise():
    """Rotate the turtle 10 degrees to the right"""
    timmy.right(10)

def clear():
    """Delete the turtle's drawing from the screen and re-center's the turtle in the home position"""
    timmy.reset()

screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear, key="c")











screen.exitonclick()
