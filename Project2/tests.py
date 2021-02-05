import unittest
from Project2.SLL import crafting, RecursiveSinglyLinkList as RSLL
from Project2.Node import Node
import random


class MyTestCase(unittest.TestCase):

    def sll_to_list(self, sll):
        """
        This function is only used in the comprehensive test. It will take in a singly link list
        and create a python list with the same contents
        :param sll: Source singly linked list
        :return: A python list the same contents and order as the given singly linked list
        """

        new_list = []

        def walk_sll(curr):
            if curr is None:
                return
            new_list.append(curr.val)
            walk_sll(curr.next)

        walk_sll(sll.head)
        return new_list

    def test_push(self):
        sll = RSLL()
        # 1. Insert into an empty list
        sll.push(3)
        self.assertEqual(3, sll.head.val)  # 1

        # 2. Insert into a one element list
        sll.push(3)
        self.assertEqual(3, sll.head.next.val)  # 2

        # 3. Push into a list with multiple nodes
        sll.push(1)
        self.assertEqual(1, sll.head.next.next.val)  # 3
        self.assertEqual(None, sll.head.next.next.next)  # 3

    def test_to_string(self):
        sll = RSLL()
        # 1. Get the string of an empty list
        self.assertEqual("None", sll.to_string(sll.head))  # 1

        # 2. Get the string of an one element list
        sll.head = Node(3)
        self.assertEqual("3", sll.to_string(sll.head))  # 2

        # 3. Get the string of a two element list
        sll.head.next = Node(3)
        self.assertEqual("3 --> 3", sll.to_string(sll.head))  # 3

        # 4. Get the string of a multi-element list
        sll.head.next.next = Node(1)
        self.assertEqual("3 --> 3 --> 1", sll.to_string(sll.head))  # 4

    def test_remove(self):

        sll = RSLL()

        # 1. Removing from an empty list
        sll.remove(42)
        self.assertEqual(None, sll.head)  # 1

        sll.head = Node(3)
        sll.head.next = Node(4)
        sll.head.next.next = Node(3)
        sll.head.next.next.next = Node(1)

        # 2. Remove from the middle of the list
        sll.remove(4)
        self.assertEqual(3, sll.head.val)  # 2
        self.assertEqual(3, sll.head.next.val)  # 2
        self.assertEqual(1, sll.head.next.next.val)  # 2
        self.assertEqual(None, sll.head.next.next.next)  # 2

        # 3. Remove from the end of the list
        sll.remove(1)
        self.assertEqual(3, sll.head.val)  # 3
        self.assertEqual(3, sll.head.next.val)  # 3
        self.assertEqual(None, sll.head.next.next)  # 3

        # 4. Remove from the front of the list
        sll.remove(3)
        self.assertEqual(3, sll.head.val)  # 4
        self.assertEqual(None, sll.head.next)  # 4

        # 5. Remove the last node in the list
        sll.remove(3)
        self.assertEqual(None, sll.head)  # 5

    def test_remove_all(self):

        sll = RSLL()
        sll.head = Node(3)
        sll.head.next = Node(3)
        sll.head.next.next = Node(1)

        # 1. Try to remove an element that doesn't exist in the list
        sll.remove_all(6)
        self.assertEqual(3, sll.head.val)  # 1
        self.assertEqual(3, sll.head.next.val)  # 1
        self.assertEqual(1, sll.head.next.next.val)  # 1
        self.assertEqual(None, sll.head.next.next.next)  # 1

        # 2. Remove all of the 3's from the list
        sll.remove_all(3)
        self.assertEqual(1, sll.head.val)  # 2
        self.assertEqual(None, sll.head.next)  # 2

        # 3. Remove the last element from the list
        sll.remove_all(1)
        self.assertEqual(None, sll.head)  # 3

        # 4. Try to remove from an empty list
        sll.remove_all(2)
        self.assertEqual(None, sll.head)  # 4

    def test_search(self):

        sll = RSLL()
        # 1. Try to search an empty List
        self.assertEqual(False, sll.search(331))  # 1

        sll.head = Node(4)
        sll.head.next = Node(2)
        sll.head.next.next = Node(0)

        # 2. Search for a node at the start of the list
        self.assertEqual(True, sll.search(4))  # 2

        # 3. Search for a value that doesn't exist in the list
        self.assertEqual(False, sll.search(3))  # 3

        # 4. Search for a node in the middle of the list
        self.assertEqual(True, sll.search(2))  # 4

        # 5. Search for a node at the end of the list
        self.assertEqual(True, sll.search(0))  # 5

    def test_length(self):

        sll = RSLL()
        # 1. Get the length of an empty list
        self.assertEqual(0, sll.length(sll.head))  # 1

        # 2. Get the length of a list with only one element
        sll.head = Node(2)
        self.assertEqual(1, sll.length(sll.head))  # 2

        # 3. Get the length of a list with two elements
        sll.head.next = Node(5)
        self.assertEqual(2, sll.length(sll.head))  # 3

        # 4. Get the length of a list with multiple elements
        sll.head.next.next = Node(0)
        sll.head.next.next.next = Node(0)
        self.assertEqual(4, sll.length(sll.head))  # 4

    def test_sum_list(self):

        sll = RSLL()

        # 1. Get the sum of an empty list
        self.assertEqual(0, sll.sum_list(sll.head))  # 1

        # 2. Get the sum of a list with one node
        sll.head = Node(2)
        self.assertEqual(2, sll.sum_list(sll.head))  # 2

        # 3. Get the sum of a list with two nodes
        sll.head.next = Node(5)
        self.assertEqual(7, sll.sum_list(sll.head))  # 3

        # 4. Get the sum of a list with multple nodes
        sll.head.next.next = Node(0)
        sll.head.next.next.next = Node(1)
        self.assertEqual(8, sll.sum_list(sll.head))  # 4

    def test_count(self):
        sll = RSLL()

        # 1. Try to get a count from an empty list
        self.assertEqual(0, sll.count(8))  # 1

        # 2. Get the number of 2's in the one element list
        sll.head = Node(2)
        self.assertEqual(1, sll.count(2))  # 2

        # 3. Get the number of 5's in the two element list
        sll.head.next = Node(5)
        self.assertEqual(1, sll.count(5))  # 3

        # 4. Get the number of 0's from tha multi-element list
        sll.head.next.next = Node(0)
        sll.head.next.next.next = Node(0)
        self.assertEqual(2, sll.count(0))  # 4

        # 5. Try to get the count of a number that doesn't exist in the list
        self.assertEqual(0, sll.count(42))  # 5

    def test_reverse(self):
        sll = RSLL()

        # 1. Try to reverse an empty list
        sll.reverse(sll.head)
        self.assertEqual(None, sll.head)  # 1

        # 2. Reverse a one element list
        sll.head = Node(6)
        sll.reverse(sll.head)
        self.assertEqual(6, sll.head.val)  # 2
        self.assertEqual(None, sll.head.next)  # 2

        # 3. Reverse a two element list
        sll = RSLL()
        sll.head = Node(4)
        sll.head.next = Node(2)
        sll.reverse(sll.head)
        self.assertEqual(2, sll.head.val)  # 3
        self.assertEqual(4, sll.head.next.val)  # 3
        self.assertEqual(None, sll.head.next.next)  # 3

        # 4. Reverse a three element list
        sll.head = Node(3)
        sll.head.next = Node(3)
        sll.head.next.next = Node(1)
        sll.reverse(sll.head)
        self.assertEqual(1, sll.head.val)  # 4
        self.assertEqual(3, sll.head.next.val)  # 4
        self.assertEqual(3, sll.head.next.next.val)  # 4
        self.assertEqual(None, sll.head.next.next.next)  # 4

        # 5. Reverse a multi-element list
        sll = RSLL()
        sll.head = Node(4)
        sll.head.next = Node(2)
        sll.head.next.next = Node(4)
        sll.head.next.next.next = Node(2)
        sll.reverse(sll.head)
        self.assertEqual(2, sll.head.val)  # 5
        self.assertEqual(4, sll.head.next.val)  # 5
        self.assertEqual(2, sll.head.next.next.val)  # 5
        self.assertEqual(4, sll.head.next.next.next.val)  # 5
        self.assertEqual(None, sll.head.next.next.next.next)  # 5

        # 6. Reverse a long list
        sll = RSLL()
        sll.head = Node(1)
        sll.head.next = Node(2)
        sll.head.next.next = Node(3)
        sll.head.next.next.next = Node(4)
        sll.head.next.next.next.next = Node(5)
        sll.head.next.next.next.next.next = Node(6)
        sll.head.next.next.next.next.next.next = Node(7)
        sll.head.next.next.next.next.next.next.next = Node(8)
        sll.head.next.next.next.next.next.next.next.next = Node(9)
        sll.head.next.next.next.next.next.next.next.next.next = Node(10)
        sll.reverse(sll.head)
        self.assertEqual(10, sll.head.val)  # 6
        self.assertEqual(9, sll.head.next.val)  # 6
        self.assertEqual(8, sll.head.next.next.val)  # 6
        self.assertEqual(7, sll.head.next.next.next.val)  # 6
        self.assertEqual(6, sll.head.next.next.next.next.val)  # 6
        self.assertEqual(5, sll.head.next.next.next.next.next.val)  # 6
        self.assertEqual(4, sll.head.next.next.next.next.next.next.val)  # 6
        self.assertEqual(3, sll.head.next.next.next.next.next.next.next.val)  # 6
        self.assertEqual(2, sll.head.next.next.next.next.next.next.next.next.val)  # 6
        self.assertEqual(1, sll.head.next.next.next.next.next.next.next.next.next.val)  # 6
        self.assertEqual(None, sll.head.next.next.next.next.next.next.next.next.next.next)  # 6

    def test_comprehensive(self):
        sol = list(range(200)) + list(range(50))  # we want some duplicates to see how those are handled
        subject = RSLL()
        random.shuffle(sol)
        for i, val in enumerate(sol):
            subject.push(val)  # Check if push is correct
            self.assertEqual(sol[:i + 1], self.sll_to_list(subject))

        subject.reverse(subject.head)  # check if reverse is correct
        sol.reverse()
        self.assertEqual(sol, self.sll_to_list(subject))

        input_string = ""
        for i in range(len(sol)):
            input_string += str(sol[i])
            if i != len(sol) - 1:
                input_string += " --> "
        self.assertEqual(input_string, subject.to_string(subject.head))  # check if to_string is correct

        self.assertEqual(len(sol), subject.length(subject.head))  # check if the length is correct

        self.assertEqual(sum(sol), subject.sum_list(subject.head))  # check if sum_list is correct

        for val in sol:
            # make sure count is correct
            self.assertEqual(sol.count(val), subject.count(val))
            if sol.count(val) > 0:
                # make sure search is correct when the val is in the lisr
                self.assertTrue(subject.search(val))
            else:
                # make sure search is correct when the val isn't in the list
                self.assertFalse(subject.search(val))

            subject.remove(val)

            if val in sol:
                sol.remove(val)

            self.assertEqual(sol, self.sll_to_list(subject))  # make sure remove is working correctly

            if val < 50:
                # make sure remove all is working correctly
                subject.remove_all(val)

                for count in range(sol.count(val)):
                    sol.remove(val)

    def test_crafting(self):
        # Note this function uses the push function that you must write
        # So this test will not pass unless your push is working in addtion to completing
        # your crafting function

        # 1. The recipe contents are in the pocket
        recipe = RSLL()
        recipe.push('wood')
        recipe.push('wood')
        recipe.push('clay')

        pockets = RSLL()
        pockets.push('apple')
        pockets.push('wood')
        pockets.push('clay')
        pockets.push('wood')

        result = crafting(recipe, pockets)
        self.assertTrue(result)  # 1
        self.assertEqual(['apple'], self.sll_to_list(pockets))  # 1

        # 2. The pocket doesn't contain all of the needed items
        recipe = RSLL()
        recipe.push('sand dollar')
        recipe.push('sea snail')
        recipe.push('gold nugget')
        recipe.push('gold nugget')

        pockets = RSLL()
        pockets.push('wood')
        pockets.push('sand dollar')
        pockets.push('gold nugget')
        pockets.push('sea snail')
        pockets.push('clay')
        pockets.push('bamboo piece')

        result = crafting(recipe, pockets)
        self.assertFalse(result)  # 2
        self.assertEqual(['wood', 'sand dollar', 'gold nugget', 'sea snail',
                          'clay', 'bamboo piece'], self.sll_to_list(pockets))  # 2

        # 3. The pocket is empty
        recipe = RSLL()
        recipe.push('wood')
        recipe.push('wood')
        recipe.push('clay')

        pockets = RSLL()

        result = crafting(recipe, pockets)
        self.assertFalse(result)  # 3
        self.assertEqual([], self.sll_to_list(pockets))  # 3

        # 4. The recipe is empty
        recipe = RSLL()

        pockets = RSLL()
        pockets.push("large snowflake")
        pockets.push("axe")

        result = crafting(recipe, pockets)
        self.assertFalse(result)  # 4
        self.assertEqual(["large snowflake", "axe"], self.sll_to_list(pockets))  # 4

        # 5. The needed ingredients are reversed in the pocket
        recipe = RSLL()
        recipe.push('gold nugget')
        recipe.push('gold nugget')
        recipe.push('star fragment')
        recipe.push('star fragment')

        pockets = RSLL()
        pockets.push('star fragment')
        pockets.push('star fragment')
        pockets.push('gold nugget')
        pockets.push('gold nugget')

        result = crafting(recipe, pockets)
        self.assertTrue(result)  # 5
        self.assertEqual([], self.sll_to_list(pockets))  # 5

        # 6. All the same item
        recipe = RSLL()
        recipe.push('soft wood')
        recipe.push('soft wood')
        recipe.push('soft wood')
        recipe.push('soft wood')
        recipe.push('soft wood')

        pockets = RSLL()
        pockets.push('soft wood')
        pockets.push('soft wood')
        pockets.push('purple hyacinth')
        pockets.push('fireplace')
        pockets.push('soft wood')
        pockets.push('sea bass')
        pockets.push('soft wood')
        pockets.push('soft wood')

        result = crafting(recipe, pockets)
        self.assertTrue(result)  # 6
        self.assertEqual(['purple hyacinth', 'fireplace', 'sea bass'], self.sll_to_list(pockets))  # 6


if __name__ == '__main__':
    unittest.main()
