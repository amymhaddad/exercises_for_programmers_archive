#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: get input for two names 
name_1 = input("Enter a name (first and last name): ")
name_2 = input("Enter a second name (first and last name): ")

# Step 2: separate the names
space1 = name_1.find(' ')
space2 = name_2.find(' ')

first_name_name_1 = name_1[:space1]
first_name_name_2 = name_2[:space2]
last_name_name_1 = name_1[space1+1:]
last_name_name_2 = name_2[space2+1:]

# Step 3: divide each first name in half and then divide each last name in half
right_half_first_name_name_1 = first_name_name_1[2:]
left_half_first_name_name_1 = first_name_name_1[:2]
right_half_first_name_name_2 = first_name_name_2[2:]
left_half_first_name_name_2 = first_name_name_2[:2]

right_half_last_name_name_1 = last_name_name_1[2:]
left_half_last_name_name_1 = last_name_name_1[:2]
right_half_last_name_name_2 = last_name_name_2[2:]
left_half_last_name_name_2 = last_name_name_2[:2]

# Step 4: combine the names to get new names
new_first_name_name_1 = right_half_first_name_name_1 + left_half_first_name_name_2
new_first_name_name_2 = right_half_first_name_name_2 + left_half_first_name_name_1
new_last_name_name_1 = right_half_last_name_name_1 + left_half_last_name_name_2
new_last_name_name_2 = right_half_last_name_name_2 + left_half_last_name_name_1

# Step 5: print output
full_new_name_name_1 = (f"{new_first_name_name_1.capitalize()} {new_last_name_name_1.capitalize()}")
full_new_name_name_2 = (f"{new_first_name_name_2.capitalize()} {new_last_name_name_2.capitalize()}")

print(f"These are the new names: {full_new_name_name_1} and {full_new_name_name_2}")
