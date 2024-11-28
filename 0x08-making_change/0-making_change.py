#!/usr/bin/python3
"""
Making Change:
the minimum number of coins challenge
"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    count = 0
    s_coins = sorted(coins, reverse=True)
    balance = total
    for coin in s_coins:
        if coin > balance:
            continue
        count += balance // coin
        balance = balance % coin
        if balance == 0:
            return count
    return -1
