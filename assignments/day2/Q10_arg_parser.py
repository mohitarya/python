""" Day2, Program10
    Write a program which accept three positional
    parameter (--debug,--info,--error) and base on
    passed parameter display the parameter status
    "on" or "off".
"""
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help=" turn on the debugging ", action="store_true")
parser.add_argument("-i", "--info", help=" print info messages ", action="store_true")
parser.add_argument("-err", "--error", help=" print error messages", action="store_true")

args = parser.parse_args()

if args.debug:
    print "Debug = ON"
else:
    print "Debug = OFF"
if args.info:
    print "Info = ON"
else:
    print "Info = OFF"
if args.error:
    print "Error = ON"
else:
    print "Error = OFF"

