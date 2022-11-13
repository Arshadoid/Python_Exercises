# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:43:29 2022

@author: Arshad Mehtiyev

A certain CS professor gives 100-point exams that are graded on the scale
90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F. Write a program that ac­
cepts an exam score as input and prints out the corresponding grade.

"""
#quizzgrader2.py


def grader(score):
    
    gradeList = ['A','A','B','C','D','F']
    #below formula generates correct index number(0-5) based on the score
    index=(abs(int((score-60)/10)-4))*(score//60)+5*(1-score//60)
    
    return gradeList[index]
    

def main():
    score = int(input("Type quizz score(0-100): "))
    print("Grade is: ",grader(score))

main()
