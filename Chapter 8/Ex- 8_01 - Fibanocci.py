# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:14:57 2022

@author: Arshad Mehtiyev
"""
def findFib(n):
    a=1
    b=0
    
    for i in range(1,n+1,1):
        fib=a+b
        a=b
        b=fib      
    return fib
    
def main():
    cond = False
    while cond==False:
        try:
            n=int(input("Type n (integer)  to get nth Fibanocci number: "))
            if n<0:
                print("Number can not be negative, try again")
            else:
                cond=True
        except:
            print("Given value is not correct, try again")
    
    print(f"{n}th Fibanocci nunber is {findFib(n)}")


if __name__ == "__main__":
    main()