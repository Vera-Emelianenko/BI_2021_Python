#!/usr/bin/env python

# ls analog with option -a

import os
import argparse

parser = argparse.ArgumentParser(description='List all files/directories in the directory')
parser.add_argument('-a', default=False, action='store_true', help='do not ignore entries starting with .')
parser.add_argument('directory', default='./', metavar='file', type=str, nargs='*', help='file to be processed, default ./')

args = parser.parse_args()
path = args.directory[0]
with os.scandir(path) as it:
    if args.a:
        for entry in it:
            print(entry.name)
    else:
        for entry in it:
            if not entry.name.startswith('.'):
                print(entry.name)
