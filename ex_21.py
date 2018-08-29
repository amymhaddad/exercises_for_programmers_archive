#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: create constant that's a dictionary to contain months and numbers
MONTHS_TO_NUMBERS = {
    '1': 'january',
    '2': 'february',
    '3': 'march',
    '4': 'april',
    '5': 'may',
    '6': 'june',
    '7': 'july',
    '8': 'august',
    '9': 'september',
    '10': 'october',
    '11': 'november',
    '12': 'december',
}

# Step 2: create prompt to get user input
user_number = input("Enter a number of the month: ")

# Step 3: write conditional to print user's input
if user_number in MONTHS_TO_NUMBERS:
    convert_number_to_month = MONTHS_TO_NUMBERS[user_number]
    print(f"The name of the month is {convert_number_to_month.capitalize()}.")
