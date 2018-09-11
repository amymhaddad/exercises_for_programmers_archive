#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import random

contestants = []

while True:
    contestant_name = input("Enter a name: ")
    if contestant_name == ' ':
        random_winner = random.randint(0, len(contestants)-1)
        winner = contestants[random_winner]
        print(f"The winner is {winner.title()}.")
        break
    else:
        contestants.append(contestant_name)
        
