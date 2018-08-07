#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:08:53 2018

@author: amyhaddad
"""

age = int(input("What is your current age? "))

retire = int(input("What age would you like to retire? "))

years_to_retirement = retire - age

print(f"You have {years_to_retirement} years left until you can retire.")

retirement_year = 2018 + years_to_retirement

print(f"It's 2018, so you can retire in {int(retirement_year)}.")
