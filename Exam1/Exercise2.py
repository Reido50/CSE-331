# Reid Harry
# 2/9/2021

from typing import TypeVar, List, Tuple

T = TypeVar("T")            # represents generic type
Node = TypeVar("Node")      # represents a Node object (forward-declare to use in Node __init__)

class Node:
    """
    Implementation of a doubly linked list node.
    Do not modify.
    """
    __slots__ = ["value", "next", "prev"]

    def __init__(self, value: T, next: Node = None, prev: Node = None) -> None:
        """
        Construct a doubly linked list node.
        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

    def __repr__(self) -> str:
        """
        Represents the Node as a string.
        :return: string representation of the Node.
        """
        return str(self.value)

    def __str__(self) -> str:
        """
        Represents the Node as a string.
        :return: string representation of the Node.
        """
        return str(self.value)


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.
        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.
        :return: string representation of the DLL.
        """
        result = ""
        node = self.head
        while node is not None:
            result += str(node)
            if node.next is not None:
                result += " <-> "
            node = node.next
        return result

    def __str__(self) -> str:
        """
        Represent the DLL as a string.
        :return: string representation of the DLL.
        """
        return repr(self)

def remove_middle(data: DLL) -> DLL:
    """
    Removes the middle node(s) from a doubly linked list
    :param data: a DLL
    :return: the modified DLL
    """
    # Init frontCurNode
    frontCurNode = data.head
    # Init backCurNode
    backCurNode = data.tail

    # Check for empty list
    if frontCurNode is None or backCurNode is None:
        return data

    # Init odd flag
    odd = True

    # Increment/Decrement each CurNode until they are in the center of the DLL
    while True:
        if frontCurNode is backCurNode:
            # Found the center and the list is odd
            break
        elif frontCurNode.next is backCurNode:
            # Found the center and the list is even
            odd = False
            break
        frontCurNode = frontCurNode.next
        backCurNode = backCurNode.prev

    # Check to see if we are removing the only 1-2 nodes
    if frontCurNode.prev is None:
        data.head = None
        data.tail = None
        data.size = 0
    else:
        if odd:
            # Remove the one center node
            frontCurNode.prev.next = frontCurNode.next
            frontCurNode.next.prev = frontCurNode.prev
            data.size -= 1
        else:
            # Remove the two center nodes
            frontCurNode.prev.next = backCurNode.next
            backCurNode.next.prev = frontCurNode.prev
            data.size -= 2

    return data