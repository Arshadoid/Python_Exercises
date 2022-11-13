# -*- coding: utf-8 -*-
"""
Created on Tue May 31 11:41:08 2022

@author: Arshad Mehtiyev
"""
class Cube:
    def __init__(self, length):
        self.l=length
    def getLength(self):
        return self.l
    def surfaceArea(self):
        return 6*self.l**2
    def volume(self):
        return self.l**3
    
def main():
    try:
        length=float(input("Provide length of the side of the cube: "))
        cube=Cube(length)
        print("Cube with the given side length of", cube.getLength())
        print("has the volume of", cube.volume())
        print("and the surface area of", cube.surfaceArea())
        
        
    except:
        print('Something went wrong')

if __name__=='__main__':
    main()
        