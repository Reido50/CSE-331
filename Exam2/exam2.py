from typing import List, Generator, TypeVar
from copy import deepcopy
from queue import SimpleQueue

BSTNode = TypeVar('BSTNode') # BST Node Type
BST = TypeVar('BST')         # BST Type
T = TypeVar('T')             # Generic Type

class BSTNode:
    """
    BST Node Class:

    Attributes:
        val  : int
        left : BSTNode
        right: BSTNode
    """

    __slots__ = ['val', 'left', 'right']

    def __init__(self, val: int) -> None:
        """ Initialize BST Node """
        self.val = val
        self.left = self.right = None

    def __str__(self):
        return str(self.val)

    __repr__ = __str__

    def __eq__(self, other: BSTNode):
        return self.val == other.val

class BST:
    """
    BST Class: Contains only unique nodes

    Attributes:
        root: BSTNode
        size: int
    """

    __slots__ = ['root', 'size']

    def __init__(self, vals: List[int] = []) -> None:
        """ Initialize BST """
        self.root = None
        self.size = 0
        for val in vals:
            self.insert(self.root, val)

    def __eq__(self, other: BST) -> bool:
        """ Equality Comparator for BSTs """
        comp = lambda n1, n2: n1==n2 and ((comp(n1.left, n2.left) and comp(n1.right, n2.right)) if (n1 and n2) else True)
        return self.size == other.size and comp(self.root, other.root)

    def insert(self, root: BSTNode, val: int) -> None:
        """ Insert Node in BST """
        if root is None:
            self.root = BSTNode(val)
        elif val < root.val:
            if root.left is None:
                root.left = BSTNode(val)
            else:
                return self.insert(root.left, val)
        elif val > root.val:
            if root.right is None:
                root.right = BSTNode(val)
            else:
                return self.insert(root.right, val)
        self.size += 1

    def break_tree(self, val1: int, val2: int) -> BST:
        """ Creates copy of tree with two specified nodes swapped """

        copy = BST()
        copy.size = self.size
        copy.root = deepcopy(self.root)

        def find(root, val):
            if val < root.val:
                return find(root.left, val)
            elif val > root.val:
                return find(root.right, val)
            return root

        node1 = find(copy.root, val1)
        node2 = find(copy.root, val2)

        node1.val, node2.val = node2.val, node1.val

        return copy

    def inorder(self, root: BSTNode) -> Generator[BSTNode, None, None]:
        """
        Perform an inorder traversal of the subtree rooted at root
        :param root: The root Node of the subtree currently being traversed
        :return: Generator object which yields Node objects only
        """
        if root is None:
            return
        # Check left
        if root.left is not None:
            yield from self.inorder(root.left)
        # Return current if no more left to go
        yield root
        # Check right
        if root.right is not None:
            yield from self.inorder(root.right)

    def levelorder(self, root: BSTNode) -> Generator[BSTNode, None, None]:
        """
        Perform a level-order traversal of the subtree rooted at root
        :param root: The root Node of the subtree being traversed
        :return: Generator object which yields Node objects only
        """
        if root is None:
            return

        yield root

        q = SimpleQueue()
        q.put(root)

        while not q.empty():
            cur = q.get()
            if cur.left is not None:
                yield cur.left
                q.put(cur.left)
            if cur.right is not None:
                yield cur.right
                q.put(cur.right)
        return

#=== complete the following function ===#

def repair_tree(tree: BST) -> None:
    node1 = None    # Always used
    nodealt = None  # Used if misplaced nodes are connected to each other
    node2 = None    # Used if misplaced nodes are not connected to each other

    # Traverse the tree and check for bad nodes
    gen = tree.inorder(tree.root)
    previous = None
    for n in gen:
        # Check previous
        if (previous and n.val < previous.val):
            if not node1:
                # node1 empty, fill it and nodealt
                node1 = previous
                nodealt = n
            else:
                # node2 empty, fill it
                node2 = n
        previous = n

    if (node1 and node2):    
        node1.val, node2.val = node2.val, node1.val
    elif (node1 and nodealt):
        node1.val, nodealt.val = nodealt.val, node1.val
