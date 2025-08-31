# Fruitful functions are functions that return a value after you call them
# This function will return the area of a circle after we provide the radius. 

import math
def circle_area(radius): #radius will be the "input" or argument of the function
    temp = math.pi * radius ** 2 #equation for the area of a circle is pi * r^2
    return temp

r = float(input ("Give me the radius of a circle.")) # we ask the user for a radius and convert the string value of the input function to a floating point 
Area = circle_area(r) #we call the function circle_area and provide the argument
print("The area of a circle with radius", r, "is", Area)
