import graphics
from graphics import *
global x
global y
global startx
global starty
global win
def main():
    global x
    global y
    global startx
    global starty
    global win
    win = graphics.GraphWin('Shapes', 500, 500)
    x = 25
    y = 250
    startx = 0
    starty = 250
    drawA()


def drawA():
    global win
    global startx
    global starty
    global x
    global y
    linea = Line(starty, startx)
