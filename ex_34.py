#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: create list of names and find length of list
employee_list = ['john johns', 'mary kay', 'sue smith', 'paul haddad', 'nina jones']

total_employees = len(employee_list)

# Step 2: print total names, then write a for loop to print all employee names
print(f"There are {total_employees} total employees: ")
for employee in employee_list:
    print(employee.title())

print('\n')
        
# Step 3: ask user which employee to remove and remove employee from list
employee_to_remove = input("Which employee should I remove? ")
normalized_employee_to_remove = employee_to_remove.lower()

if normalized_employee_to_remove not in employee_list:
    print("Error: name not found.")
    sys.exit()

if normalized_employee_to_remove in employee_list:
    employee_list.remove(normalized_employee_to_remove)

print('\n')

total_employees = len(employee_list)

# Step 4: print remaining total employees and their names
print(f"There are {total_employees} remaining employees: ")
for employee in employee_list:
    print(employee.title())
    
