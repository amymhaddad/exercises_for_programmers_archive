#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: get input from user for two first and last names
full_name_1 = input("Enter one full name in the format FIRST LAST: ")

full_name_2 = input("Enter a second full name in the format FIRST LAST: ")

#step2: create variables to separate each first name and each last name

space1 = full_name_1.find(" ")
first_firstname = full_name_1[0:space1]
first_lastname = full_name_1[space1 + 1:]

space2 = full_name_2.find(" ")
second_firstname = full_name_2[0:space2]
second_lastname = full_name_2[space2+1:]

#step3: write a line of code to change the first letter of each name using index and use .replace
first_letter_firstname_name_1 = first_firstname[0]
first_letter_lastname_name_1 = first_lastname[0]

first_letter_firstname_name_2 = second_firstname[0]
first_letter_lastname_name_2 = second_lastname[0]

new_firstname = first_firstname.replace(first_letter_firstname_name_1, first_letter_firstname_name_2)
new_lastname = first_lastname.replace(first_letter_lastname_name_1, first_letter_lastname_name_2)
print(f"Here's the first new name option: {new_firstname} {new_lastname}")

#step4: write a line of code to swap the names using a tuple
swap_firstname = (first_firstname, second_firstname) = (second_firstname, first_firstname)
swap_lastname = (first_lastname, second_lastname) = (second_lastname, first_lastname)

#step4a: add the truples together so all objects are within one truple
swapped_name = swap_firstname + swap_lastname

#step4b: index the newly formed truple to form new first and last names for one name
swapped_new_first_name1 = swapped_name[0]
swapped_new_last_name1 = swapped_name[3]
swapped_first_and_lastname_v1 = (swapped_new_first_name1, swapped_new_last_name1)

swapped_new_firstname_name1 = swapped_first_and_lastname_v1[0]
new_lastname_name1 = swapped_first_and_lastname_v1[1]

#step4c: index the newly formed truple to form new first and last names for second name
swapped_new_first_name2 = swapped_name[1]
swapped_new_last_name2 = swapped_name[2]
swapped_first_and_lastname_v2 = (swapped_new_first_name2, swapped_new_last_name2)

swapped_new_firstname_name2 = swapped_first_and_lastname_v2[0]
swapped_new_lastname_name2 = swapped_first_and_lastname_v2[1]

print(f"Here's the second new name option: {swapped_new_firstname_name2} {swapped_new_lastname_name2}.")
