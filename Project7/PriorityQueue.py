"""
Your Name Here
Project 5 - PriorityHeaps - Solution Code
CSE 331 Fall 2020
Dr. Sebnem Onsay
"""

from typing import List, Any
from Project7.PriorityNode import PriorityNode, MaxNode, MinNode


class PriorityQueue:
    """
    Implementation of a priority queue - the highest/lowest priority elements
    are at the front (root). Can act as a min or max-heap.
    """

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   DO NOT MODIFY the following attributes/functions
    #   Modify only below indicated line
    __slots__ = ["_data", "_is_min"]

    def __init__(self, is_min: bool = True):
        """
        Constructs the priority queue
        :param is_min: If the priority queue acts as a priority min or max-heap.
        """
        self._data = []
        self._is_min = is_min

    def __str__(self) -> str:
        """
        Represents the priority queue as a string
        :return: string representation of the heap
        """
        return F"PriorityQueue [{', '.join(str(item) for item in self._data)}]"

    __repr__ = __str__

    def to_tree_str(self) -> str:
        """
        Generates string representation of heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""

        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self._data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    def is_min_heap(self) -> bool:
        """
        Check if priority queue is a min or a max-heap
        :return: True if min-heap, False if max-heap
        """
        return self._is_min

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line
    def __len__(self) -> int:
        """
        TODO
        :return:
        """
        pass

    def empty(self) -> bool:
        """
        TODO
        :return:
        """
        pass

    def peek(self) -> PriorityNode:
        """
        TODO
        :return:
        """
        pass

    def get_left_child_index(self, index: int) -> int:
        """
        TODO
        :param index:
        :return:
        """
        pass

    def get_right_child_index(self, index: int) -> int:
        """
        TODO
        :param index:
        :return:
        """
        pass

    def get_parent_index(self, index: int) -> int:
        """
        TODO
        :param index:
        :return:
        """
        pass

    def push(self, priority: Any, val: Any) -> None:
        """
        TODO
        :param priority:
        :param val:
        :return:
        """
        pass

    def pop(self) -> PriorityNode:
        """
        TODO
        :return:
        """
        pass

    def get_minmax_child_index(self, index: int) -> int:
        """
        TODO
        :param index:
        :return:
        """
        pass

    def percolate_up(self, index: int) -> None:
        """
        TODO
        :param index:
        :return:
        """
        pass

    def percolate_down(self, index: int) -> None:
        """
        TODO
        :param index:
        :return:
        """
        pass


class MaxHeap:
    """
    Implementation of a max-heap - the highest value is at the front (root).

    Initializes a PriorityQueue with is_min set to False.

    Uses the priority queue to satisfy the min heap properties by initializing
    the priority queue as a max-heap, and then using value as both the priority
    and value.
    """

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   DO NOT MODIFY the following attributes/functions
    #   Modify only below indicated line

    __slots__ = ['_pqueue']

    def __init__(self):
        """
        Constructs a priority queue as a max-heap
        """
        self._pqueue = PriorityQueue(False)

    def __str__(self) -> str:
        """
        Represents the max-heap as a string
        :return: string representation of the heap
        """
        # NOTE: This hides implementation details
        return F"MaxHeap [{', '.join(item.value for item in self._pqueue._data)}]"

    __repr__ = __str__

    def to_tree_str(self) -> str:
        """
        Generates string representation of heap in Breadth First Ordering Format
        :return: String to print
        """
        return self._pqueue.to_tree_str()

    def __len__(self) -> int:
        """
        Determine the amount of nodes on the heap
        :return: Length of the data inside the heap
        """
        return len(self._pqueue)

    def empty(self) -> bool:
        """
        Checks if the heap is empty
        :returns: True if empty, else False
        """
        return self._pqueue.empty()

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line
    def peek(self) -> Any:
        """
        TODO
        :return:
        """
        pass

    def push(self, val: Any) -> None:
        """
        TODO
        :param val:
        :return:
        """
        pass

    def pop(self) -> Any:
        """
        TODO
        :return:
        """
        pass


class MinHeap(MaxHeap):
    """
    Implementation of a max-heap - the highest value is at the front (root).

    Initializes a PriorityQueue with is_min set to True.

    Inherits from MaxHeap because it uses the same exact functions, but instead
    has a priority queue with a min-heap.
    """

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   DO NOT MODIFY the following attributes/functions
    __slots__ = []

    def __init__(self):
        """
        Constructs a priority queue as a min-heap
        """
        super().__init__()
        self._pqueue._is_min = True


def heap_sort(array: List[Any]) -> None:
    """
    TODO
    :param array:
    :return:
    """
    pass


def current_medians(array: List[int]) -> List[int]:
    """
    TODO
    :param array:
    :return:
    """
    pass
