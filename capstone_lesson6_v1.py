#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

print("One way to solve: ")
#step 1: state number of minutes
total_minutes = 121

#step 2: convert number of minutes to hours
number_of_hours = round(total_minutes / 60)
print("Hours:", number_of_hours)

#step 3: convert remainder from conversion to minutes
remainder_minutes = round(.0166 * 60)
print("Minutes:", remainder_minutes)

