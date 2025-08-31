# SPIRAL EDIT BY CHEYENNE PIERCE 8/31/2025

# idea is to draw a shape different than the one I did last unit
# sharing my step by step
# starting off with the start command

import turtle


def draw_pentagon(t, num):
    """Make a turtle t draw a pentagon num times in a spiral pattern"""
    for i in range(num):  # Repeat the process num times
        for j in range(5):  # A pentagon has 5 sides
            t.forward(100)  # Commanding pen to move forward 100 units
            t.right(72)    # Turn right by 72 degrees (360 degrees / 5 sides)
        t.forward(5)  # Moving pen forward a little
        t.right(20)  # Turning pen in order to make a spiral


def main():
    """This is where the turtle and window should be set up for the main function in this program"""
    wn = turtle.Screen()  # make the window
    wn.bgcolor("pink")   # set the background color
    # Draw a pentagon
    pen = turtle.Turtle()
    pen.color("purple")  # Setting the pen color to purple
    pen.speed(4)  # You can adjust this value (1-10, or 0 for fastest)
    # Draw the pentagons
    draw_pentagon(pen, 10)

    wn.exitonclick()


# Calling the main function
main()
