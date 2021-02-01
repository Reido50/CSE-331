import unittest

from SLL import SLL


class SLLTests(unittest.TestCase):
    """
    This testing class inherits from `unittest.TestCase`, Python's built-in unit testing framework.
    For more information, see https://docs.python.org/3/library/unittest.html.
    """

    def test_empty(self):
        # (1) empty list
        subject = SLL()                     # here, we define the test "subject," or thing being tested
        self.assertTrue(subject.empty())    # here, we assert that the test subject behaves as expected

        # (2) single element list: 1
        subject = SLL([1])
        self.assertFalse(subject.empty())

        # (3) longer list:  0 -> 1 -> 2 -> 3 -> 4
        subject = SLL(list(range(5)))
        self.assertFalse(subject.empty())

    def test_push_front(self):
        subject = SLL()
        for val in range(25):
            # (1) push onto front and ensure list structure is proper
            subject.push_front(val)
            self.assertEqual(SLL(list(range(val, -1, -1))), subject)    # expected is 1st parameter; actual is 2nd

    def test_push_back(self):
        subject = SLL()
        for val in range(25):
            # (1) push onto back and ensure list structure is proper
            subject.push_back(val)
            self.assertEqual(SLL(list(range(val + 1))), subject)

    def test_remove(self):
        # (1) remove from empty
        subject = SLL()
        self.assertFalse(subject.remove(1))
        self.assertEqual(SLL(), subject)

        # (2) remove nonexistent node from longer list
        subject = SLL(list(range(7)))
        self.assertFalse(subject.remove(10))
        self.assertEqual(SLL(list(range(7))), subject)

        # (3) remove existing node from start of longer list
        self.assertTrue(subject.remove(0))
        self.assertEqual(SLL(list(range(1, 7))), subject)

        # (4) remove existing node from end of longer list
        self.assertTrue(subject.remove(6))
        self.assertEqual(SLL(list(range(1, 6))), subject)

        # (5) remove existing node from middle of longer list
        self.assertTrue(subject.remove(3))
        self.assertEqual(SLL([1, 2, 4, 5]), subject)

    def test_reverse(self):
        # (1) reverse empty list
        subject = SLL()
        subject.reverse()
        self.assertEqual(SLL(), subject)

        # (2) reverse one element
        subject = SLL([1])
        subject.reverse()
        self.assertEqual(SLL([1]), subject)

        # (3) reverse two elements
        subject = SLL([1, 2])
        subject.reverse()
        self.assertEqual(SLL([2, 1]), subject)

        # (4) reverse long list
        subject = SLL(list(range(25)))
        subject.reverse()
        self.assertEqual(SLL(list(range(24, -1, -1))), subject)


if __name__ == '__main__':
    unittest.main()
