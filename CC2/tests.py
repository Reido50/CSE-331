import unittest
import random
import pandas as pd
from typing import List, Tuple
from CC2.linked_list import LinkedList, DLLNode
from CC2.solution import pokemon_machine


# Thank you https://www.kaggle.com/mariotormo/complete-pokemon-dataset-updated-090420 for pokemon list
def generate_order(size: int, list_size: int, pokedex: List[str], seed: int = 331):
    """
    This is the function helping generate the order to add, remove, and
    swap pokemon in the computer
    :param size: Size of order
    :param list_size: Size of pokemon list
    :param pokedex: List of all pokemon
    :param seed: Random seed
    :return: The list of order
    """
    random.seed(seed)
    order_list = []
    current_position = 0
    for _ in range(size):
        order_number = random.randint(0, 331) % 3
        if order_number == 0:
            added_position = random.randint(max(0, current_position - 10),
                                            min(current_position + 20, list_size))
            added_pokemon = random.choice(pokedex)
            order_list.append(("add", added_position, added_pokemon))
            current_position = added_position
            list_size += 1
        elif order_number == 1 and list_size > 0:
            removed_position = random.randint(max(0, current_position - 10),
                                              min(current_position + 20, list_size - 1))
            order_list.append(("remove", removed_position))
            current_position = removed_position
            list_size -= 1
        else:
            first_position = random.randint(max(0, current_position - 10),
                                            min(current_position + 20, list_size - 1))
            current_position = first_position
            second_position = random.randint(max(0, current_position - 10),
                                             min(current_position + 20, list_size - 1))
            order_list.append(("swap", first_position, second_position))
    return order_list


def linked_list_to_list(linked_list: LinkedList):
    """
    DO NOT MODIFY
    Converting the linked list to list
    :return: list that contain the same elements as linked list
    """
    actual_list = []
    node = linked_list.head.nxt
    while node is not None:
        actual_list.append(node.val)
        node = node.nxt
    return actual_list


class CC2Tests(unittest.TestCase):
    def test_add(self):
        # adding front
        pokemon1 = ["Rhyperior", "Togekiss", "Dialga"]
        orders1 = [("add", 0, "Tyranitar"), ("add", 0, "Excadrill")]
        pokemon1 = LinkedList(pokemon1)
        actual = linked_list_to_list(pokemon_machine(pokemon1, orders1))
        expected = ["Excadrill", "Tyranitar", "Rhyperior", "Togekiss", "Dialga"]
        self.assertEqual(expected, actual)

        # adding between
        pokemon2 = ["Sceptile", "Blaziken", "Swampert"]
        orders2 = [("add", 1, "Torchic"), ("add", 3, "Mudkip")]
        pokemon2 = LinkedList(pokemon2)
        actual = linked_list_to_list(pokemon_machine(pokemon2, orders2))
        expected = ["Sceptile", "Torchic", "Blaziken", "Mudkip", "Swampert"]
        self.assertEqual(expected, actual)

        # adding back
        pokemon3 = ["Beautifly", "Butterfree", "Luxio"]
        orders3 = [("add", 3, "Beedrill"), ("add", 4, "Pidgeot")]
        pokemon3 = LinkedList(pokemon3)
        actual = linked_list_to_list(pokemon_machine(pokemon3, orders3))
        expected = ["Beautifly", "Butterfree", "Luxio", "Beedrill", "Pidgeot"]
        self.assertEqual(expected, actual)

        # adding comprehensive
        pokemon4 = []
        orders4 = [("add", 0, "Charizard"), ("add", 1, "Hydreigon"), ("add", 1, "Gyrados")]
        pokemon4 = LinkedList(pokemon4)
        actual = linked_list_to_list(pokemon_machine(pokemon4, orders4))
        expected = ["Charizard", "Gyrados", "Hydreigon"]
        self.assertEqual(expected, actual)

    def test_remove(self):
        # remove front
        pokemon1 = ["Rhyperior", "Togekiss", "Dialga"]
        orders1 = [("remove", 0), ("remove", 0)]
        pokemon1 = LinkedList(pokemon1)
        actual = linked_list_to_list(pokemon_machine(pokemon1, orders1))
        expected = ["Dialga"]
        self.assertEqual(expected, actual)

        # remove between
        pokemon2 = ["Beautifly", "Butterfree", "Luxio", "Beedrill", "Pidgeot"]
        orders2 = [("remove", 1), ("remove", 2)]
        pokemon2 = LinkedList(pokemon2)
        actual = linked_list_to_list(pokemon_machine(pokemon2, orders2))
        expected = ["Beautifly", "Luxio", "Pidgeot"]
        self.assertEqual(expected, actual)

        # remove back
        pokemon3 = ["Charizard", "Mew", "Mew-Two", "Bulbasaure", "Venusaur"]
        orders3 = [("remove", 4), ("remove", 3)]
        pokemon3 = LinkedList(pokemon3)
        actual = linked_list_to_list(pokemon_machine(pokemon3, orders3))
        expected = ["Charizard", "Mew", "Mew-Two"]
        self.assertEqual(expected, actual)

        # remove comprehensive
        pokemon4 = ['Bulbasaur', 'Ivysaur', 'Venusaur',
                    'Charmander', 'Charmeleon', 'Charizard',
                    'Squirtle', 'Wartortle', 'Blastoise']
        orders4 = [("remove", 4), ("remove", 3), ("remove", 0), ("remove", 1), ("remove", 4), ("remove", 0),
                   ("remove", 2), ("remove", 1), ("remove", 0)]
        pokemon4 = LinkedList(pokemon4)
        actual = linked_list_to_list(pokemon_machine(pokemon4, orders4))
        expected = []
        self.assertEqual(expected, actual)

    def test_swap(self):
        # Swap front with either between or end
        pokemon1 = ['Grookey', 'Sobble', 'Scorbunny']
        orders1 = [('swap', 0, 2), ('swap', 0, 1)]
        pokemon1 = LinkedList(pokemon1)
        actual = linked_list_to_list(pokemon_machine(pokemon1, orders1))
        expected = ['Sobble', 'Scorbunny', 'Grookey']
        self.assertEqual(expected, actual)

        # Swap back between with either front or between
        pokemon2 = ["Charizard", "Bulbasaure", "Venusaur"]
        orders2 = [('swap', 2, 0), ('swap', 2, 1)]
        pokemon2 = LinkedList(pokemon2)
        actual = linked_list_to_list(pokemon_machine(pokemon2, orders2))
        expected = ["Venusaur", "Charizard", "Bulbasaure"]
        self.assertEqual(expected, actual)

        # Swap between with between
        pokemon3 = ['Grookey', 'Sobble', 'Scorbunny', "Charizard", "Bulbasaure", "Venusaur", "Pikachu"]
        orders3 = [('swap', 3, 2), ('swap', 3, 4), ('swap', 1, 5)]
        pokemon3 = LinkedList(pokemon3)
        actual = linked_list_to_list(pokemon_machine(pokemon3, orders3))
        expected = ['Grookey', 'Venusaur', 'Charizard', "Bulbasaure", "Scorbunny", "Sobble", "Pikachu"]
        self.assertEqual(expected, actual)

    def test_example(self):
        pokemon1 = ["Charizard", "Bulbasaur", "Venusaur"]
        orders1 = [("add", 1, "Mew"), ("add", 2, "Mew-Two"), ("remove", 3)]
        pokemon1 = LinkedList(pokemon1)
        actual = linked_list_to_list(pokemon_machine(pokemon1, orders1))
        expected = ["Charizard", "Mew", "Mew-Two", "Venusaur"]
        self.assertEqual(expected, actual)

        pokemon2 = ["Kyoqre", "Groudon", "Rayguaza"]
        orders2 = [("swap", 0, 2), ("remove", 0), ("add", 0, "Pikachu")]
        pokemon2 = LinkedList(pokemon2)
        actual = linked_list_to_list(pokemon_machine(pokemon2, orders2))
        expected = ["Pikachu", "Groudon", "Kyoqre"]

        self.assertEqual(expected, actual)

    def test_small_case_comprehensive(self):
        random.seed(3310)

        pokedex = pd.read_csv("pokedex.csv").name.tolist()
        pokemon1 = random.choices(pokedex, k=20)
        orders1 = generate_order(20, len(pokemon1), pokedex)
        pokemon1 = LinkedList(pokemon1)
        actual = linked_list_to_list(pokemon_machine(pokemon1, orders1))
        expected = ['Medicham', 'Drampa', 'Bagon', 'Hypno', 'Mega Scizor', 'Zygarde Complete Forme', 'Xurkitree',
                    'Clefairy', 'Lycanroc Midnight Form', 'Horsea', 'Type: Null', 'Togetic', 'Stufful', 'Grimmsnarl',
                    'Bounsweet', 'Golbat', 'Polteageist', 'Meowstic Male']

        self.assertEqual(expected, actual)

        pokemon2 = random.choices(pokedex, k=25)
        orders2 = generate_order(15, len(pokemon2), pokedex, seed=662)
        pokemon2 = LinkedList(pokemon2)
        actual = linked_list_to_list(pokemon_machine(pokemon2, orders2))
        expected = ['Togedemaru', 'Grookey', 'Barbaracle', 'Golbat', 'Shedinja', 'Arceus', 'Sizzlipede',
                    'Feraligatr', 'Lampent', 'Stunky', 'Mandibuzz', 'Omastar', 'Omastar', 'Applin', 'Happiny',
                    'Smeargle', 'Togepi', 'Seadra', 'Exeggutor', 'Lombre', 'Larvitar', 'Galarian Mr. Mime', 'Arctozolt',
                    'Yungoos', 'Magikarp', 'Gogoat']

        self.assertEqual(expected, actual)

    def test_large_case_comprehensive(self):
        random.seed(3311)
        pokedex = pd.read_csv("pokedex.csv").name.tolist()

        pokemon1 = random.choices(pokedex, k=100)
        orders1 = generate_order(120, len(pokemon1), pokedex, seed=1234)
        pokemon1 = LinkedList(pokemon1)
        actual = linked_list_to_list(pokemon_machine(pokemon1, orders1))
        expected = ['Pineco', 'Boltund', 'Alolan Rattata', 'Butterfree', 'Phantump', 'Natu',
                    'Gallade', 'Mega Gallade', 'Kabutops', 'Throh', 'Mega Rayquaza', 'Solgaleo', 'Noivern', 'Mr. Rime',
                    'Servine', 'Shellder', 'Kadabra', 'Torchic', 'Meloetta Aria Forme', 'Klang', 'Krabby', 'Rufflet',
                    'Pachirisu', 'Vanilluxe', 'Torkoal', 'Mega Gengar', 'Mega Pidgeot', 'Pikachu', 'Mega Glalie',
                    'Psyduck', 'Appletun', 'Sunkern', 'Bidoof', 'Exploud', 'Pyukumuku', 'Sentret', 'Morgrem',
                    'Talonflame', 'Cufant', 'Tynamo', 'Combusken', 'Furret', 'Lanturn', 'Regice', 'Tranquill',
                    'Pansage', 'Houndoom', 'Weepinbell', 'Eevee', 'Bonsly', 'Spinarak', 'Eelektross', 'Sizzlipede',
                    'Roserade', 'Primeape', 'Bronzong', 'Gourgeist Super Size', 'Girafarig', 'Wartortle', 'Ambipom',
                    'Ivysaur', 'Shinx', 'Natu', 'Sizzlipede', 'Rapidash', 'Golduck', 'Pyukumuku', 'Vanillite', 'Kabuto',
                    'Deoxys Defense Forme', 'Sunkern', 'Slowbro', 'Dawn Wings Necrozma', 'Tsareena', 'Mega Latias',
                    'Dreepy', 'Ralts', 'Frosmoth', 'Bagon', 'Throh', 'Palkia', 'Roselia', 'Sandaconda', 'Arcanine',
                    'Lucario', 'Glaceon', 'Chewtle', 'Relicanth', 'Chespin', 'Wooper', 'Centiskorch', 'Blacephalon',
                    'Perrserker', 'Alolan Sandslash', 'Swanna', 'Duskull', 'Zigzagoon', 'Alolan Sandshrew',
                    'Galarian Linoone', 'Mega Swampert', 'Aerodactyl', 'Rolycoly', 'Shroomish', 'Lunatone', 'Gible',
                    'Palossand']
        self.assertEqual(expected, actual)

        pokemon2 = random.choices(pokedex, k=200)
        orders2 = generate_order(500, len(pokemon2), pokedex, seed=11235)
        pokemon2 = LinkedList(pokemon2)
        actual = linked_list_to_list(pokemon_machine(pokemon2, orders2))
        expected = ['Wormadam Sandy Cloak', 'Beheeyem', 'Galvantula', 'Dreepy', 'Komala', 'Petilil',
                    'Persian', 'Lickilicky', "Oricorio Pa'u Style", 'Chandelure', 'Melmetal', 'Pyroar',
                    "Oricorio Pa'u Style", 'Petilil', 'Haxorus', 'Exeggutor', 'Eternatus Eternamax',
                    'Shaymin Land Forme', 'Tympole', 'Own Tempo Rockruff', 'Nidoqueen', 'Persian', 'Wailmer',
                    'Cutiefly', 'Mega Banette', 'Seismitoad', 'Lotad', 'Baltoy', 'Hoothoot', 'Boltund', 'Croagunk',
                    'Aegislash Shield Forme', 'Swampert', 'Panpour', 'Frosmoth', 'Ekans', 'Avalugg', 'Trumbeak',
                    'Makuhita', 'Cherubi', 'Poliwrath', 'Flabébé', 'Gligar', 'Morpeko Hangry Mode', 'Ekans',
                    'Chesnaught', 'Simipour', 'Wynaut', 'Growlithe', 'Beedrill', 'Binacle', 'Crabrawler', 'Audino',
                    'Froslass', 'Chansey', 'Mr. Rime', 'Joltik', 'Lugia', 'Greninja', 'Sinistea', 'Drednaw', 'Boldore',
                    'Volbeat', 'Black Kyurem', 'Ursaring', 'Mega Banette', 'Mega Sharpedo', 'Celesteela', 'Houndour',
                    'Mega Gallade', 'Sandshrew', 'Servine', 'Wailmer', 'Vikavolt', 'Sceptile', 'Oricorio Pom-Pom Style',
                    'Stantler', 'Shelmet', 'Snorlax', 'Dreepy', 'Flareon', 'Mega Venusaur', 'Milcery', 'Accelgor',
                    'Pineco', 'Primal Groudon', 'Mega Mewtwo X', 'Doduo', 'Landorus Therian Forme', 'Meditite',
                    'Froakie', 'Diancie', 'Duskull', 'Cherubi', 'Roggenrola', 'Combee', 'Mothim', 'Rayquaza',
                    'White Kyurem', 'Chespin', 'Venipede', 'Zweilous', 'Mega Abomasnow', 'Luxray', 'Watchog',
                    "Galarian Farfetch'd", 'Castform', 'Ponyta', 'Palkia', 'Noivern', 'Magcargo', 'Joltik', 'Psyduck',
                    'Crawdaunt', 'Sceptile', 'Toxicroak', 'Kecleon', 'Dewpider', 'Audino', 'Galvantula', 'Dreepy',
                    'Kricketot', 'Appletun', 'Raboot', 'Doduo', 'Zygarde Complete Forme', 'Oshawott', 'Poliwag',
                    'Porygon2', 'Pheromosa', 'Kabuto', 'Mega Aerodactyl', 'Corviknight', 'Mantine', 'Mega Pinsir',
                    'Vanillite', 'Woobat', 'Clefairy', 'Noibat', 'Galarian Corsola', 'Ralts', 'Galarian Linoone',
                    'Munna', 'Mega Metagross', 'Cutiefly', 'Pidove', 'Tangela', 'Klinklang', 'Grumpig', 'Claydol',
                    'Carnivine', 'Frogadier', 'Vikavolt', 'Suicune', 'Seedot', 'Kyurem', 'Mega Scizor', 'Bidoof',
                    'Regice', 'Marowak', 'Shiinotic', 'Alolan Golem', 'Sceptile', 'Lapras', 'Abomasnow', 'Tympole',
                    'Lurantis', 'Bastiodon', 'Alolan Raichu', 'Ho-oh', 'Spiritomb', 'Pheromosa', 'Arceus', 'Frillish',
                    'Tropius', 'Emolga', 'Glaceon', 'Spoink', 'Taillow', 'Beheeyem', 'Steelix', 'Machamp', 'Luxray',
                    'Buneary', 'Castform Snowy Form', 'Electrike', 'Chespin', 'Uxie', 'Poipole', 'Anorith',
                    'Thundurus Therian Forme', 'Axew', 'Hakamo-o', 'Spritzee', 'Raikou', 'Lapras', 'Sharpedo',
                    'Darmanitan Zen Mode', 'Tsareena', 'Swoobat', 'Phantump', 'Celesteela', 'Amaura',
                    'Oricorio Pom-Pom Style', 'Oricorio Pom-Pom Style', 'Mega Tyranitar', 'Galarian Zigzagoon']
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
