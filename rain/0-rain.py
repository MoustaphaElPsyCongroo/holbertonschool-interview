#!/usr/bin/python3
"""
0_main
"""


def rain(walls):
    n = len(walls)
    if n <= 2:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
         

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    total_water = 0
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        trapped_water = water_level - walls[i]
        total_water += trapped_water

    return total_water
