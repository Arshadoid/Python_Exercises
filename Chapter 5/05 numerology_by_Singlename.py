# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 15:21:47 2022

@author: Arshad Mehtiyev
"""
def main():
    name=str(input("Type your name to get numeric value: "))
    name=name.lower()
    sumNum=0
    for letter in name:
        sumNum=sumNum+ord(letter)-96
    
    print("Numeric value of the name is ",sumNum)

main()