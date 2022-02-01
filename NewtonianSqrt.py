# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 19:31:04 2022

@author: Arshad Mehtiyev
"""

import math

value =eval(input("Type the value to be square-rooted: "))
guessNumber= eval(input("Number of times guess to be improved: "))

guess=value/2

for i in range(guessNumber):
    guess=(guess+value/guess)/2
print("Guess is: ", guess)
print("It is this much close to the actual root: ", round(guess-math.sqrt(value),7))

    