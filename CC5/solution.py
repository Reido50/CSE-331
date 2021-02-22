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
    leftStack = []
    leftOut = [0] * len(walls)
    for i in range(len(walls)):
        if not leftStack:
            leftStack.append(walls[i])
        else:
            if walls[i] > leftStack[len(leftStack)-1]:
                leftStack.pop()
                leftOut[i] += len(leftStack)
            else:
                leftStack.pop()
                leftOut[i] += leftOut[i-1]+1
            leftStack.append(walls[i])

    # Find all seen walls from the right
    rightStack = []
    rightOut = [0] * len(walls)
    for i in range(len(walls)-1, -1, -1):
        if not rightStack:
            rightStack.append(walls[i])
        else:
            if walls[i] > rightStack[len(rightStack)-1]:
                rightStack.pop()
                rightOut[i] += len(rightStack)
            else:
                rightStack.pop()
                rightOut[i] += rightOut[i+1]+1
            rightStack.append(walls[i])

    for i in range(len(walls)):
        output[i] = leftOut[i] + rightOut[i]

    return output

test = [5, 2, 1, 10, 8, 4, 11]
print(str(check_walls_cover(test)))