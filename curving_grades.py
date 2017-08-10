# -*- coding: utf-8 -*-
"""
Created on August 10th, 2017

@author: Pardis Ranjbar
E-mail: pardis.ranjbar@gmail.com
#==============================================================================
# This code gets a grade from user, and adds 1 point if it's above 16, 
and adds 2 points if it's lower than 15
#==============================================================================
"""
try:
    grade=int(input('enter the grade:\n'))
    while 0<=grade<=20: #grades must be between 0 and 20
        if grade>16:
            grade=grade+1
        elif grade<15:
            grade=grade+2
        else:
            pass
        print (grade)
        break # If the while loop has been completed, get out of the loop
    else:
        print('The grade must be between 0 and 20.')
except ValueError: #if user enters sth other than an integer:
    print('The grade must be an integer.')
