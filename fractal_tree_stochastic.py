import turtles
from PIL import Image
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
        "0": [(0.5, "1[0]0"), (0.5, "0")],  # The probabilities should add up to 1.
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


expanded = expand_n(axiom, 11)

# ------------------------------------------------------------------------------#
#                            Printing                                           #
# ------------------------------------------------------------------------------#

# Start at the bottom.
turtles.bottom()
turtles.set_angle(90)

for c in expanded:
    if c == "0":
        turtles.forward(5)
    elif c == "1":
        turtles.forward(5)
    elif c == "[":
        turtles.save_position()
        turtles.left(45)
    elif c == "]":
        turtles.restore_position()
        turtles.right(45)

# Write out the image.
im = Image.fromarray(turtles.canvas)
im.save("fractal_tree_stochastic.jpg")
