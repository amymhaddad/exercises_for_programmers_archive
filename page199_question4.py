#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: state constant
SECRET_NUMBER = 11

#step2: get user input to guess the number
user_guess = int(input("Guess my secret number: "))

#step3: write conditionals
if user_guess < 11:
    print("Too low.")
elif user_guess > 11:
    print("Too high.")
else: 
    print("You got it!")
