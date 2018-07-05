#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: get input for principal amount
principal_amount = int(input("Enter the principal amount: $ "))

#step2: get input for interest rate as a percent (ie, "15" and not ".15")
interest_rate = float(input("Enter the interest rate: "))

#step3: turn interest rate into decimal
interest_rate_as_decimal = (interest_rate/100) 

#step4: get input for length of time invested
years_invested = int(input("Enter the number of years invested: "))

#step5: calculate interest rate
end_amount = principal_amount * (1 + interest_rate_as_decimal * years_invested)

#step6: print statement
print(f"After {years_invested} years at {interest_rate} interest, the investment will be worth ${int(end_amount)}.")
