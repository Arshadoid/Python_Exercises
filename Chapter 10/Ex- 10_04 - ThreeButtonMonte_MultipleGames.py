# -*- coding: utf-8 -*-
"""
Created on Wed May 25 09:34:33 2022

@author: Arshad Mehtiyev
"""
from button import Button
from graphics import *
from random import randint



class Monte:
    def __init__(self, win):
        self.win=win
        self.doorList=list()
        self.door1=Button(win, Point(1,3), 1, 1,'Door 1')
        self.doorList.append(self.door1)
        self.door2=Button(win, Point(2.5,3), 1, 1,'Door 2')
        self.doorList.append(self.door2)
        self.door3=Button(win, Point(4,3), 1, 1,'Door 3')
        self.doorList.append(self.door3)
        
        # creating quit buttin
        self.quitButton=Button(win, Point(6,1), 1,0.8,'Quit')
        self.quitButton.activate()
        # creating replay button
        self.replayButton=Button(win, Point(6,2), 1,0.8,'Replay')
        self.replayButton.deactivate()
        self.wins=0
        self.losses=0
        self.selDoor=0
        self.quitStatus=False
        self.replayStatus=False
        
        self.feedback=Text(Point(2.5,2), 'Select a Door!') 
        self.feedback.draw(self.win)
        
        
        # Creating Winas and Losses labels
        winLabel=Text(Point(0.5,1),'Wins:')
        winLabel.draw(self.win)
        lossLabel=Text(Point(2.5,1),'Losses:')
        lossLabel.draw(self.win)
        self.winNumber=Text(Point(1.25,1),str(self.wins))
        self.winNumber.draw(self.win)
        self.lossNumber=Text(Point(3.25,1),str(self.losses))
        self.lossNumber.draw(self.win)
        
    def play(self):
       
        for door in self.doorList:
            door.activate()
        
        self.specialDoor=randint(1,3)
        
        
        while True:
            click=self.win.getMouse()
            
            if click:
                if self.quitButton.clicked(click):
                    self.quitStatus=True
                    break
                elif self.replayButton.clicked(click):
                    self.replayStatus=True
                    break
                elif self.replayClicked() or ((self.wins+self.losses)==0):
                    if self.doorList[0].clicked(click):
                        self.selDoor=1
                        break
                    elif self.doorList[1].clicked(click):
                        self.selDoor=2
                        break
                    elif self.doorList[2].clicked(click):
                        self.selDoor=3
                        break

                    
                    
    def quitClicked(self):
       return self.quitStatus
   
    def replayClicked(self):
       return self.replayStatus
                
    def selectedDoor(self):
        return self.selDoor
    def setReplay(self):
        self.replayButton.activate()
        
    def setReplayStatus(self,status=True):
        self.replayStatus=status
                
    def feedbackText(self, text='Select a Door!'):

        self.feedback.setText(text)
    
    def displayResult(self):
        for door in self.doorList:
            door.deactivate()
        
        if self.specialDoor==self.selDoor:
            self.feedbackText('Correct!')
            self.doorList[self.selDoor-1].buttonSetFill('green')
            self.wins+=1
            self.selDoor=0
            self.setReplayStatus(False)
            
        elif self.selDoor!=0:
            self.feedbackText('Wrong!')
            self.doorList[self.selDoor-1].buttonSetFill('red')
            self.doorList[self.specialDoor-1].buttonSetFill('green')
            self.losses+=1
            self.selDoor=0
            self.setReplayStatus(False)
      
    def replay(self):
        for door in self.doorList:
            door.activate()
            door.buttonSetFill('lightgrey')
        self.feedbackText()
    
    def updateScores(self):  
    # Inilizing and drawing scores
        self.winNumber.setText(str(self.wins))
        self.lossNumber.setText(str(self.losses))
        
        

def main():
    win=GraphWin("Tree Button Monte", 400, 200)
    win.setCoords(0, 0, 7, 4)
    
    game=Monte(win)
            
        
    while True:
        
        game.play()
        if game.quitClicked():
            break
        
        if game.selectedDoor()!=0:
            game.displayResult()
        
        if game.replayClicked():
            game.replay()
        game.updateScores()
        
        game.setReplay()        
    win.close()
    
main()