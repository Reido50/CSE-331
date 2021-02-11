import unittest
import random
from solution import finding_best_bot


class CC3Tests(unittest.TestCase):
    def test_basic(self):
        test1 = [1, 2, 3, 20, 1]
        actual = finding_best_bot(test1)
        expected = 4
        self.assertEqual(expected, actual)

        test2 = [1, 10, 20, 5, 1]
        actual = finding_best_bot(test2)
        expected = 3
        self.assertEqual(expected, actual)

    def test_all_increase(self):
        random.seed(2)
        test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual = finding_best_bot(test1)
        expected = len(test1)
        self.assertEqual(expected, actual)

        test2 = [10]
        actual = finding_best_bot(test2)
        expected = len(test2)
        self.assertEqual(expected, actual)

        test3 = [random.randint(1, 2000) for _ in range(30)]
        test3 = list(set(test3))  # removing duplicate
        test3.sort()
        actual = finding_best_bot(test3)
        expected = len(test3)
        self.assertEqual(expected, actual)

    def test_all_decrease(self):
        random.seed(2021)
        test1 = [10, 9, 8, 7, 6]
        actual = finding_best_bot(test1)
        expected = 1
        self.assertEqual(expected, actual)

        test2 = [10, 7, 6, 1]
        actual = finding_best_bot(test2)
        expected = 1
        self.assertEqual(expected, actual)

        test3 = [random.randint(1, 120) for _ in range(30)]
        test3 = list(set(test3))  # removing duplicate
        test3.sort(reverse=True)
        actual = finding_best_bot(test3)
        expected = 1
        self.assertEqual(expected, actual)

    def test_comprehensive_small(self):
        random.seed(3312021)
        test1_increase = [random.randint(10, 210) for _ in range(20)]
        test1 = sorted(list(set(test1_increase))) + [9, 8, 7, 6, 5]
        expected = len(test1_increase)
        actual = finding_best_bot(test1)
        self.assertEqual(expected, actual)

        test2_decrease = [random.randint(1, 1200) for _ in range(20)]
        test2 = [1, 50, 300, 400, 450, 1520] + sorted(list(set(test2_decrease)), reverse=True)
        expected = 6
        actual = finding_best_bot(test2)
        self.assertEqual(expected, actual)

        # Making sure that student can pass the corner test for comprehensive
        test3 = [random.randint(1, 33121) for _ in range(30)]
        test3 = list(set(test3))  # removing duplicate
        test3.sort()
        expected = len(test3)
        actual = finding_best_bot(test3)
        self.assertEqual(expected, actual)

        test4 = test3[::-1]
        expected = 1
        actual = finding_best_bot(test4)
        self.assertEqual(expected, actual)

    def test_comprehensive_large(self):
        random.seed(331)
        test1 = [i for i in range(501)] + [i for i in range(499, -1, -1)]
        expected = 501
        actual = finding_best_bot(test1)
        self.assertEqual(expected, actual)

        test2_increase = list(set([random.randint(7000, 10000) for _ in range(10000)]))
        test2 = sorted(test2_increase) + [i for i in range(6995, -1, -random.randint(1, 15))]
        expected = len(test2_increase)
        actual = finding_best_bot(test2)
        self.assertEqual(expected, actual)

        # Making sure that student can pass the corner test for comprehensive
        test3 = [random.randint(1, 33121) for _ in range(10000)]
        test3 = list(set(test3))  # removing duplicate
        test3.sort()
        expected = len(test3)
        actual = finding_best_bot(test3)
        self.assertEqual(expected, actual)

        test4 = test3[::-1]
        expected = 1
        actual = finding_best_bot(test4)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
