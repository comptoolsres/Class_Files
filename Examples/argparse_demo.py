#!/usr/bin/env python

# argparse_demo.py: Demo of argparse
import sys
import argparse
import math

# Define a __version__ variable used below.
__version__ = '1.0'

parser = argparse.ArgumentParser(prog="Program to demonstrate different argparse features")

# Positional argument; no flag, will be last, after optional arguments.
# This example also adds checking the type of an argument.
parser.add_argument('square', help='Display a square of a given number',
                    type=float)

# Optional argument types

# Long, double-dash flag and short single-dash equivalent
parser.add_argument('--input', '-i', help="Name of input file, lines in file will be printed.") 

# Actions
# By defualt, the action is to store the value passed with the argument
# e.g. -i file.txt stores 'file.txt' as the value for --input.

# Some other actions (See docs for more options):
parser.add_argument('--pi', action='store_const',
                    help="Use constant value of 3.1415 for pi", 
                    const=3.1415)

parser.add_argument('--print', action='store_true',
                    help="Also print blank lines to screen?")

parser.add_argument('--verbose', '-v', action='count', default=0,
                    help='Verbosity level: pass multiple times to increase output level 0-2)')

parser.add_argument('--version', action='version',
                    help='Print version number',
                    version='%(prog)s. Version: ' + __version__)

# Setting default values that can be changed if passed

parser.add_argument('--times', '-t',
                    help='Number of times to print each line, default=1',
                    default=1)
# Parse the command line arguments
args = parser.parse_args()

if args.verbose > 0:
  print(f"Opening file {args.input}.")

# Open the file
try:
  file_handle=open(args.input, 'r')
except Exception as exception:
  print(f"Couldn't open {args.input}, {exception}. \nExiting")
  sys.exit() 

if args.verbose > 1:
  print(f"I made it this far, so {args.input} has been opened.")

for line in file_handle:
  line=line.strip()
  #ignore blank lines initially
  if not (len(line) == 0):
    print(line)
  # if --print was passed, print the blank lines
  elif args.print:
    print(line)

if args.verbose > 1 :
  print(f"Finished reading {args.input}.")


print(f"The square of {args.square} is {args.square**2}")

if args.pi:
  print(f"Pi is: {args.pi}")
else:
  print(f"Pi is: {math.pi}")

if args.verbose > 0:
  print("Done")

