#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: set constant
WI_TAX = 5.5

# Step 2: get input from user
order_amount = int(input("Enter the order amount:$"))
state = input("Enter your state (use state abbreviations): ")
normalized_state = state.lower()

# Step 3: write conditional
if normalized_state == "wi":
    tax = (WI_TAX / 100) * order_amount
    print("You're going to pay ${:.2f}".format(tax) + " in tax.")
    subtotal = order_amount + tax
    print("Your order total is ${:.2f}.".format(order_amount))
    print("Your subtotal is ${:.2f}.".format(subtotal))
else:
    print(f"Your subtotal is ${order_amount}.")
