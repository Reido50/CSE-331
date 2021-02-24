"""
Reid Harry
Coding Challenge 5
CSE 331 Spring 2021
Professor Sebnem Onsay
"""
from typing import List


def check_walls_cover(walls: List[int]) -> List[int]:
    """
    Please fill out this doc-string
    """
    output = [0] * len(walls)

    # Find all seen walls from the left
    left = []
    for i in range(len(walls)):
        if not left:
            left.append(walls[i])
        else:
            while left and walls[i] >= left[len(left)-1]:
                left.pop()
            output[i] += len(left)
            left.append(walls[i])

    # Find all seen walls from the right
    right = []
    for i in range(len(walls) - 1, -1, -1):
        if not right:
            right.append(walls[i])
        else:
            while right and walls[i] >= right[len(right)-1]:
                right.pop()
            output[i] += len(right)
            right.append(walls[i])

    return output
