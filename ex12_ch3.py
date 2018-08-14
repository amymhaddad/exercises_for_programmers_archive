#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step1: get input for principal amount
principal_amount = float(input("Enter the principal amount:$"))

# Step2: get input for interest rate as a percent (ie, "15" and not ".15")
interest_rate = float(input("Enter the interest rate: "))

# Step3: turn interest rate into decimal
interest_rate_as_decimal = (interest_rate / 100) 

# Step4: get input for length of time invested
years_invested = float(input("Enter the number of years invested: "))

# Step5: calculate interest rate
end_amount = principal_amount * (1 + interest_rate_as_decimal * years_invested)

# Step6: print statement
print(f"After {years_invested} years at {interest_rate} interest, the investment will be worth ${int(end_amount)}.")
