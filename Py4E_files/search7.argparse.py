#!/usr/bin/env python3

# A modified version of script using argparse

import argparse

parser = argparse.ArgumentParser(
            description="Count the Subject: lines in a mbox file")
parser.add_argument("file", 
            help="File to count Subject: lines")
args=parser.parse_args()



try:
    fhand = open(args.file)
except:
    print('File cannot be opened:', args.file)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', args.file)
