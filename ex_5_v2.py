#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:36:53 2018

@author: amyhaddad
"""

number_1 = input("What is the first number? ")
number_2 = input("What is the second number? ")

sum = int(number_1) + int(number_2)
print(f"{number_1} + {number_2} = {sum}")

difference = int(number_1) - int(number_2)
print(f"{number_1} - {number_2} = {difference}")

product=int(number_1) * int(number_2)
print(f"{number_1} * {number_2} = {product}")

quotient = int(number_1) % int(number_2)
print(f"{number_1} / {number_2} = {quotient}")
