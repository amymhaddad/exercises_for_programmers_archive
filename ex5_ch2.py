#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:08:53 2018

@author: amyhaddad
"""

import math 

#step1: write input statement asking for one number
first_number = int(input("This is your first number: "))

#step2: write input statement asking for second number
second_number = int(input("This is your second number: "))

#step2: create variable "sum" and write an equation that adds the two numbers together and print equation and solutoin 
sum = first_number + second_number 

print(f"{first_number} + {second_number} = {sum}")

#step3: create variable "difference" and write an equation that subtracts the two numbers and print the equation and solutionon 
difference = first_number - second_number

print(f"{first_number} - {second_number} = {difference}")

#step4: create variable "product" and write an equation that multiplies the two numbers together; print eq and soltuion
product = first_number * second_number

print(f"{first_number} * {second_number} = {product}")

#step5: create variable "quotient" and write an equation that divides the two numbers; print equation and soltuoin
quotient = first_number / second_number

print(f"{first_number} / {second_number} = {math.ceil(quotient)}")