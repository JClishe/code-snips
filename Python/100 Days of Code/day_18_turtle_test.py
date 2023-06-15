import random
from turtle import Turtle, Screen
from tkinter_colors import colors

timmy = Turtle()
heading = [0, 90, 180, 270]
timmy.pensize(5)
timmy.speed("fast")

def dashed_line():
    """Makes a dashed line"""
    for _ in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

def draw_shape(num_sides):
    """Makes shapes with increasing number of sides"""
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

def random_lines():
    """This function makes a bunch of random lines"""
    for _ in range (50):
        timmy.color(random.choice(colors))
        timmy.forward(25)
        timmy.setheading(random.choice(heading))

def draw_spirograph():
    """Draws a spirograph"""
    circle_heading = 0
    for _ in range(10):
        timmy.color(random.choice(colors))
        timmy.setheading(circle_heading)
        timmy.circle(100)
        circle_heading += 36

def hirst_painting():
    """Hirst painting, final project in lesson"""
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)
    def move_forward():
        for _ in range(10):
            timmy.dot(20, (random.choice(colors)))
            timmy.forward(50)

    def turn_left():
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)

    def turn_right():
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(0)

    for _ in range(8):
        move_forward()
        turn_left()
        move_forward()
        turn_right()

#dashed_line()

#for shape_sides in range(3, 11):
#    draw_shape(shape_sides)

#random_lines()

#draw_spirograph()

hirst_painting()
















screen = Screen()
screen.exitonclick()
