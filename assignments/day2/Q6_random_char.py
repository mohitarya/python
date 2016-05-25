""" Day2, Program-6
    Given a string "ABkl86df$^$", write a code to print
    any random character. [Hint: Use random module]
"""
import random

test_str = 'ABkl86df$^$'

for i in range(20):
    print random.choice(test_str)
