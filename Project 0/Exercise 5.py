'''
Reid Harry
1/17/2021

In python, when passing an object to a function, all objects that are not primitive 
types are passed by reference. Understanding this is incredibly important to understanding 
the content of CSE 331. This can be seen in many contexts - e.g. In the snippet below, 
`a` and `b` reference the same list. Modifying one modifies the other:

a = [1, 2, 3]

b = a

b.append(4)

print(a)

>> [1, 2, 3, 4]

Exercise 5: Write a function that takes as input a 2-dimensional list, and produces a 
deep copy of that list.

The final result and the input should be referentially independent - you should be able 
to modify one, at any level, without modifying the other. This should also be achieved 
without using any import statements.
'''

from typing import List, Any

def exercise5(data: List[List[Any]]) -> List[List[Any]]:
    """
    param data: a two dimensional list
    return: a referentially independent copy of that list
    """
    
    newData = []

    # Copies each element from each sublist into new sublists. Those are then copied into newData
    for subList in data:
        newSubList = []
        for item in subList:
            newSubList.append(item)
        newData.append(newSubList)
    
    return newData