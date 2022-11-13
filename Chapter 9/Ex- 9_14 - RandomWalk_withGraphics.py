# -*- coding: utf-8 -*-
"""
Created on Thu May 19 08:59:39 2022

@author: Arshad Mehtiyev
"""

from random import random, randint
import math
from graphics import *

def main():
    printIntro()
    steps=getInput()
    randomWalkSimulation(steps)
    
    
def printIntro():
    print("This program runs simulation of a random walk on a graphical window")


def getInput():
    steps=int(input("How many steps to simulate? "))
    return steps
    
def randomWalkSimulation(steps):
    win =GraphWin('Simulation of random walk',400, 400)
    win.setBackground('white')
    # starting coordinates
    xOld=200
    yOld=200
    
    for i in range(steps):
        angle= random()*2*math.pi
        xNew=xOld+5*math.cos(angle)
        yNew=yOld+5*math.sin(angle)
        drawStep(xOld,yOld,xNew,yNew, win)
        xOld=xNew
        yOld=yNew
    print('Done')
    win.getMouse()
    win.close()
    
def drawStep(xOld,yOld,xNew,yNew, win):
    p1=Point(xOld,yOld)
    p2=Point(xNew,yNew)
    line=Line(p1, p2)
    line.setWidth(3)
    line.setFill(color_rgb(randcol(), randcol(), randcol()))
    line.draw(win)

def randcol():
    return randint(0,255)


if __name__ == '__main__':
    main()