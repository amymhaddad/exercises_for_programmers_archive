#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

a = "Eat Work Play Sleep repeat"

print("Here's option 1:")
index_work = a[4:8:1] + "ing"
index_play = a[9:13:1] + "ing"

print(index_work.lower(), index_play.lower())

print("Here's option 2:")
working_playing = a.replace("Eat Work Play Sleep repeat", "working playing")
print(working_playing)

print("Here's option 3:")
a1 = a.replace("Eat ", "")
a2 = a1.replace(" Sleep repeat", "").lower()
a3 = a2.replace("work play", "working playing")
print(a3)