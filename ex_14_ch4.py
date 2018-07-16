#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: create constant
WI_RESIDENT_TAX = 5.5

#step2: get input from user for the total order amount
order_subtotal = float(input("Enter the total order amount: $"))

#step3: get input from user on the state
state = input("Enter the state you live in, using an abbreviation (eg, MA): ")

#step4: make tax calculation for WI resident
tax_amount = WI_RESIDENT_TAX / 100 * order_subtotal
total_amount_with_tax = order_subtotal + tax_amount

#step4: write if statement to determine if user's response is WI
if state == "WI":
    print("The WI sales tax is 5.5%")
    print("Your order subtotal is ${:.2f}".format(order_subtotal)+".")
    print("Your tax amount is ${:.2f}".format(total_amount_with_tax)+".")

if state != "WI":
    print("You're not a WI resident, so your total is ${:.2f}".format(order_subtotal)+".")