# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:14:25 2022

@author: Arshad Mehtiyev
"""


def wc(file):
    wordCount=0
    charCount=1 #counting 1 extra end of line character
    lineCount=0
    for line in file.readlines():
        lineCount=lineCount+1
        wordCount=wordCount+len(line.split()) 
        charCount=charCount+len(line)-1 #removing end of line characters
        
    return lineCount, wordCount, charCount



def main():
    print("This program provides information about the file")
    print("Name of the file(including .txt extension:")
    fileName=str(input())
    inFile=open(fileName,"r")
    
    #lineCount = len(inFile.readlines())
    lC, wC, cC = wc(inFile)
    input()
    print("There are {0} lines, {1} words and {2} characters".format(lC,wC,cC))
    
    inFile.close()

main()