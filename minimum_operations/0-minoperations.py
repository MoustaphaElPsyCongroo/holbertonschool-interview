#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write a
method that calculates the fewest number of operations needed to result in
exactly n H characters in the file."""
from math import sqrt


def minOperations(n):
    number_operations = 0
    while n != 1:
        n, divider_operations = calc_highest_divider(n)
        number_operations += divider_operations
    return number_operations


def calc_highest_divider(num):
    """Find the highest divider of a number

        Return: The number of operations to obtain this divider
    """
    num_operations = num
    highest_divider = 1
    if num < 0:
        return (1, 0)
    for i in range(2, round(sqrt(num)) + 1):
        if num % i == 0:
            highest_divider = num // i
            num_operations = i
            break
    return (highest_divider, num_operations)
