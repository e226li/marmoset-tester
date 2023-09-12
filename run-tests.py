#!/bin/python3

import glob
import subprocess
import os
import sys

# will break if there are namespace collisions

file_list = [x.rstrip(".case") for x in glob.glob(f"{os.path.dirname(__file__)}/**/*.case", recursive=True)]
file_only_list = [os.path.basename(x) for x in file_list]

if sys.platform == "win32":
    os.system("color") # enables ANSI escape characters, bug in Python

for file_name in glob.glob("*.c", recursive=False):
    if file_name.rstrip(".c") in file_only_list:
        should_continue = input(f"{file_name}; run (y/N)?").lower()
        if should_continue is not "y":
            continue
        subprocess.run(["gcc", "-std=c11", "-Wall", "-g", file_name], check=True)
        with open(next(x for x in file_list if file_name in x)) as f:
            to_run = f.read().split("\n\n")
            for x in to_run:
                return_data = subprocess.run(["./a.out"], input=x[0].rstrip(), capture_output=True).stdout
                print(f"\u001b[{31 + int(return_data.rstrip() == x[1].rstrip())}m{return_data}\u001b[0m")
