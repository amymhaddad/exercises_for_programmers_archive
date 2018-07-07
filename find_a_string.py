#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#write variable for string and one for substring
string = "AAABBB CDCDCDCDCDCD eeee"
substring = "CDC"

#write line of code to find the number of times the substring is repeated
substring_frequency = string.count("CDC")

print(f"The subtring occurs {substring_frequency} times.")