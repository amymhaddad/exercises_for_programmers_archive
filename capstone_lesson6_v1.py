#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: Create constant
TOTAL_MINUTES = 123

total_hours = TOTAL_MINUTES // 60

leftover_minutes = TOTAL_MINUTES % 60

print(f"Hours:\n{total_hours}\nMinutes:\n{leftover_minutes}")
