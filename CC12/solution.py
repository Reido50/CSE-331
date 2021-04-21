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
    catstr = [["" for i in range(len(dialogue))] for j in range(len(dialogue))]

    # First time population of the matrix
    for i in range(len(dialogue)):
        for j in range(len(dialogue)):
            if i == j:
                cat[i][j] = 0
                catstr[i][j] = dialogue[i]

    # Populate the matrix
    for i in range(1, len(dialogue), 1):
        for j in range(0, len(dialogue)-i, 1):
            s1 = cat[i+j-1][j] + len(dialogue[i+j]) + len(catstr[i+j-1][j])
            s2 = cat[i+j][j+1] + len(dialogue[j]) + len(catstr[i+j][j+1])
            cat[i+j][j] = min(s1 ,s2)
            cstr1 = catstr[i+j-1][j] + dialogue[i+j]
            cstr2 = dialogue[j] + catstr[i+j][j+1]
            catstr[i+j][j] = catstr[i+j-1][j] + dialogue[i+j]

    for a in cat:
        print(str(a))

    return cat[len(dialogue)-1][0]

#print(str(colonel_concat(["aaa", "aa", "a"])))
#print(str(colonel_concat(["a", "bbbb", "c"])))
print(str(colonel_concat(["a", "b", "cc", "ddd", "eeee", "fffff"])))