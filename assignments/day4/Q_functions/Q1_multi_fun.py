""" Day4, Problem-1
    Write multiple functions with series of calls.
    Ex a calling b, b calling c and so on.
"""

def funC():
    """
    Description: It prints that the control
                 in function C
    """
    print "In func C"

def funB():
    """
    Description: It prints that the control
                 in function B 
    """
    print "In func B & calling func C"
    funC()

def funA():
    """
    Description: It prints that the control
                 in function A
    """
    print "In func A & calling func B"
    funB()

funA()
