import turtles
from PIL import Image

# L-System
# ----------
#
# Variables: 0 | 1
# Constants: [ | ]
# Axiom    : 0
# Rules    : 1 -> 11 | 0 -> 1[0]0
axiom = "0"


# ------------------------------------------------------------------------------#
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


expanded = expand_n(axiom, 11)

# ------------------------------------------------------------------------------#
#                            Printing                                           #
# ------------------------------------------------------------------------------#


# Start at the bottom.
turtles.bottom()
turtles.set_angle(90)

for c in expanded:
    if c == "0":
        turtles.forward(1)
    elif c == "1":
        turtles.forward(3)
    elif c == "[":
        turtles.save_position()
        turtles.left(45)
    elif c == "]":
        turtles.restore_position()
        turtles.right(45)

# Write out the image.
im = Image.fromarray(turtles.canvas)
im.save("fractal_tree.jpg")