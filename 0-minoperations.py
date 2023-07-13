#!/usr/bin/python3

import math
"""
 a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    if n <= 1:
        return 0

    operations = [0] * (n + 1)
    for i in range(2, n + 1):
        operations[i] = float('inf')
        j = 1
        while j * j <= i:
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + (i // j))
                operations[i] = min(operations[i], operations[i // j] + j)
            j += 1

    return operations[n] if operations[n] != float('inf') else 0
