# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:20:46 2022

@author: Arshad Mehtiyev
"""

from random import random

def main():
    printIntro()
    n = getInput()
    
    hitCount=simulateNThrows(n)
    pi=approximatePi(hitCount,n)  
    printSummary(pi)

def printIntro():
    print("This program runs simultion by Monte Carlo technique to determine")
    print("pi value. This is done simulatiing dart throw to a dartboard and")
    print("counting the hits on and off the dartboard. Area off the dartboard")
    print("is the sorrounding space of the dartboard in the smallest square")
    print("to which dartboard fits")

def getInput():
    n=int(input("How many dart will be thrown? "))
    return n


def simulateNThrows(n):
    hitCount=0
    
    for i in range(n):
        
        if simulateSingleThrow():
            hitCount+=1
           
    return hitCount

def simulateSingleThrow():
    x=2*random()-1
    y=2*random()-1
    return x**2+y**2<=1

def approximatePi(hitCount,n):
    return 4*(hitCount/n)

def printSummary(pi):
    print("Estimated pi valus is {0: 0.6}".format(pi))


if __name__=='__main__':
    main()