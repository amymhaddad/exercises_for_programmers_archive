#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: import random and create empty list
import random

contestants = []

# Step 2: write while loop
contestant_prompt = "Enter a name: "

active = True
while active:
    message = input(contestant_prompt)

    if message == ' ':
        random_contestant = random.randint(0, len(contestants)-1)
        select_winner = contestants[random_contestant]
        print(f"The winner is {select_winner.capitalize()}.")
        active = False
    else:
        contestants.append(message)
