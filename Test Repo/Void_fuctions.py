# creating void functions
# A void function is a function that does not return a value
# Either no return statement, a  "return None" statement, or a return statement without an expression.

def say_hi():
    print("Greetings!")
    print("Salutations!")
    print("Hi!")

say_hi() #calling the function

x = say_hi()

print(x)

def greeter(name, age):
    print("Hello", name, "!")
    print("Next year you'll be", age + 1, "years old")
    return

greeter("Mickey", 84)

x = greeter("Minnie", 84)
print(x)

def foo():
    7 + 10 # there is no return statement in this function, so the calculation is lost as soon as python executes the function

foo()
print(foo()) #prints None because there is no return statement

def bar(x):
    print(x +7)
    return None #this function has a return statement, but it does not return a value

bar(3)

x = bar(3)
print(x) #prints None because the function returns None