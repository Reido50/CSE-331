'''
Reid Harry
1/17/2021

Exercise 4: Write a function that takes a 2-dimensional list as input, and returns 
a 1-dimensional list of the same elements.

Examples:

[[],
 [1, 2, 3],
 [2, 3, 4, 5]] -> [1,2,3,2,3,4,5]

[[]] -> []
'''

from typing import List, Any

def exercise4(data: List[List[Any]]) -> List[Any]:
    """
    param data: a list of basic types
    return: `data`, with duplicates removed
    """

    newData = []

    # Appends all elements in all sub-lists into newData
    for subList in data:
        for item in subList:
            newData.append(item)

    return newData
    