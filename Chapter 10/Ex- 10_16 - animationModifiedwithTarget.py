# -*- coding: utf-8 -*-
"""
Created on Thu May 19 10:12:43 2022

@author: Arshad Mehtiyev
"""
from graphics import *
# file: animation.py

from projectile import Projectile
from button import Button
from random import randint
class ShotTracker:
    def __init__(self, win, angle, velocity, height):
        """win is the GraphWin to display the shot. agnle, velocity,
           and height are initial projectile parameters.
        """
        
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0,height), 3)
        self.marker.setFill( "red")
        self.marker.setOutline("red" )
        self.marker.draw(win)
    
    def update(self, dt):
        """ Move the shot dt seconds farther along its flight"""
        
        # update the proj ectile
        self.proj.update(dt)
        # move the circle to the new projectile location
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy)
    def getX(self):
        """ return the current x coordinate of the shot's center"""
        return self.proj.getX()
    def getY(self):
        """ return the current y coordinate of the shot's center"""
        return self.proj.getY()
    def undraw(self):
        """undraw the shot """
        self.marker.undraw()

class InputDialog:

    """ A custom window for getting simulation values (angle, velocity,
    and height) from the user."""
    def __init__(self, angle, vel, height):
        """ Build and display the input window """
        
        self.win = win = GraphWin("Initial Values", 200, 300)
        win.setCoords(0,4.5,4,.5)
        
        Text(Point(1,1), "Angle").draw(win)
        self.angle = Entry(Point(3,1), 5).draw(win)
        self.angle.setText(str(angle))
        
        Text(Point(1,2), "Velocity").draw(win)
        self.vel = Entry(Point(3,2), 5).draw(win)
        self.vel.setText(str(vel))
        
        Text(Point(1,3), "Height").draw(win)
        self.height = Entry(Point(3,3), 5).draw(win)
        self.height.setText(str(height))
        
        self.fire = Button(win, Point(1,4), 1.25, .5, "Fire ! ")
        self.fire.activate()
        
        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate()
        
    def interact(self):
        """ wait for user to click Quit or Fire button
        Returns a string indicating which button was clicked
        """
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire ! "
    def getValues(self):
        """ return input values """
        a = float (self.angle.getText())
        v = float (self.vel.getText())
        h = float (self.height.getText())
        return a,v,h
    
    def close (self):
        """ close the input window """
        self.win.close()

class Target:
    def __init__(self,win):
        x=randint(0,207)
        self.target = Rectangle(Point(x-3, -3), Point(x+3,3))
        self.target.setFill('green')
        self.target.setOutline('yellow')
        self.target.draw(win)
    
    def hit(self, shotX):
        center=self.target.getCenter()        
        targetX=center.getX()
        
        if abs(shotX-targetX)<=3:
            return True
        else:
            return False
        
        
                 
       
       
        
        

def main ():
    # create animation window
    win = GraphWin ("Projectile Animation" , 640, 480, autoflush=False)
    win.setCoords (-10, -10, 210, 155)
    
    # draw baseline
    Line(Point(-10,0), Point(210,0)).draw(win)
    
    # draw labeled ticks every 50 meters
    for x in range (0, 210, 50):
        Text(Point(x,-5), str(x)).draw(win)
        Line(Point(x,0), Point(x,2)).draw(win)
    
    #adding target
    
    target=Target(win)
    
    # event loop, each time through fires a single shot
    angle, vel, height = 45.0, 40.0, 2.0
    inputwin = InputDialog(angle, vel, height)
    
    while True:
        # interact with the user
        
        choice = inputwin.interact()
        
        if choice == "Quit" : # loop exit
            break
        
        # create a shot and track until it hits ground or leaves window
        angle, vel, height = inputwin.getValues()
        shot = ShotTracker(win, angle, vel, height)
        while 0 <= shot.getY() and -10 < shot.getX() <= 210:
            shot.update(1/50)
            update(50)
        
        if target.hit(shot.getX()):
            break
        
    inputwin.close()
    win.close()
    
    
if __name__=='__main__':
    main()