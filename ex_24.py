#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: print directions
print("Enter two strings and I'll tell you if they are anagrams:")

# Step 2: get input from user on two words
user_string_1 = input("Enter string one: ")
user_string_2 = input("Enter string two: ")

# Step 3: write a function to see if the words are anagrams
def is_anagram(word_1, word_2):
    """Compare two strings to determine if they are anagrams"""
    word_1_length = len(word_1)
    word_2_length = len(word_2)

    if word_1_length == word_2_length:
        sorted_word_1 = sorted(word_1)
        sorted_word_2 = sorted(word_2)
        if sorted_word_1 == sorted_word_2:
            print(f"\'{word_1}\' and \'{word_2}\' are anagrams.")
    else:
        print(f"\'{word_1}\' and \'{word_2}\' are not anagrams.")

        
user_input = is_anagram(user_string_1, user_string_2)
