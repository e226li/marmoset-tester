#!/bin/python3

import glob
import subprocess
import os
import sys
import difflib

# will break if there are namespace collisions

if os.path.isfile("a.out"):
    raise FileExistsError # TODO: generate uuid .out

file_list = glob.glob(f"{os.path.dirname(__file__)}/**/*.cases", recursive=True)
file_only_list = [os.path.basename(os.path.splitext(x)[0]) for x in file_list]

if sys.platform == "win32":
    os.system("color") # enables ANSI escape characters, bug in Python

exit_code = 0
for file_name in glob.glob("*.c", recursive=False):
    if file_name.rstrip(".c") in file_only_list:
        should_continue = "y" if os.getenv("DEBIAN_FRONTEND") == "noninteractive" else input(f"{file_name}; run (y/N)? ").lower()
        if should_continue != "y":
            continue
        subprocess.run(["gcc", "-o", "a.out", "-std=c11", "-Wall", "-g", file_name], check=True)
        with open(next(x for x in file_list if os.path.splitext(file_name)[0] == os.path.basename(os.path.splitext(x)[0]))) as f:
            to_run = f.read().strip().split("\n\n")
            total_tests, passed_tests = 0, 0
            for x in to_run:
                x_split = x.split("\n", 1)
                return_data = subprocess.run(["./a.out"], input=x_split[0].rstrip().encode(), capture_output=True).stdout.decode().rstrip()
                test_passed_int = int([z.rstrip() for z in return_data.rstrip().splitlines()] == [z.rstrip() for z in x_split[1].rstrip().splitlines()])
                total_tests += 1
                passed_tests += test_passed_int
                print(f"\u001b[{31 + test_passed_int}m({x_split[0]})\u001b[0m")
                if not test_passed_int:
                    [print(x) for x in difflib.Differ().compare(x_split[1].splitlines(), return_data.splitlines())]
                else:
                    [print(x) for x in return_data.splitlines()]
            print(f"\u001b[32m{passed_tests} tests passed\u001b[0m, \u001b[{31 - 31*int(total_tests == passed_tests)}m{total_tests - passed_tests} tests failed\u001b[0m")
            exit_code += total_tests - passed_tests
            os.remove("a.out")

sys.exit(exit_code)