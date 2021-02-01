"""
Name
Coding Challenge 2
CSE 331 Spring 2021
Reid Harry
"""
from typing import List, Tuple
from CC2.linked_list import DLLNode, LinkedList


def pokemon_machine(pokemon: LinkedList, orders: List[Tuple]) -> LinkedList:
    """
    Add, remove, and swap Pokemon in a pokemon DLL
    :param pokemon: A list of pokemon names represented as strings
    :param orders: List of tuples that represent actions
        add: Adds a pokemon to the pokemon DLL in a position (ex: ("add",37, "vulpix))
        remove: Removes a pokemon at a position (ex: ("remove",2))
        swap: Swaps two pokemon at two separate positions (ex: ("swap",37,157))
    """

    def add_pokemon(cur_node: DLLNode, added_pokemon: str) -> None:
        """
        Adds a pokemon after the given node
        :param cur_node: Node that will preceed the added pokemon
        :param added_pokemon: Pokemon to be added to the list
        """
        new_node = DLLNode(added_pokemon, None, cur_node)
        new_node.prev.nxt = new_node

        if cur_node is pokemon.tail:
            pokemon.tail = new_node
        else:
            new_node.nxt = cur_node.nxt
            new_node.nxt.prev = new_node
        pass

    def remove_pokemon(cur_node: DLLNode) -> None:
        """
        Removes the pokemon at the current node
        :param cur_node: Node to be removed
        """
        if cur_node is pokemon.head:
            pokemon.head = cur_node.nxt
        else:
            cur_node.prev.nxt = cur_node.nxt

        if cur_node is pokemon.tail:
            pokemon.tail = cur_node.prev
        else:
            cur_node.nxt.prev = cur_node.prev
        pass

    def swap_pokemon(first_node: DLLNode, second_node: DLLNode) -> None:
        """
        """
        pass

    for order in orders:
        if order[0] == "add":
            # Get cur_node
            cur_node = pokemon.head
            for i in range(order[1]):
                cur_node = cur_node.nxt
            # Add the pokemon after cur_node
            add_pokemon(cur_node, order[2])
        elif order[0] == "remove":
            # Get cur_node
            cur_node = pokemon.head
            for i in range(order[1]):
                cur_node = cur_node.nxt
            # Remove the pokemon at cur_node
            remove_pokemon(cur_node)
        elif order[0] == "swap":
            # Get first node
            # Get second node
            # Swap the pokemon at the first and second node
            print("swap")

    return pokemon
