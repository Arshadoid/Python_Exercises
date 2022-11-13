# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:08:56 2022

@author: Arshad Mehtiyev
"""

# dateconvert2_formatting.py
# Converts a date in form "mm./dd/yyyy" to "month day, year"
def main() :
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")
    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")
    # convert monthStr to the month name
    months = ["January" , "February" , "March" , "April" ,
              "May" , "June" , "July" , "August" ,
              "September" , "October" , "November" , "December"]
    monthStr = months[int(monthStr)-1]
    # output result in month day, year format
    print("The converted date is {0} {1}, {2}".format(monthStr,
                                                      int(dayStr),yearStr))
    
main()