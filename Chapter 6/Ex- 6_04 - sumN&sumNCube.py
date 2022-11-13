# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:21:34 2022

@author: Arshad Mehtiyev
"""

import numpy as np

def sumN(n):
    return sum(np.arange(1,n+1))

def sumNCubes(n):
    return sum(np.arange(1,n+1)**3)

def main():
    
    n=int(input("Enter a natural number:"))
    sumOfN=sumN(n)
    sumOfNCubes=sumNCubes(n)
    
    print(f"Sum of the first {n} natural numbers: {sumOfN}")
    print(f"Sum of the cubse of the first {n} natural numbers: {sumOfNCubes}")
    
if __name__=="__main__":
    main()