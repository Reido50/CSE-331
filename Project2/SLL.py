"""
Project 1
CSE 331 S21 (Onsay)
Your Name
DLL.py
"""

from Project2.Node import Node       # Import `Node` class
from typing import TypeVar  # For use in type hinting

# Type Declarations
T = TypeVar('T')        # generic type
SLL = TypeVar('SLL')    # forward declared


class RecursiveSinglyLinkList:
    """
    Recursive implementation of an SLL
    """

    __slots__ = ['head']

    def __init__(self) -> None:
        """
        Initializes an `SLL`
        :return: None
        """
        self.head = None

    def __repr__(self) -> str:
        """
        Represents an `SLL` as a string
        """
        return self.to_string(self.head)

    def __str__(self) -> str:
        """
        Represents an `SLL` as a string
        """
        return self.to_string(self.head)

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right hand operand of `==`
        :return: `True` if equal, else `False`
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

# ============ Modify below ============ #

    def to_string(self, curr: Node) -> str:
        """
        Generates and returns a string representation of the list, starting at curr
        :param curr: Starting point of the string representation of the list
        :return: String representation of the list
        Time complexity: O(n^2)
        """
        if curr is None:
            # Base case: Empty list
            return "None"
        if curr.next is None:
            # Base case: Last element
            return str(curr.val)
        # Recursive case
        return str(curr.val) + " --> " + self.to_string(curr.next)

    def length(self, curr: Node) -> int:
        """
        Determines the number of nodes in the list starting with curr
        :param curr: Starting node from which the function determines the length
        :return: Number of nodes in the list starting with curr
        Time complexity: O(n)
        """
        if curr is None:
            # Base case: Empty node (last node or empty list)
            return 0
        # Recursive case
        return 1 + self.length(curr.next)

    def sum_list(self, curr: Node) -> T:
        """
        Calculates and returns the sum of the values in the list starting with head curr
        :param curr: starting node from which the function determines the sum
        :return: Sum of the list elements starting with curr
        Time complexity: O(n)
        """
        if curr is None:
            # Base case: Empty node (last node or empty list)
            return 0
        # Recursive case
        return curr.val + self.sum_list(curr.next)

    def push(self, value: T) -> None:
        """
        Insert the given value at the end of the linked list
        :param value: Value for the pushed node
        Time complexity: O(n)
        """
        # Init new node
        newNode = Node(value, None)
        def push_inner(curr: Node) -> None:
            """
            This is a helper function for push
            Insert the given value (from push) into the linked list that has head curr
            :param curr: Node to start with when determining where to push
            Time complexity: O(n)
            """
            if curr is None:
                # Base case: Empty list
                self.head = newNode
                return
            if curr.next is None:
                # Base case: End of list
                curr.next = newNode
                return
            # Recursive case
            push_inner(curr.next)
        # Push the new node
        push_inner(self.head)

    def remove(self, value: T) -> None:
        """
        Remove the first node in the list with the given value
        :param value: Value of the node to be removed
        Time complexity: O(n)
        """
        def remove_inner(curr: Node) -> Node:
            """
            Helper function for remove
            Remove the first node in the list with the given value starting at curr
            :param curr: Starting node looking for node to remove
            Time complexity: O(n)
            """
            if curr.next is None:
                # Base case: End of list
                return
            if curr.next.val == value:
                # Base case: Found node to remove
                curr.next = curr.next.next
                return
            # Recursive case
            remove_inner(curr.next)
        if self.head is None:
            # Empty list
            return
        if self.head.val == value:
            # Remove the head
            self.head = self.head.next
            return
        # Search the rest of the list for node to remove
        remove_inner(self.head)

    def remove_all(self, value: T) -> None:
        """
        Removes all nodes in the list with a given value
        :param value: Value of nodes to remove
        Time complexity: O(n)
        """
        def remove_all_inner(curr):
            """
            Helper function for remove
            Removes all nodes in the list with a given value start at curr
            :param curr: Starting node for looking for nodes to remove
            Time complexity: O(n)
            """
            if curr.next is None:
                # Base case: End of list
                return
            if curr.next.val == value:
                # Recursive case: Removal of Node
                curr.next = curr.next.next
                remove_all_inner(curr.next)
            # Recursive case: No removal
            remove_all_inner(curr.next)
        if self.head is None:
            # Empty list
            return
        # Search the list for nodes to remove
        remove_all_inner(self.head)
        # Check if head needs to be removed
        if self.head.val == value:
            self.head = self.head.next

    def search(self, value: T) -> bool:
        """
        Looks for value in the list and returns true if found, false otherwise
        :param value: Value to search for in the list
        :return: True if value was found in the list, false otherwise
        Time complexity: O(n)
        """
        def search_inner(curr):
            """
            Helper function for search
            Looks for value in the list starting with curr
            :param curr: Starting node for searching for value
            :return: True if the value is found, false otherwise
            Time complexity: O(n)
            """
            if curr is None:
                # Base case: End of list (value was not found)
                return False
            if curr.val == value:
                # Base case: Found the value
                return True
            # Recursive case
            return search_inner(curr.next)
        return search_inner(self.head)

    def count(self, value: T) -> int:
        """
        Counts and returns how many times the given value occurs in the list
        :param value: Value to search for how many occurences in the list
        :return: Number of times the given value occurs in the list
        Time complexity: O(n)
        """
        def count_inner(curr):
            """
            Helper function for count
            Counts and returns how many times the given value occures in the list starting at curr
            :param curr: Starting point for looking for the given value
            :return: Number of times the given value occures in the list
            Time complexity: O(n)
            """
            if curr is None:
                # Base case: End of list
                return 0
            if curr.val == value:
                # Recursive case: Node's value matches value
                return 1 + count_inner(curr.next)
            # Recursive case: Node's value doesn't match value
            return 0 + count_inner(curr.next)
        return count_inner(self.head)

    def reverse(self, curr):
        """
        Given a list starting with head curr, reverse this list.
        :param curr: Starting node for reversing the list
        :return: Head of the reversed list
        Time complexity: O(n)
        """
        if curr is None or curr.next is None:
            # Base case: List is empty or length 1
            return self.head
        temp = curr.next
        curr.next = temp.next
        temp.next = self.head
        self.head = temp
        if curr.next is None:
            # Base case: End of list
            return self.head
        # Recursive case
        return self.reverse(curr)

def crafting(recipe, pockets):
    """
    Given two linked lists, recipe and pockets, determines if the values in the recipe list are 
    contained in the pockets list.
    If all the values in recipe are present in pockets, they will be consumed, and therefore 
    must be removed from pockets.
    :param recipe: Linked list containing all items needed for a recipe
    :param pockets: Linked list containing all items in a player's pockets
    :return: True if the item in the recipe can be crafted, false otherwise
    Time complexity: O(rp)
    """
    matches = RecursiveSinglyLinkList()
    pocketsWithRemoval = RecursiveSinglyLinkList()

    def crafting_pockets(pItem):
        if pItem is None:
            # Base case: End of list
            return
        # Recursive case: Search for pItem in recipe
        if recipe.search(pItem.val):
            matches.push(1)
        else:
            pocketsWithRemoval.push(pItem.val)
            matches.push(0)
        crafting_pockets(pItem.next)

    crafting_pockets(pockets.head)
    if recipe.head is None:
        # Empty recipe condition
        return False
    if matches.sum_list(matches.head) == recipe.length(recipe.head):
        # Successful craft condition
        pockets.head = pocketsWithRemoval.head
        return True
    # Unsuccessful craft condition
    return False
