
import os
import sys

# Get the directory of the current file.
current_file_dir = os.path.dirname(os.path.realpath(__file__))

# Insert the current_file_dir in front of sys.path.
sys.path.insert(0, os.path.join(current_file_dir, '..'))

from model.package4.package5 import ClassE

if __name__ == '__main__':
    e = ClassE()
    e.do_stuff()
