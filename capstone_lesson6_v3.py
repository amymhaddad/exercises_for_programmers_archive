#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

print("A third way to solve: ")

#step 1: get input from user for total number of minutes as an integer
total_minutes = int(input("What is the total number of minutes? "))
print(total_minutes)

#step 2: convert minutes to hours
total_hours = int(total_minutes / 60)
# print(total_hours)

#step 3: calculate remainder and turn into minutes
leftover_minutes = round(total_minutes % 60)
# print(leftover_minutes)

print("Hours:", total_hours)
print("Minutes:", leftover_minutes)







