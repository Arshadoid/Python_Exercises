# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:51:14 2022

@author: Arshad Mehtiyev
"""

class Student:
    def __init__(self, name, hours, qpoints):
        self.name =name
        self.hours =float (hours)
        self.qpoints =float (qpoints)
    
    def getName(self):
        return self.name
    def getHours(self):
        return self.hours
    def getQPoints(self):
        return self.qpoints
    def gpa(self):
        if self.hours==0:
            return 0.0
        else:
            return self.qpoints/self.hours
    def addGrade(self, gradePoint,credit):
        self.hours+=credit
        self.qpoints+=gradePoint*credit
    def addLetterGrade(self, letterGrade,credit):
        
        letterGradeList=['A+','A','A-','B+','B','B-',
                        'C+','C','C-','D+','D','E','F']
        gradePointList=[4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3,
                        2.0, 1.7, 1.3, 1.0, 0.0, 0.0]
        grade=gradePointList[letterGradeList.index(letterGrade)]
        self.addGrade(grade, credit)
  
    
def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints =infoStr.split("\t")
    return Student(name, hours, qpoints)

def main ():

    newStudent=Student('Arshad, Mehtiyev', 0, 0)
    
    
    print("Type course grade point and credit hours separated with comma")
    while True:
                
        userInput=input('Grade point, credit hours: ').split(',')
    
        try:
            grade,credit=userInput
            newStudent.addGrade(float(grade), float(credit))
            
            
        except ValueError:
            
            try:
                grade,credit=userInput
                newStudent.addLetterGrade(str(grade), float(credit))
                
            except:
                if len(userInput)==1 and len(userInput[0])==0:
                    break
                else:
                    print("Entered Value is wrong, try again")
    
    print ("The best student is: " , newStudent.getName())
    print ("hours: " , newStudent.getHours())
    print ("GPA: " , newStudent.gpa())
    
if __name__ == '__main__' :
    main ()
    
