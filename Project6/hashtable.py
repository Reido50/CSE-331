"""
Project 6
CSE 331 S21 (Onsay)
Your Name
hashtable.py
"""

from typing import TypeVar, List, Tuple

T = TypeVar("T")
HashNode = TypeVar("HashNode")
HashTable = TypeVar("HashTable")


class HashNode:
    """
    DO NOT EDIT
    """
    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key: str, value: T, deleted: bool = False) -> None:
        self.key = key
        self.value = value
        self.deleted = deleted

    def __str__(self) -> str:
        return f"HashNode({self.key}, {self.value})"

    __repr__ = __str__

    def __eq__(self, other: HashNode) -> bool:
        return self.key == other.key and self.value == other.value

    def __iadd__(self, other: T) -> None:
        self.value += other


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity: int = 8) -> None:
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other: HashTable) -> bool:
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __str__(self) -> str:
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    __repr__ = __str__

    def _hash_1(self, key: str) -> int:
        """
        ---DO NOT EDIT---
        Converts a string x into a bin number for our hash table
        :param key: key to be hashed
        :return: bin number to insert hash item at in our table, None if key is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key: str) -> int:
        """
        ---DO NOT EDIT---
        Converts a string x into a hash
        :param key: key to be hashed
        :return: a hashed value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value

    def __len__(self) -> int:
        """
        Getter for the size in the HashTable
        :return: Size of the HashTable
        """
        return self.size

    def __setitem__(self, key: str, value: T) -> None:
        """
        Sets the value with an associated key in the HashTable
        :param key: The key we are hasing
        :param value: The associated value we are storing
        """
        self._insert(key, value)

    def __getitem__(self, key: str) -> T:
        """
        Looks up the value with an associated key in the HashTable
        :param key: The key we are searching for the associated value of
        """
        item = self._get(key)
        if item is None:
            raise KeyError('Given key not found in hash table')
        return item.value

    def __delitem__(self, key: str) -> None:
        """
        Deletes the value with an associated key in the HashTable
        :param key: The key we are deleting the associated value of
        """
        if self._get(key) is None:
            raise KeyError('Given key not found in hash table')
        self._delete(key)

    def __contains__(self, key: str) -> bool:
        """
        Determines if a node with the key denoted by the parameter exists in the table
        :param key: The key we are checking to be a part of the hash table
        :return: True if the key is in the hash table, false otherwise
        """
        return self._get(key) is not None

    def hash(self, key: str, inserting: bool = False) -> int:
        """
        Given a key string return an index in the hash table
        :param key: The key being used in our hash function
        :param inserting: Whether or not we are doing an insertion
        """
        i = 0
        while i < self.capacity:
            index = (self._hash_1(key) + i * self._hash_2(key)) % self.capacity
            if self.table[index] is None:
                # Hash index location is open, return index
                return index
            elif self.table[index].deleted:
                # Hash index location is open (Deleted element)
                if inserting:
                    return index
                i += 1
            elif self.table[index].key == key:
                # Hash index location holds the key, return index
                return index
            else:
                # Keep looking for a location
                i += 1

    def _insert(self, key: str, value: T) -> None:
        """
        Use the key and value parameters to add a HashNode to the hash table
        :param key: The key associated with the value we are storing
        :param value: The associated value we are storing
        """
        # Insert a node
        index = self.hash(key, True)
        if self.table[index] is not None:
            if self.table[index].key != key:
                self.size += 1
        else:
            self.size += 1
        self.table[index] = HashNode(key, value)

        # Grow if load factor is greater than 0.5
        if self.size / self.capacity >= 0.5:
            self._grow()

    def _get(self, key: str) -> HashNode:
        """
        Find the HashNode with the given key in the hash table
        :param key: The key we are looking up
        :return: HashNode with the key we looked up
        """
        index = self.hash(key, False)
        if self.table[index] is None:
            # Key was not found, return None
            return None
        if self.table[index].key == key:
            # Key was found, return node
            return self.table[index]

    def _delete(self, key: str) -> None:
        """
        Removes the HashNode with the given key from the hash table
        :param key: The key of the Node we are looking to delete
        """
        found = self._get(key)
        found.key = None
        found.value = None
        found.deleted = True
        self.size -= 1

    def _grow(self) -> None:
        """
        Double the capacity of the existing hash table
        """
        # Update capacity and make new table
        self.capacity *= 2
        newtable = [None] * self.capacity

        # Update prime_index
        for i in range(len(self.primes)):
            if self.primes[i] > self.capacity:
                break
            self.prime_index = i

        # Rehash all nodes
        for node in self.table:
            if node is None:
                # Empty element (No need to add to new table)
                continue
            elif node.deleted:
                # Deleted element (not need to add to new table)
                continue
            else:
                # Must rehash
                i = 0
                while i < self.capacity:
                    index = (self._hash_1(node.key) + i * self._hash_2(node.key)) % self.capacity
                    if newtable[index] is None:
                        # Hash index location is open, return index
                        newtable[index] = node
                        break
                    else:
                        # Keep looking for a location
                        i += 1
        # Replace current table with the bigger one
        self.table = newtable


    def update(self, pairs: List[Tuple[str, T]] = []) -> None:
        """
        Updates the hash table using an iterable of key value pairs
        :param pairs: List of tuple (key, value) being updated
        """
        # Insert each pair into the table
        for pair in pairs:
            self._insert(pair[0], pair[1])

    def keys(self) -> List[str]:
        """
        Makes a list that contains all of the keys in the table
        :return: List of the keys
        """
        keys = []
        for node in self.table:
            if node is not None:
                keys.append(node.key)
        return keys

    def values(self) -> List[T]:
        """
        Makes a list that contains all of the values in the table
        :return: List of the values
        """
        values = []
        for node in self.table:
            if node is not None:
                values.append(node.value)
        return values

    def items(self) -> List[Tuple[str, T]]:
        """
        Makes a list that contains all of the keys/values in the table
        :return: List of key/value pairs
        """
        items = []
        for node in self.table:
            if node is not None:
                items.append((node.key, node.value))
        return items

    def clear(self) -> None:
        """
        Should clear the table of HashNodes completely
        """
        for i in range(len(self.table)):
            self.table[i] = None
        self.size = 0


class CataData:
    def __init__(self) -> None:
        """
        ADD DOCSTRING HERE
        """
        pass

    def enter(self, idx: str, origin: str, time: int) -> None:
        """
        ADD DOCSTRING HERE
        """
        pass

    def exit(self, idx: str, dest: str, time: int) -> None:
        """
        ADD DOCSTRING HERE
        """
        pass

    def get_average(self, origin: str, dest: str) -> float:
        """
        ADD DOCSTRING HERE
        """
        pass
