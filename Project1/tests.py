"""
Project 1
CSE 331 S21 (Onsay)
Reid Harry
tests.py
"""

from DLL import DLL, Node, Stock, intellivest
from typing import TypeVar, List
from random import seed, shuffle
import datetime
import copy
import unittest
import cProfile

# for more information on typehinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")            # represents generic type


class DLLTests(unittest.TestCase):

    def check_dll(self, expected: List[T], dll: DLL):
        """
        Assert structure of dll is proper and contains the values of result.
        Used as helper function throughout testcases. Not an actual testcase itself.
        Collapse/hide this by clicking the minus arrow on the left sidebar.

        :param expected: list of expected values in dll
        :param dll: DLL to be validated
        :return: None. Raises exception and fails testcase if structure is DLL is not properly structured
                 or contains values different from those in result.
        """
        # check size
        self.assertEqual(len(expected), dll.size)

        # short-circuit if empty list
        if dll.size == 0:
            self.assertIsNone(dll.head)
            self.assertIsNone(dll.tail)
            return

        # check head and tail
        self.assertIsNone(dll.head.prev)
        self.assertEqual(expected[0], dll.head.value)
        self.assertIsNone(dll.tail.next)
        self.assertEqual(expected[-1], dll.tail.value)

        # check all intermediate connections and values
        left, right = dll.head, dll.head.next
        i = 0
        while right is not None:
            self.assertIs(left.next, right)
            self.assertIs(left, right.prev)
            self.assertEqual(expected[i], left.value)
            self.assertEqual(expected[i + 1], right.value)
            left, right = left.next, right.next
            i += 1

    def test_empty(self):

        # (1) empty DLL
        dll = DLL()
        self.assertTrue(dll.empty())

        # (2) DLL with one node
        dll.head = dll.tail = Node(1)
        dll.size += 1
        self.assertFalse(dll.empty())

        # (3) DLL with multiple nodes
        for i in range(0, 50):
            dll.tail.next = Node(i, None, dll.tail)
            dll.tail = dll.tail.next
            dll.size += 1
            self.assertFalse(dll.empty())

        # (4) DLL after removing all nodes
        dll.head = dll.tail = None
        dll.size = 0
        self.assertTrue(dll.empty())

    def test_push(self):

        # (1) push single node on back
        dll = DLL()
        dll.push(0)
        self.assertIs(dll.head, dll.tail)   # see note 8 in specs for `is` vs `==`
        self.check_dll([0], dll)            # if failure here, see (1).
        # pro tip: use CTRL + B with your cursor on check_dll to jump to its definition at the top of the file.
        # then, use CTRL + Alt + RightArrow to jump back here!
        # https://www.jetbrains.com/help/pycharm/navigating-through-the-source-code.html

        # (2) push single node on front
        dll = DLL()
        dll.push(0, back=False)
        self.assertIs(dll.head, dll.tail)
        self.check_dll([0], dll)            # if failure here, see (2)

        # (3) push multiple nodes on back
        dll = DLL()
        lst = []
        for i in range(5):
            dll.push(i)
            lst.append(i)
            self.check_dll(lst, dll)        # if failure here, see (3)

        # (4) push multiple nodes on front
        dll = DLL()
        lst = []
        for i in range(5):
            dll.push(i, back=False)
            lst.insert(0, i)
            self.check_dll(lst, dll)        # if failure here, see (4)

        # (5) alternate pushing onto front and back
        dll = DLL()
        lst = []
        for i in range(50):
            dll.push(i, i % 2 == 0)         # push back if i is even, else push front
            if i % 2 == 0:                  # pushed back, new tail
                lst.append(i)
                self.check_dll(lst, dll)    # if failure here, see (5)
            else:                           # pushed front, new head
                lst.insert(0, i)
                self.check_dll(lst, dll)    # if failure here, see (5)

    def test_pop(self):

        # (1) pop back on empty list (should do nothing)
        dll = DLL()
        try:
            dll.pop()
        except Exception as e:
            self.fail(msg=f"Raised {type(e)} when popping from back of empty list.")

        # (2) pop front on empty list (should do nothing)
        dll = DLL()
        try:
            dll.pop(back=False)
        except Exception as e:
            self.fail(msg=f"Raised {type(e)} when popping from front of empty list.")

        # (3) pop back on multiple node list
        dll = DLL()
        lst = []
        for i in range(5):          # construct list
            dll.push(i)
            lst.append(i)
        for i in range(5):          # destruct list
            dll.pop()
            lst.pop()
            self.check_dll(lst, dll)     # if failure here, see (3)

        # (4) pop front on multiple node list
        dll = DLL()
        lst = []
        for i in range(5):          # construct list
            dll.push(i)
            lst.append(i)
        for i in range(5):          # destruct list
            dll.pop(back=False)
            lst.pop(0)
            self.check_dll(lst, dll)     # if failure here, see (4)

        # (5) alternate popping from front, back
        dll = DLL()
        lst = []
        for i in range(50):
            dll.push(i)
            lst.append(i)
        for end in range(49):           # remove all but one node
            dll.pop(end % 2 == 0)       # pop back if even, front if odd
            if end % 2 == 0:            # removed tail
                lst.pop()
                self.check_dll(lst, dll)     # if failure here, see (5)
            else:                       # removed head
                lst.pop(0)
                self.check_dll(lst, dll)     # if failure here, see (5)

        # (6) check there is exactly one node left in DLL (middle of original), then remove
        self.check_dll([24], dll)        # if failure here, see (6)
        dll_copy = copy.deepcopy(dll)
        dll.pop()                   # remove tail
        dll_copy.pop(back=False)    # remove head
        self.check_dll([], dll)          # if failure here, see (6)
        self.check_dll([], dll_copy)     # if failure here, see (6)

    def test_from_list(self):

        # (1) create DLL from empty list
        dll = DLL()
        dll.from_list([])
        self.check_dll([], dll)              # if failure here, see (1)

        # (2) create DLL from longer lists
        for i in range(50):
            source = list(range(i))
            dll = DLL()
            dll.from_list(source)
            self.check_dll(source, dll)      # if failure here, see (2)

    def test_to_list(self):

        # (1) create list from empty DLL
        dll = DLL()
        output = dll.to_list()
        self.check_dll(output, dll)          # if failure here, see (1)

        # (2) create list from longer DLLs
        for i in range(50):
            dll = DLL()
            for j in range(i):
                dll.push(j)
            output = dll.to_list()
            self.check_dll(output, dll)      # if failure here, see (2)

    def test_find(self):

        # (1) find in empty DLL
        dll = DLL()
        node = dll.find(331)
        self.assertIsNone(node)

        # (2) find existing value in single-node DLL
        dll = DLL()
        dll.push(0)
        node = dll.find(0)
        self.assertIsInstance(node, Node)
        self.assertEqual(0, node.value)
        self.assertIsNone(node.next)
        self.assertIsNone(node.prev)

        # (3) find non-existing value in single-node DLL
        node = dll.find(331)
        self.assertIsNone(node)

        # (4) find in longer DLL with all unique values
        dll = DLL()
        for i in range(10):
            dll.push(i)

        node = dll.find(0)
        self.assertIsInstance(node, Node)
        self.assertIs(dll.head, node)
        self.assertIsNone(node.prev)
        self.assertEqual(0, node.value)
        self.assertEqual(1, node.next.value)

        node = dll.find(9)
        self.assertIsInstance(node, Node)
        self.assertIs(dll.tail, node)
        self.assertIsNone(node.next)
        self.assertEqual(9, node.value)
        self.assertEqual(8, node.prev.value)

        node = dll.find(4)
        self.assertIsInstance(node, Node)
        self.assertEqual(4, node.value)
        self.assertEqual(3, node.prev.value)
        self.assertEqual(5, node.next.value)

        node = dll.find(331)
        self.assertIsNone(node)

        # (5) find first instance in longer DLL with duplicated values
        for i in range(9, 0, -1):     # DLL will be 0, 1, ..., 9, 9, 8, ..., 0
            dll.push(i)

        node = dll.find(0)      # should find head 0, not tail 0
        self.assertIsInstance(node, Node)
        self.assertIs(dll.head, node)
        self.assertIsNone(node.prev)
        self.assertEqual(0, node.value)
        self.assertEqual(1, node.next.value)

        node = dll.find(9)      # should find first 9
        self.assertIsInstance(node, Node)
        self.assertEqual(9, node.value)
        self.assertEqual(8, node.prev.value)
        self.assertEqual(9, node.next.value)

        node = dll.find(4)      # should find first 4
        self.assertIsInstance(node, Node)
        self.assertEqual(4, node.value)
        self.assertEqual(3, node.prev.value)
        self.assertEqual(5, node.next.value)

        node = dll.find(331)
        self.assertIsNone(node)

    def test_find_all(self):
        # (1) find_all in empty DLL
        dll = DLL()
        nodes = dll.find_all(331)
        self.assertEqual([], nodes)

        # (2) find_all existing value in single-node DLL
        dll = DLL()
        dll.push(0)
        nodes = dll.find_all(0)
        self.assertIsInstance(nodes, List)
        self.assertEqual(1, len(nodes))
        self.assertEqual(0, nodes[0].value)
        self.assertIsNone(nodes[0].next)
        self.assertIsNone(nodes[0].prev)

        # (3) find non-existing value in single-node DLL
        nodes = dll.find_all(331)
        self.assertEqual([], nodes)

        # (4) find_all in longer DLL with all unique values
        dll = DLL()
        for i in range(10):
            dll.push(i)

        nodes = dll.find_all(0)
        self.assertIsInstance(nodes, List)
        self.assertEqual(1, len(nodes))
        self.assertIs(dll.head, nodes[0])
        self.assertIsNone(nodes[0].prev)
        self.assertEqual(0, nodes[0].value)
        self.assertEqual(1, nodes[0].next.value)

        nodes = dll.find_all(9)
        self.assertIsInstance(nodes, List)
        self.assertEqual(1, len(nodes))
        self.assertIs(dll.tail, nodes[0])
        self.assertIsNone(nodes[0].next)
        self.assertEqual(9, nodes[0].value)
        self.assertEqual(8, nodes[0].prev.value)

        nodes = dll.find_all(4)
        self.assertIsInstance(nodes, List)
        self.assertEqual(1, len(nodes))
        self.assertEqual(4, nodes[0].value)
        self.assertEqual(3, nodes[0].prev.value)
        self.assertEqual(5, nodes[0].next.value)

        nodes = dll.find_all(331)
        self.assertEqual([], nodes)

        # (5) find all instances in longer DLL with duplicated values
        for i in range(9, -1, -1):     # DLL will be 0, 1, ..., 9, 9, 8, ..., 0
            dll.push(i)

        nodes = dll.find_all(0)
        self.assertIsInstance(nodes, List)
        self.assertEqual(2, len(nodes))
        self.assertIs(dll.head, nodes[0])
        self.assertIsNone(nodes[0].prev)
        self.assertEqual(0, nodes[0].value)
        self.assertEqual(1, nodes[0].next.value)
        self.assertIs(dll.tail, nodes[1])
        self.assertIsNone(nodes[1].next)
        self.assertEqual(0, nodes[1].value)
        self.assertEqual(1, nodes[1].prev.value)

        nodes = dll.find_all(9)
        self.assertIsInstance(nodes, List)
        self.assertEqual(2, len(nodes))
        self.assertEqual(9, nodes[0].value)
        self.assertEqual(8, nodes[0].prev.value)
        self.assertEqual(9, nodes[0].next.value)
        self.assertEqual(9, nodes[1].value)
        self.assertEqual(9, nodes[1].prev.value)
        self.assertEqual(8, nodes[1].next.value)

        nodes = dll.find_all(4)
        self.assertIsInstance(nodes, List)
        self.assertEqual(2, len(nodes))
        self.assertEqual(4, nodes[0].value)
        self.assertEqual(3, nodes[0].prev.value)
        self.assertEqual(5, nodes[0].next.value)
        self.assertEqual(4, nodes[1].value)
        self.assertEqual(5, nodes[1].prev.value)
        self.assertEqual(3, nodes[1].next.value)

        nodes = dll.find_all(331)
        self.assertEqual([], nodes)

    def test_delete(self):

        # (1) delete from empty DLL
        dll = DLL()
        result = dll.delete(331)
        self.assertFalse(result)

        # (2) delete existing value in single-node DLL
        dll = DLL()
        dll.push(0)
        result = dll.delete(0)
        self.assertTrue(result)
        self.check_dll([], dll)              # if failure here, see (2)

        # (3) delete non-existing value in single-node DLL
        dll = DLL()
        dll.push(0)
        result = dll.delete(331)
        self.assertFalse(result)
        self.check_dll([0], dll)             # if failure here, see (3)

        # (4) delete from longer DLL with all unique values
        dll = DLL()
        lst = []
        for i in range(10):
            dll.push(i)
            lst.append(i)

        to_delete = [1, 4, 7, 5, 6, 3, 2, 9, 0, 8]
        for i in range(10):
            result = dll.delete(to_delete[i])
            self.assertTrue(result)
            result = dll.delete(331)
            self.assertFalse(result)

            lst.remove(to_delete[i])
            self.check_dll(lst, dll)     # if failure here, see (4)

        # (5) delete first instance in longer DLL with duplicated values
        dll = DLL()
        lst = []
        for i in range(10):
            dll.push(i)
            lst.append(i)
        for i in range(9, -1, -1):      # DLL will be 0, 1, ..., 9, 9, 8, ..., 0
            dll.push(i)
            lst.append(i)

        to_delete = [1, 4, 7, 5, 6, 3, 2, 9, 0, 8]
        for i in range(10):
            result = dll.delete(to_delete[i])
            self.assertTrue(result)
            result = dll.delete(331)
            self.assertFalse(result)

            lst.remove(to_delete[i])
            self.check_dll(lst, dll)     # if failure here, see (5)

        # (6) sanity check after deletions
        lst = list(range(9, -1, -1))
        self.check_dll(lst, dll)         # if failure here, see (6)

    def test_delete_all(self):

        # (1) delete all from empty DLL
        dll = DLL()
        count = dll.delete_all(331)
        self.assertEqual(0, count)

        # (2) delete existing value in single-node DLL
        dll = DLL()
        dll.push(0)
        count = dll.delete_all(0)
        self.assertEqual(1, count)
        self.check_dll([], dll)              # if failure here, see (2)

        # (3) delete non-existing value in single-node DLL
        dll = DLL()
        dll.push(0)
        count = dll.delete_all(331)
        self.assertEqual(0, count)
        self.check_dll([0], dll)             # if failure here, see (3)

        # (4) delete from longer DLL with all unique values
        dll = DLL()
        lst = []
        for i in range(10):
            dll.push(i)
            lst.append(i)

        to_delete = [1, 4, 7, 5, 6, 3, 2, 9, 0, 8]
        for i in range(10):
            count = dll.delete_all(to_delete[i])
            self.assertEqual(1, count)
            count = dll.delete_all(331)
            self.assertEqual(0, count)

            lst.remove(to_delete[i])
            self.check_dll(lst, dll)         # if failure here, see (4)

        # (5) delete all in longer DLL with duplicated values
        dll = DLL()
        lst = []
        for i in range(10):
            dll.push(i)
            lst.append(i)
        for i in range(9, -1, -1):      # DLL will be 0, 1, ..., 9, 9, 8, ..., 0
            dll.push(i)
            lst.append(i)

        to_delete = [1, 4, 7, 5, 6, 3, 2, 9, 0, 8]
        for i in range(10):
            count = dll.delete_all(to_delete[i])
            self.assertEqual(2, count)
            count = dll.delete_all(331)
            self.assertEqual(0, count)

            lst.remove(to_delete[i])
            lst.remove(to_delete[i])    # delete both instances
            self.check_dll(lst, dll)         # if failure here, see (5)

        # (6) sanity check empty list after all deletions
        self.check_dll([], dll)              # if failure here, see (6)

    def test_reverse(self):

        # (1) reverse empty DLL
        dll = DLL()
        dll.reverse()
        self.check_dll([], dll)      # if failure here, see (1)

        # (2) reverse single-node DLL
        dll = DLL()
        dll.push(0)
        dll.reverse()
        self.check_dll([0], dll)      # if failure here, see (2)

        # (3) reverse longer DLL
        dll = DLL()
        lst = []
        for i in range(10):
            dll.push(i)
            lst.append(i)
        old_head, old_tail = dll.head, dll.tail
        dll.reverse()
        new_head, new_tail = dll.head, dll.tail
        lst.reverse()

        self.check_dll(lst, dll)
        self.assertIs(new_head, old_tail)
        self.assertIs(new_tail, old_head)

        # (4) reverse palindrome DLL
        dll = DLL()
        lst = []
        for i in range(10):
            dll.push(i)
            lst.append(i)
        for i in range(9, -1, -1):
            dll.push(i)
            lst.append(i)
        old_head, old_tail = dll.head, dll.tail
        dll.reverse()
        new_head, new_tail = dll.head, dll.tail
        lst.reverse()

        self.check_dll(lst, dll)
        self.assertIs(new_head, old_tail)
        self.assertIs(new_tail, old_head)

    def test_DLL_comprehensive(self):

        # test all functions: empty, push, pop, from_list, to_list, find, find_all, delete, delete_all, reverse

        # (1) test functions on empty DLL
        dll = DLL()
        self.assertTrue(dll.empty())

        dll.pop()       # should not raise exception

        lst = dll.to_list()
        self.assertEqual([], lst)

        node = dll.find(331)
        self.assertIsNone(node)
        nodes = dll.find_all(331)
        self.assertEqual([], nodes)

        result = dll.delete(331)
        self.assertFalse(result)
        count = dll.delete_all(331)
        self.assertEqual(0, count)

        dll.reverse()   # should not raise exception

        # (2) test functions on single-node DLL
        dll = DLL()
        dll.push(331)
        self.assertFalse(dll.empty())
        self.assertIs(dll.head, dll.tail)
        self.assertEqual(331, dll.head.value)
        self.assertEqual(331, dll.tail.value)

        dll.pop()
        self.assertTrue(dll.empty())
        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

        dll.from_list([331])
        lst = dll.to_list()
        self.assertEqual([331], lst)

        node = dll.find(331)
        self.assertIsInstance(node, Node)
        self.assertEqual(331, node.value)
        self.assertIsNone(node.prev)
        self.assertIsNone(node.next)

        nodes = dll.find_all(331)
        self.assertIsInstance(nodes, List)
        self.assertEqual(1, len(nodes))
        self.assertEqual(331, nodes[0].value)
        self.assertIsNone(nodes[0].next)
        self.assertIsNone(nodes[0].prev)

        result = dll.delete(331)
        self.assertTrue(result)
        self.assertTrue(dll.empty())

        dll.push(331)
        count = dll.delete_all(331)
        self.assertEqual(1, count)
        self.assertTrue(dll.empty())

        dll.push(331)
        dll.reverse()
        self.assertFalse(dll.empty())
        self.assertEqual(331, dll.head.value)
        self.assertEqual(331, dll.tail.value)
        self.assertIs(dll.head, dll.tail)

        # (3) test functions on large, randomly-populated DLL containing 0-999 and 10 duplicates of 0-9
        seed(331)
        source = list(range(1000)) + [i for i in range(10) for _ in range(10)]
        # shuffle(source)
        source_rev = source[::-1]

        # (3.1) empty, push, pop
        dll, dll_rev = DLL(), DLL()
        self.assertTrue(dll.empty())
        self.assertTrue(dll_rev.empty())

        for num in source:
            dll.push(num)
            dll_rev.push(num, back=False)

        self.assertFalse(dll.empty())
        self.assertFalse(dll_rev.empty())
        self.check_dll(source, dll)
        self.check_dll(source_rev, dll_rev)

        for i in range(10):
            dll.pop()
            dll_rev.pop(back=False)
        self.check_dll(source[:-10], dll)
        self.check_dll(source_rev[10:], dll_rev)

        # (3.2) from_list, to_list
        dll, dll_rev = DLL(), DLL()
        dll.from_list(source)
        dll_rev.from_list(source_rev)
        lst = dll.to_list()
        lst_rev = dll_rev.to_list()
        self.assertEqual(source, lst)
        self.assertEqual(source_rev, lst_rev)
        self.check_dll(source, dll)
        self.check_dll(source_rev, dll_rev)

        # (3.3) find, find_all, delete, delete_all
        for i in range(1000):
            # search existing values
            result, result_rev = dll.find(i), dll_rev.find(i)
            self.assertEqual(i, result.value)
            self.assertEqual(i, result_rev.value)
            result, result_rev = dll.find_all(i), dll.find_all(i)
            if i < 10:
                self.assertEqual(11, len(result))
                self.assertEqual(11, len(result_rev))
            else:
                self.assertEqual(1, len(result))
                self.assertEqual(1, len(result_rev))
        # search non-existing values
        result, result_rev = dll.find(1000), dll_rev.find(1000)
        self.assertIsNone(result)
        self.assertIsNone(result_rev)
        result, result_rev = dll.find_all(1000), dll.find_all(1000)
        self.assertEqual([], result)
        self.assertEqual([], result_rev)

        # delete existing values
        for i in range(1000):
            result, result_rev = dll.delete(i), dll_rev.delete(i)
            self.assertTrue(result)
            self.assertTrue(result_rev)
            result, result_rev = dll.find_all(i), dll.find_all(i)
            if i < 10:
                self.assertEqual(10, len(result))
                self.assertEqual(10, len(result_rev))
            else:
                self.assertEqual([], result)
                self.assertEqual([], result_rev)

        # delete non-existing values
        result, result_rev = dll.delete(1000), dll_rev.delete(1000)
        self.assertFalse(result)
        self.assertFalse(result_rev)

        # delete all remaining existing values
        for i in range(1000):
            count, count_rev = dll.delete_all(i), dll_rev.delete_all(i)
            if i < 10:
                self.assertEqual(10, count)
                self.assertEqual(10, count_rev)
            else:
                self.assertEqual(0, count)
                self.assertEqual(0, count_rev)
            result, result_rev = dll.find_all(i), dll.find_all(i)
            self.assertEqual([], result)
            self.assertEqual([], result_rev)
        self.assertTrue(dll.empty())

        # (3.4) reverse
        dll.from_list(source)
        dll_rev.from_list(source_rev)
        dll.reverse()
        dll_rev.reverse()
        self.check_dll(source_rev, dll)
        self.check_dll(source, dll_rev)

    def test_intellivest(self):

        # (1) test empty stock sequence
        stocks = DLL()
        result = intellivest(stocks)
        self.assertEqual((None, None, 0), result)

        # (2) test single-day stock sequence
        stocks = DLL()
        stocks.push(Stock(datetime.date(2021, 1, 1), 331))
        result = intellivest(stocks)
        self.assertEqual((datetime.date(2021, 1, 1), datetime.date(2021, 1, 1), 0), result)

        # (3) test two-day increasing stock sequence
        stocks = DLL()
        stocks.push(Stock(datetime.date(2021, 1, 1), 331))
        stocks.push(Stock(datetime.date(2021, 1, 2), 332))
        result = intellivest(stocks)
        self.assertEqual((datetime.date(2021, 1, 1), datetime.date(2021, 1, 2), 1), result)

        # (4) test two-day decreasing stock sequence
        stocks = DLL()
        stocks.push(Stock(datetime.date(2021, 1, 1), 332))
        stocks.push(Stock(datetime.date(2021, 1, 2), 331))
        result = intellivest(stocks)
        self.assertEqual((datetime.date(2021, 1, 1), datetime.date(2021, 1, 1), 0), result)

        # (5) test five-day down-up-down stock sequence
        stocks = DLL()
        prices = [300, 100, 200, 300, 100]
        for i, price in enumerate(prices):
            stocks.push(Stock(datetime.date(2021, 1, i+1), price))
        result = intellivest(stocks)
        self.assertEqual((datetime.date(2021, 1, 2), datetime.date(2021, 1, 4), 200), result)

    def test_intellivest_comprehensive(self):

        # (1) test ten-day constant stock sequence
        stocks = DLL()
        prices = [100] * 10
        for i, price in enumerate(prices):
            stocks.push(Stock(datetime.date(2021, 1, i + 1), price))
        result = intellivest(stocks)
        self.assertEqual((datetime.date(2021, 1, 1), datetime.date(2021, 1, 1), 0), result)

        # (2) test ten-day increasing stock sequence
        stocks = DLL()
        prices = [100 * i for i in range(10)]
        for i, price in enumerate(prices):
            stocks.push(Stock(datetime.date(2021, 1, i + 1), price))
        result = intellivest(stocks)
        self.assertEqual((datetime.date(2021, 1, 1), datetime.date(2021, 1, 10), 900), result)

        # (3) test ten-day decreasing stock sequence
        stocks = DLL()
        prices = [100 * i for i in range(10, -1, -1)]
        for i, price in enumerate(prices):
            stocks.push(Stock(datetime.date(2021, 1, i + 1), price))
        result = intellivest(stocks)
        self.assertEqual((datetime.date(2021, 1, 1), datetime.date(2021, 1, 1), 0), result)

        # (4) test ten-day shuffled stock sequence
        stocks = DLL()
        prices = [0, 600, 300, 800, 500, 200, 400, 900, 100, 700]
        for i, price in enumerate(prices):
            stocks.push(Stock(datetime.date(2021, 1, i + 1), price))
        result = intellivest(stocks)
        self.assertEqual((datetime.date(2021, 1, 6), datetime.date(2021, 1, 8), 700), result)

        # (5) test on Google stock from https://finance.yahoo.com/quote/GOOG/history?p=GOOG
        google = DLL()
        with open("google.csv") as file:
            for line in file.readlines()[1:]:       # iterate over each row of CSV
                line = line.strip()                 # strip and split line into values
                values = line.split(",")            # columns: Date (0), Open, High, Low, Close (4), Adj Close, Volume
                value = Stock(datetime.date.fromisoformat(values[0]), float(values[4]))
                google.push(value)
        result = intellivest(google)
        self.assertEqual((datetime.date(2020, 10, 28), datetime.date(2020, 11, 5), 246.75), result)

    def test_cProfile(self):

        # Use cProfile to gain insight into your code's runtime complexity!
        # It is a very powerful tool for use in CSE 331 and beyond.
        #  - Change the first argument to runctx to profile different testcases
        #  - Change the sort argument to one of "calls", "cumulative", "tottime", "name", line", "module"
        # More information is available at https://docs.python.org/3/library/profile.html

        # Comment out "pass" and uncomment the following line to profile one of your testcases.
        # cProfile.runctx("DLLTests.test_DLL_comprehensive(self)", globals(), locals(), sort="calls")
        pass


if __name__ == '__main__':
    unittest.main()
