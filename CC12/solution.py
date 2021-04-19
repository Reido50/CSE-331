"""
Your Name Here
CC12 - Dynamic Programming
CSE 331 Spring 2021
Professor Sebnem Onsay
"""

from typing import List


def colonel_concat(dialogue: List[str]) -> int:
    """
    Find out how many copies it will take in optimal concatination
    :param dialogue: List of strings to concatenate
    :return: Mininum number of copies to concatenate the string
    """
    # Create the matrix to hold how many copies
    # Help from: https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
    cat = [[float("inf") for i in range(len(dialogue))] for j in range(len(dialogue))]

    # First time population of the matrix
    for i in range(len(dialogue)):
        for j in range(len(dialogue)):
            if i == j:
                cat[i][j] = 0

    # Populate the matrix
    for i in range(1, len(dialogue), 1):
        for j in range(0, i, 1):
            cat[i][j] = str(i) + str(j)

    print(str(cat))


colonel_concat(["a", "bb", "ccc"])