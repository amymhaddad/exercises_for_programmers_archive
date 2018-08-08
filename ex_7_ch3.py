#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

SQ_FT_TO_METERS = 0.092903

length = int(input("What is the length of the room in feet? "))
width = int(input("What is the width of the rrom in feet? "))

print(f"You entered dimensions of {length} feet by {width} feet.")

square_feet = length * width
print(f"The area of the room is {square_feet} square feet.")

square_meters = square_feet * SQ_FT_TO_METERS 
print(f"The area of the room is {square_meters} square meters.")
