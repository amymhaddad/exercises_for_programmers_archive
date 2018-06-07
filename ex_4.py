#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:22:10 2018

@author: amyhaddad
"""
print("This is exercise 4.")
print("""
Here are the instructions:
Create a simple mad-lib program that prompts 
for a noun, a verb, an adverb, and an adjective 
and injects those into a story that you create.
""")

noun = input("What's your favoriate animal? ")
verb = input("What's one activity you enjoy with your {}? ".format(noun))
adjective = input("What color is your {}? ".format(noun))
adverb = input("How fast does your {} move? ".format(noun))


print(f"Do you walk your {adjective} {noun} {adverb}? That's hilarious!")
