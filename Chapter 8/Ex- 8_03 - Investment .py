# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:21:39 2022

@author: Arshad Mehtiyev
"""



initVal=10000
rate=0.1

finalVal=initVal
year=0

while 2*initVal>finalVal:
    year+=1
    finalVal+=finalVal*rate
    
print(year)