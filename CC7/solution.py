"""
Your name here
Coding Challenge 7
CSE 331 Spring 2021
Professor Sebnem Onsay
"""
from __future__ import annotations  # allow self-reference
from typing import List, Optional


class TreeNode:
    """Tree Node that contains a value as well as left and right pointers"""
    def __init__(self, val: int, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


def rewind_combo(points: List[int]) -> List[Optional[int]]:
    """
    Returns a list of greatest smaller predecessors
    :param points: Python list of size n representing hit points
    :return: List of greatest smaller predecessors of points
    """
    # Create output list and root node
    output = []
    root = TreeNode(None)

    first  = True
    for p in points:
        # Init gsp of p
        gsp = None

        if first:
            # If first, init root value
            root.val = p
            first = False
        else:
            # If not first, find greatest smaller predecessor
            current = root
            while True:
                if p <= current.val:
                    # Traverse left if p is less than or equal current value
                    if current.left is None:
                        break
                    current = current.left
                else:
                    # Traverse right if p is greater than current value
                    gsp = current.val
                    if current.right is None:
                        break
                    current = current.right

            # Place p in the tree
            if p > current.val:
                current.right = TreeNode(p)
            elif p < current.val:
                current.left = TreeNode(p)
        # Add gsp to output array
        output.append(gsp)

    # Return output list
    return output
