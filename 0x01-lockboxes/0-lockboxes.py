#!/usr/bin/python3
"""
This scripts implements the lockboxes task
Details:
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.

    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """returns true if all boxes can be opened"""
    n = len(boxes)
    if n == 1 or not boxes:
        return True

    key_store = []
    queue = [0]
    while queue:
        temp_q = []
        for key in set(queue):
            if key not in key_store and key < n:
                temp_q.extend(boxes[key])
                key_store.append(key)
        queue = temp_q
    if len(key_store) == n:
        flag = True
    else:
        flag = False
    return flag
