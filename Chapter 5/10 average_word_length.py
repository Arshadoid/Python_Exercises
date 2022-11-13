# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 18:45:20 2022

@author: Arshad Mehtiyev
"""

def main():
    print("Write a sentence and we will find the average word length:")
    sentence = str(input())
   
    wordCount=sentence.count(" ")+1
    totalWL=len(sentence)-sentence.count(" ")
    averageWL=totalWL/wordCount
            
    print("Average word lenght in the sentence is {0:0.2f}".format(averageWL))

main()