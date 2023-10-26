#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list all the folders name under one directory and replace '-' with '_' in the folder name
import os

path = '/Users/sheldon/kaios/working-directory'
files = os.listdir(path)

for file in files:
    if os.path.isdir(os.path.join(path, file)):
        os.rename(os.path.join(path, file), os.path.join(path, file.replace('-', '_')))
        print(file)
        print(os.path.join(path, file))
        print(os.path.join(path, file.replace('-', '_')))
        print('------------------')
    else:
        print('Not a folder.')

# Path: change_folder_name.py