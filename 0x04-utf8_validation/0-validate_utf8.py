#!/usr/bin/python3
"""validate utf8"""


def validUTF8(data):
    """
    checks if a set of data is utf8 valid
    Return: boolean
    """
    mask = 1 << 7
    leading_bits = 0
    for byte in data:
        # print(f'checking byte: {byte}')
        byte = byte & 0xFF
        mask_byte = mask

        if byte < 0x7f:
            continue
        # check leading bits of utf8 bytes
        if leading_bits == 0:
            while mask_byte & byte:
                leading_bits += 1
                # print(f'\tleading_bits: {leading_bits}')
                mask_byte = mask_byte >> 1

            if leading_bits == 1 or leading_bits > 4:
                # print('\tchecking leading bits')
                return False

        else:
            if not (byte & mask and not (byte & (mask >> 1))):
                # print('\tchecking for continuation byte')
                return False

        leading_bits -= 1
    if leading_bits != 0:
        return False
    return True
