"""
Project 4
CSE 331 S21 (Onsay)
Name
CircularDeque.py
"""

from __future__ import annotations
from typing import TypeVar, List
# from re import split as rsplit
import re

# for more information on typehinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")                                # represents generic type
CircularDeque = TypeVar("CircularDeque")        # represents a CircularDeque object


class CircularDeque:
    """
    Class representation of a Circular Deque
    """

    __slots__ = ['capacity', 'size', 'queue', 'front', 'back']

    def __init__(self, data: List[T] = [], capacity: int = 4):
        """
        Initializes an instance of a CircularDeque
        :param data: starting data to add to the deque, for testing purposes
        :param capacity: amount of space in the deque
        """
        self.capacity: int = capacity
        self.size: int = len(data)

        self.queue: list[T] = [None] * capacity
        self.front: int = None
        self.back: int = None

        for index, value in enumerate(data):
            self.queue[index] = value
            self.front = 0
            self.back = index

    def __str__(self) -> str:
        """
        Provides a string represenation of a CircularDeque
        :return: the instance as a string
        """
        if self.size == 0:
            return "CircularDeque <empty>"

        string = f"CircularDeque <{self.queue[self.front]}"
        current_index = self.front + 1 % self.capacity
        while current_index <= self.back:
            string += f", {self.queue[current_index]}"
            current_index = (current_index + 1) % self.capacity
        return string + ">"

    def __repr__(self) -> str:
        """
        Provides a string represenation of a CircularDeque
        :return: the instance as a string
        """
        return str(self)

    # ============ Modify below ============ #

    def __len__(self) -> int:
        pass

    def is_empty(self) -> bool:
        pass

    def front_element(self) -> T:
        pass

    def back_element(self) -> T:
        pass

    def front_enqueue(self, value: T) -> None:
        pass

    def back_enqueue(self, value: T) -> None:
        pass

    def front_dequeue(self) -> T:
        pass

    def back_dequeue(self) -> T:
        pass

    def grow(self) -> None:
        pass

    def shrink(self) -> None:
        pass


def LetsPassTrains102(infix : str) -> str:

    """
    regex = r"\-*\d+\.\d+|\-\d+|[\(\)\-\^\*\+\/]|(?<!-)\d+|\w"
    ops = {'*': 3, '/': 3,  # key: operator, value: precedence
           '+': 2, '-': 2,
           '^': 4,
           '(': 0}  # '(' is lowest bc must be closed by ')'
    """

    pass
