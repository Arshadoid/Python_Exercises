# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 18:14:36 2022

@author: Arshad Mehtiyev
"""

from graphics import *

def main():
    win = GraphWin()
        
    face = Circle(Point(100,100),75)
    face.setFill("beige")
    face.setOutline("black")
    face.draw(win)
    
    leftEye = Circle(Point(75,75), 13) 
    leftEye.setFill("white")
    leftEye.setOutline("black")
    leftEye.draw(win)
    
    leftEyeCent = Circle(Point(75,75), 2)
    leftEyeCent.setFill("black")    
    leftEyeCent.draw(win)
    
    rightEye = leftEye.clone()
    rightEye.move(50, 0)
    rightEye.draw(win)
    
    rightEyeCent = leftEyeCent.clone()
    rightEyeCent.move(50, 0)
    rightEyeCent.draw(win)
    
    lipA = Line(Point(50, 125),Point(75, 150))
    lipA.setWidth(4)
    lipA.draw(win)    
    
    lipB = Line(lipA.getP2(),Point(125, 150))
    lipB.setWidth(4)
    lipB.draw(win)
    
    lipC = Line(lipB.getP2(), Point(150,125))
    lipC.setWidth(4)
    lipC.draw(win)
    
    nose = Oval(Point(95,125), Point(105,95))
    nose.setWidth(2)
    nose.draw(win)
    
    win.getMouse()
    win.close()
main()