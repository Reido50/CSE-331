'''
Reid Harry
1/17/2021

Exercise 8: given a list of integers, and a target value, find two integers from distinct 
positions in the input list which sum to the target. Return their indices as a tuple.

Examples:

[1,2,3,4,5,6,7], target = 4 -> (0,2)

[-1,0,1], target = 0 -> (0,2)

[1,2], target = 5 -> None

Note: if multiple index pairs are valid, any may be returned.

Hint: There is an easy, but slow, solution, and a harder, but much faster, solution. The 
latter uses a dictionary.
'''

from typing import List, Tuple

def exercise8(data: List[int], target: int) -> Tuple[int, int]:
    """
    param data: a list of integers
    param target: the target value for integers to sum to
    return: a tuple where element 1 and element 2 sum to target
    """
    
    sums = {}

    for num1 in data:
        for num2 in data:
            sums[num1 + num2] = (num1, num2)

    return sums.get(target)