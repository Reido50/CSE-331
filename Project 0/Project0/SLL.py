"""
Project 0B - Singly Linked List - Spring 2021
Name: Solution
"""
from typing import Any, List, TypeVar

# Type Declarations - Used for Type Hinting
Node = TypeVar('Node')      # Node type
SLL = TypeVar('SLL')        # SLL type


class Node:
    """
    Implementation of a singly linked list node.
    """
    __slots__ = ["next", "value"]
    # The __slots__ list tells Python to preallocate space for certain class attributes,
    # saving memory and improving runtime. For more information, see
    # https://stackoverflow.com/questions/472000/usage-of-slots

    def __init__(self, value: Any, next: Node = None) -> None:
        """
        Creates a Node instance.
        param value: value to store in the node.
        param next: the next node in the linked list.
        return: None.
        """
        self.value = value
        self.next = next

    def __eq__(self, other: Node) -> bool:
        """
        Defines equality (`==`) operator between Node instances.
        param other: right-hand operand.
        return: `True` if equal, else `False`.
        """
        return self.value == other.value if other is not None else False

    def __repr__(self) -> str:
        """
        Represents the Node as a string.
        :return: string representation of Node.
        """
        return str(self.value)

    def __str__(self) -> str:
        """
        Represents the Node as a string.
        :return: string representation of Node.
        """
        return str(self.value)


class SLL:
    """
    Implementation of a basic singly linked list.
    """
    __slots__ = ["head"]

    def __init__(self, vals_list: List[Any] = None) -> None:
        """
        Creates an SLL instance.
        param vals_list: a list of values the linked list will contain.
        return: None.
        """
        if vals_list:
            vals_list.reverse()                         # reverse to remove from end of list
            curr = self.head = Node(vals_list.pop())    # pop() removes from end of list
            while vals_list:
                curr.next = Node(vals_list.pop())
                curr = curr.next
        else:
            self.head = None

    def __eq__(self, other: SLL) -> bool:
        """
        Equality operator for SLL class.
        param other: right side of `==` operator.
        return: `True` if equal, else `False`.
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

    def __repr__(self) -> str:
        """
        Represents the Node as a string.
        :return: string representation of Node.
        """
        if self.head is None:
            return "Empty SLL"

        result = ""
        node = self.head
        while node is not None:
            result += str(node)
            if node.next is not None:
                result += " -> "
            node = node.next
        return result

    def __str__(self) -> str:
        """
        Represents the Node as a string.
        :return: string representation of Node.
        """
        return repr(self)

    def empty(self) -> bool:
        """
        Return boolean indicating whether SLL is empty.
        :return: True if SLL is empty, else False.
        """
        return (self.head == None)
        pass

    def push_front(self, val: Any) -> None:
        """
        Adds a Node with value `val` at the head of the list.
        param val: value to be added to the SLL.
        return: None.
        """
        node = Node(val, self.head)
        self.head = node
        pass

    def push_back(self, val: Any) -> None:
        """
        Adds a Node with value `val` at the tail of the list.
        param val: value to be added to the SLL.
        return: None.
        """
        # Insert newNode after the last element (the tail)
        newNode = Node(val, None)
        current = self.head
        if(self.head != None):
            while(current.next != None):
                current = current.next
            current.next = newNode
        else:
            # Empty list case
            self.push_front(val)
        pass

    def remove(self, val: Any) -> bool:
        """
        Traverses the list until it encounters a node with value `val`, and removes that node.
        param val: value to be removed from the SLL.
        return: True if a node is removed, else False.
        """
        current = self.head

        if(current != None):
            # Remove head case
            if(current.value == val):
                self.head = current.next
                return True

            while(current.next != None):
                if(current.next.value == val):
                    current.next = current.next.next
                    return True
                current = current.next

        return False
        pass

    def reverse(self) -> None:
        """
        Reverses the SLL.
        return: None.
        """
        current = self.head

        if(current != None):
            # Extract list of SLL values
            values = [current.value]
            while(current.next != None):
                current = current.next
                values.append(current.value)

            # Reverse the list of SLL values
            values.reverse()

            # Transfer reversed values from list to SLL
            current = self.head
            for val in values:
                current.value = val
                current = current.next
            
        pass
