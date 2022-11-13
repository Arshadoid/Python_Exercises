# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 13:49:09 2022

@author: Arshad Mehtiyev
"""

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("For 1st column enter a number between 0 and 1: "))
    y = eval(input("For 2nd column enter a number between 0 and 1: "))
    z = eval(input("How many numbers should I print?: "))
    print(" ")
    print("index     {0:^5}        {1:^5}".format(x,y))
    print("--------------------------------")
    for i in range(z):
        x=3.9 * x * (1-x)
        y=3.9 * y * (1-y)
        print(" {0:>3}     {1:^7.6f}      {2:^7.6F}".format(i+1,x,y))

main()

