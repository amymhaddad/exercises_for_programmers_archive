#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

import math 

# Get input from user
credit_card_balance = int(input("Enter your credit card balance: $"))
apr = int(input("Enter the APR as a percent: "))
monthly_payment = int(input("Enter your monthly payment: $"))
apr_as_decimal = apr / 100
apr_daily_rate = apr_as_decimal / 365

def calc_months_until_paid_off(credit_card_balance, apr, monthly_payment):
    """Write a function to determine the number of months until credit card is paid off"""

    number_of_months_to_pay_cc = (-(1 / 30) * \
                                math.log(1 + credit_card_balance / monthly_payment * (1 - (1 + apr_daily_rate) ** 30)) / math.log(1 + apr_daily_rate))
    
    print("It will take you {:.2f}".format(number_of_months_to_pay_cc) + " months to pay off your credit card.")

calc_months_until_paid_off(credit_card_balance, apr, monthly_payment)
