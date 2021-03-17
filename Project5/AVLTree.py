"""
Project 5
CSE 331 S21 (Onsay)
Your Name
AVLTree.py
"""

import queue
from typing import TypeVar, Generator, List, Tuple

# for more information on typehinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")            # represents generic type
Node = TypeVar("Node")      # represents a Node object (forward-declare to use in Node __init__)
AVLWrappedDictionary = TypeVar("AVLWrappedDictionary")      # represents a custom type used in application


####################################################################################################


class Node:
    """
    Implementation of an AVL tree node.
    Do not modify.
    """
    # preallocate storage: see https://stackoverflow.com/questions/472000/usage-of-slots
    __slots__ = ["value", "parent", "left", "right", "height"]

    def __init__(self, value: T, parent: Node = None,
                 left: Node = None, right: Node = None) -> None:
        """
        Construct an AVL tree node.

        :param value: value held by the node object
        :param parent: ref to parent node of which this node is a child
        :param left: ref to left child node of this node
        :param right: ref to right child node of this node
        """
        self.value = value
        self.parent, self.left, self.right = parent, left, right
        self.height = 0

    def __repr__(self) -> str:
        """
        Represent the AVL tree node as a string.

        :return: string representation of the node.
        """
        return f"<{str(self.value)}>"

    def __str__(self) -> str:
        """
        Represent the AVL tree node as a string.

        :return: string representation of the node.
        """
        return f"<{str(self.value)}>"


####################################################################################################


class AVLTree:
    """
    Implementation of an AVL tree.
    Modify only below indicated line.
    """
    # preallocate storage: see https://stackoverflow.com/questions/472000/usage-of-slots
    __slots__ = ["origin", "size"]

    def __init__(self) -> None:
        """
        Construct an empty AVL tree.
        """
        self.origin = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the AVL tree as a string. Inspired by Anna De Biasi (Fall'20 Lead TA).

        :return: string representation of the AVL tree
        """
        if self.origin is None:
            return "Empty AVL Tree"

        # initialize helpers for tree traversal
        root = self.origin
        result = ""
        q = queue.SimpleQueue()
        levels = {}
        q.put((root, 0, root.parent))
        for i in range(self.origin.height + 1):
            levels[i] = []

        # traverse tree to get node representations
        while not q.empty():
            node, level, parent = q.get()
            if level > self.origin.height:
                break
            levels[level].append((node, level, parent))

            if node is None:
                q.put((None, level + 1, None))
                q.put((None, level + 1, None))
                continue

            if node.left:
                q.put((node.left, level + 1, node))
            else:
                q.put((None, level + 1, None))

            if node.right:
                q.put((node.right, level + 1, node))
            else:
                q.put((None, level + 1, None))

        # construct tree using traversal
        spaces = pow(2, self.origin.height) * 12
        result += "\n"
        result += f"AVL Tree: size = {self.size}, height = {self.origin.height}".center(spaces)
        result += "\n\n"
        for i in range(self.origin.height + 1):
            result += f"Level {i}: "
            for node, level, parent in levels[i]:
                level = pow(2, i)
                space = int(round(spaces / level))
                if node is None:
                    result += " " * space
                    continue
                if not isinstance(self.origin.value, AVLWrappedDictionary):
                    result += f"{node} ({parent} {node.height})".center(space, " ")
                else:
                    result += f"{node}".center(space, " ")
            result += "\n"
        return result

    def __str__(self) -> str:
        """
        Represent the AVL tree as a string. Inspired by Anna De Biasi (Fall'20 Lead TA).

        :return: string representation of the AVL tree
        """
        return repr(self)

    def height(self, root: Node) -> int:
        """
        Return height of a subtree in the AVL tree, properly handling the case of root = None.
        Recall that the height of an empty subtree is -1.

        :param root: root node of subtree to be measured
        :return: height of subtree rooted at `root` parameter
        """
        return root.height if root is not None else -1

    def left_rotate(self, root: Node) -> Node:
        """
        Perform a left rotation on the subtree rooted at `root`. Return new subtree root.

        :param root: root node of unbalanced subtree to be rotated.
        :return: new root node of subtree following rotation.
        """
        if root is None:
            return None

        # pull right child up and shift right-left child across tree, update parent
        new_root, rl_child = root.right, root.right.left
        root.right = rl_child
        if rl_child is not None:
            rl_child.parent = root

        # right child has been pulled up to new root -> push old root down left, update parent
        new_root.left = root
        new_root.parent = root.parent
        if root.parent is not None:
            if root is root.parent.left:
                root.parent.left = new_root
            else:
                root.parent.right = new_root
        root.parent = new_root

        # handle tree origin case
        if root is self.origin:
            self.origin = new_root

        # update heights and return new root of subtree
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        return new_root

    ########################################
    # Implement functions below this line. #
    ########################################

    def right_rotate(self, root: Node) -> Node:
        """
        Perform a right rotation on the subtree rooted at 'root'. Return new subtree root

        :param root: root node of unbalanced subtree to be rotated.
        :return: new root node of subtree following rotation.
        """
        if root is None:
            return None

        # pull left child up and shift left-right child across tree, update parent
        new_root, rl_child = root.left, root.left.right
        root.left = rl_child
        if rl_child is not None:
            rl_child.parent = root

        # left child has been pulled up to new root -> push old root down right, update parent
        new_root.right = root
        new_root.parent = root.parent
        if root.parent is not None:
            if root is root.parent.right:
                root.parent.right = new_root
            else:
                root.parent.left = new_root
        root.parent = new_root

        # handle tree origin case
        if root is self.origin:
            self.origin = new_root

        # update heights and return new root of subtree
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        new_root.height = 1 + max(self.height(new_root.left), self.height(new_root.right))
        return new_root

    def balance_factor(self, root: Node) -> int:
        """
        Computer balance factor of the subtree rooted at root
        :param root: The root Node of the subtree on which to compute the balance factor
        :return: int representing the balance factor of root
        """
        # Check for root of none
        if root is None:
            return 0
        
        # Find heights of right and left subtree
        left_height = -1
        right_height = -1
        if root.left is not None:
            left_height = root.left.height
        if root.right is not None:
            right_height = root.right.height

        # Compute and return balance factor
        return left_height - right_height

    def rebalance(self, root: Node) -> Node:
        """
        Rebalance the subtree rooted at root and return the new root of the resulting subtree
        :param root: Root of the subtree in which to rebalance
        :return: Root of new subtree after rebalancing
        """
        def rightcase() -> Node:
            """
            Do a Right-Right or Right-Left rotation
            :return: New root of the subtree
            """
            if self.balance_factor(root.right) > 0:
                # Right Left case
                self.right_rotate(root.right)
                return self.left_rotate(root)
            else:
                # Right Right case
                return self.left_rotate(root)

        def leftcase() -> Node:
            """
            Do a Left-Left or Left-Right rotation
            :return: New root of the subtree
            """
            if self.balance_factor(root.left) < 0:
                # Left Right case
                self.left_rotate(root.left)
                return self.right_rotate(root)
            else:
                # Left Left case
                return self.right_rotate(root)


        # Check if the subtree doesn't need rebalancing
        if abs(self.balance_factor(root)) <= 1:
            return root
        
        # Determine if it's a left case or right case
        new_root = None
        if root.left is None:
            new_root = rightcase()
        elif root.right is None:
            new_root = leftcase()
        elif root.right.height > root.left.height:
            new_root = rightcase()
        else:
            new_root = leftcase()

        return new_root

    def insert(self, root: Node, val: T) -> Node:
        """
        Insert a node with val into the subtree rooted at root
        :param root: Root of the subtree in which the node with val will be inserted
        :param val: Value for the inserted node
        :return: Root of the subtree after insertion and rebalancing
        """
        # Check if empty
        if self.origin is None:
            self.origin = Node(val)
            self.size += 1
            return self.origin

        if val > root.value:
            # Try to insert into right
            if root.right is None:
                # Base case: Inserted into right
                root.right = Node(val, root)
                self.size += 1
            else:
                # Recursive case: Search right
                self.insert(root.right, val)
        elif val < root.value:
            # Try to insert into left
            if root.left is None:
                # Base case: Inserted into left
                root.left = Node(val, root)
                self.size += 1
            else:
                # Recursive case: Search left
                self.insert(root.left, val)
        else:
            return self.rebalance(root)

        # Update height
        root.height = 1 + max(self.height(root.right), self.height(root.left))
        # Rebalance the ancestors
        return self.rebalance(root)

    def min(self, root: Node) -> Node:
        """
        Find and return the Node with the smallest value in the subtree rooted at root
        :param root: Root node of the subtree in which to search for a min
        :return: Node with the smallest value in the subtree
        """
        # Check for root of none
        if root is None:
            return None

        # If there is not a left child, return itself
        if root.left is None:
            return root
        return self.min(root.left)

    def max(self, root: Node) -> Node:
        """
        Find and return the Node with the largest value in the subtree rooted at root
        :param root: Root node of the subtree in which to search for a max
        :return: Node with the largest value in the subtree
        """
        # Check for root of none
        if root is None:
            return None

        # If there is not a right child, return itself
        if root.right is None:
            return root
        return self.max(root.right)

    def search(self, root: Node, val: T) -> Node:
        """
        Find and return the Node with the largest value in the subtree rooted at root
        If not found, return the Node below which val would be inserted as a child
        :param root: The root Node of the subtree to search
        :param val: The value being searched in the subtree
        :return: Node containing val if it exists, else the Node object below which val would be inserted as a child
        """
        # Check for root of none
        if root is None:
            return None

        # Determine whether val is left or right
        if val > root.value:
            if root.right is None:
                return root
            return self.search(root.right, val)
        elif val < root.value:
            if root.left is None:
                return root
            return self.search(root.left, val)
        else:
            return root

    def inorder(self, root: Node) -> Generator[Node, None, None]:
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
            

    def preorder(self, root: Node) -> Generator[Node, None, None]:
        """
        Perform a preorder traversal of the subtree rooted at root
        :param root: The root Node of the subtree currently being traversed
        :return: Generator object which yields Node objects only
        """
        if root is None:
            return
        # Return current
        yield root
        # Check left
        if root.left is not None:
            yield from self.preorder(root.left)
        # Check right
        if root.right is not None:
            yield from self.preorder(root.right)

    def postorder(self, root: Node) -> Generator[Node, None, None]:
        """
        Perform a postorder traversal of the subtree rooted at root
        :param root: The root Node of the subtree currently being traversed
        :return: Generator object which yields Node objects only
        """
        if root is None:
            return
        # Check left
        if root.left is not None:
            yield from self.postorder(root.left)
        # Check right
        if root.right is not None:
            yield from self.postorder(root.right)
        # Return current after left and right
        yield root

    def levelorder(self, root: Node) -> Generator[Node, None, None]:
        """
        Perform a level-order traversal of the subtree rooted at root
        :param root: The root Node of the subtree being traversed
        :return: Generator object which yields Node objects only
        """
        if root is None:
            return

        yield root

        q = queue.SimpleQueue()
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

    def remove(self, root: Node, val: T) -> Node:
        """
        Removes the node with value val from the subtree rooted at root and returns the root
        :param root: The root Node of the subtree from which to delete val
        :return: Root of new subtree after removal and rebalancing (could be the original root)
        """
        # Check if empty
        if root is None:
            return root

        remorigin = False

        if val < root.value:
            # Check left
            root.left = self.remove(root.left, val)
        elif val > root.value:
            # Check right
            root.right = self.remove(root.right, val)
        else:
            # Remove root
            self.size -= 1
            if root is self.origin:
                remorigin = True
            if root.right is None and root.left is None:
                # Remove leaf node
                if remorigin:
                    self.origin = None
                return None
            elif root.right is not None and root.left is None:
                # Remove node with only right child
                temp = root.right
                root = None
                if remorigin:
                    self.origin = temp
                return temp
            elif root.right is None and root.left is not None:
                # Remove node with only left child
                temp = root.left
                root = None
                if remorigin:
                    self.origin = temp
                return temp
            else:
                # Remove node with two children
                pred = self.max(root.left)
                root.value = pred.value
                self.size += 1  # Accounts for the second removal
                root.left = self.remove(root.left, pred.value)
        # Update height
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # Rebalance and return
        return self.rebalance(root)


avl = AVLTree()
avl.insert(avl.origin, 0)
avl.insert(avl.origin, 1)
avl.insert(avl.origin, 2)
avl.insert(avl.origin, 3)

print(str(avl.origin))
print(str(avl.origin.left))
print(str(avl.origin.right))
print()
print(str(avl.remove(avl.origin, 3)))
print(str(avl.origin.left))
print(str(avl.origin.right))


####################################################################################################


class AVLWrappedDictionary:
    """
    Implementation of a helper class which will be used as tree node values in the
    NearestNeighborClassifier implementation. Compares objects with keys less than
    1e-6 apart as equal.
    """
    # preallocate storage: see https://stackoverflow.com/questions/472000/usage-of-slots
    __slots__ = ["key", "dictionary"]

    def __init__(self, key: float) -> None:
        """
        Construct a AVLWrappedDictionary with a key to search/sort on and a dictionary to hold data.

        :param key: floating point key to be looked up by.
        """
        self.key = key
        self.dictionary = {}

    def __repr__(self) -> str:
        """
        Represent the AVLWrappedDictionary as a string.

        :return: string representation of the AVLWrappedDictionary.
        """
        return f"key: {self.key}, dict: {self.dictionary}"

    def __str__(self) -> str:
        """
        Represent the AVLWrappedDictionary as a string.

        :return: string representation of the AVLWrappedDictionary.
        """
        return f"key: {self.key}, dict: {self.dictionary}"

    def __eq__(self, other: AVLWrappedDictionary) -> bool:
        """
        Implement == operator to compare 2 AVLWrappedDictionaries by key only.
        Compares objects with keys less than 1e-6 apart as equal.

        :param other: other AVLWrappedDictionary to compare with
        :return: boolean indicating whether keys of AVLWrappedDictionaries are equal
        """
        return abs(self.key - other.key) < 1e-6

    def __lt__(self, other: AVLWrappedDictionary) -> bool:
        """
        Implement < operator to compare 2 AVLWrappedDictionarys by key only.
        Compares objects with keys less than 1e-6 apart as equal.

        :param other: other AVLWrappedDictionary to compare with
        :return: boolean indicating ordering of AVLWrappedDictionaries
        """
        return self.key < other.key and not abs(self.key - other.key) < 1e-6

    def __gt__(self, other: AVLWrappedDictionary) -> bool:
        """
        Implement > operator to compare 2 AVLWrappedDictionaries by key only.
        Compares objects with keys less than 1e-6 apart as equal.

        :param other: other AVLWrappedDictionary to compare with
        :return: boolean indicating ordering of AVLWrappedDictionaries
        """
        return self.key > other.key and not abs(self.key - other.key) < 1e-6


class NearestNeighborClassifier:
    """
    Implementation of a one-dimensional nearest-neighbor classifier with AVL tree lookups.
    Modify only below indicated line.
    """
    # preallocate storage: see https://stackoverflow.com/questions/472000/usage-of-slots
    __slots__ = ["resolution", "tree"]

    def __init__(self, resolution: int) -> None:
        """
        Construct a one-dimensional nearest neighbor classifier with AVL tree lookups.
        Data are assumed to be floating point values in the closed interval [0, 1].

        :param resolution: number of decimal places the data will be rounded to, effectively
                           governing the capacity of the model - for example, with a resolution of
                           1, the classifier could maintain up to 11 nodes, spaced 0.1 apart - with
                           a resolution of 2, the classifier could maintain 101 nodes, spaced 0.01
                           apart, and so on - the maximum number of nodes is bounded by
                           10^(resolution) + 1.
        """
        self.tree = AVLTree()
        self.resolution = resolution

        # pre-construct lookup tree with AVLWrappedDictionary objects storing (key, dictionary)
        # pairs, but which compare with <, >, == on key only
        for i in range(10**resolution + 1):
            w_dict = AVLWrappedDictionary(key=(i/10**resolution))
            self.tree.insert(self.tree.origin, w_dict)

    def __repr__(self) -> str:
        """
        Represent the NearestNeighborClassifier as a string.

        :return: string representation of the NearestNeighborClassifier.
        """
        return f"NNC(resolution={self.resolution}):\n{self.tree}"

    def __str__(self) -> str:
        """
        Represent the NearestNeighborClassifier as a string.

        :return: string representation of the NearestNeighborClassifier.
        """
        return f"NNC(resolution={self.resolution}):\n{self.tree}"

    def fit(self, data: List[Tuple[float, str]]) -> None:
        """
        Fits the one-dimensional NearestNeighborClassifier to data
        :param data: A list of (float,str) pairs associating feature x values in the range [0, 1] to target y values.
        """
        # Iterate through the list
        for tup in data:
            # Round x to the number of digits specified by self.resolution
            rounded = round(tup[0], self.resolution)
            searchterm = AVLWrappedDictionary(rounded)
            node = self.tree.search(self.tree.origin, searchterm)
            if node.value.dictionary.get(tup[1]) is None:
                node.value.dictionary[tup[1]] = 1
            else:
                node.value.dictionary[tup[1]] += 1


    def predict(self, x: float, delta: float) -> str:
        """
        Predicts the class label of a single x value
        :param x: Feature value in range [0, 1] with unknown class to be predicted
        :param delta: Width of interval to search across for neighbors of x
        :return: str of the predicted class label y
        """
        rounded = round(x, self.resolution)
        count = {}
        searchnum = max(rounded - delta, 0)
        while searchnum <= min(rounded + delta, 1):
            searchterm = AVLWrappedDictionary(searchnum)
            found = self.tree.search(self.tree.origin, searchterm)
            if found is not None:
                if found.value == searchterm:
                    for key in found.value.dictionary:
                        if count.get(key) is None:
                            count[key] = found.value.dictionary[key]
                        else:
                            count[key] += found.value.dictionary[key]
            searchnum += pow(0.1, self.resolution)
        if len(count) == 0:
            return None
        else:
            maxclass = "null"
            maxnum = -1
            for key in count:
                if count[key] > maxnum:
                    maxclass = key
                    maxnum = count[key]
            return maxclass
