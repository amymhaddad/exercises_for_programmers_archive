#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: create constant
DOLLAR_EXCHANGE_RATE = 1.17

#step2: get input on amount of money in euros
amount_of_euros = float(input("How much money in euros do you have? "))

#step3: get input about the exchange rate
euro_exchange_rate = float(input("What is the current euro exchange rate? "))

#step4: convert euro_echange_rate and dollar_exchange rate into decimals
decimal_euro_exchange_rate = euro_exchange_rate / 100

decimal_dollar_exchange_rate = DOLLAR_EXCHANGE_RATE / 100

#step5: calculate the new amount of money in US dollars
us_dollars = amount_of_euros * decimal_dollar_exchange_rate // decimal_dollar_exchange_rate

#step6: print output
print(f"You have {amount_of_euros} euros at an exhange rate of {euro_exchange_rate}, which is ${us_dollars} US dollars.")
