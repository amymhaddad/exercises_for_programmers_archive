#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: state constant
WI_TAX_PERCENT = 5.5

#step2: get inputs from user on order amount and state
order_amount = float(input("Enter the order amount:$"))
state = input("What state do you live in? Enter the state abbreviation (eg, MA): ")
normalized_state = state.lower()

#step3: set up first conditional to see if user lives in WI
if normalized_state == "wi":
    print(f"You're a Wisonsin resident, and will be charged a tax of {WI_TAX_PERCENT}%.")
    tax_amount = WI_TAX_PERCENT / 100 * order_amount
    total_with_tax = tax_amount + order_amount
    print("Your order amount before tax is ${:.2f}".format(order_amount)+", but with tax your grand total is ${:.2f}.".format(total_with_tax))
#step4: set up conditional for users who don't live in WI
else: 
    print("You're not a Wisconsin resident, so your total is ${:.2f}.".format(order_amount))
