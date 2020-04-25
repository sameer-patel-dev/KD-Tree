from math import acos,radians
from turtle import Screen
import turtle

DOT_DIAMETER = 20
GENERATION_DISTANCE = 75
mainheight = 12.5
width=50
mainangle = radians(90)


def tree(turtle, d,height, origin):
    # d is the depth

    turtle.penup()
    turtle.setposition(origin)
    turtle.pendown()
    turtle.right(mainangle)
    turtle.forward(mainheight) 
    turtle.left(mainangle)
    turtle.forward(width)
    turtle.left(mainangle)
    turtle.forward(mainheight*2)
    turtle.left(mainangle)
    turtle.forward(width)
    turtle.left(mainangle)
    turtle.forward(mainheight)
    turtle.left(mainangle)
    turtle.penup()
    turtle.right(mainangle)
    turtle.forward(6)
    turtle.left(mainangle)
    turtle.forward(10)
    turtle.write(d[0], font=("Arial", 8, "normal"))
    turtle.penup()
    turtle.setposition(origin)
    turtle.forward(width)
    

    if d == 0:  # base case
        return

    distance = (GENERATION_DISTANCE**2 + (2**height * DOT_DIAMETER / 2)**2)**0.5
    angle = acos(GENERATION_DISTANCE / distance)
    try:
      if not isinstance(d[1],str):
        turtle.pendown()
        turtle.left(angle)
        turtle.forward(distance)
        upper = turtle.position()
        turtle.right(angle)
      if not isinstance(d[2],str):
        turtle.penup()
        turtle.setposition(origin)
        turtle.forward(width)
        turtle.pendown()
        turtle.right(angle)
        turtle.forward(distance)
        lower = turtle.position()
        turtle.left(angle)
    except IndexError:
      o=1
    try:
        tree(turtle, d[1],height-1, upper)  # recurse upper branch
    except UnboundLocalError:
        o=1
    try:
        tree(turtle, d[2],height-1, lower)  # recurse lower branch
    except UnboundLocalError:
        o=1
    turtle.penup()
    turtle.forward(10)


def create(kdtree,height):

    turtle.clearscreen()
    screen = Screen()

    yertle = turtle.Turtle()
    yertle.radians()  # to accommodate acos()

    tree(yertle,kdtree,height,(-300, 0))

    
    
