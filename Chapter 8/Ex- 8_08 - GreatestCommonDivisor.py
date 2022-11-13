# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:25:22 2022

@author: Arshad Mehtiyev
"""
n,m=input('Enter two comma seperated integers to find their GCD: ').split(',',2)
n=int(n)
m=int(m)

while m!=0:
    n,m=m,n%m

print(n)