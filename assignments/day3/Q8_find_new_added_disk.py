""" Day3, Program-8
    Create Set A with members ('sda','sda1','sda2','sdb','sdc')
    Create Set B with members ('sda','sda1','sda2','sdb','sdc','sdd')
    Identify the newly added disk. 
"""

#Set A

setA = set(['sda', 'sda1', 'sda2', 'sdb', 'sdc'])
setB = set(['sda','sda1','sda2','sdb','sdc','sdd'])

print "Newly added or deleted disk is::"
print list(setB^setA)
