#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: set up story
print("Jim is planning a trip to Ireland and we're going to find out all about it.")

#step2: get input from user
time = int(input("How many months are you going to stay in Ireland? "))

#step3: conditional statements to determine how long Jim will stay in Ireland
if time >= 2:
    print("Jim's staying a few months in Ireland.")
    if time == 3:
        print("Three months is the maximum time he can spend in Ireland without a visa.")

elif time == 1:
    print("Jim's staying one month in Ireland.")

elif time == 0:
    print("Jim's staying a few weeks in Ireland.")

else:
    print("Jim wants to move to Ireland forever!")

print("Jim loves the food in Ireland.")

#step4: set up conditional statements to find out the food Jim likes in Ireland
food = input("What food do you like the best in Ireland? ")

if "lamb" in food:
    print("The lamb is always fresh in Ireland because there are so many sheep!")

if "soda bread" in food: 
    print("Ireland is known for their soda bread.")
    bread_consumption = input("Do you eat soda bread each day, yes or no? ")
    if "yes" in bread_consumption:
        print("Jim's going to learn how to make soda bread because he eats it all of the time!")

if "cheese" in food: 
    print("Dublin has the best cheddar cheese.")

#step4: set up conditional statements to find out about working in Ireland
work = input("Do you work in Ireland? ")

if "yes" == work:
    print("It's nice to work remotely.")

elif "yes" != work:
    print("An extended vacation without worrying about work -- how nice!")

print("Jim has plenty of time for fun stuff, too!")

#step5: set up conditional statement to find out about activies in Ireland
activities = input("What's your favorite activity in Ireland? ")

if "hiking" in activities:
    print("There are many great hiking spots in Ireland.")
    number_hikes = int(input("How many hikes do you complete each week? "))
    if number_hikes == 5:
        print("Jim's an avid hiker!")
    elif number_hikes == 3:
        print("Jim hikes regurarly.")
    else: 
        print("Jim hikes when he can.")
   
elif "sightseeing" in activities:
    print("Jim likes the tourist spots!")

else:
    print("There's too many activities to pick a favorite! ")

#step6: set up last conditional statements to find out about future travel
future_travel = int(input("On a scale from 1 to 10, how likely are you to travel to another country for an extended time? "))

if future_travel >= 8:
    print("He's got the travel bug.")
    next_country = input("Where to next? ")

elif future_travel < 8 and future_travel > 5:
    print("Jim may travel again in the future, but he's ready to go home.")

else: 
    print("Jim's going to stay put in Boston, where he's from.")