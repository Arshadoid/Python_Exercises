# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:46:08 2022

@author: Arshad Mehtiyev
"""

def getWindChill(s, t):
    if s<=3:
        return '  N/A'
    else:
        index=35.74+0.6215*t-35.75*s+0.4275*t*s                
        return round(index,2)


def printDashes():
    for i in range(115):
        print('-',end='')
    print('-')  

def main():
    # print("***********************************")
    # print("|   kg     |    Lb     |    Oz    |")
    # print("***********************************")
    printDashes()  
    
    print("| {:^112} |".format('WindChill index'))  
    printDashes()  
    
    print("| {:^} |".format('     '), end='')
    for t in range(-20,51,10):
        temp=str(t)+'F'
        if t>0:
            temp='+'+temp
        print("  {:^8} |".format(temp), end='')
    print("  {:^8} |".format('+60F'))   
    
    printDashes()      
    
    for s in range(0,51,5):
        speed=str(s)+'mph'
        print("| {:^5} |".format(speed), end='')
        for t in range(-20,61,10):
            index=getWindChill(s, t)
            if not isinstance(index, str):
                if index>0:
                    index='+'+str(index)
            print("  {:<8} |".format(index), end='')
        print()  
    printDashes()


if __name__ == '__main__':
    main()
            