#!/usr/bin/env python3
#follow.py

import os
import time 
'''
A generator that yields lines being written to the end of the file.
'''
def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END) # Move file pointer 0 bytes from end of file
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        yield line