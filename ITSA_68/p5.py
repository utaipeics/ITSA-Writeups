#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.rstrip()
    n = int(line)
    
    for i in range(0, 1<<n):
        gray = i^(i>>1)
        print("{0:0{1}b}".format(gray, n))
