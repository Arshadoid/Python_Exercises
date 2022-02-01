# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 18:53:56 2022

@author: Arshad Mehtiyev


11. Five-click House.
You are to write a program that allows the user to draw a simple house
using five mouse clicks. The first two clicks will be the opposite corners of
the rectangular frame of the house. The third click will indicate the center
of the top edge of a rectangular door. The door should have a total width
that is 1/5 of the width of the house frame. The sides of the door should
extend from the corners of the top down to the bottom of the frame. The
fourth click will indicate the center of a square window. The window is
half as wide as the door. The last click will indicate the peak of the roof.
The edges of the roof will extend from the point at the peak to the corners
of the top edge of the house frame.

"""

from graphics import *

def main():
    win = GraphWin("Draw a house",400,400)
    win.setBackground("white")
     
    p1=win.getMouse()
    p2=win.getMouse()
    
    base = Rectangle(p1, p2)
    base.draw(win)
    
    print("P1: ",base.getP1())
    print("P2: ", base.getP2())
    
    p3=win.getMouse()
    
    doorWitdhHalf = (abs( p1.getX()-p2.getX())*0.2)/2
    doorP1=Point(p3.getX()-doorWitdhHalf, p3.getY())
    baseCenterPoint=base.getCenter()
    baseFloorY = baseCenterPoint.getY()+(abs(p1.getY()-p2.getY()))/2 
    baseRoofY = baseCenterPoint.getY()-(abs(p1.getY()-p2.getY()))/2 
    doorP2=Point(p3.getX()+doorWitdhHalf, baseFloorY)
    door = Rectangle(doorP1,doorP2)
    door.draw(win)    
    
    p4=win.getMouse()
    
    windowWidthHalf=doorWitdhHalf/2
    window=Rectangle(Point(p4.getX()-windowWidthHalf,p4.getY()+windowWidthHalf),
                     Point(p4.getX()+windowWidthHalf,p4.getY()-windowWidthHalf))
    window.draw(win)    
    
    
    p5=win.getMouse()
    
    trnglP1=Point(p1.getX(), baseRoofY)
    trnglP2=Point(p2.getX(), baseRoofY)
    
    roof=Polygon(trnglP1,trnglP2,p5)
    roof.draw(win)
    
    print(doorWitdhHalf)
   
    win.getMouse()
    win.close() 
    
    
    

main()