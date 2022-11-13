# -*- coding: utf-8 -*-
"""
Created on Wed May 18 14:54:11 2022

@author: Arshad Mehtiyev
"""

from random import choice

def main():
    printIntro()
    n, steps=getInput()
    totalDistance=multipleSimulations(n, steps)
    printSummary(n, totalDistance)
    
def printIntro():
    print("This program runs simulation of a random walk(back and forth) to")
    print("estimate how many steps away from the starting point would a person end up")

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
    distance=0
    
    for i in range(steps):
        distance+=choice([-1,1])
    
    return abs(distance)
    
def printSummary(n, totalDistance):
    print("With random walk of back and forth, a person on avarage can end up")
    print("approximately {0:0.2} steps away from the starting point".format(totalDistance/n))

if __name__ == '__main__':
    main()