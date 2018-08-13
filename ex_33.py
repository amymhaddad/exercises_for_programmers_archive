#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: import random
import random

# Step 2: create a list with all of the answer possibilities and tell Python to shuffle them
answers = ['yes', 'no', 'maybe', 'ask again later']
random.shuffle(answers)

# Step 3: create a loop that asks user for their question and print a response 
for answer in answers:
    question = input("What's your question? ")
    print(answer)