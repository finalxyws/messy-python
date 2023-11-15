#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list all the folders and files name under one directory and replace '-' and blank if there is with '_' in the
# folder name
import os
import sys
import re


def change_folder_name(path):
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if re.search(r'[\s-]', dir):
                new_dir = dir.replace(' ', '_').replace('-', '_')

                os.rename(os.path.join(root, dir), os.path.join(root, new_dir))
                print('change folder name from %s to %s' % (dir, new_dir))
        for file in files:
            if re.search(r'[\s-]', file):
                new_file = file.replace(' ', '_').replace('-', '_')

                os.rename(os.path.join(root, file), os.path.join(root, new_file))
                print('change file name from %s to %s' % (file, new_file))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        change_folder_name(sys.argv[1])
    else:
        print('Usage: %s path' % sys.argv[0])
        sys.exit(1)

# Path: com/functionality/change_file_name.py
