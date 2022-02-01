# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 08:49:13 2022

@author: arsha
"""
# change.py
# A program to calculate the valie of some change in dollars

def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = eval(input("Quarter: "))
    dimes = eval(input("Dimes: "))
    nickels = eval(input("Nickels: "))
    pennies = eval(input("Pennies: "))
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print()
    print("The total value of your change is ", total)

main()