# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 18:39:06 2022

@author: Arshad Mehtiyev
"""
def main():
    print("Write a sentence and we will count the words:")
    sentence = str(input())
    print("There are {0} words".format(sentence.count(" ")+1))

main()