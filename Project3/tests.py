"""
Project 3 - Hybrid Sorting - Tests
CSE 331 Spring 2021
Professor Sebnem Onsay
"""

import unittest
from HybridSort import insertion_sort, merge_sort, hybrid_sort, inversions_count, reverse_sort, password_sort
from random import seed, sample, randint, shuffle
from itertools import permutations

seed(331)

class Project3Tests(unittest.TestCase):

    def test_insertion_sort_basic(self):
        # Test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        insertion_sort(data)
        self.assertEqual(expected, data)

        # Test with basic list of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        insertion_sort(data)
        self.assertEqual(expected, data)

        # Test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        insertion_sort(data)
        self.assertEqual(expected, data)

        # Test empty
        data = []
        insertion_sort(data)
        self.assertEqual([], data)

        # Check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(insertion_sort(data))

    def test_insertion_sort_comparator(self):
        # Sort powers of ten by number of digits, in reverse
        data = [10**i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key = lambda x : -1*len(str(x)))
        insertion_sort(data, comparator = lambda x, y : len(str(x)) > len(str(y)))
        self.assertEqual(expected, data)

        # Sort strings by length
        data = ['a'*i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key = lambda x : len(x))
        insertion_sort(data, comparator = lambda x, y : len(x) <= len(y))
        self.assertEqual(expected, data)

    def test_insertion_sort_comprehensive(self):
        # Sort a lot of integers
        data = list(range(1500))
        expected = data[:]
        shuffle(data)
        insertion_sort(data)
        self.assertEqual(expected, data)

        # Sort a lot of integers with alternative comparator
        # this comparator (defined as a named lambda) compares values as follows:
        #   x <= y
        #   if and only if
        #   sum(digits(x)) <= sum(digits(y))
        # Ex: 12 <= 15 since 1 + 2 = 3 <= 6 = 1 + 5
        comp = lambda x, y : sum([int(digit) for digit in str(x)]) <= sum([int(digit) for digit in str(y)])
        data = list(range(1500))
        expected = sorted(data, key = lambda x : sum([int(digit) for digit in str(x)]))
        insertion_sort(data, comparator = comp)
        # There are multiple possible orderings, thus we must compare via sums of digits
        for index, item in enumerate(expected):
            expected_sum = sum([int(digit) for digit in str(item)])
            actual_sum = sum([int(digit) for digit in str(data[index])])
            self.assertEqual(expected_sum, actual_sum)

    def test_merge_sort_basic(self):
        # Test with basic list of integers - default comparator and threshold
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        merge_sort(data)
        self.assertEqual(expected, data)

        # Test with basic set of strings - default comparator and threshold
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        merge_sort(data)
        self.assertEqual(expected, data)

        # Test with already sorted data - default comparator and threshold
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        merge_sort(data)
        self.assertEqual(expected, data)

        # Test empty - default comparator and threshold
        data = []
        merge_sort(data)
        self.assertEqual([], data)

    def test_merge_sort_threshold(self):

        # First, all the tests from basic should work with higher thresholds

        # Test with basic list of integers - default comparator
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        merge_sort(data, threshold=2)
        self.assertEqual(expected, data)

        # Test with basic set of strings - default comparator
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        merge_sort(data, threshold=2)
        self.assertEqual(expected, data)

        # Test with already sorted data - default comparator
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        merge_sort(data, threshold=2)
        self.assertEqual(expected, data)

        #
        # now, for a longer test - a bunch of thresholds
        data = list(range(25))
        expected = sorted(data)
        for t in range(11):
            shuffle(data)
            merge_sort(data, threshold=t)
            self.assertEqual(expected, data)

    def test_merge_sort_comparator(self):
        # Sort powers of ten by number of digits, in reverse
        data = [10**i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key = lambda x : -1*len(str(x)))
        merge_sort(data, comparator = lambda x, y : len(str(x)) > len(str(y)))
        self.assertEqual(expected, data)

        # Sort strings by length
        data = ['a'*i for i in range(15)]
        shuffle(data)
        expected = sorted(data, key = lambda x : len(x))
        merge_sort(data, comparator = lambda x, y : len(x) <= len(y))
        self.assertEqual(expected, data)

    def test_merge_sort_comprehensive(self):
        # Sort a lot of integers, with a lot of thresholds
        data = list(range(500))
        for t in range(100):
            shuffle(data)
            expected = sorted(data)
            merge_sort(data, threshold=t)
            self.assertEqual(expected, data)

        # Sort a lot of integers with alternative comparator, threshold of 8
        # this comparator (defined as a named lambda) compares values as follows:
        #   x <= y
        #   if and only if
        #   sum(digits(x)) <= sum(digits(y))
        # Ex: 12 <= 15 since 1 + 2 = 3 <= 6 = 1 + 5
        comp = lambda x, y : sum([int(digit) for digit in str(x)]) <= sum([int(digit) for digit in str(y)])
        data = list(range(1500))
        expected = sorted(data, key = lambda x : sum([int(digit) for digit in str(x)]))
        merge_sort(data, threshold=8, comparator = comp)
        # There are multiple possible orderings, thus we must compare via sums of digits
        for index, item in enumerate(expected):
            expected_sum = sum([int(digit) for digit in str(item)])
            actual_sum = sum([int(digit) for digit in str(data[index])])
            self.assertEqual(expected_sum, actual_sum)

    def test_hybrid_sort_basic(self):
        # Test with basic list of integers - default comparator, threshold of zero
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data)
        hybrid_sort(data, threshold=0)
        self.assertEqual(expected, data)

        # Test with basic list of strings - default comparator, threshold
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data)
        hybrid_sort(data, threshold=0)
        self.assertEqual(expected, data)

        # Test with already sorted data - default comparator, threshold
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data)
        hybrid_sort(data, threshold=0)
        self.assertEqual(expected, data)

        # Test empty
        data = []
        hybrid_sort(data, threshold=0)
        self.assertEqual([], data)

        # Check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(hybrid_sort(data, threshold=0))

    def test_hybrid_sort_comprehensive(self):
        # This should be easy to pass if you've passed the comprehensive tests for merge and insertion

        # Sort a lot of integers with alternative comparator, thresholds in [1,...,49]
        # this comparator (defined as a named lambda) compares values as follows:
        #   x <= y
        #   if and only if
        #   sum(digits(x)) <= sum(digits(y))
        # Ex: 12 <= 15 since 1 + 2 = 3 <= 6 = 1 + 5
        comp = lambda x, y : sum([int(digit) for digit in str(x)]) <= sum([int(digit) for digit in str(y)])
        data = list(range(1000))
        expected = sorted(data, key = lambda x: sum([int(digit) for digit in str(x)]))
        for t in range(50):
            shuffle(data)
            hybrid_sort(data, threshold=t, comparator=comp)
            for index, item in enumerate(expected):
                expected_sum = sum([int(digit) for digit in str(item)])
                actual_sum = sum([int(digit) for digit in str(data[index])])
                self.assertEqual(expected_sum, actual_sum)

    def test_hybrid_sort_speed(self):
        # The point of this sort is to be fast, right?
        # This (probably) won't pass if you're not careful with time complexity
        data = list(range(300000))
        expected = data[:]
        shuffle(data)
        hybrid_sort(data, threshold=10)
        self.assertEqual(expected, data)

    def test_reverse_sort_basic(self):
        # Test with basic list of integers - default comparator, threshold of zero
        data = [7, 4, 1, 0, 8, 9, 3, 2, 12]
        expected = sorted(data, reverse=True)
        reverse_sort(data, threshold=0)
        self.assertEqual(expected, data)

        # Test with basic list of strings - default comparator, threshold
        data = ["dog", "banana", "orange", "tree", "clutter", "candy", "silence"]
        expected = sorted(data, reverse=True)
        reverse_sort(data, threshold=0)
        self.assertEqual(expected, data)

        # Test with already sorted data - default comparator, threshold
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = sorted(data, reverse=True)
        reverse_sort(data, threshold=0)
        self.assertEqual(expected, data)

        # Test empty
        data = []
        reverse_sort(data, threshold=0)
        self.assertEqual([], data)

        # Check that function does not return anything
        data = [5, 6, 3, 2]
        self.assertIsNone(reverse_sort(data, threshold=0))

        # Now let's test with multiple thresholds
        data = list(range(50))
        expected = sorted(data, reverse=True)
        for t in range(20):
            shuffle(data)
            reverse_sort(data, threshold=t)
            self.assertEqual(expected, data)

    def test_reverse_sort_speed(self):
        # should be just as fast as hybrid sort
        data = list(range(300000))
        expected = sorted(data, reverse=True)
        shuffle(data)
        reverse_sort(data, threshold=10)

    def test_inversion_count(self):
        data = [2, 4, 3, 1]
        self.assertEqual(4, inversions_count(data))

        data = [4, 3, 2, 1]
        self.assertEqual(6, inversions_count(data))

        data = [1, 2, 3, 4]
        self.assertEqual(0, inversions_count(data))

        data = [2, 4, 1, 3, 5]
        self.assertEqual(3, inversions_count(data))

        data = [5, 4, 3, 2, 1]
        self.assertEqual(10, inversions_count(data))
        self.assertEqual([5,4,3,2,1], data)

        data = [1, 2, 3, 4, 5]
        self.assertEqual(0, inversions_count(data))

        # Random Tests
        seed(1130)
        data = [randint(0, 100) for _ in range(10)]
        self.assertEqual(30, inversions_count(data))

        in_order = sorted(data)
        self.assertEqual(0, inversions_count(in_order))

        reverse = sorted(data, reverse=True)
        self.assertEqual(45, inversions_count(reverse))

        data = [randint(0, 100) for _ in range(11)]
        self.assertEqual(27, inversions_count(data))

        in_order = sorted(data)
        self.assertEqual(0, inversions_count(in_order))

        reverse = sorted(data, reverse=True)
        self.assertEqual(55, inversions_count(reverse))

        seed(22)

        # Large Even Length List
        data = [randint(0, 10000) for _ in range(100)]
        self.assertEqual(2430, inversions_count(data))

        reverse = sorted(data, reverse=True)
        self.assertEqual(4950, inversions_count(reverse))

        in_order = sorted(data)
        self.assertEqual(0, inversions_count(in_order))

        # Large Odd Length List
        data = [randint(0, 10000) for _ in range(101)]
        self.assertEqual(2530, inversions_count(data))

        reverse = sorted(data, reverse=True)
        self.assertEqual(5050, inversions_count(reverse))

        in_order = sorted(data)
        self.assertEqual(0, inversions_count(in_order))

    def test_application_small(self):
        # Test with small lists
        data = ["aa", "aaaaa", "aaaa"]
        password_sort(data)
        self.assertEqual(["aaaaa", "aaaa", "aa"], data)

        data = ["12345", "abcd", "abdc", "avef"]
        password_sort(data)
        self.assertEqual(["avef", "12345", "abdc", "abcd"], data)

        data = ["password",  "unicorn38", "ILikeApples"]
        password_sort(data)
        self.assertEqual(["unicorn38", "ILikeApples", "password"], data)

        # confirm `None` is returned
        self.assertIsNone(password_sort(data))

    def test_application_large(self):
        # all possible passwords with characters in {'a','b','c','d','e','f','g','h'}
        # this might take a while, there are ~40000 of these
        # these will all have the same number of characters, and of unique characters
        # so the resulting list should be sorted by inversion count, in reverse order
        passwords = [''.join(list(password)) for password in permutations('abcdefgh', 8)]
        shuffle(passwords)
        expected = sorted(passwords, key = lambda password : inversions_count([char for char in password]), reverse=True)
        password_sort(passwords)
        for index, item in enumerate(expected):
            expected_inversions = inversions_count([char for char in item])
            actual_inversions = inversions_count([char for char in passwords[index]])
            self.assertEqual(expected_inversions, actual_inversions)


if __name__ == '__main__':
    unittest.main()
