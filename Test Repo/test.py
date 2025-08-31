

import turtle

# Set up the screen where the magic happens
screen = turtle.Screen()
screen.bgcolor("black")  # I chose black for a clean canvas

# Meet Court, the turtle artist
Court = turtle.Turtle()
Court.shape("turtle")  # Making Court look like a turtle, because why not?
Court.speed(2)  # Let’s not rush, we want to enjoy the process
Court.color("red")  # Red is perfect for a heart!
Court.speed("slowest")
# Time to draw a heart
Court.begin_fill()  # Let's start filling in the heart shape



Court.right(50)  # Turn around to make the other side of the heart
Court.forward(133)
Court.circle(50, 200)  # And make the second curve
Court.right(140)  # Start with a little turn
Court.circle(50, 200)  # Now, let's make the first curve
Court.forward(133)  # Move forward to get the shape started

