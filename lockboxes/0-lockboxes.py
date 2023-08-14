#!/usr/bin/python3
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
