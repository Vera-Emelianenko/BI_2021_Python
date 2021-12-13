#!/usr/bin/env python

# wc analog with options -l -w- c

import sys
import argparse

parser = argparse.ArgumentParser(description='Count lines')
parser.add_argument('-l', default=False, action='store_true', help='print the line counts')
parser.add_argument('-w', default=False, action='store_true', help='print the word count')
parser.add_argument('-c', default=False, action='store_true', help='print the byte count')
parser.add_argument('file', default='', metavar='file', type=str, nargs='*', help='file to be processed')

args = parser.parse_args()

lines = 0
words = 0
bytes = 0

if args.file:
    with open(args.file[0], 'r') as input_file:
        input = input_file.readlines()
else:
    input = sys.stdin

for line in input:
    if args.l:
        lines += 1
    if args.w:
        words += len(line.split())
    if args.c:
        bytes += len(line.encode('utf-8'))

if args.l:
    print(lines)
if args.w:
    print(words)
if args.c:
    print(bytes)
