#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: write out constants
BAC_ILLEGAL_TO_DRIVE = 0.08

#step2: get input
gender = input("Enter your gender, male or female: ")

weight = int(input("Enter your weight in pounds: "))

time = int(input("Enter the number of hours since your last drink. If it's been less than one hour enter 1: "))

alcohol = int(input("Enter the amount of alcohol in ounces: "))

#step3: set up two conditionals based on male or female response (since the ratio for the BAC equation depends on gender)
if gender == "male": 
    male_bac = (alcohol * 5.14 / weight * .73) - .015 * time
    if male_bac >= BAC:
        print("You're not able to drive legally.")
    else:
        print("You're able to drive legally, but be careful.")   
elif gender == "female":
    female_bac = (alcohol * 5.14 / weight * .66) - .015 * time
    if female_bac >= BAC:
        print("You're not able to drive legally.")
    else: 
        print("You're able to drive, but be careful")