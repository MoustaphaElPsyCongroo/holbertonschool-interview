#!/usr/bin/python3
"""Determines if a given data set represents a valid UTF-8 encoding"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Returns true if data is a valid utf-8 encoding"""
    bytes_nb = 0

    for num in data:
        if bytes_nb == 0:
            if num < 128:
                bytes_nb = 0
            elif 192 <= num < 224:
                bytes_nb = 1
            elif 224 <= num < 240:
                bytes_nb = 2
            elif 240 <= num < 248:
                bytes_nb = 3
            else:
                return False
        else:
            if 128 <= num < 192:
                bytes_nb -= 1
            else:
                return False

    return bytes_nb == 0
