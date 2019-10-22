from graphics import *
import math

def inCircle(lol, circ):
    dx = lol.getX() - circ.getCenter().getX()
    dy = lol.getY() - circ.getCenter().getY()
    dist = math.sqrt(dx*dx+dy*dy)

    return dist <= circ.getRadius()

def main():
    win = GraphWin("h",1000,1000)
    white = Circle(Point (500,500) , 375)
    black = Circle(Point (500,500) , 300)
    blue = Circle(Point (500,500) , 225)
    red = Circle(Point (500,500) , 150)
    yellow = Circle(Point (500,500) , 75)

    white.setFill("white")
    black.setFill("black")
    blue.setFill("blue")
    red.setFill("red")
    yellow.setFill("yellow")

    white.draw(win)
    black.draw(win)
    blue.draw(win)
    red.draw(win)
    yellow.draw(win)
    
    click = 0
    score = 0
    total = 0
    for i in range (5):
        click = win.getMouse()
        if inCircle(click, yellow):
            score = 9
        elif inCircle(click, red):
            score = 7
        elif inCircle(click, blue):
            score = 5
        elif inCircle(click, black):
            score = 3
        elif inCircle(click, white):
            score = 1
        print("that was worth", score, "points")
        total += score
        

    print ("your total was", total)
main() 
