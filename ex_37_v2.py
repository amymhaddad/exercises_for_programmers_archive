#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: import random
import random

# Step 2: create empty string for new password
new_password = ""

# Step 3: create lists
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "<", ">"]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Step 4: get input from user
new_password_length = int(input("What's the minimum password length? "))

total_special_characters = int(input("How many special characters to you want to add? "))

total_numbers = int(input("How many numbers do you want to add? "))

total_letters = int(input("How many letters do you want to add? "))

# Step 5: write first conditional
if total_special_characters >= new_password_length and total_special_characters <= new_password_length:
    # Telling Python to do a task for each special character
    for total_special_character in range(total_special_characters):
        random_special_character = random.randint(0, len(special_characters)-1)
        new_special_character = special_characters[random_special_character]
        new_password = new_password + new_special_character

# Step 6: write conditional for numbers
if total_numbers >= 1 and total_numbers <= new_password_length:
    for total_number in range(total_numbers):
        random_number = random.randint(0, len(numbers)-1)
        new_number = numbers[random_number]
        new_password = new_password + str(new_number)

# Step 7: write conditional to see if user wants letters in password
if total_letters >= 1 and total_letters <= new_password_length:
    for total_letter in range(total_letters):
        random_letter = random.randint(0, len(letters)-1)
        new_letter = letters[random_letter]
        new_password = new_password + new_letter

print(f"The new password is {new_password}.")
