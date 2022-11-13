# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 12:05:23 2022

V=4/3*pi*r**3
A=4*pi*r**2


"""
import numpy as np



def sphereArea(r):
    return 4*np.pi*r**2

def sphereVolume(r):
    return 4/3*np.pi*r**3

def main():
    print("This program calculates Area and Volume fot he sphere given radius")
    cond=False
    while cond==False:
        try:
            radius = float(input("Enter the radius: "))
            if radius<0:
                print("Radius can not be negative, try again")
            else:
                cond=True
        except:
            print("Given value is not valid, try again")
    
    area=sphereArea(radius)
    volume=sphereVolume(radius)
    
    print(f"Area of the spehere with radius of {radius} is {round(area,4)}")
    print(f"and volume is  {round(volume,4)}")
    
    
if __name__=='__main__':
    main()
    