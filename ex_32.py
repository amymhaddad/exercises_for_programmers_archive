#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

# Step 1: import random
import random

# Step 2: create constants: 3 lists, one for each game level
LEVEL_1 = list(range(1, 10))
LEVEL_2 = list(range(1, 100))
LEVEL_3 = list(range(1, 1000))

GAME_LEVEL_PROMPT = "Which game level do you want to play?"
GAME_LEVEL_PROMPT += "\nType: 1, 2, or 3: "
USER_GUESS_PROMPT = "Guess the number: "
HIGH = "Your guess is too high. Try again."
LOW = "Your guess is too low. Try again."
REPEAT = "Type 'yes' to play again."

# Step 2: create while loop to intiate game
message = int(input(GAME_LEVEL_PROMPT))
    
if message == 1:
    print("Let's start the game.")
    create_random_number_level_1 = random.randint(0, len(LEVEL_1)-1)

    user_guess_number = 1
    active = True
    while active:
        level_1_user_guess = int(input(USER_GUESS_PROMPT))
        
        if level_1_user_guess == create_random_number_level_1:
            active = False
            if user_guess_number == 1:
                print(f"You guessed it in {user_guess_number} guess!")
            else:
                print(f"You guessed it in {user_guess_number} guesses!")

        if level_1_user_guess > create_random_number_level_1:
            print(f"{HIGH}: {user_guess_number}")
            user_guess_number += 1
        elif level_1_user_guess < create_random_number_level_1:
            print(f"{LOW} {user_guess_number}")
            user_guess_number += 1   
elif message == 2:
    print("Let's start the game.")
    create_random_number_level_2 = random.randint(0, len(LEVEL_2)-1)
    
    user_guess_number = 1
    active = True
    while active:
        level_2_user_guess = int(input(USER_GUESS_PROMPT))
        
        if level_2_user_guess == create_random_number_level_2:
            active = False
            if user_guess_number == 1:
                print(f"You guessed it in {user_guess_number} guess!")
            else:
                print(f"You guessed it in {user_guess_number} guesses!")

        if level_2_user_guess > create_random_number_level_2:
            print(f"{HIGH} {user_guess_number}")
            user_guess_number += 1
        elif level_2_user_guess < create_random_number_level_2:
            print(f"{LOW} {user_guess_number}")
            user_guess_number += 1 
else:
    print("Let's start the game.")
    create_random_number_level_3 = random.randint(0, len(LEVEL_3)-1)

    user_guess_number = 1
    active = True
    while active:
        level_3_user_guess = int(input(USER_GUESS_PROMPT))
        
        if level_3_user_guess == create_random_number_level_3:
            active = False
            if user_guess_number == 1:
                print(f"You guessed it in {user_guess_number} guess!")
            else:
                print(f"You guessed it in {user_guess_number} guesses!")

        if level_3_user_guess > create_random_number_level_3:
            print(f"{HIGH}: {user_guess_number}")
            user_guess_number += 1
        elif level_3_user_guess < create_random_number_level_3:
            print(f"{LOW} {user_guess_number}")
            user_guess_number += 1
