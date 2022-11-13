# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:33:32 2022

@author: Arshad Mehtiyev
"""
import matplotlib.pyplot as plt 

def main():
    n=int(input("Provide starting natural number: "))
    syrVal=0
    syrSeq=[n]
    
    while syrVal!=1:
        syrVal=syrSeq[-1]
        if syrVal%2==0:
            syrVal=int(syrVal/2)
            
        else:
            syrVal=3*syrVal+1
        syrSeq.append(syrVal)
    
    
    
    print("Syracuse sequence for the starting number",n,"is:")
    print(syrSeq)
    plt.plot(syrSeq)        

main()
    