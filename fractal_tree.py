import turtle
import time

# L-System
# ----------
#
# Variables: 0 | 1
# Constants: [ | ]
# Axiom    : 0
# Rules    : 1 -> 11 | 0 -> 1[0]1
axiom = "0"


# -------------fractal_tree.py-----------------------------------------------------------------#
#                            Expansion                                          #
# ------------------------------------------------------------------------------#

def expand(s):
    switch = {
        "0": "1[0]0",
        "1": "11",
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
    if c == "0":
        turtle.forward(5)
    elif c == "1":
        turtle.forward(5)
    elif c == "[":
        save_position()
        turtle.left(45)
    elif c == "]":
        restore_position()
        turtle.right(45)

time.sleep(50000)  # Wait before you close all the windows.
