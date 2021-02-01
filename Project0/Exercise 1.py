'''
Reid Harry
1/17/2021

Python has several basic data types: integers, floating point numbers, strings, and booleans 
(which are a subclass of integers). Integers and floating point numbers are unbounded, and 
strings can be indexed as if they were character arrays. These fundamental data types, as well 
as any other object, can be stored in python's lists. Lists are, in many ways, the fundamental 
data structure of the language.

Exercise 1: Write a function which returns the maximum of an input list. For this exercise,
and each subsequent exercise, use the 'starter code' provided.

Examples:

[1, 2, 3, 5, 2, 1] -> 5

[-1, -2, 0] -> 0

['a', 'b'] -> 'b'

[] -> None
'''

from typing import List, Any

# do not modify function declaration

"""
You'll notice that in the function declaration, parameter `data` is given as
`data: List[Any]`. This is an example of type hinting. The type of `data` is 
a list containing elements of type `Any`. The return type of the function is given
by `-> Any`, indicating return type `Any`
"""


def exercise1(data: List[Any]) -> Any:
    """
    param data: a list of like objects
    return: maximal element of `data`
    """
    currentMax = None

    # Finds maximum element
    for item in data:
        if(currentMax == None or item > currentMax):
            currentMax = item

    return currentMax
