#!/usr/bin/python3
"""A utf8 validation script"""

def validUTF8(data):
    """
    A function that validates a data set to be UTF8 comliant
    Returns True if valid else False
    """
    number_bytes = 0

    mask_1 = 1 << 7
    # print(f'mask_1: {mask_1}, bin of mask {bin(mask_1)}')
    mask_2 = 1 << 6
    # print(f'mask_2: {mask_2}, bin of mask {bin(mask_2)}')

    for i in data:

        mask_byte = 1 << 7
        # print(f'mask_byte: {mask_byte}, bin of mask {bin(mask_byte)}')

        if number_bytes == 0:
           # print(f'number_bytes: {number_bytes}')

            while mask_byte & i:
               # print(f'mask_byte & i: {mask_byte & i}')
                number_bytes += 1
                mask_byte = mask_byte >> 1
               # print(f'mask_byte end of while loop: {mask_byte}')
               # print(f'number_byte: {number_bytes}')

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
