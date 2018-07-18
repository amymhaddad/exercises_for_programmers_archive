#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: get input on user's weight
weight = float(input("Enter you weight in pounds: "))

#step2: get input on user's height and convert it to inches
feet_height = int(input("Enter your height in feet: "))
inches_height = int(input("Enter your height in inches: "))

total_height = (feet_height * 12) + inches_height

#step3: write BMI calculation to use in conditional statements
bmi = (weight / (total_height * total_height)) * 703

#step4: write first conditional
if bmi >= 18.5 and bmi <= 25:
    print("Your BMI is {:.1f}".format(bmi)+". You're within the ideal weight range.")

#step5: write second conditional:
elif bmi > 25:
    print("Your BMI is {:.1f}".format(bmi)+". You're overweight and should see your doctor.")

#step6: write third conditional:
else: 
    print("Your BMI is {:.1f}".format(bmi)+". You're underweight.")