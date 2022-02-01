# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 16:37:55 2022

@author: Arshad Mehtiyev
"""

# clickntype . py
from graphics import *
def main ():
    win = GraphWin ( " Click and Type " , 400 , 400)
    for i in range (10):
        pt = win.getMouse ()
        key = win.getKey()
        label = Text (pt , key)
        label.draw(win)
        
    win.getMouse ()
    win.close()
main()