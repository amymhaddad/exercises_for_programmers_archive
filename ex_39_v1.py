#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# employee_names = ['john johnson', 'tou xiong', 'michaela michaelson', 'jake jacobson', 'jacquelyn jackson', 'sally weber']
# sorted_employee_names = sorted(employee_names)


# new_list_sorted_employee_names = []
    
# for name in sorted_employee_names:
#     new_list_sorted_employee_names.append(str(name))

employee_1 = {
    'first_name': 'tou',
    'last_name': 'xiong',
    'position': 'software engineer',
    'separation_date': '2016-10-05',
}

employee_2 = {
    'first_name': 'john',
    'last_name': 'johnson',
    'position': 'manager',
    'separation_date': '2016-12-31',
}

employee_3 = {
    'first_name': 'michaela',
    'last_name': 'michaelson',
    'position': 'district manager',
    'separation_date': '2015-12-19',
 }

employee_4 = {
    'first_name': 'jake',
    'last_name': 'jacobson',
    'position': 'programmer',
    'separation_date': ' ',
 }

employee_5 = {
    'first_name': 'jacquelyn',
    'last_name': 'jackson',
    'position': 'dba',
    'separation_date': ' ',
 }

employee_6 = {
    'first_name': 'sally',
    'last_name': 'weber',
    'position': 'web developer',
    'separation_date': '2015-12-18',
 }

employees = [employee_1, employee_2, employee_3, employee_4, employee_5, employee_6]

for employee in employees:
    if employee['position'] == 'dba':
        employee['position'] = "DBA"
    else: 
        employee_position = employee['position'].title()
    for employee_details in employee.values():
        employee_full_name = employee['first_name'].capitalize() + ' ' + employee['last_name'].capitalize()
        employee_separation_date = employee['separation_date']
        total_employees_details = employee_full_name + ' | ' + employee_position + ' | ' + employee_separation_date
    print(total_employees_details)
