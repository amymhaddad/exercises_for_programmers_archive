#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

age = 15

if age < 2:
    print("You're a baby.")

elif age == 2 or age < 4:
    print("You're a toddler.")

elif age == 4 or age < 13:
    print("You're a kid.")

elif age == 13 or age < 20: 
    print("You're a teen.")

elif age == 20 or age < 65:
    print("You're an adult.")

else:
    print("You're a senior.")