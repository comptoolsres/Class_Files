#!/usr/bin/env python3

# A modified version of script using argparse and writing output to file
 
import argparse

parser = argparse.ArgumentParser(
            description="Count the Subject: lines in a mbox file")
parser.add_argument("file", 
            help="File to count Subject: lines")
parser.add_argument("output",
            help="File to ouptut results to")
args=parser.parse_args()



try:
    fhand = open(args.file)
except:
    print('File cannot be opened:', args.file)
    exit()


try:
    out_file = open(args.output, 'a')
except:
    print('File cannot be opened for output:', args.output)
    exit()


count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
result=" ".join(['There were', str(count), 'subject lines in', args.file])
out_file.write(result)
print(result)
