import turtles
from PIL import Image

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


expanded = expand_n(axiom, 20)

# ------------------------------------------------------------------------------#
#                            Printing                                           #
# ------------------------------------------------------------------------------#

# Setup turtle start values.
turtles.setposition((5000, 5000))
turtles.left(90)  # Go up to start.


for c in expanded:
    if c == "F":
        turtles.forward(10)
    elif c == "-":
        turtles.left(90)
    elif c == "+":
        turtles.right(90)

# Write out the image.
im = Image.fromarray(turtles.canvas)
im.save("dragon_curve.jpg")
