import unittest
from solution import count_good_dungeons
from game import Game
from itertools import combinations
import random


class TestCodingChallenge7(unittest.TestCase):

    def test_basic(self):
        
        # Test empty graph
        game = Game()
        actual = count_good_dungeons(game)
        self.assertEqual(0, actual)

        # Test one room / dungeon
        game.add_to_game("A")
        actual = count_good_dungeons(game)
        self.assertEqual(0, actual)

        #       A

        # Test two rooms / dungeons
        game.add_to_game("B")
        actual = count_good_dungeons(game)
        self.assertEqual(0, actual)

        #       A
        #
        #   B

        # Test three rooms / dungeons
        game.add_to_game("C")
        actual = count_good_dungeons(game)
        self.assertEqual(0, actual)

        #       A
        #
        #   B       C

        # Add edge from A to B - Two dungeons
        game.add_hallway("A", "B")
        actual = count_good_dungeons(game)
        self.assertEqual(0, actual)

        #       A
        #     /
        #   B       C

        # Add edge from B to C - One dungeon
        game.add_hallway("B", "C")
        actual = count_good_dungeons(game)
        self.assertEqual(0, actual)

        #       A
        #     /
        #   B  ---  C

        # Add edge from A to C - One GOOD dungeon
        game.add_hallway("A", "C")
        actual = count_good_dungeons(game)
        self.assertEqual(1, actual)

        #       A
        #     /   \
        #   B  ---  C

    def test_good_dungeons(self):

        game = Game()

        # Add single good dungeon
        game.add_to_game("A")
        game.add_to_game("B")
        game.add_to_game("C")
        game.add_to_game("D")

        game.add_hallway("A", "B")
        game.add_hallway("B", "C")
        game.add_hallway("C", "D")
        game.add_hallway("D", "A")

        actual = count_good_dungeons(game)
        self.assertEqual(1, actual)

        # Add another good dungeon
        game.add_to_game("E")
        game.add_to_game("F")
        game.add_to_game("G")

        game.add_hallway("E", "F")
        game.add_hallway("F", "G")
        game.add_hallway("E", "G")

        actual = count_good_dungeons(game)
        self.assertEqual(2, actual)

        # Link two dungeons
        game.add_hallway("C", "E")
        actual = count_good_dungeons(game)
        self.assertEqual(1, actual)

    def test_bad_dungeons(self):

        game = Game()

        # Create linked list
        rooms = ["A", "B", "C", "D", "E", "F", "G"]
        for room in rooms:
            game.add_to_game(room)

        for i in range(len(rooms) - 1):
            game.add_hallway(rooms[i], rooms[i + 1])

        # Linked list is not good dungeon
        actual = count_good_dungeons(game)
        self.assertEqual(0, actual)

        # Add link in middle, making it good dungeon
        game.add_hallway("B", "E")
        actual = count_good_dungeons(game)
        self.assertEqual(1, actual)

        # Create another linked list
        rooms = ["H", "I", "J", "K"]
        for room in rooms:
            game.add_to_game(room)

        for i in range(len(rooms) - 1):
            game.add_hallway(rooms[i], rooms[i + 1])

        # Linked list is not good dungeon
        actual = count_good_dungeons(game)
        self.assertEqual(1, actual)

        # Adding link from bad dungeon to good dungeon creates one good dungeon
        game.add_hallway("E", "H")
        actual = count_good_dungeons(game)
        self.assertEqual(1, actual)

    def test_complex_dungeons(self):

        game = Game()

        rooms = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        for room in rooms:
            game.add_to_game(room)

        # Add 6-room fully linked dungeon
        for edge in combinations(rooms[:6], 2):
            game.add_hallway(edge[0], edge[1])

        actual = count_good_dungeons(game)
        self.assertEqual(1, actual)

        # Add 4-room fully linked dungeon
        for edge in combinations(rooms[6:10], 2):
            game.add_hallway(edge[0], edge[1])

        actual = count_good_dungeons(game)
        self.assertEqual(2, actual)

        # Add 2-room fully linked dungeon
        for edge in combinations(rooms[10:12], 2):
            game.add_hallway(edge[0], edge[1])

        actual = count_good_dungeons(game)
        self.assertEqual(2, actual)

        # Add 14-room fully linked dungeon
        for edge in combinations(rooms[12:], 2):
            game.add_hallway(edge[0], edge[1])

        actual = count_good_dungeons(game)
        self.assertEqual(3, actual)

        # Link together each dungeon by a hallway
        game.add_hallway("A", "G")
        actual = count_good_dungeons(game)
        self.assertEqual(2, actual)

        game.add_hallway("G", "M")
        actual = count_good_dungeons(game)
        self.assertEqual(1, actual)

        game.add_hallway("M", "K")
        actual = count_good_dungeons(game)
        self.assertEqual(1, actual)

    def test_comprehensive(self):

        def add_random_edge():
            hallway = random.sample(game._rooms_set, 2)
            while not game.add_hallway(hallway[0], hallway[1]):
                hallway = random.sample(game._rooms_set, 2)

        game = Game()
        random.seed(453)

        # Create 100 room game
        for i in range(100):
            game.add_to_game(i)

        # Add 56 random edges
        for _ in range(56):
            add_random_edge()
            actual = count_good_dungeons(game)
            self.assertEqual(0, actual)

        # Add three random edges
        for _ in range(3):
            add_random_edge()
            actual = count_good_dungeons(game)
            self.assertEqual(1, actual)

        # Add twelve random edges
        for _ in range(12):
            add_random_edge()
            actual = count_good_dungeons(game)
            self.assertEqual(2, actual)

        # Add three random edges
        for _ in range(3):
            add_random_edge()
            actual = count_good_dungeons(game)
            self.assertEqual(3, actual)

        # Add four random edges
        for _ in range(4):
            add_random_edge()
            actual = count_good_dungeons(game)
            self.assertEqual(4, actual)

        # Add another random edge
        add_random_edge()
        actual = count_good_dungeons(game)
        self.assertEqual(3, actual)

        # Add two random edges
        for _ in range(2):
            add_random_edge()
            actual = count_good_dungeons(game)
            self.assertEqual(2, actual)

        # Add another random edge
        add_random_edge()
        actual = count_good_dungeons(game)
        self.assertEqual(1, actual)


if __name__ == '__main__':
    unittest.main()
