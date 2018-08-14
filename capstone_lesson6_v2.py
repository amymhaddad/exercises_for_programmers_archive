#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

print("A second way to solve: ")
#step 1: state total number of minutes
total_minutes = 123

#step 2: convert total minutes to hours  
total_hours = round(total_minutes / 60)
# print(total_hours)

#setp 3: create new variable to calculate the remainder and put into minutes using "%"
leftover_minutes = total_minutes % 60
# print(leftover_minutes)

print("Hours:", total_hours)
print("Minutes:", leftover_minutes)
