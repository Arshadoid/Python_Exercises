# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 17:00:48 2022

@author: Arshad Mehtiyev
"""

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(30,70), Point(70,30))
    #Circle(Point (50 , 50) , 20)
    shape.setOutline ( "red" )
    shape.setFill ( "red" )
    shape.draw(win)
    
    for i in range (10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX () - c.getX()
        dy = p.getY () - c.getY()
        copiedShape=shape.clone()
        copiedShape.draw(win)
        copiedShape.move(dx,dy)
        shape= copiedShape.clone()
    
    label = Text(Point(100,100),"Click again to quit")
    label.setStyle("bold")
    label.draw(win)    
    win.getMouse()
    win.close ()
main()