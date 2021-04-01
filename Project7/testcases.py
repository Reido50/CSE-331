import unittest

from PriorityQueue import MinNode, MaxNode, PriorityQueue, MaxHeap, heap_sort, current_medians
import random


class TestPriorityQueue(unittest.TestCase):
    """
    PriorityQueue + Heaps Project Test Cases
    """

    def test_minmax_nodes(self):

        # Compare Min Nodes
        node = MinNode(1, 1)
        other = MinNode(2, 2)
        self.assertTrue(node < other)
        self.assertFalse(node > other)

        other = MinNode(1, 2)
        self.assertTrue(node < other)
        self.assertFalse(node > other)

        other = MinNode(1, 1)
        self.assertFalse(node < other)
        self.assertFalse(node > other)

        other = MinNode(1, 0)
        self.assertFalse(node < other)
        self.assertTrue(node > other)

        other = MinNode(0, 0)
        self.assertFalse(node < other)
        self.assertTrue(node > other)

        # Compare Max Nodes
        node = MaxNode(1, 1)
        other = MaxNode(2, 2)
        self.assertFalse(node < other)
        self.assertTrue(node > other)

        other = MaxNode(1, 2)
        self.assertFalse(node < other)
        self.assertTrue(node > other)

        other = MaxNode(1, 1)
        self.assertFalse(node < other)
        self.assertFalse(node > other)

        other = MaxNode(1, 0)
        self.assertTrue(node < other)
        self.assertFalse(node > other)

        other = MaxNode(0, 0)
        self.assertTrue(node < other)
        self.assertFalse(node > other)

    def test_simple(self):

        # Test len, empty, peek
        pq = PriorityQueue()
        self.assertEqual(0, len(pq))
        self.assertTrue(pq.empty())
        self.assertIsNone(pq.peek())

        # Using integers in simple test rather than priority nodes
        pq._data = [10, 14, 19]
        self.assertEqual(3, len(pq))
        self.assertFalse(pq.empty())
        self.assertEqual(10, pq.peek())
        self.assertEqual(3, len(pq))

        pq._data.pop(0)
        self.assertEqual(2, len(pq))
        self.assertFalse(pq.empty())
        self.assertEqual(14, pq.peek())
        self.assertEqual(2, len(pq))

    def test_left_right_child(self):

        pq = PriorityQueue()
        # Using integers in rather than priority nodes for debugging
        pq._data = [10, 14, 19, 26, 31, 42, 27, 44, 35, 33]

        #                         10
        #                       /    \
        #                     14      19
        #                   /   \    /  \
        #                  26   31  42  27
        #                /  \   /
        #              44  35  33

        # Testing left child index
        self.assertEqual(1, pq.get_left_child_index(0))
        self.assertEqual(3, pq.get_left_child_index(1))
        self.assertEqual(5, pq.get_left_child_index(2))
        self.assertEqual(7, pq.get_left_child_index(3))
        self.assertEqual(9, pq.get_left_child_index(4))

        # Make sure the rest of results turn up None
        for i in range(5, len(pq)):
            self.assertIsNone(pq.get_left_child_index(i))
        # Test on edge case, now index doesn't exist
        pq._data.pop(0)
        self.assertIsNone(pq.get_left_child_index(4))

        # Using integers in rather than priority nodes for debugging
        pq._data = [10, 14, 19, 26, 31, 42, 27, 44, 35, 33]

        # Testing right child index
        self.assertEqual(2, pq.get_right_child_index(0))
        self.assertEqual(4, pq.get_right_child_index(1))
        self.assertEqual(6, pq.get_right_child_index(2))
        self.assertEqual(8, pq.get_right_child_index(3))

        for i in range(4, len(pq)):
            self.assertIsNone(pq.get_right_child_index(i))
        # Test on edge case, now index exists
        pq._data.append(36)
        self.assertEqual(10, pq.get_right_child_index(4))

    def test_parent_minmax_child(self):

        pq = PriorityQueue()
        # Using integers in rather than priority nodes for debugging
        pq._data = [10, 14, 19, 26, 31, 42, 27, 44, 35, 33]

        #                         10
        #                       /    \
        #                     14      19
        #                   /   \    /  \
        #                  26   31  42  27
        #                /  \   /
        #              44  35  33

        # Testing parent index
        self.assertIsNone(pq.get_parent_index(0))
        self.assertEqual(0, pq.get_parent_index(1))
        self.assertEqual(0, pq.get_parent_index(2))
        self.assertEqual(1, pq.get_parent_index(3))
        self.assertEqual(1, pq.get_parent_index(4))
        self.assertEqual(2, pq.get_parent_index(5))
        self.assertEqual(2, pq.get_parent_index(6))
        self.assertEqual(3, pq.get_parent_index(7))
        self.assertEqual(3, pq.get_parent_index(8))
        self.assertEqual(4, pq.get_parent_index(9))

        # Testing min / max child index
        self.assertEqual(1, pq.get_minmax_child_index(0))
        self.assertEqual(3, pq.get_minmax_child_index(1))
        self.assertEqual(6, pq.get_minmax_child_index(2))
        self.assertEqual(8, pq.get_minmax_child_index(3))
        self.assertEqual(9, pq.get_minmax_child_index(4))

        for i in range(5, len(pq)):
            self.assertIsNone(pq.get_minmax_child_index(i))

    def test_percolate_up(self):

        pq = PriorityQueue()
        # Using integers in rather than priority nodes for debugging
        pq._data = [26, 19, 42, 44, 31, 14, 27, 10, 35, 33]

        #                         26
        #                       /    \
        #                     19      42
        #                   /   \    /  \
        #                  44   31  14  27
        #                /  \   /
        #              10  35  33

        pq.percolate_up(1)
        expected = [19, 26, 42, 44, 31, 14, 27, 10, 35, 33]
        self.assertEqual(expected, pq._data)

        #                         19
        #                       /    \
        #                     26      42
        #                   /   \    /  \
        #                  44   31  14  27
        #                /  \   /
        #              10  35  33

        pq.percolate_up(5)
        expected = [14, 26, 19, 44, 31, 42, 27, 10, 35, 33]
        self.assertEqual(expected, pq._data)

        #                         14
        #                       /    \
        #                     26      19
        #                   /   \    /  \
        #                  44   31  42  27
        #                /  \   /
        #              10  35  33

        pq.percolate_up(7)
        expected = [10, 14, 19, 26, 31, 42, 27, 44, 35, 33]
        self.assertEqual(expected, pq._data)

        #                         10
        #                       /    \
        #                     14      19
        #                   /   \    /  \
        #                  26   31  42  27
        #                /  \   /
        #              44  35  33

        # Assert heap structure no longer needs to percolate up
        for i, _ in enumerate(pq._data):
            pq.percolate_up(i)
            expected = [10, 14, 19, 26, 31, 42, 27, 44, 35, 33]
            self.assertEqual(expected, pq._data)

    def test_percolate_down(self):

        pq = PriorityQueue()
        # Using integers in rather than priority nodes for debugging
        pq._data = [33, 35, 42, 10, 14, 19, 27, 44, 26, 31]

        #                         33
        #                       /    \
        #                     35      42
        #                   /   \    /  \
        #                  10   14  19  27
        #                /  \   /
        #              44  26  31

        pq.percolate_down(2)
        expected = [33, 35, 19, 10, 14, 42, 27, 44, 26, 31]
        self.assertEqual(expected, pq._data)

        #                         33
        #                       /    \
        #                     35      19
        #                   /   \    /  \
        #                  10   14  42  27
        #                /  \   /
        #              44  26  31

        pq.percolate_down(1)
        expected = [33, 10, 19, 26, 14, 42, 27, 44, 35, 31]
        self.assertEqual(expected, pq._data)

        #                         33
        #                       /    \
        #                     10      19
        #                   /   \    /  \
        #                  26   14  42  27
        #                /  \   /
        #              44  35  31

        pq.percolate_down(0)
        expected = [10, 14, 19, 26, 31, 42, 27, 44, 35, 33]
        self.assertEqual(expected, pq._data)

        #                         10
        #                       /    \
        #                     14      19
        #                   /   \    /  \
        #                  26   31  42  27
        #                /  \   /
        #              44  35  33

        # Assert heap structure no longer needs to percolate down
        for i, _ in enumerate(pq._data):
            pq.percolate_down(i)
            expected = [10, 14, 19, 26, 31, 42, 27, 44, 35, 33]
            self.assertEqual(expected, pq._data)

    def test_push(self):

        pq = PriorityQueue()

        pq.push(1, 'S')
        pq.push(2, 'P')
        pq.push(3, 'A')
        pq.push(4, 'R')
        pq.push(5, 'T')
        pq.push(6, 'Y')
        expected_values = ['S', 'P', 'A', 'R', 'T', 'Y']

        for i, node in enumerate(pq._data):
            self.assertEqual(expected_values[i], node.value)

        self.assertEqual(6, len(pq._data))

        #                         S
        #                       /   \
        #                      P     A
        #                    /  \   /
        #                   R   T  Y

        pq = PriorityQueue()

        pq.push(8, 'A')
        pq.push(4, 'L')
        pq.push(3, 'G')
        pq.push(2, 'O')
        pq.push(5, 'R')
        pq.push(1, 'I')
        pq.push(6, 'T')
        pq.push(9, 'H')
        pq.push(7, 'M')
        expected_set = {'A', 'L', 'G', 'O', 'R', 'I', 'T', 'H', 'M'}

        # Only makes sure each value is in pq's data
        for i, node in enumerate(pq._data):
            self.assertIn(node.value, expected_set)

        self.assertEqual(9, len(pq._data))

        #                          I
        #                       /    \
        #                     G       O
        #                   /   \    /  \
        #                  M    R   L   T
        #                /   \
        #               H    A

    def test_push_comprehensive(self):

        # Test push with more inputs and duplicate values / priorities
        random.seed(2021)
        values = "Michigan State Spartans Presented by Rocket Mortgage"
        values_array = list(values)
        priorities = [random.randint(0, 100) for _ in range(len(values))]

        pq = PriorityQueue()

        for i, val in enumerate(values_array):
            pq.push(priorities[i], val)

        expected_priorities = [4, 6, 6, 8, 13, 14, 14, 20, 9, 14, 28, 31, 28, 59, 25, 77, 56, 35, 21, 47, 35, 31, 56,
                               37, 69, 34, 68, 87, 69, 60, 37, 80, 81, 56, 81, 60, 67, 43, 85, 95, 50, 88, 73, 86, 51,
                               91, 59, 81, 60, 82, 70, 40]
        expected_values = ['a', 'r', 'r', 't', 'a', 'g', 'n', 'p', 'S', 't', ' ', 'i', 'e', 'e', 't', 'e', ' ', 'y',
                           'a', 'c', 'h', 'M', 'r', 'P', 'g', 't', 'e', 's', 'c', ' ', 'e', 'i', 'd', 'n', 'b', ' ',
                           ' ', 'R', 'o', 't', 'k', 'e', 'S', 'n', 'M', 's', 'o', 'g', 't', 'a', ' ', 'a']

        self.assertEqual(4, pq.peek().priority)
        self.assertEqual('a', pq.peek().value)
        self.assertEqual(len(values_array), len(pq))
        self.assertFalse(pq.empty())

        for i, node in enumerate(pq._data):
            self.assertEqual(expected_priorities[i], node.priority)
            self.assertEqual(expected_values[i], node.value)

        expected = pq._data[:]
        # Assert no need to percolate down anymore, priority queue is correctly prioritized
        for i, _ in enumerate(pq._data):
            pq.percolate_down(i)
            self.assertEqual(expected, pq._data)

        # Assert no need to percolate up anymore, priority queue is correctly prioritized
        for i, _ in enumerate(pq._data):
            pq.percolate_up(i)
            self.assertEqual(expected, pq._data)

    def test_pop(self):

        pq = PriorityQueue()

        pq.push(1, 'S')
        pq.push(2, 'P')
        pq.push(3, 'A')
        pq.push(4, 'R')
        pq.push(5, 'T')
        pq.push(6, 'Y')
        expected_values = ['S', 'P', 'A', 'R', 'T', 'Y']

        #                         S
        #                       /   \
        #                      P     A
        #                    /  \   /
        #                   R   T  Y

        for i in range(6):
            popped = pq.pop()
            self.assertEqual(expected_values[i], popped.value)

        self.assertIsNone(pq.pop())
        self.assertEqual(0, len(pq))

        pq = PriorityQueue()

        pq.push(8, 'A')
        pq.push(4, 'L')
        pq.push(3, 'G')
        pq.push(2, 'O')
        pq.push(5, 'R')
        pq.push(1, 'I')
        pq.push(6, 'T')
        pq.push(9, 'H')
        pq.push(7, 'M')
        expected_set = {'A', 'L', 'G', 'O', 'R', 'I', 'T', 'H', 'M'}

        #                          I
        #                       /    \
        #                     G       O
        #                   /   \    /  \
        #                  M    R   L   T
        #                /   \
        #               H    A

        # Only makes sure each value popped is in pq's data
        for i in range(9):
            popped = pq.pop()
            self.assertIn(popped.value, expected_set)

        self.assertIsNone(pq.pop())
        self.assertEqual(0, len(pq))

    def test_pop_comprehensive(self):

        # Test pop with more inputs and duplicate values / priorities
        random.seed(2021)
        values = "It wasn't my idea to release this project right before March Madness, I promise!"
        values_array = list(values)
        priorities = [random.randint(0, 100) for _ in range(len(values))]

        pq = PriorityQueue()

        for i, val in enumerate(values_array):
            pq.push(priorities[i], val)

        expected_priorities = [0, 2, 4, 6, 6, 6, 8, 9, 9, 10, 13, 14, 14, 14, 17, 20, 21, 21, 22, 24, 25, 28, 28, 29,
                               31,
                               31, 31, 33, 34, 35, 35, 35, 35, 36, 37, 37, 40, 43, 47, 47, 50, 51, 51, 54, 56, 56, 56,
                               57, 59, 59, 59, 60, 60, 60, 60, 67, 68, 68, 69, 69, 70, 73, 74, 74, 77, 80, 81, 81, 81,
                               82, 83, 85, 86, 87, 88, 88, 91, 95, 96, 96]
        expected_values = ['r', 'c', 'n', 'a', 'r', 't', 'm', 'e', 'm', 'i', ' ', 'b', 'r', 't', 'M', 'a', ' ', 'n',
                           's', 'a', 'h', 'i', 'o', 'M', 'a', 'e', 'g', 'p', ' ', 'a', 'o', 'r', 'w', ' ', 'e', 'i',
                           'y', 'j', 'I', 'c', 't', 'I', 's', 's', ' ', "'", 't', '!', ' ', 'h', 'r', ' ', 'd', 'e',
                           't', 'o', 'h', 's', ' ', 'f', 'l', ' ', ',', 'e', 'i', 't', 'p', 's', 's', 'e', ' ', 'e',
                           'r', 'e', ' ', ' ', 'e', 'o', ' ', 'd']

        # Assert priority queue properly implemented
        for i, _ in enumerate(values_array):
            popped = pq.pop()
            self.assertEqual(expected_priorities[i], popped.priority)
            self.assertEqual(expected_values[i], popped.value)

        # Assert priority queue is empty and no longer can be popped from
        self.assertTrue(pq.empty())
        self.assertIsNone(pq.pop())

    def test_heap_sort(self):

        # Test empty array
        array = []
        expected = []
        heap_sort(array)
        self.assertEqual(expected, array)

        # Test sorted array
        array = [1, 2, 3, 4, 5]
        expected = array[:]
        heap_sort(array)
        self.assertEqual(expected, array)

        # Test unsorted array
        array = [33, 35, 42, 10, 14, 19, 27, 44, 26, 31]
        expected = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
        heap_sort(array)
        self.assertEqual(expected, array)

    def test_comprehensive(self):

        # Test Max Priority Queue
        pq = PriorityQueue(False)

        self.assertTrue(pq.empty())

        random.seed(2021)
        values = "Fun fact: A heap in which each node has up to two parents is called a beap :)"
        values_array = list(values)
        priorities = [random.randint(0, 100) for _ in range(len(values))]

        for i, val in enumerate(values_array):
            pq.push(priorities[i], val)

        expected_priorities = [96, 96, 95, 91, 88, 82, 87, 85, 88, 86, 81, 70, 68, 60, 80, 81, 83, 81, 67, 50, 60,
                               31, 73, 60, 69, 59, 60, 35, 59, 68, 29, 56, 51, 74, 77, 51, 35, 10, 43, 31, 47, 13,
                               14, 8, 28, 59, 56, 40, 14, 37, 69, 6, 28, 34, 36, 4, 17, 0, 2, 14, 37, 25, 24, 9, 21,
                               31, 35, 20, 54, 56, 47, 21, 33, 6, 35, 6, 9]

        expected_values = ['l', ' ', ' ', 'i', 'p', ' ', 'a', 's', 'e', 'h', 'a', 'c', 'e', 'a', 'u', 'e', ' ', 'o',
                           'h', 'u', ':', 'o', ' ', 'w', 'p', 'r', 'e', 's', 'c', 's', 'c', 't', 'd', 'a', 'n', 'F',
                           ' ', ')', 'a', 'f', ' ', 'w', ' ', 'A', 't', ' ', 't', ' ', 'o', 'h', 'n', ' ', 'a', 'h',
                           'n', 'c', 't', ' ', 'i', 'h', 'e', ' ', 'a', 'p', 'l', 'e', ' ', ' ', ' ', 'd', 'b', 'i',
                           'a', 'p', ' ', 'n', ':']

        self.assertEqual(96, pq.peek().priority)
        self.assertEqual('l', pq.peek().value)
        self.assertEqual(len(values_array), len(pq))
        self.assertFalse(pq.empty())

        for i, node in enumerate(pq._data):
            self.assertEqual(expected_priorities[i], node.priority)
            self.assertEqual(expected_values[i], node.value)

        expected = pq._data[:]
        # Assert no need to percolate down anymore, priority queue is correctly prioritized
        for i, _ in enumerate(pq._data):
            pq.percolate_down(i)
            self.assertEqual(expected, pq._data)

        # Assert no need to percolate up anymore, priority queue is correctly prioritized
        for i, _ in enumerate(pq._data):
            pq.percolate_up(i)
            self.assertEqual(expected, pq._data)

        expected_priorities = [96, 96, 95, 91, 88, 88, 87, 86, 85, 83, 82, 81, 81, 81, 80, 77, 74, 73, 70, 69, 69, 68,
                               68, 67, 60, 60, 60, 60, 59, 59, 59, 56, 56, 56, 54, 51, 51, 50, 47, 47, 43, 40, 37, 37,
                               36, 35, 35, 35, 35, 34, 33, 31, 31, 31, 29, 28, 28, 25, 24, 21, 21, 20, 17, 14, 14, 14,
                               13, 10, 9, 9, 8, 6, 6, 6, 4, 2, 0]
        expected_values = ['l', ' ', ' ', 'i', 'p', 'e', 'a', 'h', 's', ' ', ' ', 'o', 'e', 'a', 'u', 'n', 'a', ' ',
                           'c', 'p', 'n', 's', 'e', 'h', 'w', 'e', 'a', ':', 'r', 'c', ' ', 't', 't', 'd', ' ', 'd',
                           'F', 'u', 'b', ' ', 'a', ' ', 'h', 'e', 'n', 's', ' ', ' ', ' ', 'h', 'a', 'o', 'f', 'e',
                           'c', 't', 'a', ' ', 'a', 'l', 'i', ' ', 't', 'o', 'h', ' ', 'w', ')', 'p', ':', 'A', 'p',
                           'n', ' ', 'c', 'i', ' ']

        # Assert as you remove nodes priorities and values are correct
        for i, _ in enumerate(values_array):
            self.assertEqual(len(values_array) - i, len(pq))

            self.assertEqual(expected_priorities[i], pq.peek().priority)
            self.assertEqual(expected_values[i], pq.peek().value)

            popped = pq.pop()
            self.assertEqual(expected_priorities[i], popped.priority)
            self.assertEqual(expected_values[i], popped.value)

        # Assert priority queue is empty and no longer can be popped from
        self.assertTrue(pq.empty())
        self.assertIsNone(pq.pop())

        random.seed(2021)
        # Heap Sort!
        array = [random.randint(0, 331) for _ in range(21)]
        expected = [17, 27, 32, 39, 53, 82, 84, 126, 138, 141, 151, 160, 206, 227, 242, 243, 278, 280, 294, 322, 325]
        heap_sort(array)
        self.assertEqual(expected, array)

        array = [random.randint(0, 273331721) for _ in range(10000)]
        expected = sorted(array)
        heap_sort(array)
        self.assertEqual(expected, array)

    def test_max_heap(self):

        heap = MaxHeap()
        self.assertTrue(heap.empty())

        random.seed(2021)
        values = [random.randint(0, 331) for _ in range(102)]

        expected_data = [331, 326, 325, 322, 323, 299, 325, 269, 299, 315, 323, 278, 274, 308, 322, 143, 230, 296, 223,
                         294, 243, 280, 287, 259, 273, 58, 138, 99, 243, 297, 225, 140, 141, 190, 227, 202, 219, 137,
                         203, 237, 242, 240, 177, 231, 277, 237, 113, 242, 221, 239, 143, 2, 10, 102, 117, 17, 87, 126,
                         205, 151, 218, 188, 133, 27, 39, 39, 43, 82, 89, 172, 112, 84, 70, 57, 206, 27, 124, 112, 90,
                         53, 218, 69, 226, 126, 145, 55, 59, 5, 32, 150, 150, 26, 180, 57, 38, 160, 47, 144, 167, 69,
                         49, 51]

        for i, elem in enumerate(values):
            heap.push(elem)
            self.assertEqual(i + 1, len(heap))

        for i, value in enumerate(expected_data):
            self.assertEqual(expected_data[i], heap._pqueue._data[i].value)
            self.assertEqual(expected_data[i], heap._pqueue._data[i].priority)

        self.assertEqual(331, heap.peek())
        self.assertFalse(heap.empty())

        expected = heap._pqueue._data[:]
        # Assert no need to percolate down anymore, heap is correct
        for i, _ in enumerate(heap._pqueue._data):
            heap._pqueue.percolate_down(i)
            self.assertEqual(expected, heap._pqueue._data)

        # Assert no need to percolate up anymore, heap is correct
        for i, _ in enumerate(heap._pqueue._data):
            heap._pqueue.percolate_up(i)
            self.assertEqual(expected, heap._pqueue._data)

        expected_popped = [331, 326, 325, 325, 323, 323, 322, 322, 315, 308, 299, 299, 297, 296, 294, 287, 280, 278,
                           277, 274, 273, 269, 259, 243, 243, 242, 242, 240, 239, 237, 237, 231, 230, 227, 226, 225,
                           223, 221, 219, 218, 218, 206, 205, 203, 202, 190, 188, 180, 177, 172, 167, 160, 151, 150,
                           150, 145, 144, 143, 143, 141, 140, 138, 137, 133, 126, 126, 124, 117, 113, 112, 112, 102,
                           99, 90, 89, 87, 84, 82, 70, 69, 69, 59, 58, 57, 57, 55, 53, 51, 49, 47, 43, 39, 39, 38,
                           32, 27, 27, 26, 17, 10, 5, 2]

        # Assert as you remove nodes priorities and values are correct
        for i, _ in enumerate(values):
            self.assertEqual(len(values) - i, len(heap))

            self.assertEqual(expected_popped[i], heap.peek())

            popped = heap.pop()
            self.assertEqual(expected_popped[i], popped)

        # Assert heap is empty and no longer can be popped from
        self.assertTrue(heap.empty())
        self.assertIsNone(heap.pop())

    def test_current_medians_simple(self):
        data_list = [2, 4, 6, 8, 10]
        self.assertEqual([2, 3, 4, 5, 6], current_medians(data_list))

    def test_current_medians(self):
        # test 1: tests empty list
        array = []
        result = current_medians(array)
        self.assertEqual([], result)

        # test 2: tests list with one element
        array = [4]
        result = current_medians(array)
        self.assertEqual([4], result)

        # test 3: tests that decimal values are returned for averages
        array = [4, 9]
        result = current_medians(array)
        self.assertEqual([4, 6.5], result)

        # test 4: tests that values are being sorted as data read in
        array = [1, 2, 10, 11, 12, 13, 14, 6, 7, 8]
        result = current_medians(array)
        self.assertEqual([1, 1.5, 2, 6, 10, 10.5, 11, 10.5, 10, 9], result)

        array = [47, 98, 2, 34, 51, 20, 32, 19, 99, 23, 1, 9, 4, 2, 22]
        result = current_medians(array)
        self.assertEqual([47, 72.5, 47, 40.5, 47, 40.5, 34, 33, 34, 33, 32, 27.5, 23, 21.5, 22], result)

        # test 5: tests skewed data
        array = [200, 234, 231, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        result = current_medians(array)
        self.assertEqual([200, 217, 231, 215.5, 200, 101, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], result)

        # test 5: tests negatives
        array = [i for i in range(-5, 6)]
        result = current_medians(array)
        self.assertEqual([-5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5, 0], result)

    def test_current_medians_comprehensive(self):
        random.seed(20)

        # test1: tests very large random array for heap sort
        array = []
        for i in range(0, 100):
            array.append(random.randint(0, 1000))
        array = set(array)
        array = list(array)
        heap_sort(array)
        last = -1
        for i in range(0, 92):
            self.assertGreaterEqual(array[i], last)
            last = array[i]

        # test2: tests very large array for current medians
        array = [i for i in range(0, 40000, 2)]
        result = current_medians(array)
        solution = [i for i in range(20000)]
        self.assertEqual(solution, result)

if __name__ == '__main__':
    unittest.main()
