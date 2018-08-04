#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: write out constants
BAC_ILLEGAL_TO_DRIVE = 0.08

#step2: get input
gender = input("Enter your gender: male or female: ")
normalized_gender = gender.lower()

weight = int(input("Enter your weight in pounds: "))

time = int(input("Enter the number of hours since your last drink. If it's been less than one hour enter 1: "))

alcohol = int(input("Enter the amount of alcohol consumed in ounces: "))

#step3: set up two conditionals based on male or female response (since the ratio for the BAC equation depends on gender)
if normalized_gender == "male":
    male_bac = (alcohol * 5.4 / weight * 0.73) - .015 * time
    print("Your BAC is {:.2f}.".format(male_bac))
    if male_bac >= BAC_ILLEGAL_TO_DRIVE:
        print("It's not legal for you to drive.")
    else:
        print("You're able to drive legally, but be careful.")
elif normalized_gender == "female":
    female_bac = (alcohol * 5.4 / weight * 0.66) - .015 * time
    print("Your BAC is {:.2f}.".format(female_bac))
    if female_bac >= BAC_ILLEGAL_TO_DRIVE:
        print("It's not legal for you to drive.")
    else:
        print("You're able to drive legally, but be careful.")
