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
    winsA, winsB, ties = simNGames(n, probA, probB)
    printSummary(winsA, winsB, ties)

def printlntro():
    print("This program simulates a game of volleyball between two")
    print('teams called "A" and "B". The ability of each team is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the team wins the point when serving. Team A always")
    print("has the first serve.")
    
def getlnputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. team A wins a serve? "))
    b = float(input("What is the prob.team B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of volleyball between teamss whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = ties = 0
    for i in range(n):
        
        scoreA, scoreB = simOneGame(probA, probB)
        if abs(scoreA-scoreB)!=2:
            if scoreA > scoreB:
                winsA += 1
            else:
                winsB += 1
        else: 
            ties+=1
    return winsA, winsB, ties

def simOneGame(probA, probB):
    # Simulates a single game or volleyball between teams whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    if random()<0.5:
        serving = "A"
    else:
        serving = "B"
        
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
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
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    
    return a== 15 or b== 15

def printSummary(winsA, winsB, ties):
    # Prints a summary of wins for each team and ties.
    n = winsA + winsB +ties
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1: 0.1%})".format(winsB, winsB/n))
    print("Ties: {0} ({1:0.1%})".format(ties, ties/n))

if __name__ == '__main__' : 
    main()