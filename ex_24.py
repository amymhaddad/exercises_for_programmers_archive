#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

print("Enter two strings and I'll tell you if they're anagrams. ")

string1 = input("Enter one string: ")
string2 = input("Enter second string: ")


def isAnagram(string1, string2):
    """Test to see if string1 and string2 are anagrams"""

    length_of_string1 = len(string1)
    length_of_string2 = len(string2)

    if length_of_string1 != length_of_string2:
        print(f"{string1.title()} and {string2} are not anagrams.")
    else:
        sorted_string1 = sorted(string1)
        sorted_string2 = sorted(string2)
        if sorted_string1 == sorted_string2:
            print(f"{string1.title()} and {string2} are anagrams!")
        else: 
            print(f"{string1.title()} and {string2} are not anagrams.")

isAnagram(string1, string2)
