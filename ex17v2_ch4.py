#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: set up constant
BAC = 0.08

#step2: get inputs from user
weight = float(input("Enter your weight in pounds: "))
gender = input("Enter your gender, male or female: ")
normalized_gender = gender.lower()
alcohol_consumed = int(input("Enter the amount of alcohol you've consumed in ounces: "))
hours = float(input("Enter the number of hours since your last drink. If it's been one hour or less, enter 1: "))

if gender != "male" and gender != "female":
    print("Please enter a valid answer for your gender.")

elif gender == "male":
    male_bac = (alcohol_consumed * 5.14 / weight * 0.73) -.015 * hours
    if male_bac >= BAC:
        print("You're not legally able to drive.")
    else:
        print("You're legally able to drive, but be careful!")

elif gender == "female":
    female_bac = (alcohol_consumed * 5.14 / weight * 0.66) - .015 * hours
    if female_bac >= BAC:
        print("You're not legally able to drive.")
    else:
        print("You're legally able to drive, but be careful!")