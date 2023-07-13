#!/usr/bin/python3

import math
"""
 a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
"""

import math

def minOperations(n):
    if n == 1:
        return 0
    
    def helper(num):
        if num == 1:
            return 0
        
        operations = float('inf')
        for i in range(1, int(math.sqrt(num))+1):
            if num % i == 0:
                operations = min(operations, helper(i) + (num // i))
                operations = min(operations, helper(num // i) + i)
        
        return operations
    
    result = helper(n)
    return result if result != float('inf') else 0

