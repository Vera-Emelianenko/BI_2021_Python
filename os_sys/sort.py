#!/usr/bin/env python

# ls analog with options -a

import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Count lines')
parser.add_argument('-a', default=False, action='store_true', help='do not ignore entries starting with .')
parser.add_argument('file', default='', metavar='file', type=str, nargs='*', help='file to be processed')

args = parser.parse_args()

if args.file:
    with open (args.file[0], 'r') as input_file:
         input = input_file.readlines()
else:
    input = sys.stdin

for line in input:
    if args.l:
        lines += 1
    if args.w:
        words+= len(line.split())
    if args.c:
        bytes+= len (line.encode('utf-8'))

if args.l:
    print(lines)
if args.w:
    print(words)
if args.c:
    print(bytes)
