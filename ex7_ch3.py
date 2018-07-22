#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#create a constant to set up conversion from square feet to square meters
SQUAREFEET_TO_SQUAREMETERS = 0.092903

#step1: ask user for input for length of room in feet
room_length = int(input("What is the length of the room in feet? "))

#step2: ask user for input for width of room in feet
room_width = int(input("What is the width of the room in feet? "))

#step3: print the entered results
print(f"You entered dimensions of {room_length} feet for the length and {room_width} feet for the width.")

#step4: write a calculation for the area of room in square feet
area_in_squarefeet = room_length * room_width

#step5: print area of room in square feet
print(f"The area of the room in square feet is: {area_in_squarefeet}.")

#step6: write calculation to convert square feet to square meters
area_in_squaremeters = area_in_squarefeet * SQUAREFEET_TO_SQUAREMETERS

#step7: print area of room in square meters
print(f"The area of the room in square meters is: {area_in_squaremeters}.")