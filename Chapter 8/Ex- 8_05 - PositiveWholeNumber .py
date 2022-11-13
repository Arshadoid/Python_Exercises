# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:55:33 2022

@author: Arshad Mehtiyev
"""
import math

def main():
    n=int(input("Provide positive whole number(except 1,2): "))
    prime=True
    if n>2:
        for i in range(2,int(math.sqrt(n)+1),1):
            if n%i==0:
                print(i)
                print('Number is not prime')
                prime=False
                break
    
        if prime==True:
            print('Number is prime')
    
      

main()