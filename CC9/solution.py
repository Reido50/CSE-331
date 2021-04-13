"""
Name: Reid Harry
Coding Challenge 9
CSE 331 Spring 2021
Professor Sebnem Onsay
"""

from typing import List, Tuple
from collections import deque

class Dungeon:
    """
    Represents a dungeon made of rooms connected by hallways
    Implemented as an adjacency matrix
    """

    __slots__ = ['adjacency_matrix']

    def __init__(self, rooms: List[int], hallways: List[Tuple[int, int]]) -> None:
        self.adjacency_matrix = [[0] * len(rooms) for _ in range(len(rooms))]
        for hall in hallways:
            self._add_connecting_hallway(*hall)

    def _add_connecting_hallway(self, start_room: int, end_room: int) -> None:
        """
        Adds a hallway to the dungeon
        :param start_room: start room
        :param end_room: end room
        :return: None
        """
        self.adjacency_matrix[start_room][end_room] = self.adjacency_matrix[end_room][start_room] = 1

    def get_connecting_rooms(self, current_room: int) -> List[int]:
        """
        Gets a list of rooms connected to the current room
        :param current_room: current room represented by an index in the matrix
        :return: List of connected, adjacent rooms
        """
        connecting_rooms = []
        for connected_room, required_stamina in enumerate(self.adjacency_matrix[current_room]):
            if required_stamina > 0:
                connecting_rooms.append(connected_room)
        return connecting_rooms

    def get_required_stamina(self, start_room: int, end_room: int) -> int:
        """
        Gets the required stamina between two edges
        :param start_room: First room at the end of a hallway
        :param end_room: Second room at the other end of a hallway
        :return: Stamina of hallway as an int
            will be 1 if the rooms are connected by a single hallway,
            0 if the rooms are not connected by a single hallway
        """
        return self.adjacency_matrix[start_room][end_room]


def dungeon_escape(dungeon: Dungeon, start_room: int, end_room: int,
                   stamina_limit: int) -> Tuple[List[int], int]:
    """
    REPLACE
    """
    # Create and populate dict visited[int, bool]
    visited = {}
    for i in range(len(dungeon.adjacency_matrix)):
        visited[i] = False
    visited[start_room] = True

    # Create and setup the bfs queue
    bfsqueue = deque()
    bfsqueue.append(start_room)

    # Value to track how much stamina we have used
    staminaused = 0

    # Loop for dfs
    while len(bfsqueue) != 0:
        cur = bfsqueue.popleft()
        if cur == end_room:

            break
        connectedrooms = dungeon.get_connecting_rooms(cur)
        for room in connectedrooms:
            if not visited[room]:
                bfsqueue.append(room)
                visited[room] = True
    
    