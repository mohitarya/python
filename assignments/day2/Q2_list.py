""" Day2, Program-2
    2) Create a simple list. Can you add integers and
       strings in the same string? Show with example.
"""
#Simple List
test_list = [1, 'Hello', 2, 'world']

print "List is::\n\t{0}".format(test_list)

#Addition element in a list

test_list.insert(2, 23)

print "List after insertion at position 2 is::\n\t{0}".format(test_list)

#Remove an item from the list

test_list.remove(23)

print "List after removing an element ::\n\t{0}".format(test_list)
