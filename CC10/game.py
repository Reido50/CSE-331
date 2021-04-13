from __future__ import annotations  # allow self-reference


class Room:
    """
    This class represents a room in the dungeon. It functions as a node/vertex in a graph and
    contains a room_id and a list of the rooms adjacent to it. It contains a function that
    will add adjacent rooms.
    """
    __slots__ = ["room_id", "adjacent_rooms", "_adj_rooms_set"]

    def __init__(self, name):
        """
        Constructs a room object with the given name as the room_id
        :param name: A variable that the room will use as it's ID. Must be hashable.
        """
        self.room_id = name
        self.adjacent_rooms = []
        self._adj_rooms_set = set()  # used to quickly lookup if the room already exists in the
                                     # adjacent list

    def __str__(self):
        """
        Creates a string representation of the room
        :return: A string representation of the room
        """
        return f"<Room>{self.room_id}(Adjacent Rooms: {self.adjacent_rooms})"

    __repr__ = __str__

    def __eq__(self, other):
        """
        Determines if two rooms are equal. Returns a bool representing if they are
        :param other: The second room to compare
        :return: A boolean representing if the two rooms are equal
        """
        return self.room_id == other.room_id and self.adjacent_rooms == other.adjacent_rooms

    def add_adjacent(self, adj_node: Room) -> bool:
        """
        If the given node is not already in the room’s adjacent rooms list then it will be added and
        True will be returned. Otherwise it will not be added and False will be returned
        :param adj_node: The room object to add to the room’s adjacent list
        :return: A boolean representing whether or not the room could be added to adjacent list
        """
        if adj_node.room_id not in self._adj_rooms_set:
            self.adjacent_rooms.append(adj_node)
            self._adj_rooms_set.add(adj_node.room_id)
            return True
        return False


class Game:
    """
    This class represents a graph implemented using an adjacency list and contains all of the rooms
    in the game. Rooms connect with one another to form dungeons as a result you may not be able
    to travel from one node across the graph to another because each dungeon is a “subgraph” in
    the overall game graph. This class contains the functions add_to_game and add_hallway.
    """
    __slots__ = ["rooms", "_rooms_set"]

    def __init__(self):
        """
        This function will initialize a Game object and take in nothing as input.
        """
        self.rooms = []
        self._rooms_set = set()  # used to quickly lookup if the room already exists in the graph

    def __str__(self):
        """
        Creates a string representation of the game
        :return: A string representation of the game
        """
        graph_str = ""
        for vert, i in enumerate(self.rooms):
            graph_str += str(vert)
            if i > 0:
                graph_str += "\n"

    __repr__ = __str__

    def add_to_game(self, room_id):
        """
        Creates and adds a new room to the game with the provided room_id. Will return True if the
        room_id already exists in the game, False otherwise.
        :param room_id: The value that will be used to create and identify the the new room
        :return: A bool representing whether or not the room could be added to the game’s room list
        """
        if room_id not in self._rooms_set:
            self.rooms.append(Room(room_id))
            self._rooms_set.add(room_id)
            return True
        return False

    def add_hallway(self, room1, room2) -> bool:
        """
        This function will add a hallway between the rooms with the given room_ids. If the hallway
        between the rooms could be created True will be returned, otherwise False will be returned.
        :param room1: The room_id of the first node to create the hallway to.
        :param room2: The room_id of the second node to create the hallway to.
        :return: A bool representing whether or not a hallway could be added connecting room1
        and room2.
        """
        start_room = None
        end_room = None
        for room in self.rooms:
            if room.room_id == room1:
                start_room = room
            if room.room_id == room2:
                end_room = room

        if start_room is not None and end_room is not None:
            return start_room.add_adjacent(end_room) and end_room.add_adjacent(start_room)
        return False
