#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: given variable
total_minutes = 123

#step2: calculate total hours
total_hours = total_minutes // 60

#step3: calculate minutes
leftover_minutes = total_minutes % 60

#step4: print output
print(f"Hours:\n{total_hours}\nMinutes:\n{leftover_minutes}")
