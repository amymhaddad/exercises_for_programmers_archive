#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: import random
import random

# Step 2: create constants
SPECIAL_CHARACTERS = ["!", "@", "#", "$", "%", "^", "&", "*", "<", ">"]

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Step 3: create empty string for new password
new_password = ""

# Step 4: get input from user
new_password_length = int(input("What's the minimum password length? "))

total_special_characters = int(input("How many special characters to you want to add? "))

total_numbers = int(input("How many numbers do you want to add? "))

total_letters = int(input("How many letters do you want to add? "))

# Step 5: write first loop
for total_special_character in range(total_special_characters):
    random_special_character = random.randint(0, len(SPECIAL_CHARACTERS)-1)
    new_special_character = SPECIAL_CHARACTERS[random_special_character]
    new_password = new_password + new_special_character

# Step 6: write second loop
for total_number in range(total_numbers):
    random_number = random.randint(0, len(NUMBERS)-1)
    new_number = NUMBERS[random_number]
    new_password = new_password + str(new_number)

# Step 7: write third loop
for total_letter in range(total_letters):
    random_letter = random.randint(0, len(LETTERS)-1)
    new_letter = LETTERS[random_letter]
    new_password = new_password + new_letter

print(f"The new password is {new_password}.")

