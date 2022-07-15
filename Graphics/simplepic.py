from graphics import *

PICWIDTH = 600
PICHEIGHT = 600

win = GraphWin(title = "Studio 6507", width = PICWIDTH, height = PICHEIGHT) 
win.setCoords(0, 0, PICWIDTH - 1, PICHEIGHT - 1)
win.setBackground("white")

# Draw a purple rectangle with corners at (100, 300) and (400, 150)
top_left = Point(100, 300)
bottom_right = Point(400, 150)
top_left.draw(win)
bottom_right.draw(win)
rect = Rectangle(top_left, bottom_right)
rect.setFill("purple")
rect.draw(win)

# Draw a black rectangle with corners at (250, 175) and (500, 100)
rect2 = Rectangle(Point(250, 175), Point(500, 100))
rect2.setFill("black")
rect2.draw(win)

win.getMouse()         # Pause to view result (otherwise image vanishes quickly)
win.close()            # Close window when done
