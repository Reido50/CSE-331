"""
Name
Coding Challenge 1 - Love Is In The Air
CSE 331 Spring 2021
Professor Sebnem Onsay
"""
from typing import List, Tuple


def story_progression(answers: List[int], questions: List[Tuple[int, int]]) -> List[str]:
    """
    Determine if each tuple in the question list to check that range of the answer list
    to determine if that chunk results in a win or a loss for the player.
    It will be a win condition if the chunk contains a majority
    :param answers: list of 0’s and 1’s, 1 represents a correct choice, 0 otherwise
    :param questions: list of questions, is a list of tuple of length 2, where
           Element [0] is starting index of the interested range
           Element [1] is ending index of the interested range
    :return: A Python list of the same length as list of question,
            each element is either “Win” or “Lose,”
    """
    results = []

    for chunk in questions:
        totals = [0, 0] # Total amount of correct and incorrect answers.
                        # Index 0 is incorrect, Index 1 is correct
        result = ""     # "Win" or "Lose" depending on the totals
        for i in range(chunk[0], chunk[1]+1):
            totals[answers[i]] += 1
            if(totals[1] > chunk[1]-chunk[0] or totals[0] > chunk[1]-chunk[0]):
                break
        if totals[1] > totals[0]:
            result = "Win"
        else:
            result = "Lose"
        results.append(result)

    return results
