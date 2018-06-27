#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: ask user for input: age
current_age = int(input("What is your age? "))

#step2: ask user for input: ideal retirement age
ideal_retirement_age = int(input("What age do you want to retire? "))

#step3: write calculation to determine the number of years until retirement
years_to_retirement = ideal_retirement_age - current_age

#step4: write calculation to determine the year you can retire
retirement_year = 2018 + years_to_retirement

#step5: print number of years until retirement
print(f"You have {years_to_retirement} years left until you can retire.")

#step 6: print current year and the year user can retire
print(f"It's 2018, so you can retire in {retirement_year}.")
