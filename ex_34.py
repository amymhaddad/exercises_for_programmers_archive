#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: create a list of names
names = ['Theo', 'Tom', 'Paul', 'Sam', 'Sally']

# Make this list lowercase
names_lowercase = [names.lower() for names in ['Theo', 'Tom', 'Paul', 'Sam', 'Sally']]

# Step 2: use loop to print each name from list
print("There are five employees:")
for name in names_lowercase:
    print(name.capitalize())

# Step 3: get input on employee to remove
employee_removal = input("Which employee needs to be removed? ")

# Step 4: remove employee from list
names_lowercase.remove(employee_removal)

# Step 5: print list of remaining employees
print("These are the remaining employees:")
for name in names_lowercase:
    print(name.capitalize())
