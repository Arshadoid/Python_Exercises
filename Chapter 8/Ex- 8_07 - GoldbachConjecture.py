# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:38:01 2022

@author: Arshad Mehtiyev
"""

import math

def isPrime(n):
    prime=True
    if n>2:
        for i in range(2,int(math.sqrt(n)+1),1):
            if n%i==0:
                prime=False
                return prime
                
        if prime:
            return prime
            
def main():
    n=int(input("Provide an even number(except 1,2) to find the prime numbers to which it can be added to: "))
    
    if n%2==0:
        a=n//2
        b1=a
        b2=a
        while b2!=2:
            b1=b1+1
            b2=b2-1
            
            if isPrime(b1) and isPrime(b2):
                print(n, 'can be added up by', b1, 'and', b2,'prime numbers')
    else:
        print('Provided number is not even')

main()