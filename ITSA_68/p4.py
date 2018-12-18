#!/usr/bin/env python3
import sys

def validate(s, sum_correct):
    sum = 0
    while s > 0:
        sum += s
        s //= 10
    return sum == sum_correct

for line in sys.stdin:
    line = line.rstrip()
    length = len(line)
    n = int(line)

    init_term = int(n * (-0.9) // (0.1 ** length - 1))

    # try until the first term is correct lol
    # we will try first term +- 10
    found = False
    for i in range(init_term - 10, init_term + 10):
        if validate(i, n) is True:
            found = True
            print(i)
    if found is False:
        print(-1)

