#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: state constant
LEGAL_DRIVING_AGE = 16

#step2: get input from user on their age
user_age = int(input("Enter your age: "))

#step3: set up first conditional
if user_age >= LEGAL_DRIVING_AGE:
    print("You're old enough to drive legally.")

#step4: set up second conditional if user enters a number less than 0
if user_age < 0: 
    print("Please enter a valid age.")

#step5: set up conditional if user is older than 0 but less than 16
if (user_age > 0) and (user_age < LEGAL_DRIVING_AGE):
    print("You're not old enough to drive legally.")