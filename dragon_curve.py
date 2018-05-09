import turtle
import time

# L-System
# ----------
#
# Variables : X | Y
# Constants : F | + | -
# Axiom     : FX
# Rules     : X -> X+YF+ | Y -> -FX-Y
axiom = "FX"


# ------------------------------------------------------------------------------#
#                            Expansion                                          #
# ------------------------------------------------------------------------------#

def expand(s):
    switch = {
        "X": "X+YF+",
        "Y": "-FX-Y",
    }
    return switch.get(s, s)


def expand_once(string):
    return [expand(c) for c in string]


def expand_n(s, n):
    for i in range(n):
        s = ''.join(expand_once(s))
    return s


expanded = expand_n(axiom, 10)
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

for c in expanded:
    if c == "F":
        turtle.forward(3)
    elif c == "-":
        turtle.left(90)
    elif c == "+":
        turtle.right(90)

time.sleep(50000)  # Wait before you close all the windows.
