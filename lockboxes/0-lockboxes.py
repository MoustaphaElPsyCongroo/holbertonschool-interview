#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    available_keys = []
    locked = {}

    for i, box in enumerate(boxes):
        if i == 0:
            available_keys.extend(box)
            continue
        if i in available_keys:
            available_keys = list(set(available_keys + box))
            for key in box:
                if key in locked:
                    available_keys = list(set(available_keys + locked[key]))
                    del locked[key]
        else:
            locked[i] = box

    if not locked:
        return True
    return False
