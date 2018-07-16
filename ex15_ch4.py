#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: create a constant
KNOWN_PASSWORD = "secret"

#step2: get input on user's username
username = input("Enter your username: ")

#step3: get input on user's password
password = input("Enter your password: ")

#step4: write if statement to verify user password with known password
if password == KNOWN_PASSWORD:
    print("Welcome")

else:
    print("I don't know you.")