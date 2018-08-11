#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: create an empty list
new_list = []

#step2: create a variable equal to the number of values I need input for
num = 5

#step3: create for loop to iterate through 5 numbers to get input
for value in range(num):
    numbers = int(input("Enter a number: "))
    new_list.append(numbers)
print("The sum is", sum(new_list),".")