# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:01:48 2022

@author: Arshad Mehtiyev
"""

# rball.py
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA_reg, winsB_reg, ties_reg, winsA_ral, winsB_ral, ties_ral = simNGames(n, probA, probB)
    printSummary(winsA_reg, winsB_reg, ties_reg, winsA_ral, winsB_ral, ties_ral)

def printIntro():
    print("This program simulates a game of regular and rally scoring ")
    print('volleyball between two teams called "A" and "B". The ability ')
    print("of each team is indicated by a probability (a number between ")
    print("0 and 1) that the team wins the point when serving. Team ")
    print("serving the first is selected randomly.")
    
def getInputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. team A wins a serve? "))
    b = float(input("What is the prob. team B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of volleyball between teamss whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA_reg = winsB_reg = ties_reg = 0
    winsA_ral = winsB_ral = ties_ral = 0
    for i in range(n):
        
        scoreA_reg, scoreB_reg = simOneGame(probA, probB, 'regular')
        scoreA_ral, scoreB_ral = simOneGame(probA, probB, 'rally')
        if abs(scoreA_reg-scoreB_reg)>=2:
            if scoreA_reg > scoreB_reg:
                winsA_reg += 1
            else:
                winsB_reg += 1
        else: 
            ties_reg+=1
        
        if abs(scoreA_ral-scoreB_ral)>=2:
            if scoreA_ral > scoreB_ral:
                winsA_ral += 1
            else:
                winsB_ral += 1
        else: 
            ties_ral+=1
        
                    
    return winsA_reg, winsB_reg, ties_reg, winsA_ral, winsB_ral, ties_ral

def simOneGame(probA, probB, gameType):
    # Simulates a single game or volleyball between teams whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    if random()<0.5:
        serving = "A"
    else:
        serving = "B"
        
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB, gameType):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
                if gameType=='rally':
                    scoreB = scoreB + 1
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
                if gameType=='rally':
                    scoreA = scoreA + 1
                
    return scoreA, scoreB

def gameOver(a, b, gameType):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    
    if gameType =='rally':     
        return  a== 25 or b== 25
    elif gameType == 'regular':
        return a==15 or b==15

def printSummary(winsA_reg, winsB_reg, ties_reg, winsA_ral, winsB_ral, ties_ral):
    # Prints a summary of wins for each team and ties.
    n = winsA_reg + winsB_reg +ties_reg
    print("\nGames simulated: ", n)
    print("Results for regular volleyball: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(winsA_reg, winsA_reg/n))
    print("Wins for B: {0} ({1: 0.1%})".format(winsB_reg, winsB_reg/n))
    print("Ties: {0} ({1:0.1%})".format(ties_reg, ties_reg/n))
    print("\nResults for rally scroing volleyball: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(winsA_ral, winsA_ral/n))
    print("Wins for B: {0} ({1: 0.1%})".format(winsB_ral, winsB_ral/n))
    print("Ties: {0} ({1:0.1%})".format(ties_ral, ties_ral/n))
    if winsA_ral/winsA_reg>1.05:
        result='magnifies'
    elif winsA_reg/winsA_ral>1.05:
        result='reduces'
    else:
        result='has no significant effect on'
    print('\nIn comparison, rally scoring type volleyball {0} winning of Team A over regular volleyball'.format(result))

if __name__ == '__main__' : 
    main()