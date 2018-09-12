#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: create constant
MINIMUM_CHARACTERS = 8

SPECIAL_CHARACTERS = ['!', '@', '#', '$', '%', '^', '<','&', '*', '()', '>', '?', '{', '}', '[', ']', '[]', '{}']
NUMBERS = list(range(1, 10))
NUMBERS = str(NUMBERS)
LETTERS = ('a', 'b', 'c', 'd')

# Step 2: write function to determine password complexity
def password_validator(password):
    """Determine strength of password"""

    password = str(password)

    if password.isdigit():
        numbers_in_password = len(password)
        if numbers_in_password < MINIMUM_CHARACTERS:
            print(f"The password \'{password}\' is very weak.")
            
    if password.isalpha():
        letters_in_password_length = len(password)
        if letters_in_password_length < MINIMUM_CHARACTERS:
            print(f"The password \'{password}\' is weak.")
    
    if password.isalnum():
        numbers_and_letters_password_length = len(password)
        if numbers_and_letters_password_length >= MINIMUM_CHARACTERS:
            print(f"The password \'{password}\' is strong.")

    # if password >= MINIMUM_CHARACTERS:
    #     print('true')
        
        # for character in SPECIAL_CHARACTERS:
        #     if character in password:
        #         for number in NUMBERS:
        #             if number in password:
        #                 for letter in LETTERS:
        #                     if letter in password:
        #                         print(f"The password \'{password}\' is very strong.")

password_validator("aaaad")