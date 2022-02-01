# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 15:59:17 2022

@author: Arshad Mehtiyev
"""

# click . py
from graphics import *

def main ( ):
    win = GraphWin ( " Click Me ! " )
    for i in range (10):
        p = win.getMouse()
        print ( "You clicked at : " , p.getX() , p.getY() )
    win.close()
main ()