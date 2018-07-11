#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: state number variable
secret_number = 11

#step2: get user input to guess the number
user_guess = int(input("Guess my secret number: "))

#step3: write one conditional statement re: if guess is too low
if user_guess < 11:
    print("Too low.")

#step4: write second conditional statement re: if guess is too high
if user_guess > 11:
    print("Too high.")

#step5: write third conditional statement re: if guess is correct
if user_guess == 11:
    print("You got it!")