import unittest
import random
from CC6.solution import gates_needed


class CC6Tests(unittest.TestCase):
    def test_basic(self):
        # (1) Example from Specs
        departures = [1, 5, 8, 20]
        arrivals = [0, 1.5, 3, 19]
        student_response = gates_needed(departures, arrivals)
        expected = 2
        self.assertEqual(expected, student_response)  # (1)

        # (2) Other example from Specs
        departures = [1, 5, 8, 20]
        arrivals = [0, 1.5, 3, 19, 21, 21.5, 22, 22.5, 23, 23.5]
        student_response = gates_needed(departures, arrivals)
        expected = 6
        self.assertEqual(expected, student_response)  # (2)

        # (3) No departures
        departures = list()
        arrivals = [1, 2, 3]
        student_response = gates_needed(departures, arrivals)
        expected = 3
        self.assertEqual(expected, student_response)  # (3)

    def test_none_left(self):
        # (1) All arrive, then all leave
        departures = [5, 6, 7, 8]
        arrivals = [1, 2, 3, 4]
        student_response = gates_needed(departures, arrivals)
        expected = 4
        self.assertEqual(expected, student_response)  # (1)

        # (2)
        departures = [2, 4, 12, 13, 14, 15]
        arrivals = [1, 3, 5, 7, 9, 11]
        student_response = gates_needed(departures, arrivals)
        expected = 4
        self.assertEqual(expected, student_response)  # (2)

        # (3)
        departures = [4, 5, 6, 21, 23]
        arrivals = [1, 2, 3, 20, 22]
        student_response = gates_needed(departures, arrivals)
        expected = 3
        self.assertEqual(expected, student_response)  # (3)

    def test_multiple_left(self):
        # (1) 3 Planes sitting overnight, maximum gates is still 4
        departures = [5, 6, 7, 8]
        arrivals = [1, 2, 3, 4, 9, 10, 11]
        student_response = gates_needed(departures, arrivals)
        expected = 4
        self.assertEqual(expected, student_response)  # (1)

        # (2) 4 Planes sitting overnight, maximum gates is still 4
        departures = [5, 6, 7, 8]
        arrivals = [1, 2, 3, 4, 9, 10, 11, 12]
        student_response = gates_needed(departures, arrivals)
        expected = 4
        self.assertEqual(expected, student_response)  # (2)

        # (3) 5 Planes sitting overnight, maximum hits 5
        departures = [5, 6, 7, 8]
        arrivals = [1, 2, 3, 4, 9, 10, 11, 12, 13]
        student_response = gates_needed(departures, arrivals)
        expected = 5
        self.assertEqual(expected, student_response)  # (3)

        # (4) 5 Planes sitting overnight, maximum hits 8
        departures = [9, 10, 11]
        arrivals = [1, 2, 3, 4, 5, 6, 7, 8]
        student_response = gates_needed(departures, arrivals)
        expected = 8
        self.assertEqual(expected, student_response)  # (4)

        # (5) 6 Planes sitting overnight
        departures = [5]
        arrivals = [1, 2, 3, 20, 21, 22, 23]
        student_response = gates_needed(departures, arrivals)
        expected = 6
        self.assertEqual(expected, student_response)  # (5)

    def test_small_comprehensive(self):
        # (1) No departures
        departures = list()
        arrivals = [num for num in range(25)]
        student_response = gates_needed(departures, arrivals)
        expected = 25
        self.assertEqual(expected, student_response)  # (1)

        # (2) Toggle arrive and leave, never need more than 1
        departures = [num + 0.5 for num in range(0, 25)]
        arrivals = [num for num in range(25)]
        student_response = gates_needed(departures, arrivals)
        expected = 1
        self.assertEqual(expected, student_response)  # (2)

        # (3) All touch and go
        departures = [num for num in range(25)]
        arrivals = [num for num in range(25)]
        student_response = gates_needed(departures, arrivals)
        expected = 0
        self.assertEqual(expected, student_response)  # (3)

        # (4)
        departures = [num for num in range(5, 10)] + [num for num in range(23, 25)]
        arrivals = [num for num in range(5)] + [num for num in range(10, 23)] + [25, 26]
        student_response = gates_needed(departures, arrivals)
        expected = 13
        self.assertEqual(expected, student_response)  # (4)

    def test_large_comprehensive(self):
        # (1) All touch and go except 1 at end of night
        departures = [num for num in range(25)]
        arrivals = [num for num in range(26)]
        student_response = gates_needed(departures, arrivals)
        expected = 1
        self.assertEqual(expected, student_response)  # (1)

        # (2)
        departures = list()
        for _ in range(10000):
            departures.append(random.randint(0, 10000))
        departures.sort()
        arrivals = departures[:]
        student_response = gates_needed(departures, arrivals)
        expected = 0
        self.assertEqual(expected, student_response)  # (2)

        # (3)
        departures = [num + 0.5 for num in range(10000)]
        arrivals = [num for num in range(10000)] + [num for num in range(10000, 10005)]
        student_response = gates_needed(departures, arrivals)
        expected = 5
        self.assertEqual(expected, student_response)  # (3)

        # (4)
        departures = [num for num in range(1000)] + [num for num in range(1022, 1029)]
        arrivals = [num for num in range(1012)] + [num for num in range(1016, 1025)]
        student_response = gates_needed(departures, arrivals)
        expected = 18
        self.assertEqual(expected, student_response)  # (4)


if __name__ == '__main__':
    unittest.main()
