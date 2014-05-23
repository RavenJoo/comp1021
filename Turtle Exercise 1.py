"""
    This program acts like a sketchbook.
    Drag the turtle to draw freely on the window.
"""

import turtle

# This function jumps the turtle to the place clicked on the screen.
def jump(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

turtle.reset()

turtle.shape("turtle")
turtle.pencolor("blue") # Color is set to blue
turtle.pensize(3) # Pensize is set to 3

turtle.onscreenclick(jump)
turtle.ondrag(turtle.goto) # The goto function uses the x and y coordinates passed by ondrag event
turtle.speed(0)

turtle.done()
