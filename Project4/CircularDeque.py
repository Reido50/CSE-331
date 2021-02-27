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
        if self.size != 0:
            return self.queue[self.front]
        return None

    def back_element(self) -> T:
        """
        Returns the back item of the deque
        :return: Back item of the deque
        """
        if self.size != 0:
            return self.queue[self.back]
        return None

    def front_enqueue(self, value: T) -> None:
        """
        Adds a value to the front of the deque
        :param value: Value to be added to the deque
        """
        if self.size == 0:
            self.front = 1
            self.back = 0
        self.front -= 1
        if self.front < 0:
            self.front = self.front + self.capacity
        self.queue[self.front] = value
        self.size += 1
        self.grow()

    def back_enqueue(self, value: T) -> None:
        """
        Adds a value to the back of the deque
        :param value: Value to be added to the deque
        """
        if self.size == 0:
            self.front = 0
            self.back = -1
        self.back += 1
        if self.back >= self.capacity:
            self.back = 0
        self.queue[self.back] = value
        self.size += 1
        self.grow()

    def front_dequeue(self) -> T:
        """
        Removes the item at the front of the circular queue
        :return: Item at the front of the circular queue, None if empty
        """
        if self.size == 0:
            return None
        rem = self.queue[self.front]
        self.front += 1
        if self.front >= self.capacity:
            self.front = 0
        self.size -= 1
        self.shrink()
        return rem

    def back_dequeue(self) -> T:
        """
        Removes the item at the back of the circular queue
        :return: Item at the back of the circular queue, None if empty
        """
        if self.size == 0:
            return None
        rem = self.queue[self.back]
        self.back -= 1
        if self.back < 0:
            self.back = self.capacity-1
        self.size -= 1
        self.shrink()
        return rem

    def grow(self) -> None:
        """
        Doubles the capacity of the deque if the size is equal
        to the current capacity
        """
        if self.capacity == self.size:
            newqueue = [self.queue[self.front]]
            oldfront = self.front
            self.front += 1
            while self.front != oldfront:
                if self.front == self.capacity:
                    self.front = 0
                else:
                    newqueue.append(self.queue[self.front])
                    self.front += 1
            self.front = 0
            self.back = self.capacity-1
            newqueue.extend([None]*self.capacity)
            self.queue = newqueue
            self.capacity *= 2

    def shrink(self) -> None:
        """
        Halves the capacity of the queue if needed
        """
        if self.size <= (self.capacity//4) and (self.capacity//2) >= 4:
            newqueue = [None] * (self.capacity//2)
            i = 0
            newqueue[i] = self.queue[self.front]
            self.front += 1
            i += 1
            while self.front != self.back+1:
                if self.front == self.capacity:
                    self.front = 0
                else:
                    newqueue[i] = self.queue[self.front]
                    self.front += 1
                    i += 1
            self.front = 0
            self.back = self.size - 1
            self.queue = newqueue
            self.capacity //= 2


def LetsPassTrains102(infix: str) -> str:

    """
    Converts an equation of infix to postfix and outputs the result
    :param infix: Expression in infix
    :return: Tuple containing evaluated expression and the postfix expression
    """
    if infix == "":
        return (0, "")

    postfix = CircularDeque()
    output = ""
    regex = r"\-*\d+\.\d+|\-\d+|[\(\)\-\^\*\+\/]|(?<!-)\d+|\w"
    ops = {'*': 3, '/': 3,  # key: operator, value: precedence
           '+': 2, '-': 2,
           '^': 4,
           '(': 0}  # '(' is lowest bc must be closed by ')'

    symbols = re.findall(regex, infix)

    for s in symbols:
        if ops.get(s) is None:
            if s == ")":
                while ops[postfix.back_element()] != 0:
                    output += postfix.back_dequeue()
                    output += " "
                postfix.back_dequeue()
            else:
                output += s
                output += " "
        elif ops[s] == 0:
            postfix.back_enqueue(s)
        else:
            while (postfix.size != 0) and (ops[postfix.back_element()] >= ops[s]):
                output += postfix.back_dequeue()
                output += " "
            postfix.back_enqueue(s)
    while not postfix.is_empty():
        output += postfix.back_dequeue()
        output += " "
    output = output[0:-1]

    evaluation = CircularDeque()
    postnums = re.findall(regex, output)
    for c in postnums:
        if c == "+":
            op1 = float(evaluation.back_dequeue())
            op2 = float(evaluation.back_dequeue())
            evaluation.back_enqueue(op1 + op2)
        elif c == "-":
            op1 = float(evaluation.back_dequeue())
            op2 = float(evaluation.back_dequeue())
            evaluation.back_enqueue(op2 - op1)
        elif c == "*":
            op1 = float(evaluation.back_dequeue())
            op2 = float(evaluation.back_dequeue())
            evaluation.back_enqueue(op1 * op2)
        elif c == "/":
            op1 = float(evaluation.back_dequeue())
            op2 = float(evaluation.back_dequeue())
            evaluation.back_enqueue(op1 / op2)
        elif c == "^":
            op1 = float(evaluation.back_dequeue())
            op2 = float(evaluation.back_dequeue())
            evaluation.back_enqueue(op1 ** op2)
        else:
            evaluation.back_enqueue(float(c))

    return (evaluation.back_dequeue(), output)
