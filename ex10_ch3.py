#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#create constant
SALES_TAX = 5.5

#step1: get input for price of item 1
item1_price = int(input("Enter the price of item 1: "))

#step2: get input for quantity of item 1
item1_quantity = int(input("Enter the quantity of item 1: "))

#step3: get input for price of item 2
item2_price = int(input("Enter the price of item 2: "))

#step4: get input for quantity of item 2
item2_quantity = int(input("Enter the quantity of item 2: "))

#step5: get input for price of item 3
item3_price = int(input("Enter the price of item 3: "))

#step6: get input for price of item 3
item3_quantity = int(input("Enter the quantity of item 3: "))

#step7: make calculations for each item (multiply quantity * cost) and calculate subtotal for all items
#item1 calculation
item1_total = item1_price * item1_quantity

#item2 calculation
item2_total = item2_price * item2_quantity

#item3 calculation
item3_total = item3_price * item3_quantity

#add calculation for each of the three items together
subtotal = item1_total + item2_total + item3_total

#step8: create calculation to determine sales tax
total_tax = float(SALES_TAX/100) * subtotal

#step9: add sales tax to subtotal
grand_total = total_tax + subtotal

#step10: print out all totals
print(f"""
Subtotal: ${subtotal}
Tax: ${total_tax}
Grand total: ${grand_total}
""")