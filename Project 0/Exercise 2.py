'''
Reid Harry
1/17/2021

Lists can store other lists, creating multidimensional arrays. These are 
often used in CSE 331.

Exercise 2: Write a function which takes as input a list of lists, and 
returns the minimal element of any list.

Examples:

[[1,2,3],
 [2,4],
 [],
 [5,3,4]] -> 1

[[]] -> None

[[],
 []] -> None
'''

from typing import List, Any

def FindMin(data: List[Any]) -> Any:
    """
    param data: input - a list of like objects
    return: minimal element of the list
    """
    currentMin = None
    
    # Finds minimum element
    for item in data:
        if(currentMin == None or item < currentMin):
            currentMin = item

    return currentMin

def exercise2(data: List[List[Any]]) -> Any:
    """
    param data: input - a 2d list
    return: minimal element of any sublist
    """
    currentMin = None

    # Finds minumum element of all the sub-lists
    for subList in data:
        testMin = FindMin(subList)

        if(testMin != None):
            if(currentMin == None or testMin < currentMin):
                currentMin = testMin

    return currentMin