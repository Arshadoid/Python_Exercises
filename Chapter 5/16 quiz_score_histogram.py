# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 18:00:07 2022

@author: Arshad Mehtiyev
"""

import random
from graphics import *

def fillQuizResults(fileName):
    lines = random.randint(1, 20)
    #print("Lines: ", lines)
    outFile = open(fileName,'w')
    
    for i in range(lines-1):
        print(random.randint(0, 10),file=outFile)
    print(random.randint(0, 10),end="",file=outFile)    
    outFile.close()
    
    
    
def readScores(fileName):
    
    inFile = open(fileName,'r')
    scores = []
    
    for line in inFile:
        scores.append(int(line))
    
    return scores

        
    
    
def drawhistogram(scoreList):
    
    width = 350 +len(scoreList)*20
    height = 400
    
    win = GraphWin("Quiz score histogram",width,height)
    win.setCoords(0,0,len(scoreList)+4,14)
    
    sum=0
    
    for i in range(len(scoreList)):
        
        p1 = Point(3.5+i,2)
        p2 = Point(4+i,2+scoreList[i])
        
        bar = Rectangle(p1, p2)
        bar.setFill("red")
        bar.draw(win)
        
        score = Text(Point(3.75+i,1), str(scoreList[i]))
        score.draw(win)
        
        sum+= scoreList[i]
        
    scoreMean = sum/len(scoreList)
    
    meanLine = Line(Point(3,scoreMean+2),Point(3+len(scoreList),scoreMean+2))
    meanLine.draw(win)
    
    meanText = Text(Point(1.5,scoreMean+2),"Mean: "+str(round(scoreMean,2)))
    meanText.draw(win)
    
    win.getMouse()
    win.close()


def main():
    
    fillQuizResults("16 quizresults.txt")
    drawhistogram(readScores("16 quizresults.txt"))
    print(len(readScores("16 quizresults.txt")))
    
main()
        
    