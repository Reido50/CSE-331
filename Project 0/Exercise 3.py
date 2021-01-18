'''
Reid Harry
1/17/2021

As we have seen, python lists can store duplicate entries.

Exercise 3: Write a function that takes a list (containing basic, like types) as input, 
and returns the list without any duplicate entries.

Examples:

[1,1,1,2,3] -> [1,2,3]

['cat', 'dog', 'cat'] -> ['cat', dog']

[] -> []

Note: don't worry about maintaining order
'''

from typing import List, Any

def exercise3(data: List[Any]) -> List[Any]:
    """
    param data: a list of basic types
    return: `data`, with duplicates removed
    """
    newData = []

    # Only appends unique elements from data into newData
    for item in data:
        found = False
        for newItem in newData:
            if(item == newItem):
                found = True
                break
        if(not found):
            newData.append(item)

    return newData
