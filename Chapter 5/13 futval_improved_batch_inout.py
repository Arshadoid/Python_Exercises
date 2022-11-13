# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:21:11 2022

@author: Arshad Mehtiyev
"""

# futval . py
# A program to compute the value of an investment
# carried 10 years into the future
def main () :
    print ("This program calculates the value of investment")
    print ("year by year for the given period.")
    print ("It reads initial principal, rate and period from the") 
    print ('"13 futval_read_file.txt" file, which can be adjusted in the file')
    print ('Then it will write the resul in "13 futval_write_file.txt"')
    input("Now, update, save and close the read file, then press enter here")
           
    infile = open("13 futval_read_file.txt", "r")
    outfile = open("13 futval_write_file.txt", "w")
    
    principal = float((infile.readline().split(":"))[1])
    apr = float((infile.readline().split(":"))[1])
    year = int((infile.readline().split(":"))[1])
        
    print("Year    Value",file=outfile)
    print("----------------",file=outfile)
    print("{0:>3}    ${1:<0.2f}".format(0,principal),file=outfile) 
    for i in range (year):
        principal = principal * (1 + apr)
        print("{0:>3}    ${1:<0.2f}".format(i+1,principal),file=outfile)
        
        
    infile.close()
    outfile.close()

main()