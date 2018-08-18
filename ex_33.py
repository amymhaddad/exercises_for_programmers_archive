#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: import random
import random

# Step 2: create a list of answer possibilities
answers = ['Yes', 'No', 'Maybe', 'Ask again later']

# Step 3: write a loop 
for question in input("What's your question? "):
    random_number = random.randint(0, len(answers)-1)
    magic_eight_response = answers[random_number]

print(f"{magic_eight_response}")
