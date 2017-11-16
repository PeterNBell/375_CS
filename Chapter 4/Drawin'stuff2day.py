import graphics
from graphics import *
global win
global head
def main():
    global win
    win = graphics.GraphWin('Shapes', 500, 500)
    draw_head()
    x = ""
    while x != "n":
        x = win.checkKey()
        move_head()


def move_head(circ1, circ2, circ3, circ4,circ5):
    xpos = win.getMouse.getX()
    ypos = win.getMouse.getY()
    circ1.move(xpos,ypos)
    circ2.move(xpos,ypos)
    circ3.move(xpos,ypos)
    circ4.move(xpos,ypos)
    circ5.move(xpos,ypos)


def draw_head():
    global win
    global head
    win.setBackground('black')
    center = Point(100,100)
    circ1 = Circle (center, 50)
    circ1.setFill('yellow')
    circ1.draw(win)
    center = Point(100,110)
    circ2 = Circle (center, 37)
    circ2.setFill('white')
    circ2.setOutline('yellow')
    circ2.draw(win)
    center = Point(100,100)
    circ3 = Circle (center, 35)
    circ3.setFill('yellow')
    circ3.setOutline('yellow')
    circ3.draw(win)
    center = Point(120,80)
    circ4 = Circle (center, 10)
    circ4.setFill('black')
    circ4.draw(win)
    center = Point(80,80)
    circ5 = Circle (center, 10)
    circ5.setFill('black')
    circ5.draw(win)
main()


