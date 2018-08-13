#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: write constant
AGE = 11

# Step 2: write conditional
if AGE < 2:
    print("You're a baby.")
elif AGE >= 2 and AGE < 4:
    print("You're a toddler.")
elif AGE >= 4 and AGE < 13:
    print("You're a kid.")
elif AGE >= 13 and AGE < 20: 
    print("You're a teen.")
elif AGE >= 20 and AGE < 65:
    print("You're an adult.")
else:
    print("You're a senior.")
    
