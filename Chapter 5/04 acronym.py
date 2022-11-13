# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:54:01 2022

@author: Arshad Mehtiyev
"""

def main():
    phrase = str(input("Type the phrase to create an acronym: "))
    wordList = phrase.split()
    print("Acronym would be: ", end='')
    for word in wordList:
        print(word[0].upper(),end='')

main()


