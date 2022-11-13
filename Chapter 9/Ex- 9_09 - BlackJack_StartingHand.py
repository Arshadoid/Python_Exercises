# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:20:46 2022

@author: Arshad Mehtiyev
"""

from random import choice

def main():
    printIntro()
    n = getInput()
    
    startingHandList, bustCountList =simulateStartingHand(n)
    
    printSummary(n,startingHandList, bustCountList)

def printIntro():
    print("This program simulates a game of BlackJack until the dealer")
    print("does or doesn't get busted. When given number of simuluations done")
    print("program returns probability of the dealer getting busted for every")
    print("possible starting hand")

def getInput():
    n=int(input("How many games to simulate? "))
    return n


def simulateStartingHand(n):
    startingHandList=['Ace',1,2,3,4,5,7,8,9,10]
    bustCountList=[]
    for startingHand in startingHandList:
        bustCountList.append(simulateNGames(n, startingHand))            
    return startingHandList, bustCountList

def simulateNGames(n, startingHand):
    
    bustCount=0
    for i in range(n):
        busted=simulateSingleGame(startingHand)
        if busted:
            bustCount+=1
           
    return bustCount

def simulateSingleGame(startingHand):
    busted=False
    hasAce=False
    score=0
    
    drawnCard=startingHand    
    
    while score<17:
        if drawnCard=='Ace':
            hasAce=True
            score+=1
        else:
            score+=drawnCard
    
        if hasAce and (17<=score+10 and score+10<=21):
            score+=10
        
        drawnCard=drawACard()
    
    if score>21:
        busted=True
    
    return busted

def drawACard():
    deck=['Ace',2,3,4,5,6,7,8,9,10,10,10,10]
        
    return choice(deck)


def printSummary(n,startingHandList, bustCountList):
    print("\nGames simulated for each type of starting hand is", n)
    print("Probability of the dealer getting busted:")
    for i in range(len(startingHandList)):
        print("- with starting hand of {0} is {1: 0.1%}".format(startingHandList[i], bustCountList[i]/n))


if __name__=='__main__':
    main()