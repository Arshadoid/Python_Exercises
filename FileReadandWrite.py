# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:53:15 2022

@author: Arshad Mehtiyev
"""
# FileRead.py
# Prints a file to thre screen

def main():
    print("This program creates a file of usernames from a")
    print("file of names.")
    
    #get the file names
    inFileName = input("What file are the names in? ")
    outFileName = input("What file should the usernames go in? ")
    
    #open the files
    infile = open(inFileName, "r")
    outfile = open(outFileName, "w")
    
    #process each line of the input file
    for line in infile:
        #get the first and last names from line 
        first, last = line.split()
        #create the username
        uname = (first[0] + last[:7]).lower()
        #write it to the output file
        print(uname,file=outfile)
    
    #close both files
    infile.close()
    outfile.close()
    
    print("Usernames have been written to", outFileName)
main()