#!/bin/python3

import glob
import subprocess
import os

# will break if there are namespace collisions

file_list = [x.rstrip(".case") for x in glob.glob(f"{os.path.dirname(__file__)}/**/*.case", recursive=True)]
file_only_list = [os.path.basename(x) for x in file_list]

for file_name in glob.glob("*.c", recursive=False):
    if file_name.rstrip(".c") in file_only_list:
        should_continue = input(f"{file_name}; run (y/N)?").lower()
        if should_continue is not "y":
            continue
        subprocess.run(["gcc", "-std=c11", "-Wall", "-g", file_name], check=True)
        with open(next(x for x in file_list if file_name in x)) as f:
            to_run = f.read().split("\n\n")
            for x in to_run:
                subprocess.run(["./a.out"], input="", capture_output=True)
