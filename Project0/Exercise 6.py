'''
Reid Harry
1/17/2021

An essential tool for 331, and for programming in python as a whole, is the dictionary. 
Often in other languages known as a map or associative array, the dictionary maps keys 
to values. As we will see later, dictionaries operate incredibly efficiently for common operations.

Exercise 6: Write a function which takes as input a dictionary, and returns an inverted 
dictionary where each key/value pair is reversed.

Example:

{'a':1, 'b':2} -> {1:'a', 2:'b'}
'''

from typing import Dict, Any

def exercise6(data: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    param data: a dictionary
    return: the input dictionary, but with each key/value pair flipped
    """
    
    newData = {}

    # Populates newData with reversed key and values of data
    for key in data:
        newData[data[key]] = key

    return newData