#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 11:00:59 2018

@author: amyhaddad
"""

print("This is from page 16.")
number_one = input("What is the first number? ")

print(f"This is the first number: {number_one}.")

number_two = input("What is the number_two? ")

print(f"This is the second number: {number_two}.")


sum = int(number_one)+int(number_two)
print(f"{number_one} + {number_two} = {sum}")

difference = int(number_one) - int(number_two)
print(f"{number_one} - {number_two} = {difference}")

product = int(number_one) * int(number_two)
print(f"{number_one} * {number_two} = {product}")

quotient = int(number_one) / int(number_two)
print(f"{number_one} / {number_two} = {int(quotient)}")





#print("10 + 5=", 15)
#print("10 - 5=", 5)
#print("10 * 5=", 50)
#print("10 / 5=", 2)


