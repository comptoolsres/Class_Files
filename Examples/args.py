#!/usr/bin/python
# args.py: Domo of the sys.argv command line parsing

import sys

# Print number of arguments passed in
print (f'Number of arguments: {len(sys.argv)}')

# Loop through the arguments and print them
for arg in range(len(sys.argv)):
  print(f' Argument {arg} is: {sys.argv[arg]}')


