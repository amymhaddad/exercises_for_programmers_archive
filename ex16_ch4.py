#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: state constant
LEGAL_DRIVING_AGE = 16

#step2: get input from user
age = int(input("Enter your age: "))

#step3: set up conditionals: if user provides invalid input, if 16 or older, or if younger than 16
if age < 0:
    print("Please enter a valid age.")
if age >= LEGAL_DRIVING_AGE:
    print("You're legally able to drive.")
else: 
    print("You're too young to drive legally.")
