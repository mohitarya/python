""" Day2, Program-5
    Perform below operations on string - ' Welcome to calsoft \n':
    i) Print a string with all letters in upper case
    ii) Print the string such that first word
        of string is in capital letter [Hint:
        Use string concatination and slicing]
    iii) Print the string, remove additional
         spaces at the start/end, new line
         character from string.
    iv) Replace word 'Calsoft' in string with word
        'Python training' and print.[Hint: Use string
        concatination and slicing]
"""
test_str = ' Welcome to calsoft \n'

print "Str in Normal case::\n{0}".format(test_str)

# String in upper case

print "Str in upper case::\n{0}".format(test_str.upper())

# First word of string in Capital letters

split_str = test_str.split()

split_str[0] = split_str[0].upper()

print "First word in capital::\n{0}".format(' '.join(split_str))

print "String after strip::\n{0}".format(test_str.strip())

print "String after replacing calsoft with Python Traning::\n{0}".format(test_str.replace('calsoft', 'Python Traning'))
