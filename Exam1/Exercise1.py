# Reid Harry
# 2/9/2021

from typing import List, Dict, Tuple

def exercise1(data: List[Dict[str, int]]) -> Tuple[Dict[str, int], str]:
    """
    Merges a list of dictionaries into one dictionary, and returns a tuple
    where the first element is the merged dictionary, and the second is
    the key with largest associated value
    data: A list of dictionaries
    return: A tuple, where the first element is a dictionary, and the second is a str
    """
    # Init new dictionary
    newDict = {}

    # Init max value
    max = None

    # Iterate over data
    for d in data:
        # Iterate over d
        for key in d:
            # Add or increment key/value into newDict
            if newDict.get(key) == None:
                newDict[key] = d[key]
            else:
                newDict[key] += d[key]

            # Check if new max
            if max is None:
                max = key
            elif newDict[key] > newDict[max]:
                max = key
            
    return (newDict, max)
