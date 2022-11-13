# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:35:59 2022

@author: Arshad Mehtiyev
"""

from graphics import *
from button import Button

class Regression:
    def __init__(self,win):
        self.win=win
        self.points=[]
        self.n=0 # Counter of clicks()points
        self.xSum=0
        self.ySum=0
        self.xSquaredSum=0
        self.xySum=0
        pass
    
    def addPoint(self, point):
        clickX=point.getX()
        clickY=point.getY()
        
        self.n+=1            
        self.xSum+=clickX
        self.ySum+=clickY
        self.xSquaredSum+=clickX**2
        self.xySum+=clickX*clickY
        
        self.points.append((clickX,clickY))
        Point(self.points[-1][0],self.points[-1][1]).draw(self.win)
        
    def predict(self):
        
        if self.n!=0:
            m=(self.xySum-(self.xSum*self.ySum)/self.n)/(self.xSquaredSum-
                                                         self.xSum**2/self.n)
            
            x1=0
            x2=10
            
            y1=self.ySum/self.n+m*(x1-self.xSum/self.n)
            y2=self.ySum/self.n+m*(x2-self.xSum/self.n)
            
            regressionLine=Line(Point(x1,y1), Point(x2,y2))
            regressionLine.setFill("red")
            regressionLine.draw(self.win)
        
    def getPoints(self):
        return self.points



def main():
      
    
    # Creating main wirndow and done button
    win = GraphWin("Plot Regression Line", 500,500)
    win.setCoords(0, 0, 10, 11)
    
    print("Specify the data points on graphics window and click 'Done' when finish")
   
    userButton=Button(win, Point(1,0.5), 2, 1, 'Done')
    userButton.buttonSetFill('cyan')
    userButton.activate()
        
    regressionLine=Regression(win)
    
    done=False
    # Main loop
      
    while True:
                   
        p=win.getMouse()
                
        if userButton.clicked(p) and done:
            win.close()
            break
                
        elif userButton.clicked(p):
            userButton.buttonSetLabel('Quit')
            done=True
            regressionLine.predict()
        
        if not done:    
            regressionLine.addPoint(p)
                
    print(regressionLine.getPoints())

if __name__=='__main__':
    main()