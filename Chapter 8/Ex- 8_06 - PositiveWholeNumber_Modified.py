# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:55:33 2022

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
    n=int(input("Provide range to find primes numbers(except 1,2): "))
    primeNumbers=[]
    
    for i in range(3,n+1,1):
        if isPrime(i):
            primeNumbers.append(i)
        
    print(primeNumbers)

main()