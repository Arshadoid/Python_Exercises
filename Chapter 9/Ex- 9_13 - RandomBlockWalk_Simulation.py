# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:54:11 2022

@author: Arshad Mehtiyev
"""

from random import choice
import math

def main():
    printIntro()
    n, steps=getInput()
    totalDistance=multipleSimulations(n, steps)
    printSummary(n, totalDistance)
    
def printIntro():
    print("This program runs simulation of a random walk on the blocks of a ")
    print("city streets and estimates how many steps away from the starting")
    print("point would a person end up")

def getInput():
    n=int(input("How many simulations to run? "))
    steps=int(input("How many steps to simulate? "))
    return n, steps
    
def multipleSimulations(n, steps):
    totalDistance=0
    for i in range(n):
        totalDistance+=singleSimulation(steps)
    
    return totalDistance
    

def singleSimulation(steps):
    coordinates=[0,0]
    
    for i in range(steps):
        direction=choice([[-1,0], [1,0], [0,1], [0,-1]])
        coordinates[0]+=direction[0]
        coordinates[1]+=direction[1]
     
    distance= math.sqrt(coordinates[0]**2+coordinates[1]**2)                             
    
    return distance
    
def printSummary(n, totalDistance):
    print("With random walk of forward, backward, left or right a person on avarage can end up")
    print("approximately {0:0.4} steps away from the starting point".format(totalDistance/n))

if __name__ == '__main__':
    main()