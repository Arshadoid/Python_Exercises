# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 08:52:27 2022

@author: Arshad Mehtiyev
"""
# face . py
from graphics import *
import math
from button import Button
class Face:
    def __init__(self, window, center, size):
        self.window=window
        eyeSize = 0.15*size
        eyeOff = size/3.0
        self.mouthSize = 0.8*size
        self.mouthOff = size/2.0
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff,-eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(self.window)
        self.rightEye.draw(self.window)
        p1 = center.clone()
        p1.move(-self.mouthSize/2,self.mouthOff)
        p2 = center.clone()
        p2.move(self.mouthSize/2, self.mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(self.window)
        
        self.lastLip=self.mouth
        self.lastLEye=self.leftEye
        self.lastREye=self.rightEye
        
        self.__smile()
        self.__rWink()
        self.__lWink()
        self.__frown()
        
    def __smile(self):
                
        sCenter=(self.mouth.getCenter()).clone()
        lP=(self.mouth.getP1()).clone()
        lP.move(0, -sCenter.getY()*0.05)
        rP=(self.mouth.getP2()).clone()
        rP.move(0, -sCenter.getY()*0.05)
        lMP=Point(sCenter.getX()-self.mouthSize/4,sCenter.getY())
        rMP=Point(sCenter.getX()+self.mouthSize/4,sCenter.getY())
        
        self.smile=Polygon(lP,lMP,rMP,rP,rMP,lMP)

    def __rWink(self):
        centPoint=self.rightEye.getCenter()
        radius=self.rightEye.getRadius()
        p1X=centPoint.getX()-radius
        p1Y=centPoint.getY()
        p1=Point(p1X,p1Y)
        p2X=centPoint.getX()+radius
        p2Y=p1Y
        p2=Point(p2X,p2Y)
        p3X=(p2X+p1X)/2*1.05
        p3Y=(p2Y+p2Y-radius)/2
        p3=Point(p3X,p3Y)
        self.winkREye=Polygon(p3,p1,p2,p1,p3)    
    
    def __lWink(self):
        centPoint=self.leftEye.getCenter()
        radius=self.leftEye.getRadius()
        p1X=centPoint.getX()-radius
        p1Y=centPoint.getY()
        p1=Point(p1X,p1Y)
        p2X=centPoint.getX()+radius
        p2Y=p1Y
        p2=Point(p2X,p2Y)
        p3X=(p2X+p1X)/2*0.95
        p3Y=(p2Y+p2Y-radius)/2
        p3=Point(p3X,p3Y)
        self.winkLEye=Polygon(p3,p2,p1,p2,p3) 
    
    def __frown(self):
                
        sCenter=(self.mouth.getCenter()).clone()
        lP=(self.mouth.getP1()).clone()
        lP.move(0, sCenter.getY()*0.05)
        rP=(self.mouth.getP2()).clone()
        rP.move(0, sCenter.getY()*0.05)
        lMP=Point(sCenter.getX()-self.mouthSize/4,sCenter.getY())
        rMP=Point(sCenter.getX()+self.mouthSize/4,sCenter.getY())
        
        self.frown=Polygon(lP,lMP,rMP,rP,rMP,lMP)
      
    
    def frownFaceDraw(self):
        self.__faceOff()
        
        self.leftEye.draw(self.window)
        self.rightEye.draw(self.window)
        self.frown.draw(self.window)
        
        self.lastLEye=self.leftEye
        self.lastREye=self.rightEye
        self.lastLip = self.frown
        
        
    def rightWinkDraw(self):
        self.__faceOff()
        
        self.leftEye.draw(self.window)
        self.smile.draw(self.window)
        self.winkREye.draw(self.window)
        
        self.lastLEye=self.leftEye
        self.lastREye=self.winkREye
        self.lastLip = self.smile
    
    def leftWinkDraw(self):
        self.__faceOff()
        
        self.rightEye.draw(self.window)
        self.smile.draw(self.window)
        self.winkLEye.draw(self.window) 
        
        self.lastLEye=self.winkLEye
        self.lastREye=self.rightEye
        self.lastLip = self.smile
    
    def pokerFaceDraw(self):
        self.__faceOff()
                
        self.mouth.draw(self.window)
        self.leftEye.draw(self.window)
        self.rightEye.draw(self.window)
        
        self.lastLip=self.mouth
        self.lastLEye=self.leftEye
        self.lastREye=self.rightEye
             
    
    def smileDraw(self):
        self.__faceOff()
        
        self.leftEye.draw(self.window)
        self.rightEye.draw(self.window)
        self.smile.draw(self.window)
        
        self.lastLip = self.smile
        self.lastLEye=self.leftEye
        self.lastREye=self.rightEye
    
    
    def flinchDraw(self):
        self.__faceOff()
        
        self.winkLEye.draw(self.window) 
        self.winkREye.draw(self.window)
        self.frown.draw(self.window)
        
        self.lastLip =  self.frown
        self.lastLEye= self.winkLEye
        self.lastREye= self.winkREye
        
    
    
    def __faceOff(self):    
        self.lastLip.undraw()
        self.lastLEye.undraw()
        self.lastREye.undraw()
        


def main():
    win=GraphWin('Face',300,200)
    face=Face(win, Point(100,100), 50)
    
    
    qButton = Button(win, Point(225,175), 50, 20, 'QUIT')
    qButton.activate()

    flinchFaceButton = Button(win, Point(225,150), 110, 20, 'FLINCH FACE') 
    flinchFaceButton.activate()   

    pokerFaceButton= Button(win, Point(225,125), 110, 20, 'POKER FACE') 
    pokerFaceButton.activate()   

    smileFaceButton = Button(win, Point(225,100), 110, 20, 'SMILE')
    smileFaceButton.activate()
    
    RWinkFaceButton = Button(win, Point(225,75), 110, 20, 'RIGHT WINK')
    RWinkFaceButton.activate()
    
    LWinkFaceButton = Button(win, Point(225,50), 110, 20, 'LEFT WINK')
    LWinkFaceButton.activate()
    
    frownFaceButton = Button(win, Point(225,25), 110, 20, 'FROWN')
    frownFaceButton.activate() 
    
    while True:
        p=win.checkMouse()
        if p!=None:
            if qButton.clicked(p):
                break
            elif pokerFaceButton.clicked(p):
                face.pokerFaceDraw()
        
            elif smileFaceButton.clicked(p):
                face.smileDraw()
            elif RWinkFaceButton.clicked(p):
                face.rightWinkDraw()
            elif LWinkFaceButton.clicked(p):
                face.leftWinkDraw()
            elif frownFaceButton.clicked(p):
                face.frownFaceDraw()
            elif flinchFaceButton.clicked(p):
                face.flinchDraw()
            p=None
    
    
    
    
    win.close()
    
    
    
    
    
if __name__ == '__main__':
    main()