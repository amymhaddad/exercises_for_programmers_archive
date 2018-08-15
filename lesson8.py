#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:34:22 2018

@author: amyhaddad
"""

test_string = "Eat Work Play Sleep repeat"

# Option 1: using index
first_word_test_string = test_string[4:8]+"ing"
second_word_test_string = test_string[9:13]+"ing"
total_word_test_string = first_word_test_string.lower() + ' ' + second_word_test_string.lower()
print(total_word_test_string)

# Option 2: spliting the string and indexing it
new_phrase = test_string.split(' ')
word_one_new_phrase = new_phrase[1]+"ing"
word_two_new_phrase = new_phrase[2]+"ing"
both_words_new_phrase = word_one_new_phrase.lower() + ' ' + word_two_new_phrase.lower()
print(both_words_new_phrase)

# Option 3: using replace
task_1 = test_string.replace("Eat Work", "working")
task_2 = task_1.replace("Play", "playing")
task_3 = task_2.replace("Sleep repeat", " ")
print(task_3)
