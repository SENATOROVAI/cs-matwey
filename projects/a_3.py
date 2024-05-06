"""Совпадение строк."""

import sys


num_a: str = input()
num_b: str = input()
num_c: int = 1
if len(num_a) != len(num_b):
    print("no")
    sys.exit(0)
for i in range(len(num_a)):
    if ord(num_a[i]) == ord(num_b[i]):
        num_c = num_c + 0
    else:
        num_c = num_c - 1

if num_c == 1:
    print("yes")
else:
    print("no")
