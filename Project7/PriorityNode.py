"""
Your Name Here
Project 5 - PriorityHeaps - Solution Code
CSE 331 Fall 2020
Dr. Sebnem Onsay
"""

import abc
from typing import Any


class PriorityNode(metaclass=abc.ABCMeta):
    """
    Implementation of a Priority Node - a Heap Node with a Priority
    """

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   DO NOT MODIFY the following attributes/functions
    __slots__ = ['priority', 'value']

    @abc.abstractmethod
    def __init__(self, priority: Any, val: Any):
        """
        Creates PriorityNode. Abstract, so can only be used as a base constructor for subclasses.
        """
        self.priority = priority
        self.value = val

    def __str__(self) -> str:
        """
        Converts node to a string
        :return: string representation of node
        """
        return F"<{self.priority}, {self.value}>"

    __repr__ = __str__

    def __eq__(self, other: 'PriorityNode') -> bool:
        """
        Equality comparator for when priority nodes are equal
        :param other: node to compare self to
        :return: True if the nodes are equal, False if otherwise
        """
        return self.priority == other.priority and self.value == other.value


class MaxNode(PriorityNode):
    """
    Implementation of a priority node for a priority queue max heap.
    Nodes with higher priority values are at the top of
    the priority queue.
    """

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   DO NOT MODIFY the following attributes/functions
    #   Modify only below indicated line
    __slots__ = []

    def __init__(self, priority: Any, val: Any):
        """
        Constructs node
        :param priority: priority to be stored in the node
        :param val: data to be stored in the node
        """
        super().__init__(priority, val)

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line
    def __lt__(self, other: 'MaxNode') -> bool:
        """
        Less than comparator. Determines if self is greater than other node, and thus should
        be sorted lower than other node in priority queue
        :param other: Node to compare self to
        :return: False if self is less than other, True is self is greater than other
        """
        if self.priority == other.priority:
            return self.value > other.value
        return self.priority > other.priority

    def __gt__(self, other: 'MaxNode') -> bool:
        """
        Greater than comparator. Determines if self node is less than other node, and thus
        should be sorted higher than other node in priority queue
        :param other: Node to compare self to
        :return: False if self is greater than other, True is self is less than other
        """
        if self.priority == other.priority:
            return self.value < other.value
        return self.priority < other.priority


class MinNode(PriorityNode):
    """
    Implementation of a priority node for a priority queue min heap.
    Nodes with lower priority values are at the top of
    the priority queue.
    """

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   DO NOT MODIFY the following attributes/functions
    #   Modify only below indicated line
    __slots__ = []

    def __init__(self, priority: Any, val: Any):
        """
        Constructs node with specified priority and value
        :param priority: priority to be stored in the node
        :param val: data to be stored in the node
        """
        super().__init__(priority, val)

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line
    def __lt__(self, other: 'MinNode') -> bool:
        """
        Less than comparator. Determines if self node is less than other node, and thus should
        be sorted higher than other node in priority queue
        :param other: Node to compare self to
        :return: True if self is less than other, False if self is greater than other
        """
        if self.priority == other.priority:
            return self.value < other.value
        return self.priority < other.priority

    def __gt__(self, other: 'MinNode') -> bool:
        """
        Greater than comparator. Determines if self node is greater than other node, and thus
        should be sorted lower than other node in priority queue
        :param other: Node to compare self to
        :return: True if self is greater than other, False if self is less than other
        """
        if self.priority == other.priority:
            return self.value > other.value
        return self.priority > other.priority
