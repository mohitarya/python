""" Day-3, Problem-2
    Write a Python program to check the validity of password input by users. 
    Validation :

    At least 1 letter between [a-z]
    At lease 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
"""
import re

string = """Password should satisfy the following conditions:
            1. At least 1 letter between [a-z]
            2. At lease 1 letter between [A-Z]
            3. At least 1 number between [0-9]
            4. At least 1 character from [$#@]
            5. Minimum length 6 characters
            6. Maximum length 16 characters.
            """

username = raw_input("Please input the user name::\t")

password = raw_input("Input the password for {0}::\t".format(username))

short_len = len(password) < 6

large_len = len(password) > 16

l_alpha_error = re.search(r"[a-z]", password) is None

U_alpha__error = re.search(r"[A-Z]", password) is None

number_error = re.search(r"[0-9]", password) is None

special_char_error = re.search(r"[$#@]", password) is None

if short_len or large_len or l_alpha_error or U_alpha__error or number_error or special_char_error:
    print "!!Wrong Password!!"
    print string
else:
    print "Password is correct"

