""" Day3, Problem-4
    write a program to output a random number,
    which is divisible by 5 and 7, between 0 and 201
    inclusive using random module and list comprehension. 
"""
import random

list_num = [x for x in range(0,202)]

while True:
    #generate a Random Number
    num = random.choice(list_num)
    if num%35 == 0:
        print "Random no genrated divisible by 5 and 7 are {0}".format(num)
        break
    else:
        continue
