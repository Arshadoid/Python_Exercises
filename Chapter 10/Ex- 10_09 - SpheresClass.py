# -*- coding: utf-8 -*-
"""
Created on Tue May 31 11:41:08 2022

@author: Arshad Mehtiyev
"""
from math import pi

class Sphere:
    def __init__(self, radius):
        self.r=radius
    def getRadius(self):
        return self.r
    def surfaceArea(self):
        return 4*pi*self.r**2
    def volume(self):
        return 4/3*pi*self.r**2
    
def main():
    try:
        radius=float(input("Provide radius of sphere: "))
        sphere=Sphere(radius)
        print("Spehere with the given radius of", sphere.getRadius())
        print("has the volume of", sphere.volume())
        print("and the surface area of", sphere.surfaceArea())
        
        
    except:
        print('Something went wrong')

if __name__=='__main__':
    main()
        