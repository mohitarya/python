""" Problem 1
    Iterate over dictionaries using for loops

"""
server_dict = {"server1": "10.0.0.1",
                "server2": "10.0.0.2",
                "server3": "10.0.0.3",
                "server4": "10.0.0.22"
                }
#iterating over dictionary using for loop and 
#printing key and elements one by one

for key, value in server_dict.items():
    print "key = {0}, value = {1}" .format(key, value)
