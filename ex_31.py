#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: write constants
LOW_INTENSITY = 55
HIGH_INTENSITY = 95
INTERVAL = 5

# Step 2: get input from user 
age = int(input("Enter your age: "))
resting_heart_rate = int(input("Enter your resting heart rate: "))

# Step 3: write loop to determine target HR 
for value in range(LOW_INTENSITY, HIGH_INTENSITY, INTERVAL):
    intensity_as_decimal = value / 100
    target_hr = (((220 - age) - resting_heart_rate) * intensity_as_decimal) + resting_heart_rate
    print(f"At {value}%, your heart rate should be {int(target_hr)}.")
