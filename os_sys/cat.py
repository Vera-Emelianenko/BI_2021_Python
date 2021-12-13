#!/usr/bin/env python

# cat analog with no options

import argparse
import sys

parser = argparse.ArgumentParser(description='Print the contents of the file to the screen')
parser.add_argument('file', type=str, nargs='*', help='files to be printed')

args = parser.parse_args()
files = args.file

if args.file:
    for file in args.file:
        with open(file, 'r') as input_file:
            input = input_file.readlines()
            for line in input:
                print(line, end='')

else:
    input = sys.stdin
    for line in input:
        print(line, end='')
