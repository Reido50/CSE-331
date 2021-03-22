"""
Reid Harry
Coding Challenge 8
CSE 331 Spring 2021
Professor Sebnem Onsay
"""

from typing import Set, Tuple, Dict
from CC8.InventoryItems import ItemInfo, ALL_ITEMS


class Bundle:
    """ Bundle Class """

    def __init__(self) -> None:
        """
        Initializes a Bundle object
        """
        self.bundle = dict()
        self.ratio = 0

    def to_set(self) -> Set[Tuple[str, int]]:
        """
        Converts the bundle to a set of tuples where the first index in the item name
        and the second index is the amount of that item in the bundle
        """
        # Create the output set
        output = set()

        # Fill output with tuples
        for key in self.bundle:
            output.add((key, self.bundle[key]))

        # Return output
        return output

    def add_to_bundle(self, item_name: str, amount: int) -> bool:
        """
        Adds an amount of an item to the bundle if possible
        """
        # Determine what fraction of a stack the added amount would take up
        frac = amount / ALL_ITEMS[item_name].amount_in_stack

        # Use frac to check if the add is possible
        if (frac + self.ratio) > 1:
            return False

        # Add the item
        self.ratio += frac
        if self.bundle.get(item_name) is None:
            self.bundle[item_name] = amount
        else:
            self.bundle[item_name] += amount
        return True

    def remove_from_bundle(self, item_name: str, amount: int) -> bool:
        """
        Removes an amount of an item from the bundle if possible
        """
        # Determines if there is enough in bundle to remove (if there is any)
        if self.bundle.get(item_name) is None:
            return False
        elif self.bundle[item_name] < amount:
            return False

        # Determine what fraction of a stack the removed amount takes up
        frac = amount / ALL_ITEMS[item_name].amount_in_stack

        # Remove the amount of the item
        self.bundle[item_name] -= amount
        self.ratio -= frac
        if self.bundle[item_name] == 0:
            # If removed all of the item, remove it from bundle
            self.bundle.pop(item_name)
        return True
