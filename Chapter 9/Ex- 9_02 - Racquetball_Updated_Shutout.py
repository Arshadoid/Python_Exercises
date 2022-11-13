# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:01:48 2022

@author: Arshad Mehtiyev
"""

# rball.py
from random import random

def main():
    printlntro()
    probA, probB, n = getlnputs()
    winsA, winsB, shutoutA, shutoutB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, shutoutA, shutoutB)

def printlntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")
    
def getlnputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    shutoutA = shutoutB=0
    for i in range(n):
        serverTurn=i+1
        
        scoreA, scoreB, shutout = simOneGame(probA, probB, serverTurn)
        if scoreA > scoreB:
            winsA = winsA + 1
            if shutout:
                shutoutA+=1
        else:
            winsB = winsB + 1
            if shutout:
                shutoutB+=1
    return winsA, winsB, shutoutA, shutoutB

def simOneGame(probA, probB, serverTurn):
    # Simulates a single game or racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    if serverTurn%2==1:
        serving = "A"
    elif serverTurn%2==0:
        serving = "B"
        
    scoreA = 0
    scoreB = 0
    over=False
    while not over:
        over, shutout = gameOver(scoreA, scoreB)
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:   
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB, shutout

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    shutout=False
    over=False
       
    if (a==0 and b==7) or (a==7 and b==0):
        shutout=True
        over=True
    elif (a== 15 or b== 15): 
        over=True 
    return over,shutout
    
     

def printSummary(winsA, winsB, shutoutA, shutoutB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(winsA, winsA/n))
    print("Shutouts for A: {0} ({1: 0.1%})".format(shutoutA, shutoutA/winsA))
    print("Wins for B: {0} ({1: 0.1%})".format(winsB, winsB/n))
    print("Shutouts for B: {0} ({1: 0.1%})".format(shutoutB, shutoutB/winsB))

if __name__ == '__main__' : 
    main()