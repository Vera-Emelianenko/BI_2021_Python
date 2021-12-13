#!/usr/bin/env python

# rm analog with option -r

import sys
import os
import argparse

parser = argparse.ArgumentParser(description='List all files/directories in the directory')
parser.add_argument('-r', default=False, action='store_true', help='remove recoursively .')
parser.add_argument('file_or_dir', type=str, nargs='*', help='file to be deleted, default ./')

args = parser.parse_args()


def removal(dir):
    for file in dir:
        if not os.path.exists(file):
            sys.exit(f'rm.py: cannot remove {file}: file does not exist')
        if os.path.isdir(file):
            if not args.r:
                sys.exit(f'rm.py: cannot remove {file}: Is a directory')
            else:
                if any(os.scandir(file)):
                    removal([os.path.join(file, child) for child in os.listdir(file)])
                    print('removing ', file)
                    if os.path.exists(file):
                        os.removedirs(file)
                else:
                    os.removedirs(file)
        else:
            os.remove(file)


removal(args.file_or_dir)
