#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:08:53 2018

@author: amyhaddad
"""

print("""
Here are the instructions: 
Create a program that determines how many years you have left until 
retirement and the year you can retire.
It should prompt for your current age and the age you want 
to retire and display the output as shown in the example that follows.
""")
    
print("""
Example output:
What is your current age? 25
At what age would you like to retire? 65
You have 40 years left until you can retire.
It's 2015, so you can retire in 2055.
""")


age = int(input("What is your current age? "))

retire = int(input("What age would you like to retire? "))

years_to_retirement = retire - age

print(f"You have {years_to_retirement} years left until you can retire.")


retirement_year = 2018 + years_to_retirement

print(f"It's 2018, so you can retire in {int(retirement_year)}.")

