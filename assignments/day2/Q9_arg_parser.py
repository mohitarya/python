""" Day2, Prorgam-9
    write a program which accept two positional
    parameter (Name and age) and parse that Name
    is string and age is int using argpasre and
    display the help message for each parameter.
"""
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("Name", help="Input the name")
parser.add_argument("age", help="Input the age", type=int)
args = parser.parse_args()
print(args.Name)
print(args.age)
