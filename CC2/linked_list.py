# DO NOT MODIFY FILE

from __future__ import annotations  # allow self-reference
from typing import TypeVar, Generic, List  # function type

T = TypeVar("T")


class DLLNode:
    def __init__(self, val: Generic[T], nxt: DLLNode = None, prev: DLLNode = None):
        """
        DO NOT MODIFY
        Initialize of double linked list node
        :param val: value of this node
        :param nxt: pointer to the next node
        :param prev: pointer to the previous node
        """
        self.val = val  # Value of this node
        self.nxt = nxt  # Pointer to next node
        self.prev = prev

    def __str__(self):
        """
        DO NOT MODIFY
        Represent Doubly Linked List node as string
        :return: string represented Doubly linked list node
        """
        return str(self.val)

    def __repr__(self):
        """
        DO NOT MODIFY
        Represent Doubly Linked List node as string
        :return: string represented Doubly linked list node
        """
        return self.__str__()


class LinkedList:
    def __init__(self, container: List[T] = None):
        """
        DO NOT MODIFY
        Initialize of Linked list with double linked list node
        :param container: container that contain the elements in linked list
        """
        self.head = DLLNode(None)  # Head of linked list
        self.tail = self.head  # Tail of linked list

        # If container presented, creating the rest of linked lish
        if container:
            cur = self.head
            for item in container:
                cur.nxt = DLLNode(item, prev=cur)
                cur = cur.nxt
            self.tail = cur

    def linked_list_to_list(self):
        """
        DO NOT MODIFY
        Converting the linked list to list
        :return: list that contain the same elements as linked list
        """
        actual_list = []
        node = self.head.nxt
        while node is not None:
            actual_list.append(node.val)
            node = node.nxt
        return actual_list

    def __str__(self):
        """
        DO NOT MODIFY
        Represent Linked List as string
        :return: string represented linked list
        """
        return str(self.linked_list_to_list())

    def __repr__(self):
        """
        DO NOT MODIFY
        Represent Linked List as string
        :return: string represented linked list
        """
        return self.__str__()
