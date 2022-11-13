# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 18:30:33 2022

@author: Arshad Mehtiyev

Chapter 5, Programming Exercise #15

Write a program to plot a horizontal bar chart of student exam scores.
Your program should get input from a file. The first line of the file contains
the count of the number of students in the file, and each subsequent line
contains a student's last name followed by a score in the range 0-100.
Your program should draw a horizontal rectangle for each student where
the length of the bar represents the student's score. The bars should all
line up on their left-hand edges. Hint: Use the number of students to
determine the size of the window and its coordinates. Bonus: label the
bars at the left end with the students' names.


"""
from graphics import *

tempstudentLN = []
studentScore = []
studentLN = []


def drawScores(height, lLN):
    
    height=height*8+100
    width=lLN+230

    lineAnchorY=20    

    win = GraphWin("Student Scores",width,height)
    
    labels = []
    scores = []
    
    for i in range(len(studentLN)):    
        
        text=  studentLN[i].ljust(lLN," ")     
            
        label = Text(Point(40 ,lineAnchorY+5),text)
        
        labels.append(label)
        score = Rectangle(Point(lLN*10+40,lineAnchorY), 
                          Point(lLN*10+40+int(studentScore[i]),lineAnchorY+5))
        
        score.setFill('blue')
        scores.append(score)
        
        lineAnchorY=lineAnchorY+20
    
    for i in range(len(studentLN)):
        
        scores[i].draw(win)    
        labels[i].draw(win) 
        
       
    win.getMouse()
    win.close()
    
def scoreList(file):
    
    
    
    textList=(file.read()).split("\n")
    studentCount= int(((textList[0]).split(":"))[1])
    
    
    for student in textList[1:studentCount+1]:
        
        studentLN.append((student.split())[0])
        studentScore.append((student.split())[1])
    
    longestLNSize =len(max(studentLN,key=len))  
        
    for string in studentLN:
        print(longestLNSize)
        print(max(studentLN,key=len))
        #print(len(string))
        #print('s'*(longestLNSize-len(string)))   
        #print(string)
        
    return studentCount
    
    



def main():
    
    print("This program creates a window with student scores from the file")
    print('named "15 student_scores.txt"')
    
    infile = open("15 student_scores.txt","r")
    

        
    studentCount = scoreList(infile)
    infile.close()
    
    longestLNSize =len(max(studentLN,key=len))    
    
    drawScores(studentCount,longestLNSize)
    
    print(studentCount)
    print(studentLN)
    print(tempstudentLN)
    print(studentScore)
    
    
main()