# Draw My Initials useing turtle
# William Buckwell
# 3/25/18

import turtle
win = turtle.Screen()
turtle = turtle.Turtle()

def main():

    # Set new starting postion
    turtle.penup()
    turtle.backward(100)
    turtle.pendown()

    # Draw the W
    turtle.right(75)
    turtle.forward(100)
    turtle.left(150)
    turtle.forward(50)
    turtle.right(150)
    turtle.forward(50)
    turtle.left(150)
    turtle.forward(100)

    # Set new postion for next letter
    turtle.right(75)
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()

    # Draw start of B
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(35)

    # Draw the round part and connecting lines for the B
    for step in range(45):
        turtle.left(4)
        turtle.forward(1.5)

    turtle.forward(33)
    turtle.left(180)
    turtle.forward(33)

    for step in range(45):
        turtle.left(4)
        turtle.forward(2)

    turtle.forward(33)

main()
