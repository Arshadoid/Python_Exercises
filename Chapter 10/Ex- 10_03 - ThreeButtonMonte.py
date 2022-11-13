# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:53:00 2022

@author: Arshad Mehtiyev
"""

from button import Button
from graphics import *
from random import randint

def main():
    win=GraphWin("Tree Button Monte", 300, 200)
    win.setCoords(0, 0, 5, 4)
    
    doorList=list()
    door1=Button(win, Point(1,3), 1, 1,'Door 1')
    doorList.append(door1)
    door2=Button(win, Point(2.5,3), 1, 1,'Door 2')
    doorList.append(door2)
    door3=Button(win, Point(4,3), 1, 1,'Door 3')
    doorList.append(door3)
    
    for door in doorList:
        door.activate()
        
    specialDoor=randint(1,3)
    
    selectedDoor=0
    
    while selectedDoor==0:
        click = win.getMouse()
        
        if door1.clicked(click):
            selectedDoor=1
        elif door2.clicked(click):
            selectedDoor=2
        elif door3.clicked(click):
            selectedDoor=3
    
    
    for door in doorList:
        door.deactivate()
    
    
    if specialDoor==selectedDoor:
        text='Correct!'
        doorList[selectedDoor-1].buttonSetFill('green')
        
    else:
        text='Wrong! Special door was Door '+str(specialDoor)
        doorList[selectedDoor-1].buttonSetFill('red')
        doorList[specialDoor-1].buttonSetFill('green')
    
    feedback=Text(Point(2.5,2), text)    
    feedback.draw(win)
    
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
