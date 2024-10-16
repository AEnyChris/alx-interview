#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n) -> int:
    """returns the minimum number of operations"""
    if n <= 1 or type(n) != int:
        return 0


    def isPrime(n: int) -> bool:
        """
        checks if a number is a prime numnber: bool
        """
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    prime_numbers = []
    prime_factors = []
    quotient = n
    for i in range(2, n):
        if isPrime(i):
            prime_numbers.append(i)
    while not isPrime(quotient):
        if quotient % min(prime_numbers) == 0:
            quotient = quotient//min(prime_numbers)
            prime_factors.append(min(prime_numbers))
        else:
            prime_numbers.pop(prime_numbers.index(min(prime_numbers)))
    prime_factors.append(quotient)
    return sum(prime_factors)
