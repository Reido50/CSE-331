"""
Project 5
CSE 331 S21 (Onsay)
Andrew McDonald & Bank Premsri
Inspired by Brandon Field and Anna DeBiasi's implementation
tests.py
"""

import unittest
import random
import types
#import numpy as np
#import matplotlib.pyplot as plt
from AVLTree import Node, AVLTree, AVLWrappedDictionary, NearestNeighborClassifier


class AVLTreeTests(unittest.TestCase):

    def test_rotate(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.right_rotate(avl.origin))
        self.assertIsNone(avl.left_rotate(avl.origin))

        """
        (1) test basic right
        initial structure:
            3
           /
          2
         /
        1
        final structure:
          2
         / \
        1   3
        """
        avl.origin = Node(3)
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.size = 3

        node = avl.right_rotate(avl.origin)
        #print(avl)
        self.assertIsInstance(node, Node)

        assert avl.origin.value == 2 and not avl.origin.parent  # root value and parent
        assert avl.origin.left.value == 1 and avl.origin.left.parent == avl.origin  # root left value and parent
        assert not (avl.origin.left.left or avl.origin.left.right)  # shouldn't have children
        assert avl.origin.right.value == 3 and avl.origin.right.parent == avl.origin  # root right value and parent
        assert not (avl.origin.right.right or avl.origin.right.left)  # shouldn't have children

        """
        (2) test basic left
        initial structure:
        1
         \
          2
           \
            3
        final structure:
          2
         / \
        1   3
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.right = Node(2, parent=avl.origin)
        avl.origin.right.right = Node(3, parent=avl.origin.right)
        avl.size = 3

        node = avl.left_rotate(avl.origin)
        self.assertIsInstance(node, Node)

        assert avl.origin.value == 2 and not avl.origin.parent  # root value and parent
        assert avl.origin.left.value == 1 and avl.origin.left.parent == avl.origin  # root left value and parent
        assert not (avl.origin.left.left or avl.origin.left.right)  # shouldn't have any children
        assert avl.origin.right.value == 3 and avl.origin.right.parent == avl.origin  # root right value and parent
        assert not (avl.origin.right.right or avl.origin.right.left)  # shouldn't have any children

        """
        (3) test intermediate right, rotating at origin
        initial structure:
              7
             / \
            3   10
           / \
          2   4
         /
        1 
        final structure:
            3
           / \
          2   7
         /   / \
        1   4   10
        """
        avl = AVLTree()
        avl.origin = Node(7)
        avl.origin.left = Node(3, parent=avl.origin)
        avl.origin.left.left = Node(2, parent=avl.origin.left)
        avl.origin.left.left.left = Node(1, parent=avl.origin.left.left)
        avl.origin.left.right = Node(4, parent=avl.origin.left)
        avl.origin.right = Node(10, parent=avl.origin)

        node = avl.right_rotate(avl.origin)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node3 = avl.origin
        node2 = avl.origin.left
        node1 = avl.origin.left.left
        node7 = avl.origin.right
        node4 = avl.origin.right.left
        node10 = avl.origin.right.right

        assert node3.value == 3 and not node3.parent
        assert node2.value == 2 and node2.parent == node3 and not node2.right
        assert node1.value == 1 and node1.parent == node2 and not (node1.left or node1.right)
        assert node7.value == 7 and node7.parent == node3 and node7.left == node4 and node7.right == node10
        assert node4.value == 4 and node4.parent == node7 and not (node4.left or node4.right)
        assert node10.value == 10 and node10.parent == node7 and not (node10.left or node10.right)

        """
        (4) test intermediate left, rotating at origin
        initial structure:
          7
         /  \
        3   10
           /   \
          9    11
                 \
                  12
        final structure:
        	10
           /  \
          7   11
         / \    \
        3   9    12
        """
        avl = AVLTree()
        avl.origin = Node(7)
        avl.origin.left = Node(3, parent=avl.origin)
        avl.origin.right = Node(10, parent=avl.origin)
        avl.origin.right.left = Node(9, parent=avl.origin.right)
        avl.origin.right.right = Node(11, parent=avl.origin.right)
        avl.origin.right.right.right = Node(12, parent=avl.origin.right.right)

        node = avl.left_rotate(avl.origin)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node10 = avl.origin
        node7 = avl.origin.left
        node3 = avl.origin.left.left
        node9 = avl.origin.left.right
        node11 = avl.origin.right
        node12 = avl.origin.right.right

        assert node10.value == 10 and not node10.parent
        assert node7.value == 7 and node7.parent == node10
        assert node3.value == 3 and node3.parent == node7 and not (node3.left or node3.right)
        assert node9.value == 9 and node9.parent == node7 and not (node9.left or node9.right)
        assert node11.value == 11 and node11.parent == node10 and not node11.left
        assert node12.value == 12 and node12.parent == node11 and not (node12.left or node12.right)

        """
        (5) test advanced right, rotating not at origin
        initial structure:
        		10
        	   /  \
        	  5	   11
        	 / \     \
        	3	7    12
           / \
          2   4
         /
        1
        final structure:
              10
             /  \
            3    11
           / \     \
          2   5     12
         /   / \
        1   4   7
        """
        avl = AVLTree()
        avl.origin = Node(10)
        avl.origin.right = Node(11, parent=avl.origin)
        avl.origin.right.right = Node(12, parent=avl.origin.right)
        avl.origin.left = Node(5, parent=avl.origin)
        avl.origin.left.right = Node(7, parent=avl.origin.left)
        avl.origin.left.left = Node(3, parent=avl.origin.left)
        avl.origin.left.left.right = Node(4, parent=avl.origin.left.left)
        avl.origin.left.left.left = Node(2, parent=avl.origin.left.left)
        avl.origin.left.left.left.left = Node(1, parent=avl.origin.left.left.left)

        node = avl.right_rotate(avl.origin.left)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node10 = avl.origin
        node11 = avl.origin.right
        node12 = avl.origin.right.right
        node3 = avl.origin.left
        node2 = avl.origin.left.left
        node1 = avl.origin.left.left.left
        node5 = avl.origin.left.right
        node4 = avl.origin.left.right.left
        node7 = avl.origin.left.right.right

        assert node10.value == 10 and not node10.parent
        assert node3.value == 3 and node3.parent == node10
        assert node2.value == 2 and node2.parent == node3 and not node2.right
        assert node1.value == 1 and node1.parent == node2 and not (node1.left or node1.right)
        assert node5.value == 5 and node5.parent == node3
        assert node4.value == 4 and node4.parent == node5 and not (node4.left or node4.right)
        assert node7.value == 7 and node7.parent == node5 and not (node7.left or node7.right)
        assert node11.value == 11 and node11.parent == node10 and not node11.left
        assert node12.value == 12 and node12.parent == node11 and not (node12.left or node12.right)

        """
        (6) test advanced left, rotating not at origin
        initial structure:
        	3
           / \
          2   10
         /   /  \
        1   5   12
               /  \
              11   13
                     \
                      14
        final structure:
        	3
           / \
          2   12
         /   /  \
        1   10   13
           /  \    \
          5   11   14
        """
        avl = AVLTree()
        avl.origin = Node(3)
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.right = Node(10, parent=avl.origin)
        avl.origin.right.left = Node(5, parent=avl.origin.right)
        avl.origin.right.right = Node(12, parent=avl.origin.right)
        avl.origin.right.right.left = Node(11, parent=avl.origin.right.right)
        avl.origin.right.right.right = Node(13, parent=avl.origin.right.right)
        avl.origin.right.right.right.right = Node(14, parent=avl.origin.right.right.right)

        node = avl.left_rotate(avl.origin.right)
        self.assertIsInstance(node, Node)

        # note: node variable names correspond to node values as shown in image above
        node3 = avl.origin
        node2 = avl.origin.left
        node1 = avl.origin.left.left
        node12 = avl.origin.right
        node10 = avl.origin.right.left
        node5 = avl.origin.right.left.left
        node11 = avl.origin.right.left.right
        node13 = avl.origin.right.right
        node14 = avl.origin.right.right.right

        assert node3.value == 3 and not node3.parent
        assert node2.value == 2 and node2.parent == node3 and not node2.right
        assert node1.value == 1 and node1.parent == node2 and not (node1.left or node1.right)
        assert node12.value == 12 and node12.parent == node3
        assert node10.value == 10 and node10.parent == node12
        assert node5.value == 5 and node5.parent == node10 and not (node5.left or node5.right)
        assert node11.value == 11 and node11.parent == node10 and not (node11.left or node11.right)
        assert node13.value == 13 and node13.parent == node12 and not node13.left
        assert node14.value == 14 and node14.parent == node13 and not (node14.left or node14.right)

    def test_balance_factor(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertEqual(0, avl.balance_factor(avl.origin))

        """
        (1) test on balanced tree
        structure:
          2
         / \
        1   3
        """
        avl.origin = Node(2)
        avl.origin.height = 1
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 0
        avl.size = 3

        self.assertEqual(0, avl.balance_factor(avl.origin))
        self.assertEqual(0, avl.balance_factor(avl.origin.left))
        self.assertEqual(0, avl.balance_factor(avl.origin.right))

        """
        (2) test on unbalanced left
        structure:
            3
           /
          2
         /
        1
        """
        avl = AVLTree()
        avl.origin = Node(3)
        avl.origin.height = 2
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 1
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.size = 3

        self.assertEqual(2, avl.balance_factor(avl.origin))
        self.assertEqual(1, avl.balance_factor(avl.origin.left))
        self.assertEqual(0, avl.balance_factor(avl.origin.left.left))

        """
        (2) test on unbalanced right
        structure:
        1
         \
          2
           \
            3
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.height = 2
        avl.origin.right = Node(2, parent=avl.origin)
        avl.origin.right.height = 1
        avl.origin.right.right = Node(3, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.size = 3

        self.assertEqual(-2, avl.balance_factor(avl.origin))
        self.assertEqual(-1, avl.balance_factor(avl.origin.right))
        self.assertEqual(0, avl.balance_factor(avl.origin.right.right))

    def test_rebalance(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.rebalance(avl.origin))

        """
        (1) test balanced tree (do nothing)
        initial and final structure:
          2
         / \
        1   3
        since pointers are already tested in rotation testcase, only check values and heights
        """
        avl.origin = Node(2)
        avl.origin.height = 1
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 0
        avl.size = 3

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(2, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (2) test left-left rebalance
        initial structure:
            4
           /
          2
         / \
        1   3
        final structure:
          2
         / \
        1   4
           /
          3
        """
        avl = AVLTree()
        avl.origin = Node(4)
        avl.origin.height = 2
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 1
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.origin.left.right = Node(3, parent=avl.origin.left)
        avl.origin.left.right.height = 0
        avl.size = 4

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(2, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(3, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)

        """
        (2) test right-right rebalance
        initial structure:
        1
         \
          3
         /  \
        2    4
        final structure:
          3
         / \
        1   4
         \
          2
        """
        avl = AVLTree()
        avl.origin = Node(1)
        avl.origin.height = 2
        avl.origin.right = Node(3, parent=avl.origin)
        avl.origin.right.height = 1
        avl.origin.right.right = Node(4, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.origin.right.left = Node(2, parent=avl.origin.right)
        avl.origin.right.left.height = 0
        avl.size = 4

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)
        self.assertEqual(2, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)

        """
        (4) test left-right rebalance
        initial structure:
            5
           / \
          2   6
         / \
        1   3
             \
              4
        intermediate structure:
              5
             / \
            3   6
           / \
          2   4
         /
        1
        final structure:
            3 
           / \
          2   5
         /   / \
        1   4   6
        """
        avl = AVLTree()
        avl.origin = Node(5)
        avl.origin.height = 3
        avl.origin.left = Node(2, parent=avl.origin)
        avl.origin.left.height = 2
        avl.origin.right = Node(6, parent=avl.origin)
        avl.origin.right.height = 0
        avl.origin.left.left = Node(1, parent=avl.origin.left)
        avl.origin.left.left.height = 0
        avl.origin.left.right = Node(3, parent=avl.origin.left)
        avl.origin.left.right.height = 1
        avl.origin.left.right.right = Node(4, parent=avl.origin.left.right)
        avl.origin.left.right.right.height = 0

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        """
        (5) test right-left rebalance
        initial structure:
          2
         / \
        1   5
           / \
          4   6
         /
        3
        intermediate structure:
          2
         / \
        1   4
           / \
          3   5
               \
                6
        final structure:
            4 
           / \
          2   5
         / \   \
        1   3   6
        """
        avl = AVLTree()
        avl.origin = Node(2)
        avl.origin.height = 3
        avl.origin.left = Node(1, parent=avl.origin)
        avl.origin.left.height = 0
        avl.origin.right = Node(5, parent=avl.origin)
        avl.origin.right.height = 2
        avl.origin.right.left = Node(4, parent=avl.origin.right)
        avl.origin.right.left.height = 1
        avl.origin.right.right = Node(6, parent=avl.origin.right)
        avl.origin.right.right.height = 0
        avl.origin.right.left.left = Node(3, parent=avl.origin.right.left)
        avl.origin.right.left.left.height = 0

        node = avl.rebalance(avl.origin)
        self.assertIsInstance(node, Node)

        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

    def test_insert(self):

        # visualize this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        avl = AVLTree()
        """
        (1) test insertion causing right-right rotation
        final structure
          1
         / \
        0   3
           / \
          2   4
        """
        for i in range(5):
            node = avl.insert(avl.origin, i)
            self.assertIsInstance(node, Node)
        self.assertEqual(5, avl.size)
        self.assertEqual(1, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(0, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(2, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(4, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        """
        (2) test insertion causing left-left rotation
        final structure
            3
           / \
          1   4
         / \
        0   2
        """
        avl = AVLTree()
        for i in range(4, -1, -1):
            node = avl.insert(avl.origin, i)
            self.assertIsInstance(node, Node)
        self.assertEqual(5, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(2, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)

        """
        (3) test insertion (with duplicates) causing left-right rotation
        initial structure:
            5
           / \
          2   6
         / \
        1   3
             \
              4
        final structure:
            3 
           / \
          2   5
         /   / \
        1   4   6
        """
        avl = AVLTree()
        for i in [5, 2, 6, 1, 3] * 2 + [4]:
            node = avl.insert(avl.origin, i)
            self.assertIsInstance(node, Node)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        """
        (4) test insertion (with duplicates) causing right-left rotation
        initial structure:
          2
         / \
        1   5
           / \
          4   6
         /
        3
        final structure:
            4 
           / \
          2   5
         / \   \
        1   3   6
        """
        avl = AVLTree()
        for i in [2, 1, 5, 4, 6] * 2 + [3]:
            node = avl.insert(avl.origin, i)
            self.assertIsInstance(node, Node)
        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(1, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)
        self.assertEqual(6, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

    def test_min_max(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.min(avl.origin))
        self.assertIsNone(avl.max(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        min_node, max_node = avl.min(avl.origin), avl.max(avl.origin)
        self.assertIsInstance(min_node, Node)
        self.assertIsInstance(max_node, Node)
        self.assertEqual(0, min_node.value)
        self.assertEqual(9, max_node.value)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        min_node, max_node = avl.min(avl.origin), avl.max(avl.origin)
        self.assertIsInstance(min_node, Node)
        self.assertIsInstance(max_node, Node)
        self.assertEqual(-100, min_node.value)
        self.assertEqual(100, max_node.value)

        """(3) large random tree"""
        random.seed(331)
        avl = AVLTree()
        numbers = [random.randint(-1000, 1000) for _ in range(1000)]
        for num in numbers:
            avl.insert(avl.origin, num)
        min_node, max_node = avl.min(avl.origin), avl.max(avl.origin)
        self.assertIsInstance(min_node, Node)
        self.assertIsInstance(max_node, Node)
        self.assertEqual(min(numbers), min_node.value)
        self.assertEqual(max(numbers), max_node.value)

    def test_search(self):

        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.search(avl.origin, 0))

        """
        (1) search small basic tree
        tree structure
          1
         / \
        0   3
           / \
          2   4
        """
        avl = AVLTree()
        numbers = [1, 0, 3, 2, 4]
        for num in numbers:
            avl.insert(avl.origin, num)
        # search existing numbers
        for num in numbers:
            node = avl.search(avl.origin, num)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        # search non-existing numbers and ensure parent of where value would go is returned
        pairs = [(-1, 0), (0.5, 0), (5, 4), (2.5, 2), (3.5, 4), (-1e5, 0), (1e5, 4)]
        for target, closest in pairs:
            node = avl.search(avl.origin, target)
            self.assertIsInstance(node, Node)
            self.assertEqual(closest, node.value)

        """(2) search large random tree"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(1000)}
        for num in numbers:
            avl.insert(avl.origin, num)
        for num in numbers:
            # search existing number
            node = avl.search(avl.origin, num)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)

            # if this node is a leaf, search non-existing numbers around it
            # to ensure it is returned as the parent of where new insertions would go
            if node.left is None and node.right is None:
                node = avl.search(avl.origin, num + 0.1)
                self.assertIsInstance(node, Node)
                self.assertEqual(num, node.value)
                node = avl.search(avl.origin, num - 0.1)
                self.assertIsInstance(node, Node)
                self.assertEqual(num, node.value)

    def test_inorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.inorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = list(range(10))
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = list(range(-100, 101))
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(1000)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = sorted(numbers)
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)


    def test_preorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.preorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [3, 1, 0, 2, 7, 5, 4, 6, 8, 9]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [27, -37, -69, -85, -93, -97, -99, -100, -98, -95, -96, -94, -89, -91, -92, -90, -87, -88, -86, -77,
                    -81, -83, -84, -82, -79, -80, -78, -73, -75, -76, -74, -71, -72, -70, -53, -61, -65, -67, -68, -66,
                    -63, -64, -62, -57, -59, -60, -58, -55, -56, -54, -45, -49, -51, -52, -50, -47, -48, -46, -41, -43,
                    -44, -42, -39, -40, -38, -5, -21, -29, -33, -35, -36, -34, -31, -32, -30, -25, -27, -28, -26, -23,
                    -24, -22, -13, -17, -19, -20, -18, -15, -16, -14, -9, -11, -12, -10, -7, -8, -6, 11, 3, -1, -3, -4,
                    -2, 1, 0, 2, 7, 5, 4, 6, 9, 8, 10, 19, 15, 13, 12, 14, 17, 16, 18, 23, 21, 20, 22, 25, 24, 26, 59,
                    43, 35, 31, 29, 28, 30, 33, 32, 34, 39, 37, 36, 38, 41, 40, 42, 51, 47, 45, 44, 46, 49, 48, 50, 55,
                    53, 52, 54, 57, 56, 58, 75, 67, 63, 61, 60, 62, 65, 64, 66, 71, 69, 68, 70, 73, 72, 74, 91, 83, 79,
                    77, 76, 78, 81, 80, 82, 87, 85, 84, 86, 89, 88, 90, 95, 93, 92, 94, 97, 96, 99, 98, 100]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(1000)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [0, -355, -686, -859, -930, -963, -984, -991, -995, -996, -993, -987, -990, -986, -973, -979, -981,
                    -976, -967, -969, -965, -944, -953, -955, -960, -954, -951, -952, -948, -938, -941, -942, -940,
                    -933, -935, -932, -890, -915, -923, -926, -927, -925, -918, -919, -917, -905, -912, -914, -908,
                    -899, -900, -894, -875, -882, -886, -889, -884, -877, -881, -876, -866, -871, -874, -868, -862,
                    -864, -860, -767, -815, -839, -849, -852, -856, -850, -845, -847, -843, -823, -834, -836, -833,
                    -819, -821, -818, -786, -804, -812, -813, -807, -791, -798, -789, -782, -784, -785, -783, -770,
                    -774, -768, -730, -751, -760, -762, -763, -761, -758, -759, -752, -740, -744, -750, -743, -738,
                    -739, -736, -707, -717, -724, -725, -720, -712, -715, -708, -702, -705, -706, -704, -690, -701,
                    -689, -504, -589, -642, -659, -673, -677, -678, -675, -671, -672, -661, -650, -656, -657, -655,
                    -646, -648, -645, -618, -628, -638, -640, -629, -622, -623, -621, -606, -609, -611, -607, -600,
                    -604, -598, -546, -571, -576, -579, -585, -577, -574, -575, -572, -561, -567, -570, -565, -551,
                    -556, -549, -526, -538, -540, -543, -539, -529, -536, -527, -514, -521, -524, -520, -506, -507,
                    -505, -419, -453, -486, -498, -500, -502, -499, -493, -497, -487, -466, -476, -481, -470, -458,
                    -461, -454, -439, -447, -449, -450, -448, -443, -445, -441, -432, -435, -436, -434, -428, -430,
                    -422, -386, -401, -411, -415, -417, -413, -404, -408, -402, -394, -399, -400, -396, -390, -392,
                    -389, -369, -378, -380, -381, -379, -371, -377, -370, -359, -366, -368, -360, -357, -358, -356,
                    -188, -276, -307, -325, -338, -345, -349, -343, -334, -336, -330, -313, -320, -324, -316, -310,
                    -312, -308, -293, -299, -302, -305, -301, -297, -298, -294, -284, -288, -291, -287, -279, -281,
                    -278, -234, -255, -263, -269, -270, -268, -260, -262, -259, -242, -247, -248, -245, -239, -240,
                    -235, -214, -222, -229, -233, -226, -216, -217, -215, -202, -212, -213, -207, -192, -195, -190,
                    -113, -149, -166, -175, -182, -187, -181, -172, -173, -167, -161, -164, -165, -163, -156, -157,
                    -151, -127, -142, -146, -148, -145, -132, -136, -128, -119, -122, -125, -121, -116, -118, -114, -34,
                    -70, -89, -97, -108, -111, -103, -93, -96, -90, -78, -82, -85, -79, -75, -77, -74, -54, -59, -65,
                    -68, -61, -57, -58, -56, -43, -52, -53, -47, -41, -42, -38, -19, -28, -31, -33, -29, -25, -26, -24,
                    -12, -16, -17, -13, -5, -9, -10, -6, -4, -2, 647, 307, 160, 78, 40, 26, 15, 9, 11, 24, 16, 25, 35,
                    33, 28, 34, 37, 36, 39, 58, 48, 44, 41, 45, 50, 49, 57, 68, 60, 59, 67, 73, 71, 77, 125, 105, 89,
                    85, 84, 86, 101, 94, 102, 114, 109, 108, 113, 117, 116, 123, 144, 137, 128, 127, 134, 142, 139, 143,
                    155, 151, 146, 154, 158, 157, 159, 231, 203, 185, 169, 165, 164, 168, 176, 170, 177, 194, 188, 187,
                    193, 197, 195, 200, 215, 209, 205, 204, 206, 212, 210, 213, 223, 221, 220, 222, 229, 224, 230, 266,
                    251, 240, 234, 233, 237, 244, 241, 246, 256, 254, 253, 255, 260, 257, 263, 283, 279, 274, 268, 277,
                    281, 280, 282, 294, 290, 288, 293, 301, 300, 306, 475, 394, 350, 331, 316, 310, 309, 312, 328, 327,
                    329, 342, 333, 332, 340, 346, 343, 347, 364, 355, 353, 352, 354, 360, 358, 362, 385, 378, 370, 380,
                    391, 390, 392, 429, 411, 400, 396, 395, 397, 407, 402, 408, 422, 418, 413, 420, 424, 423, 427, 452,
                    442, 432, 431, 433, 446, 445, 449, 467, 458, 454, 461, 470, 469, 473, 559, 517, 492, 486, 482, 479,
                    485, 489, 487, 491, 503, 500, 498, 502, 510, 507, 511, 540, 521, 519, 518, 520, 527, 522, 529, 554,
                    550, 548, 553, 556, 555, 557, 597, 579, 571, 564, 563, 565, 574, 573, 577, 586, 584, 580, 585, 594,
                    590, 596, 620, 610, 605, 599, 608, 615, 613, 616, 637, 629, 628, 635, 641, 638, 642, 830, 742, 702,
                    678, 660, 653, 650, 657, 669, 666, 675, 697, 685, 679, 687, 700, 699, 701, 726, 711, 707, 706, 710,
                    716, 713, 720, 738, 731, 729, 733, 740, 739, 741, 782, 761, 752, 747, 746, 748, 758, 756, 759, 771,
                    767, 762, 768, 775, 772, 776, 803, 790, 785, 784, 789, 797, 795, 802, 817, 806, 804, 812, 819, 818,
                    821, 925, 880, 847, 837, 834, 832, 835, 843, 839, 844, 860, 856, 855, 857, 874, 863, 879, 906, 890,
                    888, 883, 889, 898, 892, 900, 914, 908, 907, 910, 917, 916, 922, 964, 947, 940, 935, 927, 937, 944,
                    941, 946, 955, 949, 948, 950, 960, 957, 962, 983, 972, 968, 966, 971, 976, 975, 981, 992, 989, 985,
                    990, 996, 993, 999, 1000]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_postorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.postorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [0, 2, 1, 4, 6, 5, 9, 8, 7, 3]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-100, -98, -99, -96, -94, -95, -97, -92, -90, -91, -88, -86, -87, -89, -93, -84, -82, -83, -80, -78,
                    -79, -81, -76, -74, -75, -72, -70, -71, -73, -77, -85, -68, -66, -67, -64, -62, -63, -65, -60, -58,
                    -59, -56, -54, -55, -57, -61, -52, -50, -51, -48, -46, -47, -49, -44, -42, -43, -40, -38, -39, -41,
                    -45, -53, -69, -36, -34, -35, -32, -30, -31, -33, -28, -26, -27, -24, -22, -23, -25, -29, -20, -18,
                    -19, -16, -14, -15, -17, -12, -10, -11, -8, -6, -7, -9, -13, -21, -4, -2, -3, 0, 2, 1, -1, 4, 6, 5,
                    8, 10, 9, 7, 3, 12, 14, 13, 16, 18, 17, 15, 20, 22, 21, 24, 26, 25, 23, 19, 11, -5, -37, 28, 30, 29,
                    32, 34, 33, 31, 36, 38, 37, 40, 42, 41, 39, 35, 44, 46, 45, 48, 50, 49, 47, 52, 54, 53, 56, 58, 57,
                    55, 51, 43, 60, 62, 61, 64, 66, 65, 63, 68, 70, 69, 72, 74, 73, 71, 67, 76, 78, 77, 80, 82, 81, 79,
                    84, 86, 85, 88, 90, 89, 87, 83, 92, 94, 93, 96, 98, 100, 99, 97, 95, 91, 75, 59, 27]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(1000)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [-996, -993, -995, -990, -986, -987, -991, -981, -976, -979, -969, -965, -967, -973, -984, -960,
                    -954, -955, -952, -948, -951, -953, -942, -940, -941, -935, -932, -933, -938, -944, -963, -927,
                    -925, -926, -919, -917, -918, -923, -914, -908, -912, -900, -894, -899, -905, -915, -889, -884,
                    -886, -881, -876, -877, -882, -874, -868, -871, -864, -860, -862, -866, -875, -890, -930, -856,
                    -850, -852, -847, -843, -845, -849, -836, -833, -834, -821, -818, -819, -823, -839, -813, -807,
                    -812, -798, -789, -791, -804, -785, -783, -784, -774, -768, -770, -782, -786, -815, -763, -761,
                    -762, -759, -752, -758, -760, -750, -743, -744, -739, -736, -738, -740, -751, -725, -720, -724,
                    -715, -708, -712, -717, -706, -704, -705, -701, -689, -690, -702, -707, -730, -767, -859, -678,
                    -675, -677, -672, -661, -671, -673, -657, -655, -656, -648, -645, -646, -650, -659, -640, -629,
                    -638, -623, -621, -622, -628, -611, -607, -609, -604, -598, -600, -606, -618, -642, -585, -577,
                    -579, -575, -572, -574, -576, -570, -565, -567, -556, -549, -551, -561, -571, -543, -539, -540,
                    -536, -527, -529, -538, -524, -520, -521, -507, -505, -506, -514, -526, -546, -589, -502, -499,
                    -500, -497, -487, -493, -498, -481, -470, -476, -461, -454, -458, -466, -486, -450, -448, -449,
                    -445, -441, -443, -447, -436, -434, -435, -430, -422, -428, -432, -439, -453, -417, -413, -415,
                    -408, -402, -404, -411, -400, -396, -399, -392, -389, -390, -394, -401, -381, -379, -380, -377,
                    -370, -371, -378, -368, -360, -366, -358, -356, -357, -359, -369, -386, -419, -504, -686, -349,
                    -343, -345, -336, -330, -334, -338, -324, -316, -320, -312, -308, -310, -313, -325, -305, -301,
                    -302, -298, -294, -297, -299, -291, -287, -288, -281, -278, -279, -284, -293, -307, -270, -268,
                    -269, -262, -259, -260, -263, -248, -245, -247, -240, -235, -239, -242, -255, -233, -226, -229,
                    -217, -215, -216, -222, -213, -207, -212, -195, -190, -192, -202, -214, -234, -276, -187, -181,
                    -182, -173, -167, -172, -175, -165, -163, -164, -157, -151, -156, -161, -166, -148, -145, -146,
                    -136, -128, -132, -142, -125, -121, -122, -118, -114, -116, -119, -127, -149, -111, -103, -108, -96,
                    -90, -93, -97, -85, -79, -82, -77, -74, -75, -78, -89, -68, -61, -65, -58, -56, -57, -59, -53, -47,
                    -52, -42, -38, -41, -43, -54, -70, -33, -29, -31, -26, -24, -25, -28, -17, -13, -16, -10, -6, -9,
                    -2, -4, -5, -12, -19, -34, -113, -188, -355, 11, 9, 16, 25, 24, 15, 28, 34, 33, 36, 39, 37, 35, 26,
                    41, 45, 44, 49, 57, 50, 48, 59, 67, 60, 71, 77, 73, 68, 58, 40, 84, 86, 85, 94, 102, 101, 89, 108,
                    113, 109, 116, 123, 117, 114, 105, 127, 134, 128, 139, 143, 142, 137, 146, 154, 151, 157, 159, 158,
                    155, 144, 125, 78, 164, 168, 165, 170, 177, 176, 169, 187, 193, 188, 195, 200, 197, 194, 185, 204,
                    206, 205, 210, 213, 212, 209, 220, 222, 221, 224, 230, 229, 223, 215, 203, 233, 237, 234, 241, 246,
                    244, 240, 253, 255, 254, 257, 263, 260, 256, 251, 268, 277, 274, 280, 282, 281, 279, 288, 293, 290,
                    300, 306, 301, 294, 283, 266, 231, 160, 309, 312, 310, 327, 329, 328, 316, 332, 340, 333, 343, 347,
                    346, 342, 331, 352, 354, 353, 358, 362, 360, 355, 370, 380, 378, 390, 392, 391, 385, 364, 350, 395,
                    397, 396, 402, 408, 407, 400, 413, 420, 418, 423, 427, 424, 422, 411, 431, 433, 432, 445, 449, 446,
                    442, 454, 461, 458, 469, 473, 470, 467, 452, 429, 394, 479, 485, 482, 487, 491, 489, 486, 498, 502,
                    500, 507, 511, 510, 503, 492, 518, 520, 519, 522, 529, 527, 521, 548, 553, 550, 555, 557, 556, 554,
                    540, 517, 563, 565, 564, 573, 577, 574, 571, 580, 585, 584, 590, 596, 594, 586, 579, 599, 608, 605,
                    613, 616, 615, 610, 628, 635, 629, 638, 642, 641, 637, 620, 597, 559, 475, 307, 650, 657, 653, 666,
                    675, 669, 660, 679, 687, 685, 699, 701, 700, 697, 678, 706, 710, 707, 713, 720, 716, 711, 729, 733,
                    731, 739, 741, 740, 738, 726, 702, 746, 748, 747, 756, 759, 758, 752, 762, 768, 767, 772, 776, 775,
                    771, 761, 784, 789, 785, 795, 802, 797, 790, 804, 812, 806, 818, 821, 819, 817, 803, 782, 742, 832,
                    835, 834, 839, 844, 843, 837, 855, 857, 856, 863, 879, 874, 860, 847, 883, 889, 888, 892, 900, 898,
                    890, 907, 910, 908, 916, 922, 917, 914, 906, 880, 927, 937, 935, 941, 946, 944, 940, 948, 950, 949,
                    957, 962, 960, 955, 947, 966, 971, 968, 975, 981, 976, 972, 985, 990, 989, 993, 1000, 999, 996, 992,
                    983, 964, 925, 830, 647, 0]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_levelorder(self):

        # note: Python generators will raise a StopIteration exception when there are no items
        # left to yield, and we test for this exception to ensure each traversal yields the correct
        # number of items: https://docs.python.org/3/library/exceptions.html#StopIteration

        # ensure empty tree is properly handled and returns a StopIteration
        avl = AVLTree()
        with self.assertRaises(StopIteration):
            next(avl.levelorder(avl.origin))

        """(1) small sequential tree"""
        for i in range(10):
            avl.insert(avl.origin, i)
        generator = avl.levelorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [3, 1, 7, 0, 2, 5, 8, 4, 6, 9]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(2) large sequential tree"""
        avl = AVLTree()
        for i in range(-100, 101):
            avl.insert(avl.origin, i)
        generator = avl.levelorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [27, -37, 59, -69, -5, 43, 75, -85, -53, -21, 11, 35, 51, 67, 91, -93, -77, -61, -45, -29, -13, 3,
                    19, 31, 39, 47, 55, 63, 71, 83, 95, -97, -89, -81, -73, -65, -57, -49, -41, -33, -25, -17, -9, -1,
                    7, 15, 23, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 79, 87, 93, 97, -99, -95, -91, -87, -83,
                    -79, -75, -71, -67, -63, -59, -55, -51, -47, -43, -39, -35, -31, -27, -23, -19, -15, -11, -7, -3, 1,
                    5, 9, 13, 17, 21, 25, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64,
                    66, 68, 70, 72, 74, 77, 81, 85, 89, 92, 94, 96, 99, -100, -98, -96, -94, -92, -90, -88, -86, -84,
                    -82, -80, -78, -76, -74, -72, -70, -68, -66, -64, -62, -60, -58, -56, -54, -52, -50, -48, -46, -44,
                    -42, -40, -38, -36, -34, -32, -30, -28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2,
                    0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 76, 78, 80, 82, 84, 86, 88, 90, 98, 100]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        """(3) large random tree of unique numbers"""
        random.seed(331)
        avl = AVLTree()
        numbers = {random.randint(-1000, 1000) for _ in range(1000)}
        for num in numbers:
            avl.insert(avl.origin, num)
        generator = avl.levelorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = [0, -355, 647, -686, -188, 307, 830, -859, -504, -276, -113, 160, 475, 742, 925, -930, -767, -589,
                    -419, -307, -234, -149, -34, 78, 231, 394, 559, 702, 782, 880, 964, -963, -890, -815, -730, -642,
                    -546, -453, -386, -325, -293, -255, -214, -166, -127, -70, -19, 40, 125, 203, 266, 350, 429, 517,
                    597, 678, 726, 761, 803, 847, 906, 947, 983, -984, -944, -915, -875, -839, -786, -751, -707, -659,
                    -618, -571, -526, -486, -439, -401, -369, -338, -313, -299, -284, -263, -242, -222, -202, -175,
                    -161, -142, -119, -89, -54, -28, -12, 26, 58, 105, 144, 185, 215, 251, 283, 331, 364, 411, 452, 492,
                    540, 579, 620, 660, 697, 711, 738, 752, 771, 790, 817, 837, 860, 890, 914, 940, 955, 972, 992, -991,
                    -973, -953, -938, -923, -905, -882, -866, -849, -823, -804, -782, -760, -740, -717, -702, -673,
                    -650, -628, -606, -576, -561, -538, -514, -498, -466, -447, -432, -411, -394, -378, -359, -345,
                    -334, -320, -310, -302, -297, -288, -279, -269, -260, -247, -239, -229, -216, -212, -192, -182,
                    -172, -164, -156, -146, -132, -122, -116, -97, -78, -59, -43, -31, -25, -16, -5, 15, 35, 48, 68, 89,
                    114, 137, 155, 169, 194, 209, 223, 240, 256, 279, 294, 316, 342, 355, 385, 400, 422, 442, 467, 486,
                    503, 521, 554, 571, 586, 610, 637, 653, 669, 685, 700, 707, 716, 731, 740, 747, 758, 767, 775, 785,
                    797, 806, 819, 834, 843, 856, 874, 888, 898, 908, 917, 935, 944, 949, 960, 968, 976, 989, 996, -995,
                    -987, -979, -967, -955, -951, -941, -933, -926, -918, -912, -899, -886, -877, -871, -862, -852,
                    -845, -834, -819, -812, -791, -784, -770, -762, -758, -744, -738, -724, -712, -705, -690, -677,
                    -671, -656, -646, -638, -622, -609, -600, -579, -574, -567, -551, -540, -529, -521, -506, -500,
                    -493, -476, -458, -449, -443, -435, -428, -415, -404, -399, -390, -380, -371, -366, -357, -349,
                    -343, -336, -330, -324, -316, -312, -308, -305, -301, -298, -294, -291, -287, -281, -278, -270,
                    -268, -262, -259, -248, -245, -240, -235, -233, -226, -217, -215, -213, -207, -195, -190, -187,
                    -181, -173, -167, -165, -163, -157, -151, -148, -145, -136, -128, -125, -121, -118, -114, -108, -93,
                    -82, -75, -65, -57, -52, -41, -33, -29, -26, -24, -17, -13, -9, -4, 9, 24, 33, 37, 44, 50, 60, 73,
                    85, 101, 109, 117, 128, 142, 151, 158, 165, 176, 188, 197, 205, 212, 221, 229, 234, 244, 254, 260,
                    274, 281, 290, 301, 310, 328, 333, 346, 353, 360, 378, 391, 396, 407, 418, 424, 432, 446, 458, 470,
                    482, 489, 500, 510, 519, 527, 550, 556, 564, 574, 584, 594, 605, 615, 629, 641, 650, 657, 666, 675,
                    679, 687, 699, 701, 706, 710, 713, 720, 729, 733, 739, 741, 746, 748, 756, 759, 762, 768, 772, 776,
                    784, 789, 795, 802, 804, 812, 818, 821, 832, 835, 839, 844, 855, 857, 863, 879, 883, 889, 892, 900,
                    907, 910, 916, 922, 927, 937, 941, 946, 948, 950, 957, 962, 966, 971, 975, 981, 985, 990, 993, 999,
                    -996, -993, -990, -986, -981, -976, -969, -965, -960, -954, -952, -948, -942, -940, -935, -932,
                    -927, -925, -919, -917, -914, -908, -900, -894, -889, -884, -881, -876, -874, -868, -864, -860,
                    -856, -850, -847, -843, -836, -833, -821, -818, -813, -807, -798, -789, -785, -783, -774, -768,
                    -763, -761, -759, -752, -750, -743, -739, -736, -725, -720, -715, -708, -706, -704, -701, -689,
                    -678, -675, -672, -661, -657, -655, -648, -645, -640, -629, -623, -621, -611, -607, -604, -598,
                    -585, -577, -575, -572, -570, -565, -556, -549, -543, -539, -536, -527, -524, -520, -507, -505,
                    -502, -499, -497, -487, -481, -470, -461, -454, -450, -448, -445, -441, -436, -434, -430, -422,
                    -417, -413, -408, -402, -400, -396, -392, -389, -381, -379, -377, -370, -368, -360, -358, -356,
                    -111, -103, -96, -90, -85, -79, -77, -74, -68, -61, -58, -56, -53, -47, -42, -38, -10, -6, -2, 11,
                    16, 25, 28, 34, 36, 39, 41, 45, 49, 57, 59, 67, 71, 77, 84, 86, 94, 102, 108, 113, 116, 123, 127,
                    134, 139, 143, 146, 154, 157, 159, 164, 168, 170, 177, 187, 193, 195, 200, 204, 206, 210, 213, 220,
                    222, 224, 230, 233, 237, 241, 246, 253, 255, 257, 263, 268, 277, 280, 282, 288, 293, 300, 306, 309,
                    312, 327, 329, 332, 340, 343, 347, 352, 354, 358, 362, 370, 380, 390, 392, 395, 397, 402, 408, 413,
                    420, 423, 427, 431, 433, 445, 449, 454, 461, 469, 473, 479, 485, 487, 491, 498, 502, 507, 511, 518,
                    520, 522, 529, 548, 553, 555, 557, 563, 565, 573, 577, 580, 585, 590, 596, 599, 608, 613, 616, 628,
                    635, 638, 642, 1000]
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_remove(self):

        # visualize this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        # ensure empty tree is properly handled
        avl = AVLTree()
        self.assertIsNone(avl.remove(avl.origin, 0))

        """
        (1) test removal causing right-right rotation
        initial structure:
            2
           / \
          1   3
         /     \
        0       4
        final structure (removing 1, 0):
          3 
         / \
        2   4
        """
        avl = AVLTree()
        for i in [2, 1, 3, 0, 4]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 1)  # one child removal
        avl.remove(avl.origin, 0)  # zero child removal, will need rebalancing
        self.assertEqual(3, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(4, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (2) test removal causing left-left rotation
        initial structure:
            3
           / \
          2   4
         /     \
        1       5
        final structure (removing 4, 5):
          2 
         / \
        1   3
        """
        avl = AVLTree()
        for i in [3, 2, 4, 1, 5]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 4)  # one child removal
        avl.remove(avl.origin, 5)  # zero child removal, will need rebalancing
        self.assertEqual(3, avl.size)
        self.assertEqual(2, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (3) test removal causing left-right rotation
        initial structure:
              5
             / \
            2   6
           / \   \
          1   3   7
         /     \
        0       4
        final structure (removing 1, 6):
            3 
           / \
          2   5
         /   / \
        0   4   7
        """
        avl = AVLTree()
        for i in [5, 2, 6, 1, 3, 7, 0, 4]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 1)  # one child removal
        avl.remove(avl.origin, 6)  # one child removal, will need rebalancing
        self.assertEqual(6, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(4, avl.origin.right.left.value)
        self.assertEqual(0, avl.origin.right.left.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

        """
        (4) test removal causing right-left rotation
        initial structure:
            2
           / \
          1   5
         /   / \
        0   4   6
           /     \
          3       7
        final structure (removing 6, 1):
            4 
           / \
          2   5
         / \   \
        0   3   7
        """
        avl = AVLTree()
        for i in [2, 1, 5, 0, 4, 6, 3, 7]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 6)  # one child removal
        avl.remove(avl.origin, 1)  # one child removal, will need rebalancing
        self.assertEqual(6, avl.size)
        self.assertEqual(4, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(2, avl.origin.left.value)
        self.assertEqual(1, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)
        self.assertEqual(0, avl.origin.left.left.value)
        self.assertEqual(0, avl.origin.left.left.height)
        self.assertEqual(3, avl.origin.left.right.value)
        self.assertEqual(0, avl.origin.left.right.height)

        """
        (5) test simple 2-child removal
        initial structure:
          2
         / \
        1   3
        final structure (removing 2):
         1 
          \
           3
        """
        avl = AVLTree()
        for i in [2, 1, 3]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 2)  # two child removal
        self.assertEqual(2, avl.size)
        self.assertEqual(1, avl.origin.value)
        self.assertEqual(1, avl.origin.height)
        self.assertEqual(3, avl.origin.right.value)
        self.assertEqual(0, avl.origin.right.height)

        """
        (5) test compounded 2-child removal
        initial structure:
              4
           /     \
          2       6
         / \     / \
        1   3   5   7
        intermediate structure (removing 2, 6):
            4
           / \
          1   5
           \   \
            3   7
        final structure (removing 4)
            3
           / \
          1   5
               \
                7        
        """
        avl = AVLTree()
        for i in [4, 2, 6, 1, 3, 5, 7]:
            avl.insert(avl.origin, i)
        avl.remove(avl.origin, 2)  # two child removal
        avl.remove(avl.origin, 6)  # two child removal
        avl.remove(avl.origin, 4)  # two child removal
        self.assertEqual(4, avl.size)
        self.assertEqual(3, avl.origin.value)
        self.assertEqual(2, avl.origin.height)
        self.assertEqual(1, avl.origin.left.value)
        self.assertEqual(0, avl.origin.left.height)
        self.assertEqual(5, avl.origin.right.value)
        self.assertEqual(1, avl.origin.right.height)
        self.assertEqual(7, avl.origin.right.right.value)
        self.assertEqual(0, avl.origin.right.right.height)

    def test_AVL_comprehensive(self):

        # visualize some of test in this testcase with https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
        # ensure empty tree is properly handled

        """
        First part, inserting and removing without rotation

        insert without any rotation (inserting 5, 0, 10):
          5
         / \
        1   10
        """

        def check_node_properties(current: Node, value: int = 0, height: int = 0, balance: int = 0):
            if value is None:
                self.assertIsNone(current)
                return
            self.assertEqual(value, current.value)
            self.assertEqual(height, current.height)
            self.assertEqual(balance, avl.balance_factor(current))

        avl = AVLTree()
        avl.insert(avl.origin, 5)
        avl.insert(avl.origin, 1)
        avl.insert(avl.origin, 10)
        self.assertEqual(3, avl.size)
        self.assertEqual(1, avl.min(avl.origin).value)
        self.assertEqual(10, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=5, height=1, balance=0)
        check_node_properties(avl.origin.left, value=1, height=0, balance=0)
        check_node_properties(avl.origin.right, value=10, height=0, balance=0)
        """
        Current AVL tree:
          5
         / \
        1   10
        After Removing 5:
          1
           \
            10
        """
        avl.remove(avl.origin, 5)
        self.assertEqual(2, avl.size)
        self.assertEqual(1, avl.min(avl.origin).value)
        self.assertEqual(10, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=1, height=1, balance=-1)
        check_node_properties(avl.origin.left, value=None)
        check_node_properties(avl.origin.right, value=10, height=0, balance=0)
        """
        Current AVL tree:
          1
            \
            10
        After inserting 0, 20:
          1
         /  \
        0   10
              \
               20
        """
        avl.insert(avl.origin, 0)
        avl.insert(avl.origin, 20)
        self.assertEqual(4, avl.size)
        self.assertEqual(0, avl.min(avl.origin).value)
        self.assertEqual(20, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=1, height=2, balance=-1)
        check_node_properties(avl.origin.left, value=0, height=0, balance=0)
        check_node_properties(avl.origin.right, value=10, height=1, balance=-1)
        check_node_properties(avl.origin.right.right, value=20, height=0, balance=0)

        """
        Current AVL tree:
          1
         /  \
        0   10
              \
               20
        After removing 20, inserting -20 and inserting 5
             1
            /  \
           0   10
          /   /
        -20  5
        """
        avl.remove(avl.origin, 20)
        avl.insert(avl.origin, -20)
        avl.insert(avl.origin, 5)
        self.assertEqual(5, avl.size)
        self.assertEqual(-20, avl.min(avl.origin).value)
        self.assertEqual(10, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=1, height=2, balance=0)
        check_node_properties(avl.origin.left, value=0, height=1, balance=1)
        check_node_properties(avl.origin.left.left, value=-20, height=0, balance=0)
        check_node_properties(avl.origin.right, value=10, height=1, balance=1)
        check_node_properties(avl.origin.right.left, value=5, height=0, balance=0)

        """
        Second part, inserting and removing with rotation

        inserting 5, 10:
          5
           \
            10
        """
        avl = AVLTree()
        avl.insert(avl.origin, 5)
        avl.insert(avl.origin, 10)
        self.assertEqual(2, avl.size)
        self.assertEqual(5, avl.min(avl.origin).value)
        self.assertEqual(10, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=5, height=1, balance=-1)
        check_node_properties(avl.origin.right, value=10, height=0, balance=0)
        """
        Current AVL tree:
          5
           \
            10
        After inserting 8, 9, 12
           8
         /   \
        5    10
            /  \
           9   12
        """
        avl.insert(avl.origin, 8)
        avl.insert(avl.origin, 9)
        avl.insert(avl.origin, 12)
        self.assertEqual(5, avl.size)
        self.assertEqual(5, avl.min(avl.origin).value)
        self.assertEqual(12, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=8, height=2, balance=-1)
        check_node_properties(avl.origin.right, value=10, height=1, balance=0)
        check_node_properties(avl.origin.right.left, value=9, height=0, balance=0)
        check_node_properties(avl.origin.right.right, value=12, height=0, balance=0)
        check_node_properties(avl.origin.left, value=5, height=0, balance=0)

        """
        Current AVL tree:
           8
         /   \
        5    10
            /  \
           9   12
        After inserting 3, 1, 2
               8
           /       \
          3        10
         /  \     /   \
        1    5   9    12
          \
           2
        """
        avl.insert(avl.origin, 3)
        avl.insert(avl.origin, 1)
        avl.insert(avl.origin, 2)
        self.assertEqual(8, avl.size)
        self.assertEqual(1, avl.min(avl.origin).value)
        self.assertEqual(12, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=8, height=3, balance=1)
        check_node_properties(avl.origin.right, value=10, height=1, balance=0)
        check_node_properties(avl.origin.right.left, value=9, height=0, balance=0)
        check_node_properties(avl.origin.right.right, value=12, height=0, balance=0)
        check_node_properties(avl.origin.left, value=3, height=2, balance=1)
        check_node_properties(avl.origin.left.left, value=1, height=1, balance=-1)
        check_node_properties(avl.origin.left.left.right, value=2, height=0, balance=0)
        check_node_properties(avl.origin.left.right, value=5, height=0, balance=0)
        """
        Current AVL tree:
               8
           /       \
          3        10
         /  \     /   \
        1    5   9    12
          \
           2
        After removing 5
               8
           /       \
          2        10
         /  \     /   \
        1    3   9    12
        """
        avl.remove(avl.origin, 5)
        self.assertEqual(7, avl.size)
        self.assertEqual(1, avl.min(avl.origin).value)
        self.assertEqual(12, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=8, height=2, balance=0)
        check_node_properties(avl.origin.right, value=10, height=1, balance=0)
        check_node_properties(avl.origin.right.left, value=9, height=0, balance=0)
        check_node_properties(avl.origin.right.right, value=12, height=0, balance=0)
        check_node_properties(avl.origin.left, value=2, height=1, balance=0)
        check_node_properties(avl.origin.left.left, value=1, height=0, balance=0)
        check_node_properties(avl.origin.left.right, value=3, height=0, balance=0)
        """
        Current AVL tree:
              8
           /     \
          2      10
         /  \   /   \
        1    3 9    12
        After inserting 5, 13, 0, 7, 20
               8
            /       \
           2         10
          /  \      /   \
         1    5     9    13
        /    / \        /  \
        0   3   7     12    20
        """
        avl.insert(avl.origin, 5)
        avl.insert(avl.origin, 13)
        avl.insert(avl.origin, 0)
        avl.insert(avl.origin, 7)
        avl.insert(avl.origin, 20)
        self.assertEqual(12, avl.size)
        self.assertEqual(0, avl.min(avl.origin).value)
        self.assertEqual(20, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=8, height=3, balance=0)

        check_node_properties(avl.origin.right, value=10, height=2, balance=-1)
        check_node_properties(avl.origin.right.left, value=9, height=0, balance=0)
        check_node_properties(avl.origin.right.right, value=13, height=1, balance=0)
        check_node_properties(avl.origin.right.right.right, value=20, height=0, balance=0)
        check_node_properties(avl.origin.right.right.left, value=12, height=0, balance=0)

        check_node_properties(avl.origin.left, value=2, height=2, balance=0)
        check_node_properties(avl.origin.left.left, value=1, height=1, balance=1)
        check_node_properties(avl.origin.left.left.left, value=0, height=0, balance=0)
        check_node_properties(avl.origin.left.right, value=5, height=1, balance=-0)
        check_node_properties(avl.origin.left.right.right, value=7, height=0, balance=0)
        check_node_properties(avl.origin.left.right.left, value=3, height=0, balance=0)

        """
        Current AVL tree:
               8
            /       \
           2         10
          /  \      /   \
         1    5     9    13
        /    / \        /  \
        0   3   7     12    20
        After removing 1, 9
               8
            /       \
           2         13
          /  \      /   \
         0    5   10     20
             / \     \    
             3   7    12
        """
        avl.remove(avl.origin, 1)
        avl.remove(avl.origin, 9)
        self.assertEqual(10, avl.size)
        self.assertEqual(0, avl.min(avl.origin).value)
        self.assertEqual(20, avl.max(avl.origin).value)
        # Properties of all nodes
        check_node_properties(avl.origin, value=8, height=3, balance=0)

        check_node_properties(avl.origin.right, value=13, height=2, balance=1)
        check_node_properties(avl.origin.right.left, value=10, height=1, balance=-1)
        check_node_properties(avl.origin.right.left.right, value=12, height=0, balance=0)
        check_node_properties(avl.origin.right.right, value=20, height=0, balance=0)

        check_node_properties(avl.origin.left, value=2, height=2, balance=-1)
        check_node_properties(avl.origin.left.left, value=0, height=0, balance=0)
        check_node_properties(avl.origin.left.right, value=5, height=1, balance=-0)
        check_node_properties(avl.origin.left.right.right, value=7, height=0, balance=0)
        check_node_properties(avl.origin.left.right.left, value=3, height=0, balance=0)

        """
        Part Three
        Everything but random, checking properties of tree only
        """
        random.seed(331)
        """
        randomly insert, and remove alphabet to avl tree
        """

        def random_order_1(character= True):
            order = random.randint(0, 2)
            if not len(existing_value) or (order and (not character or avl.size < 26)):
                if character:
                    inserted = chr(ord('a') + random.randint(0, 25))
                    while inserted in existing_value:
                        inserted = chr(ord('a') + random.randint(0, 25))
                else:
                    inserted = random.randint(0, 100000)
                avl.insert(avl.origin, inserted)
                existing_value[inserted] = 1
            else:
                removed = random.choice(list(existing_value.keys()))
                avl.remove(avl.origin, removed)
                existing_value.pop(removed)

        existing_value = {}
        avl = AVLTree()
        for _ in range(30):
            random_order_1()
        self.assertEqual('a', avl.min(avl.origin).value)
        self.assertEqual('y', avl.max(avl.origin).value)
        # inorder test
        expected = ['a', 'b', 'd', 'f', 'g', 'i', 'k', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y']
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        expected = ['p', 'f', 'b', 'a', 'd', 'k', 'i', 'g', 'o', 't', 'r', 'q', 's', 'w', 'v', 'y']
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        expected = ['a', 'd', 'b', 'g', 'i', 'o', 'k', 'f', 'q', 's', 'r', 'v', 'y', 'w', 't', 'p']
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        existing_value.clear()
        avl = AVLTree()
        for _ in range(1200):
            random_order_1(character=False)
        self.assertEqual(218, avl.min(avl.origin).value)
        self.assertEqual(99893, avl.max(avl.origin).value)
        # inorder test
        expected = [218, 433, 640, 927, 992, 1069, 1175, 1362, 1790, 2011,
                    2118, 2180, 3231, 3592, 3883, 4079, 4322, 4398, 4696, 4861, 5383, 5403, 5690, 5965, 6089, 6266, 6628, 6949, 7135, 7195, 7396, 7691, 7699, 8121, 8187, 8749, 8773, 8785, 8885, 9497, 9691, 10039, 10441, 10524, 11628, 11888, 12640, 12842, 12879, 13053, 13417, 13887, 13968, 14023, 14846, 14913, 15311, 15424, 16168, 16395, 16422, 16706, 17086, 17564, 17596, 17711, 17910, 18704, 19072, 19179, 19484, 19543, 19548, 19555, 19628, 19906, 19971, 20419, 20521, 20618, 20860, 21205, 21353, 21379, 21419, 21723, 22253, 22748, 22752, 23065, 23179, 23220, 23359, 23673, 23710, 24332, 25504, 26494, 26581, 26708, 26717, 26945, 27073, 27161, 27793, 27972, 28018, 28198, 28483, 28682, 28775, 29108, 29184, 29385, 29509, 29822, 30063, 30210, 30478, 30621, 30800, 30807, 31135, 31164, 31189, 31423, 31689, 32398, 32645, 33284, 33747, 34045, 34216, 34242, 34251, 34271, 34508, 34781, 34794, 35325, 35355, 35466, 35481, 35693, 35927, 35943, 36069, 36747, 37629, 37663, 37679, 38153, 39136, 39211, 39265, 39769, 40178, 40298, 40453, 40864, 41360, 41578, 41756, 41973, 42051, 42476, 43057, 43279, 43379, 43601, 44079, 44105, 44302, 44525, 44904, 45373, 45396, 45775, 46027, 46070, 46204, 46376, 46463, 46534, 46557, 46666, 46832, 46961, 47170, 47287, 47856, 47935, 48073, 48581, 48585, 48947, 49040, 49089, 49422, 49441, 49612, 49624, 49782, 49943, 50506, 50724, 50766, 51097, 51568, 51995, 52068, 52283, 52422, 52436, 52553, 52915, 53140, 53224, 53356, 53644, 53851, 53863, 54054, 54683, 55077, 55196, 55289, 55295, 55339, 55579, 55596, 55611, 55822, 55832, 56254, 56785, 56800, 57043, 57066, 57147, 57167, 57199, 57904, 58278, 58299, 58311, 58613, 58751, 58783, 58838, 59125, 59664, 60049, 60226, 61108, 61353, 61504, 61543, 61590, 61730, 61888, 61979, 62257, 62426, 62995, 63102, 63626, 64606, 65089, 65386, 65636, 66156, 66181, 66337, 66837, 67217, 67686, 67763, 68681, 68899, 69351, 69402, 69695, 69725, 70733, 70736, 71258, 71265, 71417, 71473, 71487, 71668, 71884, 71913, 71920, 72171, 72409, 72677, 72927, 73195, 73491, 73865, 74096, 74272, 74291, 74305, 74756, 75150, 75174, 75848, 75892, 76270, 76517, 76796, 76821, 76936, 77062, 77426, 77451, 77662, 77703, 77762, 77836, 78162, 78189, 78241, 78684, 78814, 78885, 79507, 79825, 80142, 80208, 80652, 80817, 80878, 81769, 81967, 82239, 82245, 82330, 82611, 82809, 82999, 83000, 83284, 83626, 83723, 85053, 85418, 85746, 85779, 85846, 85887, 85912, 85968, 86127, 86260, 86846, 86970, 87081, 87137, 87667, 87671, 87790, 88099, 88172, 88778, 88854, 88859, 89546, 89796, 90043, 90174, 90500, 90793, 90837, 91228, 91287, 91819, 91938, 92031, 92133, 92248, 92443, 92636, 93344, 93547, 93585, 93674, 93687, 93710, 94027, 94257, 94374, 94585, 94874, 95337, 96088, 96194, 96889, 97325, 97357, 97454, 97610, 97683, 97685, 98006, 98076, 98268, 99697, 99771, 99888, 99893]
        generator = avl.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        expected = [49040, 19628, 9691, 4398, 2180, 992, 640, 218, 433, 927, 1790, 1175,
                    1069, 1362, 2118, 2011, 3592, 3231, 4079, 3883, 4322, 6628, 5965, 5383, 4861, 4696, 5690, 5403, 6266, 6089, 8187, 7195, 7135, 6949, 7691, 7396, 8121, 7699, 8773, 8749, 8885, 8785, 9497, 16395, 13417, 11888, 10524, 10039, 10441, 11628, 12842, 12640, 13053, 12879, 14846, 13968, 13887, 14023, 15424, 15311, 14913, 16168, 17711, 17564, 16706, 16422, 17086, 17596, 19179, 18704, 17910, 19072, 19543, 19484, 19548, 19555, 32645, 23673, 21379, 20419, 19971, 19906, 21205, 20618, 20521, 20860, 21353, 22253, 21723, 21419, 23179, 22752, 22748, 23065, 23359, 23220, 29509, 27793, 26717, 26494, 24332, 23710, 25504, 26708, 26581, 27073, 26945, 27161, 28682, 28018, 27972, 28198, 28483, 29108, 28775, 29385, 29184, 30800, 30210, 29822, 30063, 30478, 30621, 31164, 31135, 30807, 31689, 31423, 31189, 32398, 41360, 35693, 34271, 34216, 33747, 33284, 34045, 34242, 34251, 35325, 34781, 34508, 34794, 35466, 35355, 35481, 37679, 36069, 35943, 35927, 37629, 36747, 37663, 39769, 39211, 38153, 39136, 39265, 40298, 40178, 40864, 40453, 46376, 44904, 43379, 42051, 41756, 41578, 41973, 43057, 42476, 43279, 44302, 44079, 43601, 44105, 44525, 45775, 45373, 45396, 46070, 46027, 46204, 47170, 46666, 46534, 46463, 46557, 46832, 46961, 47935, 47287, 47856, 48581, 48073, 48585, 48947, 69402, 55832, 52915, 50506, 49624, 49441, 49422, 49089, 49612, 49943, 49782, 51568, 50766, 50724, 51097, 52283, 52068, 51995, 52436, 52422, 52553, 53863, 53644, 53224, 53140, 53356, 53851, 55289, 55077, 54683, 54054, 55196, 55579, 55339, 55295, 55611, 55596, 55822, 61590, 58783, 57167, 56800, 56254, 56785, 57066, 57043, 57147, 58278, 57904, 57199, 58613, 58299, 58311, 58751, 60049, 59125, 58838, 59664, 61504, 61108, 60226, 61353, 61543, 64606, 61979, 61730, 61888, 62995, 62426, 62257, 63626, 63102, 67217, 66156, 65386, 65089, 65636, 66337, 66181, 66837, 67763, 67686, 68899, 68681, 69351, 80878, 75848, 72927, 71417, 70733, 69725, 69695, 71258, 70736, 71265, 71913, 71668, 71473, 71487, 71884, 72409, 72171, 71920, 72677, 74291, 74096, 73491, 73195, 73865, 74272, 74756, 74305, 75150, 75174, 78162, 77426, 76796, 76270, 75892, 76517, 76936, 76821, 77062, 77662, 77451, 77762, 77703, 77836, 79825, 78814, 78241, 78189, 78684, 78885, 79507, 80208, 80142, 80652, 80817, 88778, 83723, 82330, 82239, 81769, 81967, 82245, 83000, 82809, 82611, 82999, 83284, 83626, 86970, 85887, 85746, 85418, 85053, 85846, 85779, 85968, 85912, 86260, 86127, 86846, 87790, 87137, 87081, 87667, 87671, 88099, 88172, 94374, 91938, 90174, 89546, 88859, 88854, 90043, 89796, 91228, 90793, 90500, 90837, 91287, 91819, 93547, 92248, 92031, 92133, 92636, 92443, 93344, 93687, 93674, 93585, 94027, 93710, 94257, 97325, 95337, 94874,
                    94585, 96194, 96088, 96889, 98006, 97454, 97357, 97683, 97610, 97685, 99697, 98268, 98076, 99888, 99771, 99893]
        generator = avl.preorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

        expected = [433, 218, 927, 640, 1069, 1362, 1175, 2011,
                    2118, 1790, 992, 3231, 3883, 4322, 4079, 3592, 2180, 4696, 4861, 5403, 5690, 5383, 6089, 6266, 5965, 6949, 7135, 7396, 7699, 8121, 7691, 7195, 8749, 8785, 9497, 8885, 8773, 8187, 6628, 4398, 10441, 10039, 11628, 10524, 12640, 12879, 13053, 12842, 11888, 13887, 14023, 13968, 14913, 15311, 16168, 15424, 14846, 13417, 16422, 17086, 16706, 17596, 17564, 17910, 19072, 18704, 19484, 19555, 19548, 19543, 19179, 17711, 16395, 9691, 19906, 19971, 20521, 20860, 20618, 21353, 21205, 20419, 21419, 21723, 22748, 23065, 22752, 23220, 23359, 23179, 22253, 21379, 23710, 25504, 24332, 26581, 26708, 26494, 26945, 27161, 27073, 26717, 27972, 28483, 28198, 28018, 28775, 29184, 29385, 29108, 28682, 27793, 30063, 29822, 30621, 30478, 30210, 30807, 31135, 31189, 31423, 32398, 31689, 31164, 30800, 29509, 23673, 33284, 34045, 33747, 34251, 34242, 34216, 34508, 34794, 34781, 35355, 35481, 35466, 35325, 34271, 35927, 35943, 36747, 37663, 37629, 36069, 39136, 38153, 39265, 39211, 40178, 40453, 40864, 40298, 39769, 37679, 35693, 41578, 41973, 41756, 42476, 43279, 43057, 42051, 43601, 44105, 44079, 44525, 44302, 43379, 45396, 45373, 46027, 46204, 46070, 45775, 44904, 46463, 46557, 46534, 46961, 46832, 46666, 47856, 47287, 48073, 48947, 48585, 48581, 47935, 47170, 46376, 41360, 32645, 19628, 49089, 49422, 49612, 49441, 49782, 49943, 49624, 50724, 51097, 50766, 51995, 52068, 52422, 52553, 52436, 52283, 51568, 50506, 53140, 53356, 53224, 53851, 53644, 54054, 54683, 55196, 55077, 55295, 55339, 55596, 55822, 55611, 55579, 55289, 53863, 52915, 56785, 56254, 57043, 57147, 57066, 56800, 57199, 57904, 58311, 58299, 58751, 58613, 58278, 57167, 58838, 59664, 59125, 60226, 61353, 61108, 61543, 61504, 60049, 58783, 61888, 61730, 62257, 62426, 63102, 63626, 62995, 61979, 65089, 65636, 65386, 66181, 66837, 66337, 66156, 67686, 68681, 69351, 68899, 67763, 67217, 64606, 61590, 55832, 69695, 69725, 70736, 71265, 71258, 70733, 71487, 71473, 71884, 71668, 71920, 72171, 72677, 72409, 71913, 71417, 73195, 73865, 73491, 74272, 74096, 74305, 75174, 75150, 74756, 74291, 72927, 75892, 76517, 76270, 76821, 77062, 76936, 76796, 77451, 77703, 77836, 77762, 77662, 77426, 78189, 78684, 78241, 79507, 78885, 78814, 80142, 80817, 80652, 80208, 79825, 78162, 75848, 81967, 81769, 82245, 82239, 82611, 82999, 82809, 83626, 83284, 83000, 82330, 85053, 85418, 85779, 85846, 85746, 85912, 86127, 86846, 86260, 85968, 85887, 87081, 87671, 87667, 87137, 88172, 88099, 87790, 86970, 83723, 88854, 88859, 89796, 90043, 89546, 90500, 90837, 90793, 91819, 91287, 91228, 90174, 92133, 92031, 92443, 93344, 92636, 92248, 93585, 93674, 93710, 94257, 94027, 93687, 93547, 91938, 94585, 94874, 96088, 96889, 96194, 95337, 97357,
                    97610, 97685, 97683, 97454, 98076, 98268, 99771, 99893, 99888, 99697, 98006, 97325, 94374, 88778, 80878, 69402, 49040]
        generator = avl.postorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        for num in expected:
            node = next(generator)
            self.assertIsInstance(node, Node)
            self.assertEqual(num, node.value)
        with self.assertRaises(StopIteration):
            next(generator)

    def test_nnc(self):

        plot = False
        """
        (1) Day/Night image classification: Suppose brightness of an image is measured
        between 0 and 1, and we are provided labeled examples of the brightness levels of 
        images that were taken during night and during day. Given a new image brightness level,
        predict whether the image was taken during night or day.
        """
        # 1a: test from specs
        data = [(0.18, "night"), (0.21, "night"), (0.29, "night"),
                (0.49, "night"), (0.51, "day"), (0.53, "day"),
                (0.97, "day"), (0.98, "day"), (0.99, "day")]
        nnc = NearestNeighborClassifier(resolution=1)
        nnc.fit(data)

        test_images = [0.1, 0.2, 0.5, 0.8, 0.9]
        expected = ["night", "night", "day", None, "day"]
        actual = [nnc.predict(x=image, delta=0.1) for image in test_images]
        self.assertEqual(expected, actual)

        # 1b: larger test
        random.seed(331)
        night_images = [(random.random() / 2, "night") for _ in range(50)]
        day_images = [(random.random() / 2 + 0.5, "day") for _ in range(50)]
        data = night_images + day_images

        nnc = NearestNeighborClassifier(resolution=1)
        nnc.fit(data)

        test_images = [0.1, 0.2, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9]
        expected = ["night"] * 4 + ["day"] * 4
        actual = [nnc.predict(x=image, delta=0.1) for image in test_images]
        if plot:
            np.random.seed(331)
            x_night = np.array([x[0] for x in night_images])
            x_day = np.array([x[0] for x in day_images])
            x_test = np.array(test_images)
            plt.scatter(x=x_night, y=np.random.rand(len(x_night)), label="night")
            plt.scatter(x=x_day, y=np.random.rand(len(x_day)), label="day")
            plt.scatter(x=x_test, y=np.zeros(len(x_test)), c="k", label="test")
            plt.xlabel("Value")
            plt.yticks([], [])
            plt.legend()
            plt.show()

        self.assertEqual(expected, actual)

        """
        (2) Season Classification: Suppose temperature is measured between 0 and 1, and we are
        provided labeled examples of the season in which each temperature was recorded.
        Given a new temperature, predict the season we are experiencing.
        """
        random.seed(331)
        winter_temps = [(random.random() / 4, "winter") for _ in range(50)]
        spring_temps = [(random.random() / 4 + 0.25, "spring") for _ in range(50)]
        summer_temps = [(random.random() / 4 + 0.75, "summer") for _ in range(50)]
        fall_temps = [(random.random() / 4 + 0.5, "fall") for _ in range(50)]
        data = winter_temps + spring_temps + summer_temps + fall_temps

        nnc = NearestNeighborClassifier(resolution=1)
        nnc.fit(data)

        test_temps = [i / 20 for i in range(20)]
        expected = ["winter"] * 6 + ["spring"] * 5 + ["fall"] * 4 + ["summer"] * 5
        actual = [nnc.predict(x=temp, delta=0) for temp in test_temps]
        if plot:
            np.random.seed(331)
            x_winter, x_spring, x_summer, x_fall = \
                np.array([x[0] for x in winter_temps]), np.array([x[0] for x in spring_temps]), \
                np.array([x[0] for x in summer_temps]), np.array([x[0] for x in fall_temps])
            x_test = np.array(test_temps)
            plt.scatter(x=x_winter, y=np.random.rand(len(x_winter)), label="winter")
            plt.scatter(x=x_spring, y=np.random.rand(len(x_spring)), label="spring")
            plt.scatter(x=x_summer, y=np.random.rand(len(x_summer)), label="summer")
            plt.scatter(x=x_fall, y=np.random.rand(len(x_fall)), label="fall")
            plt.scatter(x=x_test, y=np.zeros(len(x_test)), c="k", label="test")
            plt.xlabel("Value")
            plt.yticks([], [])
            plt.legend()
            plt.show()

        self.assertEqual(expected, actual)

        """
        (3) Rainfall Classification: Suppose daily rainfall is measured between 0 and 1
        relative to some baseline, and we are provided labeled examples of whether each year
        experienced drought, normal, or flood conditions. Given a new rainfall measurement, predict
        whether this year will experience drought, normal, or flood conditions.
        """
        random.seed(331)
        drought_rains = [(random.random() / 2, "drought") for _ in range(1000)]
        normal_rains = [(random.random() / 5 + 0.4, "normal") for _ in range(1000)]
        flood_rains = [(random.random() / 2 + 0.5, "flood") for _ in range(1000)]
        data = drought_rains + normal_rains + flood_rains

        nnc = NearestNeighborClassifier(resolution=2)
        nnc.fit(data)

        test_rains = [i / 100 for i in range(100)]
        expected = ["drought"] * 40 + ["normal"] * 21 + ["flood"] * 39
        actual = [nnc.predict(x=rain, delta=0.01) for rain in test_rains]
        if plot:
            np.random.seed(331)
            x_drought, x_normal, x_flood = np.array([x[0] for x in drought_rains]), \
                                           np.array([x[0] for x in normal_rains]), np.array([x[0] for x in flood_rains])
            x_test = np.array(test_rains)
            plt.scatter(x=x_normal, y=np.random.rand(len(x_normal)), label="normal")
            plt.scatter(x=x_drought, y=np.random.rand(len(x_drought)), label="drought")
            plt.scatter(x=x_flood, y=np.random.rand(len(x_flood)), label="flood")
            plt.scatter(x=x_test, y=np.zeros(len(x_test)), c="k", label="test")
            plt.xlabel("Value")
            plt.yticks([], [])
            plt.legend()
            plt.show()

        self.assertEqual(expected, actual)

    def test_nnc_comprehensive(self):

        plot = False
        """
        (4) Iris Species Classification: Given measurements of sepal length, sepal width,
        petal length and petal width, predict the species of iris flower.
        Data from the UCI ML repository via sklearn.datasets, with credit to R.A. Fisher.
        https://archive.ics.uci.edu/ml/datasets/iris
        """
        iris_labels = ['setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica', 'virginica']
        sepal_length = [0.2222, 0.1667, 0.1111, 0.0833, 0.1944, 0.3056, 0.0833, 0.1944, 0.0278, 0.1667, 0.3056, 0.1389, 0.1389, 0.0, 0.4167, 0.3889, 0.3056, 0.2222, 0.3889, 0.2222, 0.3056, 0.2222, 0.0833, 0.2222, 0.1389, 0.1944, 0.1944, 0.25, 0.25, 0.1111, 0.1389, 0.3056, 0.25, 0.3333, 0.1667, 0.1944, 0.3333, 0.1667, 0.0278, 0.2222, 0.1944, 0.0556, 0.0278, 0.1944, 0.2222, 0.1389, 0.2222, 0.0833, 0.2778, 0.1944, 0.75, 0.5833, 0.7222, 0.3333, 0.6111, 0.3889, 0.5556, 0.1667, 0.6389, 0.25, 0.1944, 0.4444, 0.4722, 0.5, 0.3611, 0.6667, 0.3611, 0.4167, 0.5278, 0.3611, 0.4444, 0.5, 0.5556, 0.5, 0.5833, 0.6389, 0.6944, 0.6667, 0.4722, 0.3889, 0.3333, 0.3333, 0.4167, 0.4722, 0.3056, 0.4722, 0.6667, 0.5556, 0.3611, 0.3333, 0.3333, 0.5, 0.4167, 0.1944, 0.3611, 0.3889, 0.3889, 0.5278, 0.2222, 0.3889, 0.5556, 0.4167, 0.7778, 0.5556, 0.6111, 0.9167, 0.1667, 0.8333, 0.6667, 0.8056, 0.6111, 0.5833, 0.6944, 0.3889, 0.4167, 0.5833, 0.6111, 0.9444, 0.9444, 0.4722, 0.7222, 0.3611, 0.9444, 0.5556, 0.6667, 0.8056, 0.5278, 0.5, 0.5833, 0.8056, 0.8611, 1.0, 0.5833, 0.5556, 0.5, 0.9444, 0.5556, 0.5833, 0.4722, 0.7222, 0.6667, 0.7222, 0.4167, 0.6944, 0.6667, 0.6667, 0.5556, 0.6111, 0.5278, 0.4444]
        sepal_width = [0.625, 0.4167, 0.5, 0.4583, 0.6667, 0.7917, 0.5833, 0.5833, 0.375, 0.4583, 0.7083, 0.5833, 0.4167, 0.4167, 0.8333, 1.0, 0.7917, 0.625, 0.75, 0.75, 0.5833, 0.7083, 0.6667, 0.5417, 0.5833, 0.4167, 0.5833, 0.625, 0.5833, 0.5, 0.4583, 0.5833, 0.875, 0.9167, 0.4583, 0.5, 0.625, 0.6667, 0.4167, 0.5833, 0.625, 0.125, 0.5, 0.625, 0.75, 0.4167, 0.75, 0.5, 0.7083, 0.5417, 0.5, 0.5, 0.4583, 0.125, 0.3333, 0.3333, 0.5417, 0.1667, 0.375, 0.2917, 0.0, 0.4167, 0.0833, 0.375, 0.375, 0.4583, 0.4167, 0.2917, 0.0833, 0.2083, 0.5, 0.3333, 0.2083, 0.3333, 0.375, 0.4167, 0.3333, 0.4167, 0.375, 0.25, 0.1667, 0.1667, 0.2917, 0.2917, 0.4167, 0.5833, 0.4583, 0.125, 0.4167, 0.2083, 0.25, 0.4167, 0.25, 0.125, 0.2917, 0.4167, 0.375, 0.375, 0.2083, 0.3333, 0.5417, 0.2917, 0.4167, 0.375, 0.4167, 0.4167, 0.2083, 0.375, 0.2083, 0.6667, 0.5, 0.2917, 0.4167, 0.2083, 0.3333, 0.5, 0.4167, 0.75, 0.25, 0.0833, 0.5, 0.3333, 0.3333, 0.2917, 0.5417, 0.5, 0.3333, 0.4167, 0.3333, 0.4167, 0.3333, 0.75, 0.3333, 0.3333, 0.25, 0.4167, 0.5833, 0.4583, 0.4167, 0.4583, 0.4583, 0.4583, 0.2917, 0.5, 0.5417, 0.4167, 0.2083, 0.4167, 0.5833, 0.4167]
        petal_length = [0.0678, 0.0678, 0.0508, 0.0847, 0.0678, 0.1186, 0.0678, 0.0847, 0.0678, 0.0847, 0.0847, 0.1017, 0.0678, 0.0169, 0.0339, 0.0847, 0.0508, 0.0678, 0.1186, 0.0847, 0.1186, 0.0847, 0.0, 0.1186, 0.1525, 0.1017, 0.1017, 0.0847, 0.0678, 0.1017, 0.1017, 0.0847, 0.0847, 0.0678, 0.0847, 0.0339, 0.0508, 0.0678, 0.0508, 0.0847, 0.0508, 0.0508, 0.0508, 0.1017, 0.1525, 0.0678, 0.1017, 0.0678, 0.0847, 0.0678, 0.6271, 0.5932, 0.661, 0.5085, 0.6102, 0.5932, 0.6271, 0.3898, 0.6102, 0.4915, 0.4237, 0.5424, 0.5085, 0.6271, 0.4407, 0.5763, 0.5932, 0.5254, 0.5932, 0.4915, 0.6441, 0.5085, 0.661, 0.6271, 0.5593, 0.5763, 0.6441, 0.678, 0.5932, 0.4237, 0.4746, 0.4576, 0.4915, 0.6949, 0.5932, 0.5932, 0.6271, 0.5763, 0.5254, 0.5085, 0.5763, 0.6102, 0.5085, 0.3898, 0.5424, 0.5424, 0.5424, 0.5593, 0.339, 0.5254, 0.8475, 0.6949, 0.8305, 0.7797, 0.8136, 0.9492, 0.5932, 0.8983, 0.8136, 0.8644, 0.6949, 0.7288, 0.7627, 0.678, 0.6949, 0.7288, 0.7627, 0.9661, 1.0, 0.678, 0.7966, 0.661, 0.9661, 0.661, 0.7966, 0.8475, 0.6441, 0.661, 0.7797, 0.8136, 0.8644, 0.9153, 0.7797, 0.6949, 0.7797, 0.8644, 0.7797, 0.7627, 0.6441, 0.7458, 0.7797, 0.6949, 0.6949, 0.8305, 0.7966, 0.7119, 0.678, 0.7119, 0.7458, 0.6949]
        petal_width = [0.0417, 0.0417, 0.0417, 0.0417, 0.0417, 0.125, 0.0833, 0.0417, 0.0417, 0.0, 0.0417, 0.0417, 0.0, 0.0, 0.0417, 0.125, 0.125, 0.0833, 0.0833, 0.0833, 0.0417, 0.125, 0.0417, 0.1667, 0.0417, 0.0417, 0.125, 0.0417, 0.0417, 0.0417, 0.0417, 0.125, 0.0, 0.0417, 0.0417, 0.0417, 0.0417, 0.0, 0.0417, 0.0417, 0.0833, 0.0833, 0.0417, 0.2083, 0.125, 0.0833, 0.0417, 0.0417, 0.0417, 0.0417, 0.5417, 0.5833, 0.5833, 0.5, 0.5833, 0.5, 0.625, 0.375, 0.5, 0.5417, 0.375, 0.5833, 0.375, 0.5417, 0.5, 0.5417, 0.5833, 0.375, 0.5833, 0.4167, 0.7083, 0.5, 0.5833, 0.4583, 0.5, 0.5417, 0.5417, 0.6667, 0.5833, 0.375, 0.4167, 0.375, 0.4583, 0.625, 0.5833, 0.625, 0.5833, 0.5, 0.5, 0.5, 0.4583, 0.5417, 0.4583, 0.375, 0.5, 0.4583, 0.5, 0.5, 0.4167, 0.5, 1.0, 0.75, 0.8333, 0.7083, 0.875, 0.8333, 0.6667, 0.7083, 0.7083, 1.0, 0.7917, 0.75, 0.8333, 0.7917, 0.9583, 0.9167, 0.7083, 0.875, 0.9167, 0.5833, 0.9167, 0.7917, 0.7917, 0.7083, 0.8333, 0.7083, 0.7083, 0.7083, 0.8333, 0.625, 0.75, 0.7917, 0.875, 0.5833, 0.5417, 0.9167, 0.9583, 0.7083, 0.7083, 0.8333, 0.9583, 0.9167, 0.75, 0.9167, 1.0, 0.9167, 0.75, 0.7917, 0.9167, 0.7083]
        test_points = [i / 10 for i in range(11)]

        # exploratory visualization for the curious coder
        if plot:
            for name, feature in [("sepal length", sepal_length), ("sepal width", sepal_width),
                                  ("petal length", petal_length), ("petal width", petal_width)]:
                np.random.seed(331)
                x = np.array(feature)
                x_setosa, x_versicolour, x_virginica = x[:50], x[50:100], x[100:]
                x_test = np.array(test_points)
                plt.scatter(x=x_setosa, y=np.random.rand(len(x_setosa)), label="setosa")
                plt.scatter(x=x_versicolour, y=np.random.rand(len(x_versicolour)), label="versicolour")
                plt.scatter(x=x_virginica, y=np.random.rand(len(x_virginica)), label="virginica")
                plt.scatter(x=x_test, y=np.zeros(len(x_test)), c="k", label="test")
                plt.title(name)
                plt.xlabel("Value")
                plt.yticks([], [])
                plt.legend()
                plt.show()

        # 4a: sepal length
        data = zip(sepal_length, iris_labels)
        nnc = NearestNeighborClassifier(resolution=2)
        nnc.fit(data)
        expected = ['setosa', 'setosa', 'setosa', 'setosa', 'versicolor', 'versicolor',
                    'virginica', 'virginica', 'virginica', 'virginica', 'virginica']
        actual = [nnc.predict(x=x, delta=0.05) for x in test_points]
        self.assertEqual(expected, actual)

        # 4b: sepal width
        data = zip(sepal_width, iris_labels)
        nnc = NearestNeighborClassifier(resolution=2)
        nnc.fit(data)
        expected = ['versicolor', 'versicolor', 'versicolor', 'versicolor', 'versicolor',
                    'virginica', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa']
        actual = [nnc.predict(x=x, delta=0.05) for x in test_points]
        self.assertEqual(expected, actual)

        # 4c: petal length
        data = zip(petal_length, iris_labels)
        nnc = NearestNeighborClassifier(resolution=2)
        nnc.fit(data)
        expected = ['setosa', 'setosa', 'setosa', 'versicolor', 'versicolor', 'versicolor',
                    'versicolor', 'virginica', 'virginica', 'virginica', 'virginica']
        actual = [nnc.predict(x=x, delta=0.05) for x in test_points]
        self.assertEqual(expected, actual)

        # 4d: petal width
        data = zip(petal_width, iris_labels)
        nnc = NearestNeighborClassifier(resolution=2)
        nnc.fit(data)
        expected = ['setosa', 'setosa', 'setosa', None, 'versicolor', 'versicolor',
                    'versicolor', 'virginica','virginica', 'virginica', 'virginica']
        actual = [nnc.predict(x=x, delta=0.05) for x in test_points]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
