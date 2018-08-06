#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: get input on amount of money in euros
amount_of_euros = float(input("How much money in euros do you have? "))

#step2: get input about the exchange rate
euro_exchange_rate = float(input("What is the current euro exchange rate? "))

#step3: convert euro_echange_rate and dollar_exchange rate into decimals
decimal_euro_exchange_rate = euro_exchange_rate / 100

dollar_exchange_rate = 1.17
decimal_dollar_exchange_rate = dollar_exchange_rate / 100

#step4: calculate the new amount of money in US dollars
us_dollars = amount_of_euros * decimal_dollar_exchange_rate // decimal_dollar_exchange_rate

#step5: print output
print(f"You have {amount_of_euros} euros at an exhange rate of {euro_exchange_rate}, which is ${us_dollars} US dollars.")
