# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 15:34:56 2022

@author: Arshad Mehtiyev
"""

def main():
    compName=str(input("Type your complete name to get numeric value: "))
    compName=compName.lower()
    nameList=compName.split()
    
    sumNum=0
    for name in nameList:
        for letter in name:
            sumNum=sumNum+ord(letter)-96
    print("Numeric value of the complete name is ",sumNum)

main()

