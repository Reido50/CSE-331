import random
from copy import deepcopy


class DungeonGenerator:
    def __init__(self, width: int, height: int, fill_percent: int = 65, life_version: int = 2):
        self.width = width
        self.height = height

        self.fill_percent = fill_percent

        self.dungeon_map = []
        for y in range(self.height):
            row_list = []
            for x in range(self.width):
                row_list.append(0)
            self.dungeon_map.append(row_list)

        self.random_fill()

        for _ in range(5):
            if life_version == 1:
                self.dungeon_map = self.perform_life_version_1()
            elif life_version == 2:
                self.dungeon_map = self.perform_life_version_2()

        self.number_of_rooms = self.count_rooms()

        """
        width = 4
        height = 3
        
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
         
        which is map[height][width] or map[y][x]
        
           0   1   2   3
        [| - | - | - | - |   
         | 0 | 0 | 0 | 0 |   0
         | 0 | 0 | 0 | 0 |   1
         | 0 | 0 | 0 | 0 |   2
         | - | - | - | - |]
         
         which is map[width][height] or map[x][y]
        """

    def __str__(self):
        string = ""
        for y in range(self.height):
            for x in range(self.width):
                room_type = self.dungeon_map[y][x]
                string += "W" if room_type == 1 else "-"
            string += "\n"
        return string

    __repr__ = __str__

    def count_rooms(self):
        walls = 0
        for col in self.dungeon_map:
            walls += sum(col)
        return (self.width * self.height) - walls

    def get_connections(self):
        connections = set()
        for x in range(self.width):
            for y in range(self.height):
                # Don't care about connections between walls
                if self.dungeon_map[y][x]:
                    continue

                current_location = self.width * y + x

                if y != 0 and not self.dungeon_map[y - 1][x]:
                    top_location = self.width * (y - 1) + x
                    connections.add((current_location, top_location))
                if y != self.height - 1 and not self.dungeon_map[y + 1][x]:
                    bottom_location = self.width * (y + 1) + x
                    connections.add((current_location, bottom_location))
                if x != 0 and not self.dungeon_map[y][x - 1]:
                    left_location = self.width * y + x - 1
                    connections.add((current_location, left_location))
                if x != self.width - 1 and not self.dungeon_map[y][x + 1]:
                    right_location = self.width * y + x + 1
                    connections.add((current_location, right_location))

        return list(connections)

    def get_surrounding_walls(self, x: int, y: int) -> int:
        wall_count: int = 0
        for x_neighbor in range(x - 1, x + 2):
            for y_neighbor in range(y - 1, y + 2):
                if 0 <= x_neighbor < self.width and 0 <= y_neighbor < self.height:
                    if x_neighbor != x or y_neighbor != y:
                        wall_count += self.dungeon_map[y_neighbor][x_neighbor]
                else:
                    wall_count += 1

        return wall_count

    def random_fill(self) -> None:
        for x in range(self.width):
            for y in range(self.height):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    self.dungeon_map[y][x] = 1
                else:
                    # random_number = random.randint(0, 100)
                    self.dungeon_map[y][x] = 1 if random.randint(0, 100) < self.fill_percent else 0

    def perform_life_version_1(self):
        new_map = deepcopy(self.dungeon_map)
        for x in range(self.width):
            for y in range(self.height):
                wall_count: int = self.get_surrounding_walls(x, y)
                new_map[y][x] = 1 if wall_count > 4 else 0
        return new_map

    def perform_life_version_2(self):
        new_map = deepcopy(self.dungeon_map)
        for x in range(self.width):
            for y in range(self.height):
                wall_count: int = self.get_surrounding_walls(x, y)
                living: int = self.dungeon_map[y][x]

                if living and wall_count < 2:
                    new_map[y][x] = 0
                elif living and (wall_count == 2 or wall_count == 3):
                    pass  # stays alive
                elif living and wall_count > 3:
                    new_map[y][x] = 0
                elif not living and wall_count == 3:
                    new_map[y][x] = 1

        return new_map


print(DungeonGenerator(10, 10))
