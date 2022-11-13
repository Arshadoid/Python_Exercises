# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 13:12:07 2022

@author: Arshad Mehtiyev
"""

# gpasort .py
# A program to sort student information into GPA order .
from gpa import Student, makeStudent

def readStudents(filename):
    infile = open(filename , 'r' )
    students = []

    for line in infile:
       students.append(makeStudent(line))
    infile.close()

    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students :
        print("{0}\t{1}\t{2}".
              format(s.getName(), s.getHours(), s.getQPoints()),
               file=outfile)
    outfile.close()

def main ( ) :
    print ( "This program sorts student grade information by GPA, name or credit " )
    filename = input ("Enter the name of the data file: " )
    data = readStudents (filename)
    correctField=False
    fieldNameList=['GPA','name','credit']
    while not correctField:

        fieldName=str(input ("Enter the name of the field for sorting(GPA,name,credit): " ))
        if fieldName in fieldNameList:
            correctField=True
            if fieldName=='GPA':
                data.sort(key=Student.gpa)
            elif fieldName=='name':
                data.sort(key=Student.getName)
            else: 
                data.sort(key=Student.getHours)
        else:
          print("Entered field name is not correct, try again")  

    
    
    filename = input ( "Enter a name for the output file: " )
    writeStudents (data, filename)
    print("The data has been written to" , filename)

if __name__ == '__main__': 
    main()
