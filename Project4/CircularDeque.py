"""
Project 4
CSE 331 S21 (Onsay)
Reid Harry
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
        """
        Returns the number of items in the deque
        :return: Number of items in the deque
        """
        return self.size

    def is_empty(self) -> bool:
        """
        Returns true if the deque has no items in it
        :return: True if the deque is empty
        """
        return self.size == 0

    def front_element(self) -> T:
        """
        Returns the front item of the deque
        :return: Front item of the deque
        """
        if self.front is not None:
            return self.queue[self.front]
        return None

    def back_element(self) -> T:
        """
        Returns the back item of the deque
        :return: Back item of the deque
        """
        if self.back is not None:
            return self.queue[self.back]
        return None

    def front_enqueue(self, value: T) -> None:
        """
        Adds a value to the front of the deque
        :param value: Value to be added to the deque
        """
        if self.front is None:
            
        self.grow()
        self.front += 1
        self.queue[self.front] = value
        self.size += 1

    def back_enqueue(self, value: T) -> None:
        pass

    def front_dequeue(self) -> T:
        pass

    def back_dequeue(self) -> T:
        pass

    def grow(self) -> None:
        
        """
        Doubles the capacity of the deque if the size is equal 
        to the current capacity
        """
        if self.capacity == self.size:
            newQueue = [self.queue[self.front]]
            oldFront = self.front
            self.front += 1
            while self.front != oldFront:
                if self.front == self.capacity:
                    self.front = 0
                newQueue.append(self.queue[self.front])
                self.front += 1
            self.front = 0
            self.back = self.capacity-1
            newQueue.extend([None]*self.capacity)
            self.queue = newQueue
            self.capacity *= 2

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
