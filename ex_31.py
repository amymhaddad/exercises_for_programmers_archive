#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""


# Step 1: get input from user 
age = int(input("Enter your age: "))
resting_heart_rate = int(input("Enter your resting heart rate: "))

# Step 2: write "for" loop to determine target heart rate based on given intensities (55% to 95%)
for value in range(55, 100, 5):
    intensity_as_decimal = value / 100
    target_hr = (((220 - age) - resting_heart_rate) * intensity_as_decimal) + resting_heart_rate
    print(f"At {value}%, your heart rate should be {int(target_hr)}.")
    
