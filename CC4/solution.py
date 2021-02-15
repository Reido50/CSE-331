"""
Name
Coding Challenge 4
CSE 331 Spring 2021
Professor Sebnem Onsay
"""
from typing import List


def challenger_finder(stocks_list: List[int], k: int) -> List[int]:
    """
    Fill out doc string
    """

    def binary_search_edge(l:List[int], start:int, end:int, value:int, direction:int) -> int:
        """
        Finds and returns the index in a sorted list that matches a value and
        is either the first or last instance of it in the list
        :param l: Sorted list in which to search
        :param start: Starting index of area to search
        :param end: Ending index of area to search
        :param direction: Direction to go in to search for duplicates if the value is found (should be -1 or 1)
        :return: Index of found element in the array
        """
        if end >= start:
            mid = (start + end) // 2

            if l[mid] == value:
                # Base case: Found the value
                # Walk in a direction until we find an element that does not 
                # equal value. Return the element in front of that
                while(l[mid] == value):
                    mid += direction
                    if(mid < 0):
                        # Accounts for walking to the start of the list
                        return 0
                    elif(mid > len(l)-1):
                        # Accounts for walking to the end of the list
                        return len(l)-1
                return mid + 1

            if value > l[mid]:
                binary_search_edge(l, mid+1, end, value, direction)
            else:
                binary_search_edge(l, start, mid-1, value, direction)
        else:
            return -1

    # Create a result list of 0's with length equal to stocks_list.
    result = [0] * len(stocks_list)

    # Copy the stocks_list, but sort it
    stocks_sorted = sorted(stocks_list)

    # Iterate through stocks_list using Range() so
    # we can keep track of indices.
    for i in range(len(stocks_list)):
        # Use binary search twice on the sorted list to find the 
        # the values in the iterval [stocks_list[i]-k, stocks_list[i]+k].
        upper = binary_search_edge(stocks_sorted, 0, len(stocks_sorted)-1, stocks_list[i]+k, 1)
        lower = binary_search_edge(stocks_sorted, 0, len(stocks_sorted)-1, stocks_list[i]-k, -1)
        print("Upper: " + str(upper))
        print("Lower: " + str(lower))
        
        # Place the number of values inside the interval in
        # the result list.

    pass

stocks = [5, 1, 3, 2, 1]
challenger_finder(stocks, 1)