# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:29:39 2022

@author: Arshad Mehtiyev


A certain CS professor gives 5-point quizzes that are graded on the scale
5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a program that accepts a quiz score as
an input and prints out the corresponding grade.

"""
# quizzgrader.py

def grader(x):
    
    gradeList = ['A','B','C','D','F','F']
    
    return gradeList[5-x]

def main():
    
    score =int(input("Type the score(0-5): "))    
    print("Student's grade is {0}".format(grader(score)))
    
main()
