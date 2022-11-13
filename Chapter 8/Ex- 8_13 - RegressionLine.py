# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:35:59 2022

@author: Arshad Mehtiyev
"""

from graphics import *


def drawRegression(n, xSum,ySum, xSquaredSum, xySum, win):
    try:
        m=(xySum-(xSum*ySum)/n)/(xSquaredSum-n*(xSum/n)**2)
        
        x1=0
        x2=10
        
        y1=ySum/n+m*(x1-xSum/n)
        y2=ySum/n+m*(x2-xSum/n)
        
        regressionLine=Line(Point(x1,y1), Point(x2,y2))
        regressionLine.setFill("red")
        regressionLine.draw(win)
    except ZeroDivisionError:
        return None

def checkBox(clickX,clickY):
    if ((clickX>=0 and clickX<=2) and
        (clickY>=0 and clickY<=1)):
        return True
    else:
        return False

def getClick( clickPoint):
    
    clickX=clickPoint.getX()
    clickY=clickPoint.getY()
    return clickX, clickY

def main():
    
    points=[]
    
    
    # Creating main wirndow and done button
    win = GraphWin("Plot Regression Line", 500,500)
    win.setCoords(0, 0, 10, 11)
    
    print("Specify the data points on graphics window and click 'Done' when finish")
    
    doneBox=Rectangle(Point(0,0), Point(2,1))
    doneBox.setFill('cyan')
    doneBox.draw(win)
    doneText=Text(Point(1,0.5),'DONE')
    doneText.draw(win)
    
    # Initialization of values
    n=0 # Counter of clicks()points
    xSum=0
    ySum=0
    xSquaredSum=0
    xySum=0
    
    done=False
    # Main loop
    
   
    while True:
        clickX,clickY = getClick(win.getMouse())
        
        while not done:
                        
            if checkBox(clickX,clickY):
                doneText.setText('QUIT')
                doneText.setFill('red')
                drawRegression(n, xSum,ySum, xSquaredSum, xySum, win)
                done=True  
            else:
                n+=1            
                xSum+=clickX
                ySum+=clickY
                xSquaredSum+=clickX**2
                xySum+=clickX*clickY
                
                points.append((clickX,clickY))
                Point(points[-1][0],points[-1][1]).draw(win)
            
            clickX,clickY = getClick(win.getMouse())
            
        if checkBox(clickX,clickY) and done:
            break
            
    win.close()
    print(points)

if __name__=='__main__':
    main()