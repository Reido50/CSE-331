"""
Jacob Caurdy and Olivia Mikola
Coding Challenge 8 - Solution
CSE 331 Spring 2021
Professor Sebnem Onsay
"""

from typing import TypeVar, List, Tuple, Dict
import csv

Items = TypeVar("Items")
ItemInfo = TypeVar("ItemInfo")
Inventory = TypeVar("Inventory")


class ItemInfo:
    """ ItemInfo Class """
    def __init__(self, name: str, amount_in_stack: int) -> None:
        """
        Creates an instance of ItemInfo
        :param name: name of the item
        :param amount_in_stack: amount of an item in on stack
        """
        self.name: str = name
        self.amount_in_stack = amount_in_stack

    def __str__(self) -> str:
        """
        Provides a string representation of ItemInfo
        :return: string of ItemInfo
        """
        return f"<ItemInfo> {self.name}(stack: {self.amount_in_stack})"

    def __repr__(self) -> str:
        """
        Provides a string representation of ItemInfo
        :return: string of ItemInfo
        """
        return str(self)


class Items:
    """ Items Class """
    def __init__(self, items_to_register: List[Tuple[str, int]] = None, filename: str = None):
        """
        Creates an instance of Items
        """
        self.items: Dict[str: ItemInfo] = {}

        if items_to_register or filename:
            self._register(items_to_register, filename)

    def __str__(self) -> str:
        """
        Provides a string representation of Items
        :return: string of Items
        """
        string = "<Items> ["
        for item_name, item_info in self.items.items():
            string += f"{item_info}, "
        return string[:-2] + "]"

    def __repr__(self) -> str:
        """
        Provides a string representation of Items
        :return: string of Items
        """
        return str(self)

    def __getitem__(self, item_name: str):
        """
        Allows for indexing of the Items class
            Ex: i = Items()
                dirt = i["Dirt"]  # Assume dirt is already registered with some value
        :param item_name: item to find
        :return: the corresponding ItemInfo if itemName is in self.items, otherwise None
        """
        return self.items.get(item_name, None)

    def __setitem__(self, item_name: str, item_info: ItemInfo) -> None:
        """
        Allows for adding items to the Items class similar to adding key-value pairs to a dictionary
            Ex: i = Items()
                i["Dirt"] = 64
        :param item_name: item to add
        :param item_info: the corresponding value to add with the itemName
        :return: None
        """
        self.items[item_name] = item_info

    def _register(self, items: List[Tuple[str, int]], filename: str) -> None:
        """
        Adds many items to the Items.items dictionary
        :param items: List of tuples containing item information
        :param filename: Name of a .csv file that contains Items
        :return: None
        """
        items_to_add = items if items else []
        if filename:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row[0]:
                        items_to_add.append((row[0], int(row[1])))

        for item_name, amount_in_stack in items_to_add:
            self[item_name] = ItemInfo(item_name, amount_in_stack)


# Writing items into global Items constant from csv file
file = 'CC8/Minecraft_Items.csv'
ALL_ITEMS = Items(filename=file)