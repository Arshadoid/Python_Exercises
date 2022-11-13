# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:20:46 2022

@author: Arshad Mehtiyev
"""

from random import choice

def main():
    printIntro()
    n = getInput()
    
    bustCount = simulateNGames(n)
    printSummary(n,bustCount)

def printIntro():
    print("This program simulates a game of BlackJack until the dealer")
    print("busts or doesn't. When given number of simuluations done")
    print("program returns probability of the dealer getting busted ")

def getInput():
    n=int(input("How many games to simulate? "))
    return n

def drawACard():
    deck=['Ace',2,3,4,5,6,7,8,9,10,10,10,10]
        
    return choice(deck)
    

def simulateSingleGame():
    busted=False
    hasAce=False
    score=0
    
    while score<17:
        drawnCard=drawACard()
        if drawnCard=='Ace':
            hasAce=True
            score+=1
        else:
            score+=drawnCard
    
        if hasAce and (17<=score+10 and score+10<=21):
            score+=10
    
    if score>21:
        busted=True
    
    return busted

def simulateNGames(n):
    
    bustCount=0
    for i in range(n):
        busted=simulateSingleGame()
        if busted:
            bustCount+=1
           
    return bustCount

def printSummary(n, bustCount):
    print("\nGames simulated: ", n)
    print("Probability of the dealer getting busted is {0: 0.1%}".format(bustCount/n))


if __name__=='__main__':
    main()