#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: import random
import random

# Step 2: create constant and randomize the list
ANSWERS = ['yes', 'no', 'maybe', 'ask again later']
random.shuffle(ANSWERS)

# Step 3: create a loop that asks user for their question and print a response 
for answer in ANSWERS:
    question = input("What's your question? ")
    print(answer)
    
