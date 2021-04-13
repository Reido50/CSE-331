"""
Lukas Richters & Sean Nguyen
Inspired by: Anna De Biasi & Andrew McDonald
CC11 - Tries - Solution Code
CSE 331 Spring 2021
Professor Sebnem Onsay
"""

from __future__ import annotations
from typing import List
from collections import defaultdict


class Node:
    """
    The node class is used to implement a trie.
    """

    __slots__ = ["children", "is_end"]

    def __init__(self) -> None:
        """
        Constructs a Node.
        """
        self.children = defaultdict(Node)
        self.is_end = False

    def __str__(self) -> str:
        """
        Returns a string representation of the node.
        """
        return "Node"

    def __repr__(self) -> str:
        """
        Returns a string representation of the node.
        """
        return str(self)


class Trie:
    """
    A trie is a type of tree data structure designed to allow for similar functionality to a
    Python dictionary.
    """

    __slots__ = ["root"]

    def __init__(self) -> None:
        """
        Initializes a root and a size.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        :param word: the word to insert.
        :return: None
        """

        # If no word is given, nothing to insert.
        if len(word) == 0:
            return
        # Get the root node.
        node = self.root

        # Iterate through each character in the word to set the given value.
        for char in word:
            node = node.children[char]

        # Mark the end of the word
        node.is_end = True

    def __str__(self) -> str:
        """
        Returns a string representation of the trie.
        :return: None
        """

        def pretty_print(node: Node, prefix: str, string: str) -> str:

            for child, c_node in node.children.items():
                if c_node.is_end > 0:
                    string += f"{prefix}{child}, "
                else:
                    string = pretty_print(c_node, prefix + child, string)

            return string

        return pretty_print(self.root, '', 'Trie<')[:-2] + '>'

    def __repr__(self) -> str:
        """
        Returns a string representation of the trie.
        :return: None
        """
        return str(self)


def enemy_revealer(trie: Trie, key: str) -> List[str]:
    output = []
    root = trie.root
    nextpos = 0
    toremove = []

    def recur_helper(node: Node, c, seg: str, pos):
        # Manage current node
        output[pos] += c

        # Check if it's the end of the current word
        if node.is_end:
            if seg != "":
                toremove.append(output[pos])
            return

        # Continue through the word
        posinc = 0
        currentword = output[pos]
        for k in node.children:
            # Check if uppercase
            if k >= 'A' and k <= 'Z':
                if seg == "" or k != seg[0]:
                    toremove.append(currentword)
                    continue
            if posinc > 0:
                output.append(currentword)
            if seg != "" and k == seg[0]:
                recur_helper(node.children[k], k, seg[1:], pos + posinc)
            else:
                recur_helper(node.children[k], k, seg, pos + posinc)
            posinc += 1

    # Find first node
    for k in root.children:
        if key[0] == k:
            output.append("")
            recur_helper(root.children[k], k, key[1:], nextpos)
            break

    return output
