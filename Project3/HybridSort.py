"""
Name:
Project 3 - Hybrid Sorting
Developed by Sean Nguyen and Andrew Haas
Based on work by Zosha Korzecke and Olivia Mikola
CSE 331 Spring 2021
Professor Sebnem Onsay
"""
from typing import TypeVar, List, Callable

T = TypeVar("T")            # represents generic type


def merge_sort(data: List[T], threshold: int = 0,
               comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> int:
    """
    Perform a merge sort using a given comparator on a list of values and returns the inversion count
    :param data: List of items to be sorted
    :param threshold: The size of the data at which insertion sort should be used
    :param comparator: A function that compares two arguments and returns True if the first argument is less than or equal to the second and False otherwise
    """
    inversions = 0

    def merge(S1, S2, S) -> int:
        """
        Merge two sorted Python Lists S1 and S2 into properly sized list S
        :param S1: First list to be merged
        :param S2: Second list to be merged
        :param S: Resulting list of the merge
        """
        inversions = 0
        i = j = 0
        while i+j < len(S):
            if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
                S[i+j] = S1[i]
                i = i+1
            else:
                S[i+j] = S2[j]
                j = j+1
                inversions += 1
        return inversions
    
    n = len(data)
    if n < 2:
        return
    elif n < threshold:
        insertion_sort(data, comparator)
    mid = n // 2
    S1 = data[0:mid]
    S2 = data[mid:n]
    inversions += merge_sort(S1)
    inversions += merge_sort(S2)
    inversions += merge(S1, S2, data)
    return inversions

def insertion_sort(data: List[T], comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> None:
    """
    Perform an insertion sort using a given comparator on a list of values
    :param data: List of items to be sorted
    :param comparator: A function that compares two arguments and returns True if the first argument is less than or equal to the second and False otherwise
    """
    n = len(data)
    for j in range(1, n):
        i = j
        while (i > 0) and comparator(data[i], data[i-1]):
            data[i], data[i-1] = data[i-1], data[i]
            i -= 1
    pass


def hybrid_sort(data: List[T], threshold: int,
                comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> None:
    """
    REPLACE
    """
    pass

def inversions_count(data: List[T]) -> int:
    """
    REPLACE
    """
    pass


def reverse_sort(data: List[T], threshold: int) -> None:
    """
    REPLACE
    """
    pass


def password_rate(password: str) -> float:
    """
    REPLACE
    """
    pass

def password_sort(data: List[str]) -> None:
    """
    REPLACE
    """
    pass


data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
print(str(merge_sort(data)))
print(data)