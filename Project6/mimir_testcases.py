import unittest
import random
from Project6.hashtable import HashTable, HashNode, CataData

random.seed(331)


class TestProject1(unittest.TestCase):

    def test_hash(self):
        # (1) Basic with no double hashing
        table1 = HashTable(capacity=16)

        self.assertEqual(4, table1.hash("Ian"))
        self.assertEqual(2, table1.hash("Max"))
        self.assertEqual(5, table1.hash("Yash"))
        self.assertEqual(0, table1.hash("Brandon"))

        # (2) Basic with double hashing - Inserting Mode Only
        table2 = HashTable(capacity=16)

        table2.table = [None, None, None, None, HashNode("Ian", 150, True),
                        None, None, None, HashNode("H", 100),
                        None, None, None, None, None, None, None]

        self.assertEqual(9, table2.hash("Andrew", inserting=True))
        self.assertEqual(5, table2.hash("Andy", inserting=True))
        self.assertEqual(15, table2.hash("Lukas", inserting=True))

        # (3) Larger with Inserting and not Inserting
        table3 = HashTable(capacity=16)

        table3.table = [None, None, None,
                        HashNode('class_ever', 1), HashNode(None, None, True),
                        HashNode(None, None, True), None, None, None,
                        None, HashNode(None, None, True), None,
                        None, None, HashNode('cse331', 100), None]

        # Should insert in the first available bin
        self.assertEqual(4, table3.hash("is_the", inserting=True))

        # Should search until the first None/unused bin
        self.assertEqual(15, table3.hash("is_the"))

        # Should insert in the first available bin
        self.assertEqual(5, table3.hash("yash", inserting=True))

        # Should search until the first None/unused bin
        self.assertEqual(7, table3.hash("yash"))

        self.assertEqual(3, table3.hash("class_ever"))

        # (4) Large Comprehensive
        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        table4 = HashTable(capacity=16)

        table4.table = [None, None, HashNode('Max', 0),
                        None, HashNode('Ian', 10),
                        HashNode(None, None, True), None, None, None,
                        None, HashNode(None, None, True), None,
                        None, None, HashNode(None, None, True), None]

        expected = [2, 2, 4, 4, 9, 9, 8, 8, 8, 8, 0, 0, 8, 8, 7, 7, 6, 6, 15, 15, 3, 3, 15, 15, 14, 7, 9, 9, 1, 1, 9,
                    9, 0, 0, 5, 8, 15, 15]

        for i, key in enumerate(keys):
            # inserts every key in inserting mode and normal mode
            self.assertEqual(expected[2 * i], table4.hash(key, inserting=True))
            self.assertEqual(expected[2 * i + 1], table4.hash(key))

    def test_insert(self):
        # This test is just to make sure that the hidden method does the proper amount of work!
        # Insert Sanity Check
        table = HashTable()

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]

        table._insert('cse331', 100)
        table._insert('is_the', 3005)

        self.assertEqual(solution, table.table)

        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table._insert('best', 42)
        table._insert('class_ever', 1)

        self.assertEqual(4, table.size)
        self.assertEqual(16, table.capacity)
        self.assertEqual(solution, table.table)

    def test_get(self):
        # This test is just to make sure that the hidden method does the proper amount of work!
        # Get Sanity Check
        table = HashTable(capacity=8)

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]
        table.table = solution  # set the table so insert does not need to work
        table.size = 2

        self.assertEqual(HashNode("is_the", 3005), table._get('is_the'))
        self.assertEqual(HashNode("cse331", 100), table._get('cse331'))
        self.assertIsNone(table._get('cse320'))

    def test_delete(self):
        # This test is just to make sure that the hidden method does the proper amount of work!
        # Delete Sanity Check
        table = HashTable(capacity=16)

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None, True), None, None, None,
                         None, None, HashNode(None, None, True), None, None, None, HashNode('cse331', 100), None]

        table.table = pre_solution  # set the table so insert does not need to work
        table.size = 4

        delete = ['best', 'is_the']
        for k in delete:
            table._delete(k)

        self.assertEqual(post_solution, table.table)
        self.assertEqual(2, table.size)

    def test_len(self):
        # (1) Empty
        table = HashTable()
        self.assertEqual(0, len(table))

        # (2) Size = 1
        table.size = 1
        self.assertEqual(1, len(table))

        # (3) Size = 5
        table.size = 5
        self.assertEqual(5, len(table))

    def test_setitem(self):
        # (1) Simple (No Grow)
        table = HashTable()

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]

        table["cse331"] = 100
        table["is_the"] = 3005

        self.assertEqual(2, table.size)
        self.assertEqual(8, table.capacity)
        self.assertEqual(solution, table.table)

        # (2) Simple (Grow, builds on 1)
        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table['best'] = 42
        table['class_ever'] = 1

        self.assertEqual(4, table.size)
        self.assertEqual(16, table.capacity)
        self.assertEqual(solution, table.table)

        # (3) Large Comprehensive
        table2 = HashTable()

        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        solution = [None, None, None, None, HashNode("Ian", 10), None, None, None, HashNode("H", 30),
                    HashNode("Andrew", 20), None, None, None, None, None, None, HashNode("Olivia", 50), None,
                    HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode("Lukas", 60),
                    HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None,
                    HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None,
                    None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None,
                    HashNode("Anna", 130), None, None, None, HashNode("Angelo", 80), HashNode("Sean", 70),
                    HashNode("Andy", 40), None, None, None, None, HashNode("Max", 0), None, HashNode("Jacob", 90)]

        for i, key in enumerate(keys):
            table2[key] = vals[i]

        self.assertEqual(19, table2.size)
        self.assertEqual(64, table2.capacity)
        self.assertEqual(solution, table2.table)

    def test_getitem(self):
        # (1) Basic
        table = HashTable(capacity=8)

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]
        table.table = solution  # set the table so insert does not need to work
        table.size = 2

        self.assertEqual(3005, table["is_the"])
        self.assertEqual(100, table["cse331"])

        # (2) Slightly Larger
        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table.table = solution  # set the table so insert does not need to work
        table.capacity = 16
        table.size = 4

        self.assertEqual(3005, table["is_the"])
        self.assertEqual(100, table["cse331"])
        self.assertEqual(42, table["best"])
        self.assertEqual(1, table["class_ever"])

        # (3) Large Comprehensive
        table2 = HashTable(capacity=64)

        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        solution = [None, None, None, None, HashNode("Ian", 10), None, None, None, HashNode("H", 30),
                    HashNode("Andrew", 20), None, None, None, None, None, None, HashNode("Olivia", 50), None,
                    HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode("Lukas", 60),
                    HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None,
                    HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None,
                    None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None,
                    HashNode("Anna", 130), None, None, None, HashNode("Angelo", 80), HashNode("Sean", 70),
                    HashNode("Andy", 40), None, None, None, None, HashNode("Max", 0), None, HashNode("Jacob", 90)]

        table2.table = solution  # set the table so insert does not need to work
        table2.size = 19

        for i, key in enumerate(keys):
            self.assertEqual(vals[i], table2[key])

        # (4) KeyError Check
        with self.assertRaises(KeyError):
            abc = table2["Enbody"]

    def test_delitem(self):
        # (1) Basic
        table = HashTable(capacity=16)

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None, True), None, None, None,
                         None, None, HashNode(None, None, True), None, None, None, HashNode('cse331', 100), None]

        table.table = pre_solution  # set the table so insert does not need to work
        table.size = 4

        delete = ['best', 'is_the']
        for k in delete:
            del table[k]

        self.assertEqual(post_solution, table.table)
        self.assertEqual(2, table.size)

        # (2) Large Comprehensive
        table2 = HashTable(capacity=64)

        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        pre_solution = [None, None, None, None, HashNode("Ian", 10), None, None, None, HashNode("H", 30),
                        HashNode("Andrew", 20), None, None, None, None, None, None, HashNode("Olivia", 50), None,
                        HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode("Lukas", 60),
                        HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None,
                        HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None,
                        None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None,
                        HashNode("Anna", 130), None, None, None, HashNode("Angelo", 80), HashNode("Sean", 70),
                        HashNode("Andy", 40), None, None, None, None, HashNode("Max", 0), None, HashNode("Jacob", 90)]

        solution = [None, None, None, None, HashNode(None, None), None, None, None, HashNode(None, None),
                    HashNode(None, None), None, None, None, None, None, None, HashNode(None, None), None,
                    HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode(None, None),
                    HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None,
                    HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None,
                    None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None,
                    HashNode("Anna", 130), None, None, None, HashNode(None, None), HashNode(None, None),
                    HashNode(None, None), None, None, None, None, HashNode(None, None), None, HashNode(None, None)]

        table2.table = pre_solution  # set the table so insert does not need to work
        table2.size = 19

        for i, key in enumerate(keys):
            if i < 10:
                del table2[key]

        self.assertEqual(solution, table2.table)
        self.assertEqual(9, table2.size)

        # (3) KeyError Check
        with self.assertRaises(KeyError):
            del table2["Enbody"]
        self.assertEqual(9, table2.size)

    def test_contains(self):
        # (1) Not in Table
        table = HashTable()
        self.assertEqual(False, 'key' in table)

        # (2) In Table
        table.table[5] = HashNode('key', 331)

        self.assertEqual(True, 'key' in table)
        self.assertEqual(False, 'new_key' in table)

    def test_update(self):
        # (1) Not in Table Already
        table = HashTable()

        table.update([("minecraft", 10), ("ghast", 15)])
        self.assertEqual(10, table["minecraft"])
        self.assertEqual(15, table["ghast"])
        self.assertEqual(2, table.size)

        # (2) Update Values in Table
        table.update([("minecraft", 31), ("ghast", 42)])
        self.assertEqual(31, table["minecraft"])
        self.assertEqual(42, table["ghast"])
        self.assertEqual(2, table.size)

        # (3) Update Values in Table and Add New Values
        table.update([("minecraft", 50), ("enderman", 12)])
        self.assertEqual(50, table["minecraft"])
        self.assertEqual(12, table["enderman"])
        self.assertEqual(42, table["ghast"])
        self.assertEqual(3, table.size)

        # (4) Do Nothing
        table.update()
        self.assertEqual(50, table["minecraft"])
        self.assertEqual(12, table["enderman"])
        self.assertEqual(42, table["ghast"])
        self.assertEqual(3, table.size)

    def test_keys_values_items(self):
        # (1) Basic
        table = HashTable()

        initial_keys = ['one', 'two', 'three']
        initial_values = [1, 2, 31]
        initial_items = [('one', 1), ('two', 2), ('three', 31)]

        for i in range(3):
            table[initial_keys[i]] = initial_values[i]

        keys = table.keys()
        values = table.values()
        items = table.items()

        self.assertEqual(set(initial_keys), set(keys))
        self.assertEqual(set(initial_values), set(values))
        self.assertEqual(set(initial_items), set(items))

        # (2) Large
        table2 = HashTable()
        initial_keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach",
                        "Bank", "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        initial_values = [i * 10 for i in range(19)]
        initial_items = []

        for i, key in enumerate(initial_keys):
            table2[key] = initial_values[i]
            initial_items.append((key, initial_values[i]))

        keys = table2.keys()
        values = table2.values()
        items = table2.items()

        self.assertEqual(set(initial_keys), set(keys))
        self.assertEqual(set(initial_values), set(values))
        self.assertEqual(set(initial_items), set(items))

    def test_clear(self):
        # (1) Table with contents
        table = HashTable()

        table['table'] = 1
        table['will'] = 2
        table['be'] = 3
        table['cleared'] = 4

        self.assertEqual(4, table.size)

        table.clear()

        self.assertEqual(0, table.size)
        for node in table.table:
            self.assertIsNone(node)

        # (2) Empty Table
        table.clear()

        self.assertEqual(0, table.size)
        for node in table.table:
            self.assertIsNone(node)

        # (3) Reused Table
        table['one'] = 1

        table.clear()

        self.assertEqual(0, table.size)
        for node in table.table:
            self.assertIsNone(node)

    def test_all(self):
        table = HashTable()

        sol_keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                    "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        sol_vals = [i * 100 for i in range(19)]

        solution_a = [None, None, None, None, HashNode("Ian", 100), None, None, None, HashNode("H", 300),
                      HashNode("Andrew", 200), None, None, None, None, None, None, HashNode("Olivia", 500), None,
                      HashNode("Zach", 1000), None, None, HashNode("Yash", 1700), None, None, HashNode("Lukas", 600),
                      HashNode("Scott", 1500), None, None, None, None, HashNode("Onsay", 1200), None,
                      HashNode("Brandon", 1600), HashNode("Zosha", 1400), None, None, HashNode("Bank", 1100), None,
                      None, None, None, None, None, None, None, None, None, HashNode("Sarah", 1800), None, None,
                      HashNode("Anna", 1300), None, None, None, HashNode("Angelo", 800), HashNode("Sean", 700),
                      HashNode("Andy", 400), None, None, None, None, HashNode("Max", 0), None, HashNode("Jacob", 900)]

        solution_b = [None, None, None, None, HashNode(None, None), None, None, None, HashNode(None, None),
                      HashNode(None, None), None, None, None, None, None, None, HashNode(None, None), None,
                      HashNode("Zach", 1000), None, None, HashNode("Yash", 1700), None, None, HashNode(None, None),
                      HashNode("Scott", 1500), None, None, None, None, HashNode("Onsay", 1200), None,
                      HashNode("Brandon", 1600), HashNode("Zosha", 1400), None, None, HashNode("Bank", 1100), None,
                      None, None, None, None, None, None, None, None, None, HashNode("Sarah", 1800), None, None,
                      HashNode("Anna", 1300), None, None, None, HashNode(None, None), HashNode(None, None),
                      HashNode(None, None), None, None, None, None, HashNode(None, None), None, HashNode(None, None)]

        solution_c = [None, None, None, None, HashNode("Ian", 45), None, None, None, HashNode("H", 300),
                      HashNode("Andrew", 200), None, None, None, None, None, None, HashNode("Olivia", 500), None,
                      HashNode("Zach", 1000), None, None, HashNode("Yash", 1700), None, None, HashNode("Lukas", 600),
                      HashNode("Scott", 1500), None, None, None, None, HashNode("Onsay", 1200), None,
                      HashNode("Brandon", 1600), HashNode("Zosha", 1400), None, None, HashNode("Bank", 1100), None,
                      None, None, None, None, None, None, None, None, None, HashNode("Sarah", 1800), None, None,
                      HashNode("Anna", 1300), None, None, None, HashNode("Angelo", 800), HashNode("Sean", 700),
                      HashNode("Andy", 400), None, None, None, None, HashNode("Max", 40), None, HashNode("Jacob", 900)]

        # Insertions/Grow
        sizes = [i + 1 for i in range(19)]
        capacities = [8] * 3 + [16] * 4 + [32] * 8 + [64] * 4
        for i, key in enumerate(sol_keys):
            table[key] = sol_vals[i]
            self.assertEqual(sizes[i], table.size)
            self.assertEqual(capacities[i], table.capacity)

        self.assertEqual(solution_a, table.table)

        # Get
        for i, key in enumerate(sol_keys):
            self.assertEqual(sol_vals[i], table[key])

        with self.assertRaises(KeyError):
            abc = table["Owen"]

        # Delete
        for i, key in enumerate(sol_keys):
            if i < 10:
                del table[key]

        self.assertEqual(solution_b, table.table)
        self.assertEqual(9, table.size)

        with self.assertRaises(KeyError):
            del table["Owen"]
        self.assertEqual(9, table.size)

        # Clear
        table.clear()

        self.assertEqual(0, table.size)
        for node in table.table:
            self.assertIsNone(node)

        table = HashTable()
        for i, key in enumerate(sol_keys):
            table[key] = sol_vals[i]

        # Keys/Vals/Items
        keys = table.keys()
        values = table.values()
        items = table.items()

        self.assertEqual(set(sol_keys), set(keys))
        self.assertEqual(set(sol_vals), set(values))
        self.assertEqual({(sol_keys[i], sol_vals[i]) for i in range(19)}, set(items))

        # Contains
        for i, key in enumerate(sol_keys):
            self.assertEqual(True, key in table)
        self.assertEqual(False, "Ofria" in table)

        # Update
        table.update([("Ian", 45), ("Max", 40)])
        self.assertEqual(solution_c, table.table)

    def test_cata_query(self):
        cata_data = CataData()

        cata_data.enter("Ian", "Wilson", 1)
        cata_data.exit("Ian", "Akers", 4)
        expected = 3.0
        student_response = cata_data.get_average("Wilson", "Akers")
        self.assertAlmostEqual(expected, student_response)

        cata_data = CataData()

        cata_data.enter("Ian", "Wilson", 1)
        cata_data.enter("Max", "Wilson", 1)
        cata_data.exit("Ian", "Akers", 4)
        cata_data.exit("Max", "Akers", 5)
        expected = 3.5
        student_response = cata_data.get_average("Wilson", "Akers")
        self.assertAlmostEqual(expected, student_response)

        cata_data = CataData()

        cata_data.enter("Ian", "Engineering", 0)
        cata_data.enter("Max", "Chemistry", 7)
        cata_data.exit("Ian", "Chemistry", 1)
        cata_data.enter("Ian", "Chemistry", 4)
        cata_data.exit("Ian", "Wells", 6)
        cata_data.enter("Ian", "Wells", 8)
        cata_data.exit("Ian", "Wilson", 10)
        cata_data.exit("Max", "Wells", 12)

        expected = 3.5
        student_response = cata_data.get_average("Chemistry", "Wells")
        self.assertAlmostEqual(expected, student_response)

        expected = 1.0
        student_response = cata_data.get_average("Engineering", "Chemistry")
        self.assertAlmostEqual(expected, student_response)

        expected = 0.0
        student_response = cata_data.get_average("Akers", "Anthony")
        self.assertAlmostEqual(expected, student_response)

    def test_cata_query_large(self):
        bus_stops = ["Wilson", "Case", "Wonders", "IM West", "Wells", "1855", \
                     "Spartan Stadium", "Anthony", "Engineering", "Bessey", "Grand River", "Union", \
                     "Akers", "IM East", "Natural Resources", "Lot 89", "Biochemistry", "SnyPhy", \
                     "Landon", "Brody", "Breslin", "CommArtSci", "VetMed"]
        answers = [15.333333333333334, 9.0, 19.0, 35.0, 42.0, 27.0, 12.0, 31.0, \
                   33.0, 14.5, 16.5, 28.5, 7.0, 12.0, 22.0, 15.333333333333334, 33.0, \
                   10.0, 16.5, 24.0, 31.0, 12.5, 6.0, 1.0, 12.0, 11.5, 33.0, 19.0, \
                   31.0, 6.0, 32.5, 32.5, 12.0, 43.0, 7.0, 36.0, 12.0, 23.333333333333332, \
                   12.0, 30.0, 28.0, 20.0, 17.0, 38.0, 20.0, 30.0, 18.0, 22.0, 28.5, 19.0, \
                   39.5, 19.0, 26.0, 39.0, 23.0, 19.0, 26.0, 43.0, 15.333333333333334, 15.0, \
                   30.0, 40.0, 14.0, 23.333333333333332, 31.0, 28.0, 12.5, 17.5, 12.0, 11.0, \
                   24.0, 29.666666666666668, 33.0, 17.0, 44.0, 13.0, 5.0, 16.0, 38.0, 31.0, \
                   24.0, 33.0, 25.0, 32.0, 20.0, 33.0, 19.0, 14.0, 25.5, 34.0, 10.0, 2.0, \
                   28.0, 27.0, 8.0, 1.0, 26.0, 37.0, 17.5, 25.333333333333332, 34.0, 44.0, \
                   41.0, 44.0, 29.0, 11.0, 34.0, 19.0, 27.0, 19.5, 20.0, 41.0, 19.0, 17.0, \
                   14.0, 18.0, 25.5, 17.0, 4.0, 38.0, 39.0, 29.0, 29.666666666666668, 36.0, \
                   18.0, 30.0, 21.0, 31.5, 41.0, 29.0, 2.0, 24.0, 8.0, 21.0, 33.5, 28.0, 42.0, \
                   15.0, 21.0, 25.5, 22.0, 19.0, 37.0, 30.0, 23.5, 27.0, 1.0, 20.0, 25.0, 35.0, \
                   22.0, 30.0, 22.5, 23.0, 23.333333333333332, 6.0, 32.0, 22.0, 32.0, 18.0, 6.0, \
                   24.0, 18.0, 22.0, 43.0, 16.0, 18.0, 6.0, 13.0, 25.333333333333332, 35.0, 36.0, \
                   43.0, 14.0, 9.0, 29.666666666666668, 15.0, 24.0, 11.5, 36.0, 41.0, 43.0, 26.0, \
                   11.0, 6.0, 2.0, 25.333333333333332, 24.0, 1.0, 10.0, 39.5, 40.0, 39.5, 27.0, \
                   39.5, 42.0, 8.0, 33.0, 29.0, 4.0, 15.0, 9.0, 35.0, 41.0, 45.0, 19.5, 14.5, 43.5, \
                   23.0, 23.5, 14.0, 26.0, 31.5, 5.0, 5.0, 43.5, 1.0, 5.0, 40.0, 4.0, 8.0, 12.0, \
                   15.0, 33.5, 20.0, 24.0, 26.0, 41.0, 25.5, 35.0, 12.0, 44.0, 32.0, 18.0, 14.0, \
                   29.0, 21.0, 8.0, 22.5, 24.0, 16.0, 27.0, 4.0, 20.0, 3.0, 12.0, 20.0, 26.0, 45.0, 40.0]
        # Keeps track of trips taken
        trips = list()
        # Used to store the starting bus stop of an entry with its enter time
        stations_and_time = list()

        cata_data = CataData()
        for i in range(250):
            # Random bus stop
            start_pos = random.randint(0, 1000) % len(bus_stops)
            # Random start time
            start_time = random.randint(0, 1000)
            cata_data.enter(str(i), bus_stops[start_pos], start_time)
            stations_and_time.append((start_pos, start_time))

        for i in range(250):
            # Get the start time
            start_pos, start_time = stations_and_time[i]
            dest_pos = random.randint(0, 1000) % len(bus_stops)
            while dest_pos == start_pos:
                # Ensures random destination station is different from origin
                dest_pos = random.randint(0, 1000) % len(bus_stops)
            # Trip end time will be somewhere between 1 and 45 after start time
            end_time = start_time + random.randint(1, 45)
            cata_data.exit(str(i), bus_stops[dest_pos], end_time)
            trips.append((bus_stops[start_pos], bus_stops[dest_pos]))

        for i in range(len(answers)):
            student = cata_data.get_average(trips[i][0], trips[i][1])
            self.assertAlmostEqual(answers[i], student)


if __name__ == '__main__':
    unittest.main()
