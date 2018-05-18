import turtles
from PIL import Image

# Note:
# The angle of the fractal plant should be 25 degrees, but due to a limitation of
# the turtles library, we can only use multiples of 45 degrees.

# L-System
# ----------
#
# Variables : X | F
# Constants : [ | ] | + | -
# Axiom     : X
# Rules     : X -> F+[[X]-X]-F[-FX]+X | F -> FF

axiom = "X"


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


expanded = expand_n(axiom, 10)

# ------------------------------------------------------------------------------#
#                            Printing                                           #
# ------------------------------------------------------------------------------#

# Setup turtle start values.
turtles.left(90)  # Go up to start.
turtles.center()

for c in expanded:
    if c == "F":
        turtles.forward(7)
    elif c == "-":
        turtles.left(45)
    elif c == "+":
        turtles.right(45)
    elif c == "[":
        turtles.save_position()
    elif c == "]":
        turtles.restore_position()

# Write out the image.
im = Image.fromarray(turtles.canvas)
im.save("fractal_plant.jpg")
