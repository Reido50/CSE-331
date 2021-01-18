'''
Reid Harry
1/17/2021

Similarly to how lists may be nested within other lists, lists may be stored 
as the values within a dictionary.

Example:

{'a' : [1, 2, 3],
 'b' : [3, 4, 5],
 'c' : []}

Exercise 7: Suppose you work for a company which runs an online shop. You're 
given customer orders in the form of tuples, where the first element is a customer 
id (given as first name), and the second element is the product they have ordered. 
Write a function that processes a list of these tuples, building a dictionary 
where each customer is mapped to a list of products they have ordered.

This one definitely needs some examples...

[('alex', 'ham'), ('alex', 'shrubbery'), ('alex', 'chair'), ('brianna', 'goose'), 
('alex', 'picture frame'), ('brianna', 'goose care kit')]
->
{'alex' : ['ham', 'shrubbery', 'chair', 'picture frame'], 'brianna' : ['goose', 'goose care kit']} 

 

[]
->
{}
'''

from typing import List, Dict, Tuple

def exercise7(data: List[Tuple[str, str]]) -> Dict[str, List[str]]:
    """
    param data: a list of tuples
    return: a dictionary mapping customers to lists of orders
    """
    
    newData = {}

    # Populate newData with a conversion of the data list into a dictionary
    for t in data:
        if(newData.get(t[0]) == None):
            newData[t[0]] = [t[1]]
        else:
            newData[t[0]].append(t[1])

    return newData