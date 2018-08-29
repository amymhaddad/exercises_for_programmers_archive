#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: import math and create empty list
import math

user_times = []
squared_value_list = []

# Step 2: create while loop
time_prompt = "Enter a number: "

active = True
while active:
    user_message = input(time_prompt)

    if user_message == 'done':
        active = False
    else: 
        user_times.append(user_message)

# Step 3: convert user_times list from string to ints and print the list of numbers
list_of_numbers_from_user = ', '.join(user_times)
print(f"Numbers: {list_of_numbers_from_user}")

user_times_in_integers = [int(time) for time in user_times]

# Step 4: complete calculations:
min_time_user_times_list = min(user_times_in_integers)
max_time_user_times_list = max(user_times_in_integers)

# find mean:
user_times_sum = sum(user_times_in_integers)
length_of_user_times_list = len(user_times_in_integers)
mean_user_times_list = user_times_sum / length_of_user_times_list

# find standard deviation:
for time in user_times_in_integers:
    diff_from_mean = time - mean_user_times_list
    squared_value = diff_from_mean ** 2
    squared_value_list.append(squared_value)

# calculate the mean of the squared values to find standard deviation
squared_values_sum = sum(squared_value_list)
len_of_squared_values = len(squared_value_list)
mean_of_squared_values = squared_values_sum / len_of_squared_values
square_root_of_mean = math.sqrt(mean_of_squared_values)

# Step 5: print results
print(f"The average is: {int(mean_user_times_list)}")
print(f"The minimum is: {min_time_user_times_list}")
print(f"The maxiumum is: {max_time_user_times_list}")
print("The standard deviation is: {:.2f}.".format(square_root_of_mean))
