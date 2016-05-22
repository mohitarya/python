""" Day3, Program-3
    Write a program  to print the numbers which can be
    divisible by 5 and 7 between 0 and n in comma separated 
    form while n is input by console.

"""

max_limit = raw_input("Input the max_limit for the range::\t")

# A number divisible by 5 and 7 have to be
# in the multiple of 35
max_num_div_35 = int(max_limit)/35

list_num = [x*35 for x in range(1, (max_num_div_35 + 1))]

print "Following are the numbers in range 0 to {0}".format(max_limit)
print "\t{0}".format(list_num)
