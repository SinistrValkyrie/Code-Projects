# Unit 2 Assignment by Cheyenne Pierce

# I liked the idea of creating a rainbow shape, and the 6-pointed star was the perfect subject. 
# I wanted to arrange them in a way where if I wanted to build more points and layer them into a design, I could just change up the color scheme and move the turtle to new coordinates in the window. 
# That's why I added the 5th shape, the one in the center. 
# With that one added we can see there's a new rainbow trifecta shape created as well!
# Additionally, I chose stella.penup/pendown methods instead of simplified stella.up/down methods for my own clarity in reading and writing the code. 

import turtle
wn = turtle.Screen()
wn.bgcolor("black")

stella = turtle.Turtle()
stella.shape("turtle")
stella.pensize(3)
stella.speed(2)
side = 50
angle_outside = 60
angle_inside = 120

#Rainbow Hex 1
for aColor in ["purple", "blue", "green", "yellow", "orange", "red"]: 
    stella.color(aColor)
    stella.forward(side)
    stella.right(angle_outside)
    stella.forward(side)
    stella.left(angle_inside)

#Pick up tail, go to the next location
stella.penup()
stella.goto(150.00, 0.00)
stella.pendown()

#Rainbow Hex 2
for aColor in ["purple", "blue", "green", "yellow", "orange", "red"]: 
    stella.color(aColor)
    stella.forward(side)
    stella.right(angle_outside)
    stella.forward(side)
    stella.left(angle_inside)
    print(stella)

#Next location
stella.penup()
stella.goto(0, 86.6)
stella.pendown()
stella.right(180)

#Rainbow Hex 3
for aColor in ["yellow", "orange", "red", "purple", "blue", "green"]:
    stella.color(aColor)
    stella.forward(side)
    stella.right(angle_outside)
    stella.forward(side)
    stella.left(angle_inside)

#Another location
stella.penup()
stella.goto(-150, 86.6)
stella.pendown()

#Rainbow Hex 4
for aColor in ["yellow", "orange", "red", "purple", "blue", "green"]: 
    stella.color(aColor)
    stella.forward(side)
    stella.right(angle_outside)
    stella.forward(side)
    stella.left(angle_inside)

#One more for good measure
stella.penup()
stella.goto(0, 0)
stella.pendown()
stella.left(60)

#Rainbow Hex 5
for aColor in ["orange", "red", "purple", "blue", "green", "yellow"]: 
    stella.color(aColor)
    stella.forward(side)
    stella.right(angle_outside)
    stella.forward(side)
    stella.left(angle_inside)

wn.exitonclick()