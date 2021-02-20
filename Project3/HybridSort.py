"""
Name:
Project 3 - Hybrid sorting
Developed by sean Nguyen and Andrew Haas
Based on work by Zosha Korzecke and Olivia Mikola
CsE 331 spring 2021
Professor sebnem Onsay
"""
from typing import TypeVar, List, Callable
import math

T = TypeVar("T")            # represents generic type


def merge_sort(data: List[T], threshold: int = 0,
               comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> int:
    """
    Perform a merge sort using a given comparator on a list of values and returns
    the inversion count
    :param data: List of items to be sorted
    :param threshold: The size of the data at which insertion sort should be used
    :param comparator: A function that compares two arguments and returns True if
    the first argument is less than or equal to the second and False otherwise
    :return: Number of inversions (only accurate if threshold is 0)
    """
    inversions = 0

    def merge(left, right, main) -> int:
        """
        Merge two sorted Python Lists s1 and s2 into properly sized list s
        :param s1: First list to be merged
        :param s2: second list to be merged
        :param s: Resulting list of the merge
        """
        inversions = 0
        i = j = 0
        while i+j < len(main):
            if j == len(right) or (i < len(left) and comparator(left[i], right[j])):
                main[i+j] = left[i]
                i = i+1
            else:
                main[i+j] = right[j]
                j = j+1
                inversions += (len(left)-i)
        return inversions

    length = len(data)
    if length < 2:
        return 0
    if length < threshold:
        insertion_sort(data, comparator)
    else:
        mid = length // 2
        left = data[0:mid]
        right = data[mid:length]
        inversions += merge_sort(left, threshold, comparator)
        inversions += merge_sort(right, threshold, comparator)
        inversions += merge(left, right, data)
    return inversions


def insertion_sort(data: List[T],
                   comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> None:
    """
    Perform an insertion sort using a given comparator on a list of values
    :param data: List of items to be sorted
    :param comparator: A function that compares two arguments and returns True if
    the first argument is less than or equal to the second and False otherwise
    """
    length = len(data)
    for j in range(1, length):
        i = j
        while (i > 0) and comparator(data[i], data[i-1]):
            data[i], data[i-1] = data[i-1], data[i]
            i -= 1


def hybrid_sort(data: List[T], threshold: int,
                comparator: Callable[[T, T], bool] = lambda x, y: x <= y) -> None:
    """
    Hybrid sorting algorthm using merge sort until a certain threshold,
    then insertion sort
    :param data: List to be sorted
    :param threshold: Amount of elements at which to switch to insertion sort
    :param comparator: A function that compares two arguments and returns
    True if the first argument is less than or equal to the second and
    False otherwise
    """
    # Call merge_sort with a threshold
    merge_sort(data, threshold, comparator)

def inversions_count(data: List[T]) -> int:
    """
    Uses merge sort and a copy of the data to return how many inversions
    it would take to sort it
    :param data: List to be used in determining number of inversions
    :return: Number of inversions
    """
    # Make a copy of the list, so we don't modify the input list
    temp = data.copy()
    # Use merge_sort with default values to get the inverison count
    return merge_sort(temp)


def reverse_sort(data: List[T], threshold: int) -> None:
    """
    sorts a list in reverse using a hybrid sorting algorithm
    :param data: List to be sorted in reverse
    :param threshold: Amount of elements at which to switch to insertion sort
    """
    hybrid_sort(data, threshold, comparator= lambda x, y: x >= y)


def password_rate(password: str) -> float:
    """
    Return a stregth rating for a given password
    :param password: string of password
    :return: Rating of password (float)
    """
    # Use a set to find unique character in the password
    charset = set()
    for c in password:
        charset.add(c)
    # Calculate and return the password rate
    arg1 = math.sqrt(len(password))
    arg2 = math.sqrt(len(charset))
    arg3 = inversions_count(list(password))
    return arg1 * arg2 + arg3

def password_sort(data: List[str]) -> None:
    """
    REPLACE
    """
    passstrength = []
    for i in range(len(data)):
        passstrength.append((data[i], (password_rate(data[i]))))

    comp = lambda x, y: x[1] >= y[1]

    hybrid_sort(passstrength, 2000, comp)

    for j in range(len(data)):
        data[j] = passstrength[j][0]
