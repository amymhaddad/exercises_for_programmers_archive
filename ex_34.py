#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: create list of names and get length of list
employee_names = ['jack smith', 'jill jones', 'pam jackson', 'sally collins', 'tim goodwin']

total_employees = len(employee_names)

# Step 2: print the total number of employees and print their names
print(f"There are {total_employees} employees: ")

for name in employee_names:
    print(name.title())

print("\n")

# Step 3: get user input on employee removal and remove employee
employee_to_remove = input("Which employee should I remove? ")
normalized_employee_to_remove = employee_to_remove.lower()

employee_names.remove(normalized_employee_to_remove)

print("\n")

# Step 5: print the remaining employees
print(f"There are {total_employees} employees remaining: ")

for name in employee_names:
    print(name.title())
