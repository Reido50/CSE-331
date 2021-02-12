"""
Name
Coding Challenge 3
CSE 331 Spring 2021
Professor Sebnem Onsay
"""
from typing import List


def finding_best_bot(bots_list: List[int]) -> int:
    """
    Finds and returns the index in a given list where the data goes from
    increasing to decreasing
    :param bots_list: List of integers that contains data is increases and
    possible decreases afterward
    :return: Index of the numerically greatest point in the data set
    """

    def finding_best_bot_helper(start: int, end: int):
        """
        Finds the index where a piece of data goes from increasing to decreasing
        Halfs the size of the list each time (similar to binary search)
        :param start: Starting index of the sublist to search
        :param end: Ending index of the sublist to search
        :return: Index of the numerically greatest point in the data set
        """
        if start == end:
            # Base case: Found the best bot
            return start + 1

        # Calculate middle element
        mid = (start + end) // 2

        # Best bot is in second half of the list
        if bots_list[mid] < bots_list[mid+1]:
            return finding_best_bot_helper(mid+1, end)

        # Best bot is in first half of the list
        return finding_best_bot_helper(start, mid)

    return finding_best_bot_helper(0, len(bots_list)-1)
