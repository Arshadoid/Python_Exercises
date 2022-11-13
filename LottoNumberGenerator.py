# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 19:01:25 2022

@author: Arshad Mehtiyev
"""

import random

def main():
    
    numbList=[]
    
    for i in range(1,50):
        numbList.append(i)
        
    #print(numbList)
       
    selectNumb=[]
    
    tempNumbList = numbList.copy()
    for i in range(6):
        number=random.choice(tempNumbList)
       # print(number)
        selectNumb.append(number)
        
        tempNumbList.pop(tempNumbList.index(number))
    
    selectNumb.sort()
        
    print(selectNumb)    
      
if __name__ =='__main__':    
    main()