# -*- coding: utf-8 -*-
"""
Created on Thu May 19 08:59:39 2022

@author: Arshad Mehtiyev
"""

from random import random, randint
import math
from graphics import *
from button import Button

def main():
    printIntro()
    steps=getInput()
    win =GraphWin('Simulation of random walk',400, 400)
    win.setBackground('white')
    startButton=Button(win,Point(45, 30),40,20, 'Start')
    startButton.activate()
    quitButton=Button(win,Point(85, 30),40,20, 'Quit')
    quitButton.activate()
    while True:
        p=win.getMouse()
        if startButton.clicked(p):
            startButton.deactivate()
            randomWalkSimulation(steps, win, quitButton)
        elif quitButton.clicked(p):
            break
    win.close()
        
    
    
    
    
    
def printIntro():
    print("This program runs simulation of a random walk on a graphical window")


def getInput():
    steps=int(input("How many steps to simulate? "))
    return steps
    
def randomWalkSimulation(steps, win, quitButton):
    
    # starting coordinates
    xOld=200
    yOld=200
    
           
    for i in range(steps):
        p2=win.checkMouse()
        if p2!= None:
            if quitButton.clicked(p2):
                break
        angle= random()*2*math.pi
        xNew=xOld+5*math.cos(angle)
        yNew=yOld+5*math.sin(angle)
        drawStep(xOld,yOld,xNew,yNew, win)
        xOld=xNew
        yOld=yNew
    print('Done')

    
    
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