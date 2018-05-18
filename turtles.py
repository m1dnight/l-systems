import sys
import numpy

# Canvas
height = 9999
width = 9999
canvas = numpy.zeros(shape=(height, width)).astype('uint8')

# Turtle state.
y = width / 2
x = height
angle = 0
stack = []


############
# Position #
############

def center():
    setposition((height / 2, width / 2))


def bottom():
    setposition((0, width / 2))


def setposition((px, py)):
    global x
    x = px
    global y
    y = py


def save_position():
    global stack
    state = (angle, (x, y))
    stack.append(state)


def restore_position():
    global stack
    (a, p) = stack.pop()
    setposition(p)
    set_angle(a)


############
# Moving   #
############
#        0
#        |
# 270 ---|--- 90
#        |
#       180
# Move the turtle forward, while drawing.
def forward(n):
    global angle
    global x
    global y

    if n != 0:
        draw()
        if angle == 0:
            y -= 1
        elif angle == 45:
            x += 1
            y -= 1
        elif angle == 90:
            x += 1
        elif angle == 135:
            x += 1
            y += 1
        elif angle == 180:
            y += 1
        elif angle == 225:
            x -= 1
            y += 1
        elif angle == 270:
            x -= 1
        elif angle == 315:
            x -= 1
            y -= 1
        else:
            print "angle:"
            print angle
            sys.exit("Invalid angle!")

        forward(n - 1)


def set_angle(a):
    global angle
    angle = a


def left(a):
    global angle
    angle = ((angle - a) + 360) % 360


def right(a):
    global angle
    angle = ((angle + a) + 360) % 360


############
# Drawing  #
############

def draw():
    global canvas
    # Just ignore writing out of bounds.
    if 0 <= x < width and 0 <= y < height:
        canvas[x, y] = 255


def pprint():
    print canvas
