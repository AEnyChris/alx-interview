#!/usr/bin/python3
"""validate utf8"""


def validUTF8(data):
    """
    checks if a set of data is utf8 valid
    Return: boolean
    """
    mask = 1 << 7

    for byte in data:
        if byte < 0x7f:
            continue

        leading_bits = 0

        while mask & byte:
            leading_bits += 1
            mask = mask >> 1

        if leading_bits == 1 or leading_bits > 4:
            return False

        lsb = byte & mask

        if not(lsb & mask and not (lsb & (mask >> 1))):
            return False
    return True
