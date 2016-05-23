""" Day3, Program-6
    Write a python program to accept the Host details (IP,Hostname,username,password,os_type) 
    and store all the details in a dictionary and perform following functions:
    Display the dictionary 
    Delete an entry from the dictionary.
    Add a new entry into the dictionary.
    Check whether a particular IP is present in the dictionary.
"""
host_dict = dict()
msg = """
        1. To add an entry type add
        2. To display the host dictionary type disp
        3. To delete an entry type del
        4. To find an IP type search
        5. To exit type exit
        """
while True:
    user_input = raw_input("{0}\n:::>".format(msg))
    if(user_input == 'exit'):
        break
    elif(user_input == 'add'):
        hostname = 'host' + str(len(host_dict) + 1)
        host_dict[hostname] = dict()
        host_dict[hostname]['IP'] = raw_input("Input Ip address:::>")
        host_dict[hostname]['Hostname'] = raw_input("Input hostname  :::>")
        host_dict[hostname]['username'] = raw_input("Input username  :::>")
        host_dict[hostname]['password'] = raw_input("Input password  :::>")
        host_dict[hostname]['os_type'] = raw_input("Input os_type   :::>")
        print "Entry added successfully"
        print host_dict
    elif(user_input == 'disp'):
        print host_dict
    elif(user_input == 'del'):
        print host_dict
        del_input = raw_input("Dictionary contains the following host entries\nPlease type hostname whose entry to remove:::>")
        try:
            del(host_dict[del_input])
            print host_dict
        except ValueError:
            print "Input is wrong"
    elif(user_input == 'search'):
        search_input = raw_input("Enter an IP to search:::>")
        for k, v in host_dict.iteritems():
            if search_input == v['IP']:
                print "IP found for host entry {0}".format(k)
                continue
        else:
            print "IP not found"
    else:
        print "!!!Wrong Input!!!, Please try again"
