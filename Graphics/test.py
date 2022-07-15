from graphics import *
import random as rd

PICWIDTH = 600
PICHEIGHT = 600

win = GraphWin(title = "Lab1", width = PICWIDTH, height = PICHEIGHT) 
win.setCoords(0, 0, PICWIDTH - 1, PICHEIGHT - 1)
win.setBackground("white")
i = 8; lst = []
while i >= 0:
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    i -= 1
    c = color_rgb(r,g,b)
    lst.append(c)
print(lst)

rect1 = Rectangle(Point(0, 0), Point(200, 200))
rect1.setFill(lst[0])
rect2 = Rectangle(Point(200, 0), Point(400, 200))
rect2.setFill(lst[1])
rect3 = Rectangle(Point(400, 0), Point(600, 200))
rect3.setFill(lst[2])
rect4 = Rectangle(Point(0, 200), Point(200, 400))
rect4.setFill(lst[3])
rect5 = Rectangle(Point(200, 200), Point(400, 400))
rect5.setFill(lst[4])
rect6 = Rectangle(Point(400, 200), Point(600, 400))
rect6.setFill(lst[5])
rect7 = Rectangle(Point(0, 400), Point(200, 600))
rect7.setFill(lst[6])
rect8 = Rectangle(Point(200, 400), Point(400, 600))
rect8.setFill(lst[7])
rect9 = Rectangle(Point(400, 400), Point(600, 600))
rect9.setFill(lst[8])

rect1.draw(win)
rect2.draw(win)
rect3.draw(win)
rect4.draw(win)
rect5.draw(win)
rect6.draw(win)
rect7.draw(win)
rect8.draw(win)
rect9.draw(win)

win.getMouse()         
win.close()