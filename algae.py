import turtle
import time

# L-System
# ----------
#
# Variables: A B
# Constants: /
# Axiom    : A
# Rules    : A -> AB | B -> A
axiom = "A"


# ------------------------------------------------------------------------------#
#                            Expansion                                          #
# ------------------------------------------------------------------------------#

def expand(s):
    switch = {
        "A": "AB",
        "B": "A",
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
