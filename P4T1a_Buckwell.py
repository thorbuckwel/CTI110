# Draw a square and a triangle with the turtle program
# William Buckwell
# 3/25/18

import turtle
win = turtle.Screen()
turtle = turtle.Turtle()


def main():

    count = 0

    # Draw Square
    while count < 5:
        turtle.forward(40)
        turtle.right(90)
        count += 1

    # Move to new postion
    turtle.forward(40)
    turtle.left(90)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()
    
    count = 0

    # Draw Triangle
    while count < 2:
        turtle.forward(40)          
        turtle.left(120)
        count += 1
    turtle.forward(40)

main()
