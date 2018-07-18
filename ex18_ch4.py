#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import math 

#step1: get inputs from user on the temperature and whether the temp is in C or F
temp = float(input("Enter the temperature: "))

temp_type = input("Is that temperature in Celsius or Fahrenheit? Enter C for Celsius or F for Fahrenheit: ")

#step2: write first conditional to convert C to F
if "C" in temp_type:
    celsius_to_fahrenheit = math.ceil(temp * 9 / 5) + 32
    print(f"The temperature in Fahrenheit is {celsius_to_fahrenheit} degrees.")

#step3: write second conditional to convert F to C
elif "F" in temp_type:
    fahrenheit_to_celsius = math.ceil(temp - 32) * 5 / 9
    print(f"The temperature in Celsius is {fahrenheit_to_celsius} degrees.")

