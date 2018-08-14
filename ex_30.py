#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: set up two lists
number_outer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
number_inner = number_outer[:]

# Step 2: write a nested loop
for number_1 in number_outer:
    for number_2 in number_inner:
        product = number_1 * number_2
        print(f"{number_1} * {number_2} = {product}")
