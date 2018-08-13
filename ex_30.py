#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: set up two lists
number_outer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
number_inner = number_outer[:]

# Step 2: write "for" loop that iterates through each outer number and completes math operation on each inner number
for number1 in number_outer:
    for number2 in number_inner:
        product = number1 * number2
        print(f"{number1} * {number2} = {product}")