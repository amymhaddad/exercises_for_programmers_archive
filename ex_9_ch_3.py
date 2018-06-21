#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import math

ceiling_length = int(input("What is the length of the ceiling in feet? "))
ceiling_width = int(input("What is the width of the ceiling in feet? "))

area_of_ceiling = ceiling_length * ceiling_width

paint_gallons_needed = math.floor(350/area_of_ceiling)

print(f"You'll need to purchase {paint_gallons_needed} gallons of paint to cover {area_of_ceiling} square feet.")