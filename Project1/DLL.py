"""
Project 1
CSE 331 S21 (Onsay)
Your Name
DLL.py
"""

from typing import TypeVar, List, Tuple
import datetime

# for more information on typehinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")            # represents generic type
Node = TypeVar("Node")      # represents a Node object (forward-declare to use in Node __init__)

# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


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

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        Return boolean indicating whether DLL is empty.

        Suggested time & space complexity (respectively): O(1) & O(1).

        :return: True if DLL is empty, else False.
        """
        # Check to see if head is null
        return (self.head == None)

        pass

    def push(self, val: T, back: bool = True) -> None:
        """
        Create Node containing `val` and add to back (or front) of DLL. Increment size by one.

        Suggested time & space complexity (respectively): O(1) & O(1).

        :param val: value to be added to the DLL.
        :param back: if True, add Node containing value to back (tail-end) of DLL;
            if False, add to front (head-end).
        :return: None.
        """
        # Create the node
        newNode = Node(val, None, None)

        # Check if the DLL is not empty
        if not self.empty():
            # Determine if front or back
            if back:
                # Append node to the tail
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
            else:
                # Prepend node to the head
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
        else:
            # Add initial node
            self.head = newNode
            self.tail = newNode

        # Increment list size
        self.size += 1

        pass

    def pop(self, back: bool = True) -> None:
        """
        Remove Node from back (or front) of DLL. Decrement size by 1. If DLL is empty, do nothing.

        Suggested time & space complexity (respectively): O(1) & O(1).

        :param back: if True, remove Node from (tail-end) of DLL;
            if False, remove from front (head-end).
        :return: None.
        """
        # Check if DLL is not empty
        if not self.empty():
            # Determine location of removal (front, back, or both)
            if self.size == 1:
                self.head = None
                self.tail = None
            elif back:
                self.tail = self.tail.prev
                self.tail.next = None
            elif not back:
                self.head = self.head.next
                self.head.prev = None
            # Decrement list size
            self.size -= 1

        pass

    def from_list(self, source: List[T]) -> None:
        """
        Construct DLL from a standard Python list.

        Suggested time & space complexity (respectively): O(n) & O(n).

        :param source: standard Python list from which to construct DLL.
        :return: None.
        """
        # Traverse the Python list
        for val in source:
            # Add value from Python list to DLL
            self.push(val, True)

        pass

    def to_list(self) -> List[T]:
        """
        Construct standard Python list from DLL.

        Suggested time & space complexity (respectively): O(n) & O(n).

        :return: standard Python list containing values stored in DLL.
        """
        # Create the Python list
        l = []

        # Set first node
        curNode = self.head

        # Traverse the DLL
        while curNode != None:
            l.append(curNode.value)
            # Increment curNode
            curNode = curNode.next
        
        return l

        pass

    def find(self, val: T) -> Node:
        """
        Find first instance of `val` in the DLL and return associated Node object.

        Suggested time & space complexity (respectively): O(n) & O(1).

        :param val: value to be found in DLL.
        :return: first Node object in DLL containing `val`.
            If `val` does not exist in DLL, return None.
        """
        # Set first node
        curNode = self.head

        # Traverse the DLL
        while curNode != None:
            # Check if found
            if curNode.value == val:
                return curNode
            # Increment curNode
            curNode = curNode.next

        # Return None if val was not found
        return None

        pass

    def find_all(self, val: T) -> List[Node]:
        """
        Find all instances of `val` in DLL and return Node objects in standard Python list.

        Suggested time & space complexity (respectively): O(n) & O(n).

        :param val: value to be searched for in DLL.
        :return: Python list of all Node objects in DLL containing `val`.
            If `val` does not exist in DLL, return empty list.
        """
        # Create Python list of found nodes
        found = []

        # Set first node
        curNode = self.head

        # Traverse the DLL
        while curNode != None:
            # Check if found
            if curNode.value == val:
                found.append(curNode)
            # Increment curNode
            curNode = curNode.next

        return found

        pass

    def delete(self, val: T) -> bool:
        """
        Delete first instance of `val` in the DLL.

        Suggested time & space complexity (respectively): O(n) & O(1).

        :param val: value to be deleted from DLL.
        :return: True if Node containing `val` was deleted from DLL; else, False.
        """
        delNode = self.find(val)

        # Check if val was found
        if delNode != None:
            # Check if delNode is head and/or tail
            if delNode is self.head:
                self.pop(False)
            elif delNode is self.tail:
                self.pop(True)
            else:
                delNode.prev.next = delNode.next
                delNode.next.prev = delNode.prev
                self.size -= 1
            return True
        else:
            return False

        pass

    def delete_all(self, val: T) -> int:
        """
        Delete all instances of `val` in the DLL.

        Suggested time & space complexity (respectively): O(n) & O(1).

        :param val: value to be deleted from DLL.
        :return: integer indicating the number of Nodes containing `val` deleted from DLL;
                 if no Node containing `val` exists in DLL, return 0.
        """
        delNodes = self.find_all(val)
        delCount = 0

        # Traverse delNodes
        for n in delNodes:
            # Check if delNode is head and/or tail
            if n is self.head:
                self.pop(False)
            elif n is self.tail:
                self.pop(True)
            else:
                n.prev.next = n.next
                n.next.prev = n.prev
                self.size -= 1
            delCount += 1

        return delCount

        pass

    def reverse(self) -> None:
        """
        Reverse DLL in-place by modifying all `next` and `prev` references of Nodes in the
        DLL and resetting the `head` and `tail` references.
        Must be implemented in-place for full credit. May not create new Node objects.

        Suggested time & space complexity (respectively): O(n) & O(1).

        :return: None.
        """
        # Set first node
        curNode = self.head

        # Traverse the DLL
            # Switch next and previous of curNode

        pass


class Stock:
    """
    Implementation of a stock price on a given day.
    Do not modify.
    """

    __slots__ = ["date", "price"]

    def __init__(self, date: datetime.date, price: float) -> None:
        """
        Construct a stock.

        :param date: date of stock.
        :param price: the price of the stock at the given date.
        """
        self.date = date
        self.price = price

    def __repr__(self) -> str:
        """
        Represents the Stock as a string.

        :return: string representation of the Stock.
        """
        return f"<{str(self.date)}, ${self.price}>"

    def __str__(self) -> str:
        """
        Represents the Stock as a string.

        :return: string representation of the Stock.
        """
        return repr(self)


def intellivest(stocks: DLL) -> Tuple[datetime.date, datetime.date, float]:
    """
    Given a DLL representing daily stock prices,
    find the optimal streak of days over which to invest.
    To be optimal, the streak of stock prices must:

        (1) Be strictly increasing, such that the price of the stock on day i+1
        is greater than the price of the stock on day i, and
        (2) Have the greatest total increase in stock price from
        the first day of the streak to the last.

    In other words, the optimal streak of days over which to invest is the one over which stock
    price increases by the greatest amount, without ever going down (or staying constant).

    Suggested time & space complexity (respectively): O(n) & O(1).

    :param stocks: DLL with Stock objects as node values, as defined above.
    :return: Tuple with the following elements:
        [0]: date: The date at which the optimal streak begins.
        [1]: date: The date at which the optimal streak ends.
        [2]: float: The (positive) change in stock price between the start and end
                dates of the streak.
    """
    pass
