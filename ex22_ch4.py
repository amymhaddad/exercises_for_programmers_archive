#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: get inputs from user for three numbers
number1 = int(input("Enter one number: "))
number2 = int(input("Enter a second number: "))
number3 = int(input("Enter a third number: "))

#step2: set up inequalities to make sure all numbers are different. If they're not different, write a message that says that and exit the game.
if number1 == number2:
    print("The numbers are not different. Game over.")
elif number1 == number3:
    print("The numbers are not different. Game over.")
elif number2 == number1:
    print("The numbers are not different. Game over.")
elif number2 == number3:
    print("The numbers are not different. Game over.")
elif number3 == number1:
    print("The numbers are not different. Game over.")
elif number3 == number2:
    print("The numbers are not different. Game over.")
else:
    print("Let's continue with the game.")

#step3: set up conditional to see which number is the largest
if number1 > number2 and number1 > number3:
    print(f"{number1} is the largest number.")
elif number2 > number1 and number2 > number3:
    print(f"{number2} is the largest number.")
elif number3 > number2 and number3 > number1:
    print(f"{number3} is the largest number.")