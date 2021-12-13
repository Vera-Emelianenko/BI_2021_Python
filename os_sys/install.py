#!/usr/bin/env python

import shutil
import sys
import os

system_path = sys.path[2]

for file in os.listdir():
    if file.endswith(".py") and 'install.py' not in file:
        shutil.copy2(file, os.path.join(system_path, file))
