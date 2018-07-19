#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: state constants
EC_RES_TAX = 0.005
DUNN_RES_TAX = 0.004
IL_SALES_TAX = 8 

#step1: get input from user
order_amount = float(input("Enter the order amount:$"))
state = input("Enter the state you reside in. Use abbreviations (eg, OH or MA): ")
county = input("Enter the county you live in: ")

#step2: set up first conditional
if "WI" in state or "wi" in state: 
    if county == "Eau Clair" or county == "eau clair":
        total_amount_ecres = order_amount + EC_RES_TAX
        print("You have an extra tax of " + str(EC_RES_TAX) + ". So the total order amount is ${:.2f}.".format(total_amount_ecres))
    elif county == "Dunn" or county == "dunn":
        total_amount_dunnres = order_amount + DUNN_RES_TAX
        print("You have an extra tax of " + str(DUNN_RES_TAX) + ". So the total order amount is ${:.2f}.".format(total_amount_dunnres))
    else: 
        print("Your total amount due is ${:.2f}.".format(order_amount))

#step3: set up second conditional
elif "IL" in state or "il" in state:
    il_tax_calculation = IL_SALES_TAX / 100 * order_amount
    il_order_with_tax = il_tax_calculation + order_amount
    print("The sales tax for IL residents is " + str(IL_SALES_TAX) + "%. The total with tax is ${:.2f}.".format(il_order_with_tax))

#step4: set up third conditional
else:
    print("Your total amount due is ${:.2f}".format(order_amount))