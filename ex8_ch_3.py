#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: get input
number_people = int(input("Enter the number of people: "))
total_pizzas = int(input("Enter the total number of pizzas: "))
slices_per_pizza = int(input("Enter the slices per pizza: "))

#step2: calculate the total slices of pizza
total_slices = total_pizzas * slices_per_pizza

#step3: calucate the slices per person
slices_per_person = total_slices // number_people

#step4: calculate the leftover pizza
leftover_pizza = total_slices % number_people

#step5: write out how much pizza everyone gets using if-else to account for pluralization
if slices_per_person == 1:
    print(f"Each person gets one piece of pizza.")
else: 
    print(f"Each person gets {slices_per_person} pieces of pizza.")

#step6: write conditional if there is leftover pizza
if leftover_pizza >= 1:
    print(f"There are {leftover_pizza} slices of pizza leftover.")
