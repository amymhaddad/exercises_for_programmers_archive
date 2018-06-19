#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

people = int(input("How many people will eat pizza? "))
number_of_pizzas = int(input("How many pizzas do you have? "))
slices_per_pizza = int(input("How many slices are in each pizza? "))

total_slices = slices_per_pizza * number_of_pizzas

print(f"There are {people} people and {number_of_pizzas} pizzas.")

pizza_slices_per_person = total_slices / people
print(f"Each person gets {pizza_slices_per_person} pieces of pizza.")

leftover_pieces = total_slices % people
print(f"There are {int(leftover_pieces)} leftover pieces.")

