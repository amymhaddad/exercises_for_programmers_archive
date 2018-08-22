#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: import random
import random

# Step 2: create list of constants
ANSWERS = ['yes', 'no', 'maybe', 'ask again later']

# Step 3: create for loop
for question in input("What's your question? "):
    random_number = random.randint(0, len(ANSWERS)-1)
    response = ANSWERS[random_number]
print(response.capitalize())
