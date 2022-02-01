# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 18:03:11 2022

@author: Arshad Mehtiyev
"""

from graphics import *

def main():
    win = GraphWin()
    whiteCircle = Circle(Point(100,100), 100) 
    whiteCircle.setFill("white")
    whiteCircle.setOutline("black")
    whiteCircle.draw(win)
    
    blackCircle = Circle(Point(100,100), 80) 
    blackCircle.setFill("black")
    blackCircle.setOutline("black")
    blackCircle.draw(win)
    
    blueCircle = Circle(Point(100,100), 60) 
    blueCircle.setFill("blue")
    blueCircle.setOutline("black")
    blueCircle.draw(win)
    
    redCircle = Circle(Point(100,100), 40) 
    redCircle.setFill("red")
    redCircle.setOutline("black")
    redCircle.draw(win)
    
    yelCircle = Circle(Point(100,100), 20) 
    yelCircle.setFill("yellow")
    yelCircle.setOutline("black")
    yelCircle.draw(win)
    
    win.getMouse()   
    win.close()
    
main()