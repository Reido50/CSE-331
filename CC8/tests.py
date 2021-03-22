import unittest
import random
from solution import Bundle
from InventoryItems import ALL_ITEMS

random.seed(331)

# Converting global constant of items into a list of tuples for testing purposes
ITEMS = [(item[0], item[1].amount_in_stack) for item in ALL_ITEMS.items.items()]


class CC8Tests(unittest.TestCase):
    def test_basic(self):

        # 1 - example 1 (see Mimir)
        bundle = Bundle()
        bundle.add_to_bundle("Ender Pearl", 2)
        result = bundle.add_to_bundle("Dirt", 12)
        actual = bundle.to_set()
        expected = {("Dirt", 12), ("Ender Pearl", 2)}
        self.assertEqual(actual, expected)
        self.assertEqual(result, True)

        # 2 - example 2 (see Mimir)
        bundle = Bundle()
        bundle.add_to_bundle("Ender Pearl", 2)
        result = bundle.add_to_bundle("Dirt", 56)
        actual = bundle.to_set()
        expected = {("Dirt", 56), ("Ender Pearl", 2)}
        self.assertEqual(actual, expected)
        self.assertEqual(result, True)

        # 3 - example 3 (see Mimir)
        bundle = Bundle()
        items = [("Ender Pearl", 4), ("Dirt", 28), ("Gold Ingot", 5)]
        [bundle.add_to_bundle(i[0], i[1]) for i in items]
        result = bundle.add_to_bundle("Cobblestone", 16)
        actual = bundle.to_set()
        expected = set(items)
        self.assertEqual(actual, expected)
        self.assertEqual(result, False)

        # 4 - example 4 (see Mimir)
        bundle = Bundle()
        items = [("Cobblestone", 48), ("Gold Ingot", 10)]
        [bundle.add_to_bundle(i[0], i[1]) for i in items]
        result = bundle.remove_from_bundle("Cobblestone", 16)
        items[0] = ("Cobblestone", 32)
        actual = bundle.to_set()
        expected = set(items)
        self.assertEqual(actual, expected)
        self.assertEqual(result, True)

        # 5 - example 5 (see Mimir)
        bundle = Bundle()
        items = [("Cobblestone", 12), ("Dirt", 40)]
        [bundle.add_to_bundle(i[0], i[1]) for i in items]
        result = bundle.remove_from_bundle("Cobblestone", 16)
        actual = bundle.to_set()
        expected = set(items)
        self.assertEqual(actual, expected)
        self.assertEqual(result, False)

    def test_addToBundle(self):
        bundle = Bundle()

        # 1 - add to empty bundle, one item
        result = bundle.add_to_bundle("Cobblestone", 64)
        actual = bundle.to_set()
        expected = {("Cobblestone", 64)}
        self.assertEqual(expected, actual)  # check contents of bundle
        self.assertEqual(result, True)  # addToBundle should return true

        # 2 - add multiple items to empty bundle, all
        items = [("Cobblestone", 32), ("Dirt", 32)]
        bundle = Bundle()
        results = []
        for item in items:
            results.append(bundle.add_to_bundle(item[0], item[1]))

        actual = bundle.to_set()
        expected = set(items)
        self.assertEqual(expected, actual)
        self.assertEqual(results[0], True)
        self.assertEqual(results[1], True)

        # 3 - add one item, doesnt fit
        results.append(bundle.add_to_bundle("Diamond Sword", 1))  # bundle already contains 64 items
        actual = bundle.to_set()
        self.assertEqual(expected, actual)  # items in bundle should not change
        self.assertEqual(results[-1], False)  # addToBundle should return false

        # 4 - add one item which would fit if the amount was different amount
        bundle = Bundle()
        bundle.add_to_bundle("Dirt", 60)
        results.append(bundle.add_to_bundle("Carrot", 10))
        actual = bundle.to_set()
        expected = {("Dirt", 60)}
        self.assertEqual(expected, actual)
        self.assertEqual(results[-1], False)

        # 5 - add multiple item, none fit. Different stack sizes
        items = [("Cobblestone", 40), ("Ender Pearl", 5), ("Water Bucket", 1)]
        results.clear()
        for item in items:  # bundle is at 60 capacity from previous, none fit
            results.append(bundle.add_to_bundle(item[0], item[1]))
        actual = bundle.to_set()
        self.assertEqual(expected, actual)  # expected hasn't changed
        self.assertEqual(results, [False, False, False])

        # 6 - add multiple items, incremental fit (some fit, some don't)
        bundle = Bundle()
        items = [("Cobblestone", 32), ("Wooden Sword", 1),
                 ("Ender Pearl", 16), ("Ender Pearl", 4),
                 ("Egg", 2), ("Dirt", 12), ("Iron Ingot", 8), ("Dirt", 1)]

        results.clear()
        for item in items:  # bundle is empty initially
            results.append(bundle.add_to_bundle(item[0], item[1]))

        expected = {("Cobblestone", 32), ("Ender Pearl", 4), ("Iron Ingot", 8), ("Egg", 2)}
        actual = bundle.to_set()
        self.assertEqual(expected, actual)
        self.assertEqual(results, [True, False, False, True, True, False, True, False])

    def test_removeFromBundle(self):
        bundle = Bundle()

        # 1 - empty bundle, failure noCustomizable IO Test Casething to remove
        result = bundle.remove_from_bundle("Cobblestone", 1)
        actual = bundle.to_set()
        expected = set()
        self.assertEqual(expected, actual)
        self.assertEqual(result, False)  # failure to remove

        # 2 - one item, success
        bundle.add_to_bundle("Cobblestone", 64)
        result = bundle.remove_from_bundle("Cobblestone", 64)
        actual = bundle.to_set()
        expected = set()
        self.assertEqual(expected, actual)
        self.assertEqual(result, True)  # successful removal

        # 3 - one item, failure (wrong item)
        bundle = Bundle()
        bundle.add_to_bundle("Egg", 4)
        result = bundle.remove_from_bundle("Cobblestone", 1)
        actual = bundle.to_set()
        expected = {("Egg", 4)}
        self.assertEqual(expected, actual)
        self.assertEqual(result, False)  # successful removal

        # 4 - one item, multiple calls to remove fully
        results = []
        for i in range(5):
            results.append(bundle.remove_from_bundle("Egg", 1))
        actual = bundle.to_set()
        expected = set()
        self.assertEqual(expected, actual)
        self.assertEqual(results, [True, True, True, True, False])

        # 5 - multiple items, all successful partial removals
        results.clear()
        items = [("Cobblestone", 40), ("Ender Pearl", 5), ("Bucket", 2)]
        for item in items:
            bundle.add_to_bundle(item[0], item[1])
        for item in items:
            results.append(bundle.remove_from_bundle(item[0], item[1] // 2))
        actual = bundle.to_set()
        expected = {("Cobblestone", 20), ("Ender Pearl", 3), ("Bucket", 1)}
        self.assertEqual(expected, actual)
        self.assertEqual(results, [True, True, True])

        # 6 - multiple items, all failure
        results.clear()
        for item in items:
            results.append(bundle.remove_from_bundle(item[0], item[1]))
        actual = bundle.to_set()
        self.assertEqual(expected, actual)  # no inventory change = expected didn't change
        self.assertEqual(results, [False, False, False])

        # 7 - multiple items, intermittent success/failure
        results.clear()
        bundle = Bundle()
        items = [("Ender Pearl", 4), ("Dirt", 16),
                 ("Iron Ingot", 8), ("Carrot", 24)]
        for item in items:
            bundle.add_to_bundle(item[0], item[1])
        for item in items:
            results.append(bundle.remove_from_bundle(item[0], 16))
        actual = bundle.to_set()
        expected = {("Ender Pearl", 4), ("Iron Ingot", 8), ("Carrot", 8)}
        self.assertEqual(expected, actual)
        self.assertEqual(results, [False, True, False, True])

    def test_small_comprehensive(self):
        # Loop through all items

        # if item amount is not 1:
        # divide amount by 2

        # add item to bundle

        # if no failure to add
        # add item to curr_items list

        # else
        # check the curr items from last failure are in the bundle
        # remove all items from last failure from bundle and check empty

        # add item to curr_items list
        # add failed item to bundle

        # check full counter
        bundle = Bundle()
        results = []
        curr_items = []  # current items in the bundle for testing
        for i, item in enumerate(ITEMS):

            amount = item[1]
            if amount != 1:
                amount = amount // 2  # cutting all values in half
            results.append(bundle.add_to_bundle(item[0], amount))

            if results[-1]:
                curr_items.append((item[0], amount))

            else:
                expected = set(curr_items)
                actual = bundle.to_set()
                self.assertEqual(expected, actual)  # check bundle and curr_items match

                for itm in curr_items:
                    bundle.remove_from_bundle(itm[0], itm[1])
                expected = set()
                actual = bundle.to_set()
                self.assertEqual(expected, actual)  # check all items from bundle were removed correctly

                curr_items.clear()
                results.append(bundle.add_to_bundle(item[0], amount))  # add last item to bundle and curr_items
                curr_items.append((item[0], amount))

        failed_counter = results.count(False)  # number of failures to add
        success_counter = results.count(True)  # number of successful adds
        self.assertEqual(success_counter, 17)
        self.assertEqual(failed_counter, 10)

    def test_large_comprehensive(self):

        # same as small_comprehensive but with a larger list and shuffled
        # also curr_items becomes a dictionary since we have duplicate items

        ITEMS_LARGE = ITEMS * 10
        random.shuffle(ITEMS_LARGE)
        bundle = Bundle()
        results = []
        curr_items = dict()  # current items in the bundle for testing
        for i, item in enumerate(ITEMS_LARGE):
            amount = item[1]
            if amount != 1:
                amount = amount // 2  # cutting all values in half

            results.append(bundle.add_to_bundle(item[0], amount))

            if results[-1]:
                if item[0] not in curr_items:
                    curr_items[item[0]] = 0
                curr_items[item[0]] += amount

            else:
                expected = set(curr_items.items())
                actual = bundle.to_set()
                self.assertEqual(expected, actual)  # check bundle and curr_items match

                for item_tup in expected:
                    bundle.remove_from_bundle(item_tup[0], item_tup[1])

                expected = set()
                actual = bundle.to_set()
                self.assertEqual(expected, actual)  # check all items from bundle were removed correctly

                curr_items.clear()
                curr_items[item[0]] = 0
                curr_items[item[0]] += amount
                results.append(bundle.add_to_bundle(item[0], amount))  # add last item to bundle and curr_items

        failed_counter = results.count(False)
        success_counter = results.count(True)
        self.assertEqual(success_counter, 170)
        self.assertEqual(failed_counter, 111)


if __name__ == '__main__':
    unittest.main()
