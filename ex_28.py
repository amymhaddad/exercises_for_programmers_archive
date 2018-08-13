#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: create constant equal to the number of values I need input for
NUM = 5

# Step 2: create an empty list
new_list = []

# Step 3: create for loop to iterate through 5 numbers to get input
for value in range(NUM):
    numbers = int(input("Enter a number: "))
    new_list.append(numbers)
    
total = sum(new_list)

print(f"The sum is {total}.")
