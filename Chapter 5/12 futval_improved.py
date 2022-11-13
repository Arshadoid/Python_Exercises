# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:21:11 2022

@author: Arshad Mehtiyev
"""

# futval . py
# A program to compute the value of an investment
# carried 10 years into the future
def main () :
    print ("This program calculates the value of investment")
    print ("year by year for the given period.")

    principal = eval (input ("Enter the initial principal: ") )
    apr = eval (input ("Enter the annual interest rate: ") )
    year= int (input("Enter the number of years: "))
    
    print("Year    Value")
    print("----------------")
    print("{0:>3}    ${1:<0.2f}".format(0,principal)) 
    for i in range (year):
        principal = principal * (1 + apr)
        print("{0:>3}    ${1:<0.2f}".format(i+1,principal))

main()