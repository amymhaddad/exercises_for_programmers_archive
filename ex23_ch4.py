#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

#step1: get input from user and turn input to lowercase
turn_key = input("Is the car silent when you turn the key? Enter \"yes\" or \"no\": ")
normalized_turn_key = turn_key.lower()

#step2: write first conditional based on answer from input
if turn_key == "yes":
    battery = input("Are the battery terminals corroded? Enter \"yes\" or \"no\": ")
    normalized_battery = battery.lower()
    if battery == "yes":
        print("Clean the terminals and try starting again.")
    else: 
        print("Replace the cables and try it again.")

#step3: write second conditional based on input from user
elif turn_key == "no":
    click_sound = input("Does the car make a clicking noise? Enter \"yes\" or \"no\": ")
    normalized_click_sound = click_sound.lower()
    if click_sound == "yes":
        print("Replace the battery.")
    elif click_sound == "no":
        crank = input("Does the car crank but fail to start? Enter \"yes\" or \"no\": ")
        normalized_crank = crank.lower()
        if crank == "yes":
            print("Check spark plug connections.")
        elif crank == "no":
            engine_performance = input("Does the engine start and then die? Enter \"yes\" or \"no\": ")
            normalized_engine_performance = engine_performance.lower()
            if engine_performance == "yes":
                fuel_injection = input("Does your car have fuel injection? Enter \"yes\" or \"no\": ")
                normalized_fuel_injection = fuel_injection.lower()
                if fuel_injection == "yes":
                    print("Get it in for service.")
                else: 
                    print("Check to ensure the choke is opening and closing.")