#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: get user input
user_number_one = int(input("Enter one number: "))
user_number_two = int(input("Enter a second number: "))
user_number_three = int(input("Enter a third number: "))

# Step 2: check to see if all the numbers are different. 
# If the numbers are different, write another conditional to find the largest number
if user_number_one != user_number_two and user_number_one != user_number_three and user_number_two != user_number_three:
    if user_number_one > user_number_two and user_number_one > user_number_three:
        print(f"{user_number_one} is the largest number.")
    elif user_number_two > user_number_three and user_number_two > user_number_one:
        print(f"{user_number_two} is the largest number.")
    else:
        print(f"{user_number_three} is the largest number.")
else:
    print("These numbers are not different. Game over.")
