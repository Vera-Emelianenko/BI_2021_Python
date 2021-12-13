#!/usr/bin/env python

# sort analog without options

import sys
import argparse

parser = argparse.ArgumentParser(description='Sort input')
parser.add_argument('file', default='', metavar='file', type=str, nargs='*', help='file to be processed')

args = parser.parse_args()

if args.file:
    with open(args.file[0], 'r') as input_file:
         input = input_file.readlines()
else:
    input = sys.stdin.readlines()

sorted_list = sorted(input)

for item in sorted_list: 
    print(item, end = '')
