#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import sys

# Step 1: get input from user
user_rate = int(input("What is the rate of return? "))

# Step 2: write conditionals to check for valid input
if user_rate <= 0:
    print("That's not valid input.")
    sys.exit()
else:
    time_to_double_investment = 72 / user_rate
    print(f"It'll take you {int(time_to_double_investment)} years to double your investment.")
