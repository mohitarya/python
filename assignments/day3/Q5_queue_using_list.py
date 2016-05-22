""" Day3, Program-5
    Write a program implement Queue using lists.
"""
#intializing the list for queue

que_list = []

#Pushing the elements in queue
for i in range(0, 10):
    que_list.append(i)

print "Before poping list is:"
print que_list

#Poping an element from the list
print "poping element from the list"
print que_list.pop()

#After poping list becomes

print "After poping list is:"
print que_list
