# Revamped Unit 2 Assignment by Cheyenne Pierce
# 8/29/2025


# Import the relevent modules
import turtle
import random

# Setting the range of coordinates for the turtle screen
turtle.setup(width=600, height=600)

# Setting variables for the hexagram
side = 20
angle_outside = 60
angle_inside = 120


def draw_hexagram(t, num):
    """Make a turtle t draw a hexagram 'num' number of times at different random coordinates"""
    for i in range(num):
        # Generate a new random coordinate for each hexagram
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        # Move turtle to randomly generated coordinates
        t.penup()
        t.goto(x, y)
        t.pendown()
        # Draw the hexagram
        for aColor in ["purple", "blue", "green", "yellow", "orange", "red"]:
            t.color(aColor)
            t.forward(side)
            t.right(angle_outside)
            t.forward(side)
            t.left(angle_inside)


def main():
    """This is where the turtle and window will be set up for the main function in this program"""
    wn = turtle.Screen()  # make the window
    wn.bgcolor("black")   # set the background color

    stella = turtle.Turtle()
    stella.shape("turtle")
    stella.pensize(2)
    stella.speed(4)

    draw_hexagram(stella, 10)
    stella.hideturtle()

    wn.exitonclick()


main()
