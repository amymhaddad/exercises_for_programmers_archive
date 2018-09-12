#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""


import math 

def calc_months_until_paid_off(*months_to_pay_cc):
    """Write a function to determine the number of months until credit card is paid off"""

    # Get input from user
    credit_card_balance = int(input("Enter your credit card balance: $"))
    apr = int(input("Enter the APR as a percent: "))
    monthly_payment = int(input("Enter your monthly payment: $"))

    # Calculate apr as a decimal and the apr daily rate
    apr_as_decimal = apr / 100
    apr_daily_rate = apr_as_decimal / 365

    # Calcuate number of months to pay off credit card
    top_of_calculation = math.log(1 + credit_card_balance / monthly_payment (1 - (1 - apr_daily_rate) ** 30))
    bottom_of_calculation = math.log(1 + apr_daily_rate)
    months_to_pay_cc = -1/30 * top_of_calculation / bottom_of_calculation

    return(months_to_pay_cc)

calc_months_until_paid_off(credit_card_balance, apr, monthly_payment)

# print statement
