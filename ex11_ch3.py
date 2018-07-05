#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: get input on amount of money in euros
amount_of_euros = int(input("How much money in euros do you have? "))

#step2: get input about the exchange rate
euro_exchange_rate = float(input("What is the current euro exchange rate? "))

#step3: write calculation to convert the euros to US dollars
dollar_exchange_rate = 1.17

conversion_euros_to_dollars = (amount_of_euros * euro_exchange_rate) / dollar_exchange_rate
rounded_conversion = round(conversion_euros_to_dollars)

#step4: print a statement with number of euros, euro exchange rate and the amount in US dollars
print(f"You have {amount_of_euros} euros at an exhange rate of {euro_exchange_rate}, which is about ${rounded_conversion} US dollars.")
