#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: get input: principal amount
principal_amount = int(input("Enter the principal amount: $"))

#step2: get input: interest rate -- and use float
annual_interest_rate = float(input("Enter the annual interest rate: "))

#step3: turn interst rate into a decimal
interest_rate_as_decimal = annual_interest_rate/100

#step4: get input: number of years the amount is invested for
years_invested = int(input("Enter the number of years the amount has been invested: "))

#step5: get input: number of times the interest is compounded each year
frequency_interest_compounded_yearly = int(input("Enter the number of times the interest is compounded each year: "))

#step6: write calculation to compute the value of investment compounded over time
investment_compounded_over_time = principal_amount *(1 + int(annual_interest_rate) / frequency_interest_compounded_yearly)**frequency_interest_compounded_yearly*years_invested

#step7: write a statement with values for each input
print(f"${principal_amount} invested at {annual_interest_rate}% for {years_invested} years compounded {frequency_interest_compounded_yearly} times per year is ${int(investment_compounded_over_time)}.")