# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:51:50 2022

@author: Arshad Mehtiyev
"""

# roller . py
# Graphics program to roll a pair of dice . Uses custom widgets
# Button and DieView .
from random import randrange,randint
from graphics import GraphWin, Point, color_rgb
from cbutton import CButton
from dieviewmodified import DieView

def randColor():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    return r,g,b

def main():
# create the application window
    win = GraphWin("Dice Roller" )
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")
    # Draw the interface widgets
    die1 = DieView(win, Point(3,8), 2)
    die2 = DieView(win, Point(7,8), 2)
    rollButton = CButton(win, Point(5,4.5), 1.75, "Roll Dice" )
    rollButton.activate()
    quitButton = CButton(win, Point(5,1), 1, "Quit" )
    
    
    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            r,g,b=randColor()
            value1 = randrange(1,7)
            die1.setValue(value1)
            die1.setColor(color_rgb(r,g,b))
            value2 = randrange(1,7)
            die2.setValue(value2)
            die2.setColor(color_rgb(r,g,b))
            quitButton.activate()
        pt = win.getMouse()
    # close up shop
    win.close()
main()