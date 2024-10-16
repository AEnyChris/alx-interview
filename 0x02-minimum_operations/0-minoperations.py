#!/usr/bin/python3
"""The minimum operations challenge"""


def minOperations(n):
    """
    Computes the minimum operations to get n H
    """
    if (n < 2):
        return 0
    ops_sum, divisor = 0, 2
    while divisor <= n:
        if n % divisor == 0:
            ops_sum += divisor
            n = n / divisor
        else:
            divisor += 1
    return ops_sum
