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
        Determine the amount of nodes on the heap
        :return: The amount of nodes in the priority queue
        """
        return len(self._data)

    def empty(self) -> bool:
        """
        Checks if the heap is empty
        :return: True if Empty, else False
        """
        return len(self) == 0

    def peek(self) -> PriorityNode:
        """
        Gets the root node (min or max node)
        :return: None if heap is empty, else root node
        """
        if self.empty():
            return None
        return self._data[0]

    def get_left_child_index(self, index: int) -> int:
        """
        Gets the specified parent node's left child index
        :param index: Index of parent node
        :return: Index of left child or None if it does not exist
        """
        leftindex = 2*index + 1
        if leftindex < len(self):
            return leftindex
        return None

    def get_right_child_index(self, index: int) -> int:
        """
        Gets the specified parent node's right child index
        :param index: Index of parent node
        :return: Index of right child or None if it does not exist
        """
        rightindex = 2*index + 2
        if rightindex < len(self):
            return rightindex
        return None

    def get_parent_index(self, index: int) -> int:
        """
        Gets the specified child node's parent index
        :param index: Index of child node
        :return: Index of parent or None if it does not exist
        """
        parentindex = (index-1) // 2
        if parentindex >= 0:
            return parentindex
        return None

    def push(self, priority: Any, val: Any) -> None:
        """
        Inserts a node with the specified priority/value pair onto the heap
        :param priority: Node's priority
        :param val: Node's value
        :return: None
        """
        # Add the new node to the end of the heap
        if self.is_min_heap():
            self._data.append(MinNode(priority, val))
        else:
            self._data.append(MaxNode(priority, val))
        # Percolate up
        self.percolate_up(len(self)-1)

    def pop(self) -> PriorityNode:
        """
        Removes the top priority node from heap
        :return: The root node of the heap
        """
        # Can't pop on an empty queue
        if self.empty():
            return
        # Grab the top priority node
        removed = self._data[0]
        # Move the bottom node to the top
        self._data[0] = self._data[len(self) - 1]
        self._data.pop()
        # Percolate down
        self.percolate_down(0)
        # Return the removed node
        return removed

    def get_minmax_child_index(self, index: int) -> int:
        """
        Gets the specified parent's min or max child index
        :param index: Index of parent element
        :return: Index of min child or max child or None if invalid
        """
        right = self.get_right_child_index(index)
        left = self.get_left_child_index(index)
        # Check to see if right and/or left is None
        if right is None:
            return left
        if left is None:
            return right
        # Return the min/max value
        if self._data[right] < self._data[left]:
            return right
        return left

    def percolate_up(self, index: int) -> None:
        """
        Moves a node in the queue/heap up to its correct position (level in the tree)
        :param index: Index of node to be percolated up
        :return: None
        """
        parentindex = self.get_parent_index(index)
        # If parent does not exist, index is already the root
        if parentindex is None:
            return
        # Compare current to parent
        if self._data[parentindex] > self._data[index]:
            # Swap values and try again on parent
            self._data[parentindex], self._data[index] = self._data[index], self._data[parentindex]
            self.percolate_up(parentindex)
        else:
            # End of percolation
            return

    def percolate_down(self, index: int) -> None:
        """
        Moves a node in the queue/heap down to its correct position (level in the tree)
        :param index: Index of node to be percolated up
        :return: None
        """
        childindex = self.get_minmax_child_index(index)
        # If parent does not exist, index is already a leaf
        if childindex is None:
            return
        # Compare current to parent
        if self._data[childindex] < self._data[index]:
            # Swap values and try again on parent
            self._data[childindex], self._data[index] = self._data[index], self._data[childindex]
            self.percolate_down(childindex)
        else:
            # End of percolation
            return


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
        Gets the max element's value
        :return: Max element's value
        """
        if self._pqueue.empty():
            return None
        return self._pqueue.peek().value

    def push(self, val: Any) -> None:
        """
        Inserts a node with the specified value onto the heap
        :param val: Node's value
        :return: None
        """
        self._pqueue.push(val, val)

    def pop(self) -> Any:
        """
        Removes the max element from the heap
        :return: Value of max element
        """
        if self.empty():
            return None
        return self._pqueue.pop().value


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
    Sort array in-place using heap sort algorithm w/ max-heap
    :param array: List to be sorted
    :return: None
    """
    # Make a populate a max heap
    heap = MaxHeap()
    for i in array:
        heap.push(i)
    # Pop the max heap into the array in reverse order
    for i in range(len(array)-1, -1, -1):
        array[i] = heap.pop()
    


def current_medians(array: List[int]) -> List[int]:
    """
    Calculate a list of current medians as the input list is iterated over
    :param array: List of numeric values
    :return: List of current medians in order data was read in
    """
    medians = []
    maxh = MaxHeap()
    minh = MinHeap()
    for i in array:
        # Add number to heap system
        if minh.peek() is None:
            minh.push(i)
        elif i < minh.peek():
            # Add to max heap
            maxh.push(i)
            # Balance list lengths if needed
            if len(maxh) > len(minh) + 1:
                minh.push(maxh.pop())
        else:
            # Add to min heap
            minh.push(i)
            # Balance list lengths if needed
            if len(minh) > len(maxh) + 1:
                maxh.push(minh.pop())
        # Get current median and add it to medians
        if len(minh) < len(maxh):
            medians.append(maxh.peek())
        elif len(minh) > len(maxh):
            medians.append(minh.peek())
        else:
            medians.append((maxh.peek() + minh.peek())/2)
    return medians
