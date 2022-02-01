# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 15:26:25 2022

@author: Arshad Mehtiyev
"""
from graphics import *

# create a default 200x200 window
win = GraphWin( "Tic-Tac-Toe " )
# set coordinates to go from (0 , 0) in the lower left
# to (3 , 3) in the upper right .
win.setCoords( 0.0, 0.0 , 3.0 , 3.0)
# Draw vertical lines
Line (Point( 1 , 0) , Point( 1 , 3) ).draw (win)
Line (Point(2 , 0) , Point(2 , 3) ).draw (win)
# Draw horizontal lines
Line (Point(0 , 1 ) , Point(3 , 1 ) ).draw (win)
Line (Point(0 , 2) , Point(3 , 2) ).draw (win)

input ( "Press <Enter> to quit " )
win.close()