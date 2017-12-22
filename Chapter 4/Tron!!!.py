from graphics import *
usedPoints = []
def main():
    print("Press the arrow keys to move the rectangle, press 'q' to quit") #Explaining the how to play to the player

    window_size = 600
    canvas_size = 100

    win = GraphWin("Animation Example with Keyboard", window_size, window_size)
    win.setCoords(0, 0, canvas_size, canvas_size)
    win.setBackground("black")
    message_text = Text(Point(canvas_size/2, canvas_size/2), "CLICK TO START") # a basic "play" button
    message_text.setTextColor("white")
    message_text.setSize(30)
    message_text.draw(win)
    win.getMouse() #Wait till the player clicks to start
    message_text.undraw()
    aRectangle = Rectangle(Point (49.5,1.5), Point(50.5, 2.5)) #in order to make the rectangle a 1 x 1 square on the right coordinates,
    aRectangle.setFill("green")
    aRectangle.setOutline("green")
    aRectangle.draw(win)
    currentKey = "Up" #starts the player moving forward
    while True:
            global usedPoints
            currentPoint = Point(aRectangle.getCenter().getX(),aRectangle.getCenter().getY()) #get the center
            CheckPoint(currentPoint,canvas_size, win)
            key = win.checkKey()
            if key != "": #if the player has pressed a key that would change the direction by 90 degrees, change the direction
                if key == "Down" and currentKey != "Up":
                    currentKey = key
                elif key == "Up" and currentKey != "Down":
                    currentKey = key
                elif key == "Right" and currentKey != "Left":
                    currentKey = key
                elif key == "Left" and currentKey != "Right":
                    currentKey = key
            timer = 0.5 #wait before moving so it looks like motion
            time_check = time.time();
            while timer > 0:
                 if (time.time() - time_check) > 0:
                    time_check = time.time()
                 timer -= 0.1
            delta_x = 0
            delta_y = 0
            if currentKey == "Up":
                delta_y += 1
            elif currentKey == "Down":
                delta_y -= 1
            elif currentKey == "Left":
                delta_x -= 1
            elif currentKey == "Right":
                delta_x += 1
            bRectangle = aRectangle.clone() #make trail
            bRectangle.draw(win)
            aRectangle.move(delta_x, delta_y)

def CheckPoint(currentPoint,canvas_size, win): #see if the point that the square is in has already been touched
    global usedPoints
    usedPoints.insert(0, currentPoint)
    usedPoints.count(currentPoint)
    if usedPoints.count(currentPoint) > 1:
        endgame(canvas_size, win)
    else:
        usedPoints.insert(0,currentPoint)




def endgame(canvas_size, win): #Say game over
    message_text = Text(Point(canvas_size / 2, canvas_size / 2), "")
    message_text.setTextColor("red")
    message_text.setText("GAME OVER")
    message_text.setSize(30)
    message_text.draw(win)
    input("Game over!. Press Enter to quit.")

main()
