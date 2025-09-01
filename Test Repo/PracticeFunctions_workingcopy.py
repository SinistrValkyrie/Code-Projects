# Unit 3 Assignment 2 - Cheyenne Pierce 8/31/2025
# Draws 3 sets of shapes of related sizes
#   Draw a rectangle
#   Draw a triangle with sides the same size as rectangle length
#   Draw a filled circle with the same area as the rectangle
#   Draw a triangle with the same area as the rectangle
#   Draw a filled circle with the same diameter as the previous triangle side

import turtle
import math


def next_y_position(y, ht):
    """ Returns the next y-position, given current position y and height ht """
    next = y + ht + 30
    return next


def drawRect(t, len, wid):
    """ Draws a rectangle using turtle t with sides len and wid """
    for side in [len, wid, len, wid]:
        t.forward(side)
        t.left(90)


def drawFilledCircle(t, rad):
    """ Draws a filled circle of radius rad using turtle t """
    t.begin_fill()
    t.circle(rad)
    t.end_fill()


def drawEquilateralTriangle(t, side):
    """ Draws an equilateral triangle using turtle t with sides of length side """
    for _ in range(3):
        t.forward(side)
        t.left(120)


def getSide(len, wid):
    """ Returns the length of a side of an equilateral triangle with the same area as a rectangle of dimensions len and wid """
    return math.sqrt(4*len*wid/math.sqrt(3))


def getRad(len, wid):
    """ Returns the radius of a circle with an area of len * wid """
    return math.sqrt(len*wid/math.pi)

# My custom function - drawing a random polygon with a given number of sides


def drawRegularPolygon(t, sides, length):
    """ Draws any polygon with a given number of sides and side length using turtle t """
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)


def main():
    # named constants
    screen_size = 500
    screen_startx = 60  # x coordinate of the left edge of the graphics window

    # Set up the window and its attributes
    wn = turtle.Screen()
    wn.setup(screen_size, screen_size, screen_startx, 0)
    wn.bgcolor("yellow")

    axel = turtle.Turtle()
    axel.speed(7)

    # Initial turtle position near left edge, toward the bottom
    xpos = -screen_size/2 + 20
    ypos = -screen_size/2 + 50
    axel.up()
    axel.goto(xpos, ypos)
    axel.down()

    # y-dimension of each rectangle
    width = 50

    # draw three sets of shapes - same width(y-dimension) but different lengths
    for length in [25, 55, 75]:

        # Draw the rectangle
        drawRect(axel, length, width)
        # Here's code to draw a rectangle - before putting in a function
        # for side in [length, width, length, width]:
        # axel.forward(side)
        # axel.left(90)

        # Draw an equilateral triangle with sides the same as rectangle length
        drawEquilateralTriangle(axel, length)

        # Move a little to the right of the rectangle
        axel.up()
        axel.forward(2*length)
        axel.down()

        # Draw a circle with the same area as the rectangle
        radius = math.sqrt(length*width/math.pi)
        drawFilledCircle(axel, radius)
        # axel.begin_fill()
        # axel.circle(radius)
        # axel.end_fill()

        # Move a little to the right of the circle
        axel.up()
        axel.forward(2*radius)
        axel.down()

        # Draw an equilateral triangle with same area as rectangle
        tri_side = getSide(length, width)
        drawEquilateralTriangle(axel, tri_side)

        # Move a little to the right of the triangle
        axel.up()
        axel.forward(2*tri_side)
        axel.down()

        # Draw a circle with the same diameter as the triangle side
        drawFilledCircle(axel, tri_side/2)

        # Move a little to the right of the circle
        axel.up()
        axel.forward(2*length)
        axel.down()

        # Calling my custom drawRegularPolygon function
        drawRegularPolygon(axel, 6, length)

        # Calculate the next vertical position for a set of shapes
        ypos = next_y_position(ypos, tri_side)

        # Put turtle to left side of screen at correct height
        axel.up()
        axel.goto(xpos, ypos)
        axel.down()

    # Close window nicely after loop finishes
    wn.exitonclick()


# Run the main function. This should be the last statement in the file.
main()
