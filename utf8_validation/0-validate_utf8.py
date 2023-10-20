#!/usr/bin/python3
"""
Main file
"""


def validUTF8(data):
    bit = 0

    for elem in data:
        if bit > 0:
            bit -= 1
            if (((elem & 255) >> 6) != 2):
                return False
        elif (elem & 128) == 0:
            bit = 0
        elif (elem & 224) == 192:
            bit = 1
        elif (elem & 240) == 224:
            bit = 2
        elif (elem & 248) == 240:
            bit = 3
        else:
            return False

    return not bit
