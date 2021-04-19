import unittest
from solution import colonel_concat
from typing import List
from string import ascii_lowercase
import random


class TestCodingChallenge12(unittest.TestCase):

    def test_basic(self):
        
        # [1] (("a + "bbbb") + "c") -> ((5) + 6)
        actual = colonel_concat(["a", "bbbb", "c"])
        self.assertEqual(11, actual)

        # [2] ("aaa" + ("bb" + "c")) -> (6 + (3)) 
        actual = colonel_concat(["aaa", "bb", "c"])
        self.assertEqual(9, actual)
        
        # [3] ("aaaa" + ("bbb" + ("cc" + "d"))) -> (10 + (6 + (3)))
        actual = colonel_concat(["aaaa", "bbb", "cc", "d"])
        self.assertEqual(19, actual)

        # [4] (("aaaa" + "bbb") + ("cccc" + "d")) -> (12 + (7 + 5))
        actual = colonel_concat(["aaaa", "bbb", "cccc", "d"])
        self.assertEqual(24, actual)

        # [5] (15 + (9 + (4 + 6)))
        actual = colonel_concat(["a", "bbb", "ccccc", "dddd", "ee"])
        self.assertEqual(34, actual)

        # [6] ((2 + 4 + 7) + 9) + 16))
        actual = colonel_concat(["a", "b", "cc", "ddd", "eeee", "fffff"])
        self.assertEqual(38, actual)


    def test_intermediate(self):

        # [1] 8 elements
        actual = colonel_concat(['aaaaaa', 'bbbbbbbb', 'ccccc', 'dd', 'eeeee', 
            'fffffff', 'g', 'hhhhhh'])
        self.assertEqual(120, actual)

        # [2] 9 elements
        actual = colonel_concat(['aaaaaaaaaa', 'bbbbbb', 'cccc', 'ddd', 
            'eeeeee', 'fffffff', 'g', 'hhhhhhh', 'iii'])
        self.assertEqual(146, actual)

        # [3] 10 elements
        actual = colonel_concat(['I', 'Love', 'You', 'Colonel', 'Sanders!',
            '2:', '12', 'Herbs', 'and', 'Spices'])
        self.assertEqual(132, actual)

        # [4] 11 elements
        actual = colonel_concat(['But', 'Colonel,', "I've", 'always', 'loved', 
            'you!', 'Please', 'let', 'us', 'be', 'together!'])
        self.assertEqual(176, actual)

        # [5] 14 elements
        actual = colonel_concat(['I', "can't", 'live', 'alone', 'now', 'that', 
            "I've", 'seen', 'the', 'beauty', 'of', 'your', 'fried', 'chicken!'])
        self.assertEqual(219, actual)


    def test_large(self):
        
        # [1]
        actual = colonel_concat(['The', 'Colonel', 'embraced', 'me', 'in', 
            'his', 'arms.', 'Never', 'let', 'me', 'go!', 'A', 'ridiculous', 
            'request.', 'How', 'would', 'I', 'be', 'able', 'to', 'eat', 'my', 
            'drumsticks', 'in', 'this', 'position?', 'Do', 'you', 'continue', 
            'to', 'hug', 'the', 'Colonel,', 'or', 'do', 'you', 'reject', 'his', 
            'advances', 'to', 'sate', 'your', 'hunger?'])
        self.assertEqual(942, actual)

        # [2] 
        actual = colonel_concat(['The', 'Colonel', 'breathed', 'heavily.', 'I', 
            'could', 'smell', 'the', 'chicken', 'off', 'of', 'his', 'breath,', 
            'but', 'for', 'some', 'reason,', 'it', 'did', 'not', 'repulse', 
            'me.', 'Rather,', 'it', 'enticed', 'me..', 'to', 'immediately', 
            'find', 'the', 'closest', 'KFC', 'and', 'purchase', 'a', 'large', 
            'bucket', 'of', 'fried', 'wings.'])
        self.assertEqual(958, actual)

        # [3]
        actual = colonel_concat(['Did', 'you', 'ever', 'hear', 'the', 'tragedy', 
            'of', 'Colonel', 'Sanders', 'The', 'Handsome?', 'I', 'thought', 
            'not.', 'It’s', 'not', 'a', 'story', "Popeye's", 'would', 'tell', 
            'you.', 'It’s', 'a', 'Kentucky', 'legend.', 'Colonel', 'Sanders', 
            'was', 'a', 'Dark', 'Chef', 'of', 'the', 'Spices,', 'so', 
            'powerful', 'and', 'so', 'wise', 'he', 'could', 'use', 'the', 
            'Spices', 'to', 'influence', 'raw', 'chicken', 'to', 'create', 
            'fried', 'chicken...', 'He', 'had', 'such', 'a', 'knowledge', 'of', 
            'the', 'dark', 'side', 'that', 'he', 'could', 'even', 'keep', 'the', 
            'ones', 'he', 'cared', 'about', 'from', 'growing', 'hungry.', 'The', 
            'dark', 'side', 'of', 'the', 'Spices', 'is', 'a', 'pathway', 'to', 
            'many', 'abilities', 'some', 'consider', 'to', 'be', 'unnatural.', 
            'He', 'became', 'so', 'powerful…', 'the', 'only', 'thing', 'he', 
            'was', 'afraid', 'of', 'was', 'losing', 'his', 'power,', 'which', 
            'eventually,', 'of', 'course,', 'he', 'did.', 'Unfortunately,', 
            'he', 'taught', 'his', 'apprentice', 'everything', 'he', 'knew,', 
            'then', 'his', 'apprentice', 'starved', 'him', 'of', 'his', 
            'spices.', 'Ironic.', 'He', 'could', 'save', 'others', 'from', 
            'hunger,', 'but', 'not', 'himself.'])
        self.assertEqual(4426, actual)


    def test_comprehensive(self):

        def random_input(n: int, m: int) -> List[str]:
            ret = []
            for _ in range(n):
                ret.append(''.join((random.choice(ascii_lowercase) 
                    for _ in range(random.randint(1, m)))))
            return ret

        random.seed(453)

        # [1] 50 elements, max string length of 10
        actual = colonel_concat(random_input(50, 10))
        self.assertEqual(1565, actual)

        # [2] 100 elements, max string length of 10
        actual = colonel_concat(random_input(100, 10))
        self.assertEqual(3336, actual)
        
        # [3] 200 elements, max string length of 15
        actual = colonel_concat(random_input(200, 15))
        self.assertEqual(12436, actual)

        # [4] 300 elements, max string length of 15
        actual = colonel_concat(random_input(300, 15))
        self.assertEqual(19251, actual)
        

if __name__ == '__main__':
    unittest.main()
