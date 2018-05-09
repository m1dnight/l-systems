import turtle
import time

# L-System
# ----------
#
# Variables: X | F
# Constants: + | − | []
# Axiom    : X
# Rules    : X -> F+[[X]-X]-F[-FX]+X | F -> FF
# angle    : 25°
axiom = "FX"


# ------------------------------------------------------------------------------#
#                            Expansion                                          #
# ------------------------------------------------------------------------------#

def expand(s):
    switch = {
        "X": "F+[[X]-X]-F[-FX]+X",
        "F": "FF",
    }
    return switch.get(s, s)


def expand_once(string):
    return [expand(c) for c in string]


def expand_n(s, n):
    for i in range(n):
        s = ''.join(expand_once(s))
    return s


expanded = expand_n(axiom, 3)
print(expanded)

# ------------------------------------------------------------------------------#
#                            Printing                                           #
# ------------------------------------------------------------------------------#

# Setup turtle start values.
turtle.speed(0)  # max speed
turtle.left(90)  # Go up to start.
height = 1080
width = 1080
turtle.setup(width, height)
stack = []


def save_position():
    state = (turtle.heading(), turtle.position())
    stack.append(state)


def restore_position():
    (angle, position) = stack.pop()
    turtle.penup()
    turtle.setposition(position)
    turtle.pendown()
    turtle.setheading(angle)


for c in expanded:
    if c == "F":
        turtle.forward(7)
    elif c == "-":
        turtle.left(25)
    elif c == "+":
        turtle.right(25)
    elif c == "[":
        save_position()
    elif c == "]":
        restore_position()

time.sleep(50000)  # Wait before you close all the windows.
