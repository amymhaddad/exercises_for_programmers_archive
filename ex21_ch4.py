#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: get input from user
print("I'm going to ask you for a number, and a calendar month will populate based on the number you enter.")
number = int(input("Enter a number 1 through 12: "))

#step2: write the conditional  
if number == 1: 
    print("January")
elif number == 2: 
    print("February")
elif number == 3: 
    print("March")
elif number == 4: 
    print("April")
elif number == 5: 
    print("May")
elif number == 6: 
    print("June")
elif number == 7:
    print("July")
elif number == 8:
    print("August")
elif number == 9:
    print("September")
elif number == 10:
    print("October")
elif number == 11:
    print("November")
elif number == 12:
    print("December")
else:
    print("You've entered an incorrect value.")