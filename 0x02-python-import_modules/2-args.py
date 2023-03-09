#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1

if num_args == 0:
    print("Number of arguments: 0.")
    print(".")
else:
    print(f"Number of arguments: {num_args}.")
    if num_args == 1:
        print("Argument:")
    else:
        print("Arguments:")
    for i in range(num_args):
        print(f"{i+1}: {sys.argv[i+1]}")

