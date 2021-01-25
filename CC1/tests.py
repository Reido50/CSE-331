import unittest
from CC1.solution import story_progression
from random import seed, randint


class CC1Tests(unittest.TestCase):

    def test_basic(self):
        test1 = [0, 1, 1, 1, 0, 0, 0]
        question1 = [(0, 2)]
        expected = ['Win']
        actual = story_progression(test1, question1)
        self.assertEqual(expected, actual)

        test2 = [0, 1, 1, 1]
        question2 = [(0, 1), (0, 2), (0, 3)]
        question2.sort()
        expected = ['Lose', 'Win', 'Win']
        actual = story_progression(test2, question2)
        self.assertEqual(expected, actual)

        test3 = [1, 0, 0, 0]
        question3 = [(0, 0), (0, 3)]
        expected = ['Win', 'Lose']
        actual = story_progression(test3, question3)
        self.assertEqual(expected, actual)

    def test_ask_zero_one_elements(self):
        test1 = [0, 1, 1, 0, 1]
        question1 = [(0, 0)]
        expected = ['Lose']
        actual = story_progression(test1, question1)
        self.assertEqual(expected, actual)

        test2 = [1, 1, 0, 0]
        question2 = [(0, 0)]
        expected = ['Win']
        actual = story_progression(test2, question2)
        self.assertEqual(expected, actual)

        test3 = [1, 1, 0, 0]
        question3 = []
        expected = []
        actual = story_progression(test3, question3)
        self.assertEqual(expected, actual)

    def test_duplicate(self):
        seed(331)
        test1 = [0, 1, 0, 1, 1, 0]
        question1 = [(0, 2), (0, 2), (0, 4), (0, 4)]

        expected = ['Lose', 'Lose', 'Win', 'Win']

        actual = story_progression(test1, question1)
        self.assertEqual(expected, actual)

        test2 = [randint(0, 331) % 2 for _ in range(10)]
        question2 = [(0, randint(0, 9)) for _ in range(5)]
        question2 = question2 * 2
        question2.sort()
        expected = ['Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Lose', 'Lose', 'Lose', 'Lose']
        actual = story_progression(test2, question2)
        self.assertEqual(expected, actual)

    def test_ask_whole(self):
        seed(2021331)

        test1 = [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
        question1 = [(0, i) for i in range(len(test1))]
        question1.sort()
        expected = ['Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Win', 'Win', 'Win', 'Win']
        actual = story_progression(test1, question1)
        self.assertEqual(expected, actual)

        test2 = [1]
        question2 = [(0, 0)]
        expected = ["Win"]
        actual = story_progression(test2, question2)
        self.assertEqual(expected, actual)

        test3 = [0]
        question3 = [(0, 0)]
        expected = ["Lose"]
        actual = story_progression(test3, question3)
        self.assertEqual(expected, actual)

    def test_short_questions_random_input(self):
        seed(331)

        generate1 = 1234567
        test1 = [1 if generate1 & (1 << i) else 0 for i in range(19)]
        question1 = [(0, randint(0, len(test1) - 1)) for _ in range(len(test1))]
        question1.sort()
        expected = ['Win', 'Win', 'Lose', 'Lose', 'Lose', 'Win', 'Win', 'Win', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win']

        actual = story_progression(test1, question1)
        self.assertEqual(expected, actual)

        test2 = [randint(0, 331) % 2 for _ in range(100)]
        question2 = [(0, 0), (0, 2), (0, 5), (0, 11), (0, 98), (0, 99), (0, 99)]
        question2.sort()
        expected = ['Win', 'Win', 'Win', 'Win', 'Lose', 'Lose', 'Lose']
        actual = story_progression(test2, question2)
        self.assertEqual(expected, actual)

    def test_large_input(self):
        seed(2033121)

        test1 = [0] * 25 + [1] * 30 + [0] * 25 + [1] * 120  # Pattern of 1 and zero
        question1 = [(0, randint(0, len(test1) - 1)) for _ in range(50)]
        question1.sort()

        expected = ['Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Win',
                    'Win', 'Win', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Win', 'Win',
                    'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win',
                    'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win']

        actual = story_progression(test1, question1)
        self.assertEqual(expected, actual)

        test_large = [randint(0, 33120) % 2 for _ in range(500)]
        question_large = [(0, i) for i in range(500)] + [(0, 499)]

        expected = ['Win', 'Lose', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win',
                    'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win',
                    'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Lose',
                    'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Lose', 'Lose', 'Lose',
                    'Win', 'Lose', 'Win', 'Win', 'Win', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Win', 'Lose', 'Win', 'Win',
                    'Win',
                    'Win', 'Win', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose'] + ["Lose"]

        actual = story_progression(test_large, question_large)
        self.assertEqual(expected, actual)

    def test_extra_credit(self):
        test1 = [0, 1, 1, 0, 1, 0, 1, 0]
        question1 = [(0, 1), (0, 2), (0, 3), (1, 1), (3, 3), (5, 6)]
        expected = ['Lose', 'Win', 'Lose', 'Win', 'Lose', 'Lose']

        actual = story_progression(test1, question1)

        self.assertEqual(expected, actual)

        seed(331)
        test2 = [randint(0, 331) % 2 for _ in range(120)]
        question2 = []
        for _ in range(120):
            st = randint(0, 119)
            ed = randint(st, 119)
            question2.append((st, ed))

        expected = ['Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Win', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Win',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Win', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Win', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Win', 'Win', 'Lose', 'Lose', 'Lose', 'Lose', 'Win', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Win', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Win', 'Lose', 'Lose', 'Lose', 'Win', 'Lose', 'Win', 'Lose', 'Win', 'Win', 'Win', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Win', 'Win', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Win',
                    'Lose', 'Lose', 'Lose', 'Lose']

        actual = story_progression(test2, question2)

        self.assertEqual(expected, actual)

        test_large_random = [(randint(0, 331) * randint(0, 331)) % 2 for _ in range(500)]
        question_large = [(0, ed) for ed in range(500)]

        expected = ['Win', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Win', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose',
                    'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose', 'Lose']


        actual = story_progression(test_large_random, question_large)

        test_large_large = test_large_random * 1000
        self.assertEqual(expected, actual)

        question_large_large = [(0, len(test_large_large) - 1)] * 1000000
        expected = ['Lose'] * 1000000

        actual = story_progression(test_large_large, question_large_large)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
