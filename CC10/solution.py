"""
Reid Harry
Coding Challenge 10
CSE 331 Spring 2021
Professor Sebnem Onsay
"""
from CC10.game import Room, Game


def count_good_dungeons(game: Game) -> int:
    """
    Fill out doc-string
    """
    currentdungeon = 0
    dungeongoodness = {}
    visited = set()

    def DFS(room: Room, prev: Room):
        # Do a DFS on room and look for cycle
        visited.add(room.room_id)
        for adjroom in room.adjacent_rooms:
            if adjroom.room_id in visited:
                if prev is not None and prev.room_id != adjroom.room_id:
                    dungeongoodness[currentdungeon] = True
            else:
                DFS(adjroom, room)



    # Outer management loop
    for room in game.rooms:
        # Do a DFS on room to look for cycle
        if not room.room_id in visited:
            DFS(room, None)
            currentdungeon += 1

    # Add up number of good dungeons
    numgood = 0
    for dungeon in dungeongoodness:
        if dungeongoodness[dungeon]:
            numgood += 1

    return numgood
