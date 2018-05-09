import turtle
import time
import random

random.seed()

# L-System
# ----------
#
# Variables: 0 | 1
# Constants: [ | ]
# Axiom    : 0
# Rules    : 1 (1.0) -> 11
#          | 0 (0.5) -> 1[0]0
#          | 0 (0.5) -> 0
axiom = "0"


# ------------------------------------------------------------------------------#
#                            Expansion                                          #
# ------------------------------------------------------------------------------#

def expand(s):
    switch = {
        "0": [(0.5, "1[0]0"), (0.5, "0")], # The probabilities should add up to 1.
        "1": [(1.0, "11")],
    }
    possibilities = switch.get(s, [(1.0, s)])
    chance = random.random()

    acc = 0.0
    for rule in possibilities:
        odds = rule[0]
        subs = rule[1]
        if acc <= chance <= acc + odds:
            return subs
        else:
            acc += chance



def expand_once(string):
    return [expand(c) for c in string]


def expand_n(s, n):
    for i in range(n):
        s = ''.join(expand_once(s))
    return s


expanded = expand_n(axiom, 6)
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

# Start at the bottom.
turtle.penup()
turtle.setposition(0, -1 * (height / 2))
stack = []
turtle.pendown()


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
