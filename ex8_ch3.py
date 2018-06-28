#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: get input: number of people eating pizza?
pizza_eaters = int(input("How many people are eating pizza? "))

#step2: get input: how many pizzas are there?
total_pizzas = int(input("How many pizzas do you have? "))

#step3: get input: how many slices are in a pizza?
slices_per_pizza = int(input("How many slices are in a pizza? "))

#step4: write calculation to see how many total slices there are
total_pizza_slices = total_pizzas * slices_per_pizza

#step5: write calculation to divide the pizza slices evenly among the total people
slices_per_person = total_pizza_slices / pizza_eaters

print(f"Each person can have {int(slices_per_person)} pieces of pizza.")

#step6: write calculation to determine left over slices of pizza
leftover_pizza_slices = total_pizza_slices % pizza_eaters

print(f"There will be {leftover_pizza_slices} leftover slices of pizza.")