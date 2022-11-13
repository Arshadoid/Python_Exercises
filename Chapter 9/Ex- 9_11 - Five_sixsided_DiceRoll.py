# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:20:46 2022

@author: Arshad Mehtiyev
"""

from random import randint

def main():
    printIntro()
    n = getInput()
    
    count=simulateNRolls(n)
    printSummary(count, n)

def printIntro():
    print("This program runs simultion to estimate the probability of rolling")
    print("five of a kind in a single roll of five six-soded dice")

def getInput():
    n=int(input("How many simulations to run? "))
    return n


def simulateNRolls(n):
    counter=0
    
    for i in range(n):
        if simulateSingleRoll():
            counter+=1
        
    return counter

def simulateSingleRoll():
    
    counter=0
    dice=randint(1,6)
    for i in range(4):
        if dice==randint(1,6):
            counter+=1
        
    return counter==4
    
   
def printSummary(count,n):
    print("Probability of rolling five of a kind in a single roll of five")
    print("six-soded dice out of {0} rolls is {1: 0.2%}".format(n, count/n))


if __name__=='__main__':
    main()