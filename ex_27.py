#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Import string and add constants
import string
EMPLOYEE_ID_LENGTH = 7

LETTERS = list(string.ascii_lowercase)
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Step 1: get user input:
f_name = input("Enter your first name: ")
normalized_f_name = f_name.lower()

l_name = input("Enter your last name: ")
normalized_l_name = l_name.lower()

z_code = input("Enter your zip code: ")

employee_id = input("Enter your employee ID: ")
normalized_employee_id = employee_id.lower()

# Step 2: write first function to get valid first name
def first_name(f_name):
    """Get input on first name and see if it's valid"""
    import sys
    
    if f_name == ' ':
        print("The first name must be filled in.")
        sys.exit()

    if len(f_name) == 1:
        print(f"\'{f_name}\' is not a valid first name. It's too short.")


first_name(normalized_f_name)

# Step 3: write second function to get user's last name
def last_name(l_name):
    """Get input on last name and see if it's valid"""
    import sys

    if l_name == ' ':
        print("The last name must be filled in.")
        sys.exit()
    
    if len(l_name) == 1:
        print(f"\'{l_name}\' is not a valid last name. It's too short.")


last_name(normalized_l_name)

# Step 4: write third function to get user's zip code in correct format
def zip_code(z_code):
    """Get a five-number zip code from user"""

    try:
        z_code = int(z_code)
    except ValueError:
        print("Your zip code must be numeric.")


zip_code(z_code)

# Step 4: write third function to get employee ID
def validate_employee_id(employee_id):
    """Validate employee id"""

    employee_id_validation = True

    length_of_employee_id = len(employee_id)
    if length_of_employee_id != EMPLOYEE_ID_LENGTH:
        employee_id_validation = False

    employee_id_hyphen = employee_id[2]
    if employee_id_hyphen != employee_id[2]:
        employee_id_validation = False

    two_letters_in_employee_id = employee_id[:2]
    for letter in two_letters_in_employee_id:
        if letter not in LETTERS:
            employee_id_validation = False

    four_numbers_in_employee_id = employee_id[3:]
    for number in four_numbers_in_employee_id:
        if number not in NUMBERS:
            employee_id_validation = False

    if employee_id_validation == True:
        print("There are no errors with this ID.")
    else:
        print("This ID is invalid.")


validate_employee_id(normalized_employee_id)
