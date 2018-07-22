#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 08:52:42 2018

@author: amyhaddad
"""

print("What is your favorite quote?", end= ' ')
quote = input()

print(f"Who said \"{quote}\"? ", end = ' ')
said = input()

print("{} said the quote \"{}.\" ".format(said, quote))
