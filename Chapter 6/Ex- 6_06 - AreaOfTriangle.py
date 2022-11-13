# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:33:32 2022

@author: Arshad Mehtiyev


s=(a+b+c)/2
A=sqrt(s*(s-a)*(s-b)*(s-c))

"""
import math
from graphics import *

def calcArea(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    s=(a+b+c)/2
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return A

def check(s):
    s.sort()
    if (s[0]+s[1])>s[2]:
        return True
    else:
        return False


def drawTriangle(s):
    s.sort()
    
    win = GraphWin ( "Area of the defined Triangle " )
    win.setCoords (0.0 , 0.0 , 10.0 , 10.0)
    

    # Get and draw three vertices of triangle
    p1 = Point(1,1)
    p2 = Point(9,1)
    
    l3=8.0
    ratio=s[2]/l3
    l2=s[1]/ratio
    l1=s[0]/ratio
    
    x=(l3**2+l1**2-l2**2)/(2*l3)
    y=math.sqrt(l1**2-x**2)

    p3=Point(x+1,y+1)    
        
    # Use Polygon object to draw the triangle
    triangle = Polygon (p1 , p2 , p3)
    triangle.setFill ( "green" )
    triangle.setOutline ( "black" )
    triangle.draw(win)
    # Wait for another click to exit
    
    message = Text (Point (5 , 0.5) , " Click anywhere to quit. " )
    message.draw(win)
    
    
    win.getMouse()
    win.close()


def main():
    print("This program calculates and visualizes the area of a triangle")
    cond=False
    while cond==False:
        try:
            s =input("Enter the comma separated lentgh of sides of the triangle: ").split(',',3)
            s = [float(i) for i in s]
            
        
            if min(s)<0:
                print("Length can not be negative, try again")
            elif not check(s):
                print("Given length of sides are not valid for Triangle, try again")
            else:
                cond=True
        except:
             print("Given value is not valid, try again")
                
    
    area=calcArea(s)
                
    print(f"Area of the triangle with the given sides is {round(area,4)}")
    
    drawTriangle(s)
    
    
if __name__=='__main__':
    main()
    


