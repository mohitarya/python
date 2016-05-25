""" Day2, Program-8
    Write a simple program which take the input
    form user : Name , Age , Company Name , Address
    and then display those input on console. 
"""

name = raw_input('Input Name::>\t')
Age = raw_input('Age of the person::>\t')
company_name = raw_input('Company Name::>\t')
address = raw_input('Address::\t')

print "Input Values are::>\nname = {0}\nAge = {1}\ncompany_name = {2}\naddress = {3}".format(name, Age, company_name, address)
