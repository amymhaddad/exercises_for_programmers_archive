#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: ask user for input on bill amount
bill_amount = float(input("How much was your bill? "))

#step2: ask user for input on tip percentage
tip_percentage = int(input("How much will you tip? "))

#step3: convert tip to a decimal
tip_amount = tip_percentage/100 * bill_amount

#step4: add tip to bill amount
bill_with_tip = tip_amount + bill_amount

#step5: print statement to show tip amount and bill amount
print(f"The tip is ${int(tip_amount)} and the total bill with tip is ${int(bill_with_tip)}.")