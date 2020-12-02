#!/usr/bin/env python

# square.py: Demo of argparse

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=float)
args = parser.parse_args()
print(f"The square of {args.square} is {args.square**2}")
