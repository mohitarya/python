""" day4, Program-2
    Write 2 nested functions in a parent function
"""

def addMulFun(num1, num2):
    def add():
        return num1 + num2
    def mul():
        return num1 * num2
    
    print "addition = {0}, multiplication = {1}".format(add(), mul())

addMulFun(3, 4)
