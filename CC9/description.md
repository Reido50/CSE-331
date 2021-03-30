**CC9 - SS21 - I Want to Break Free!**
======================================

#### **Due: Tuesday, March 30th @ 11:59 pm**

_This is not a team project, do not copy someone else’s work._

**Introduction**
================

**![Valheim guide -- Where to find Surtling Cores and Burial Chambers](https://www.pcinvasion.com/wp-content/uploads/2021/02/Valheim-guide-where-to-find-Surtling-Cores-Burial-Chambers-.jpg)**

Welcome to the world of Valheim! You are the newest Viking to come and conquer this world full of monsters, bosses, and dungeons. You are particularly intrigued by the dungeons. However, many dungeons, especially those of the swamps, have proven to be complicated mazes of interconnected rooms and dead ends. This can get rather tedious really quickly.

Running into rooms you have already seen is time-consuming, and you can get lost quickly. So, you decide to write a mod that finds the exit of the dungeon in the given amount of stamina you currently possess. Beware though, Valheim is a game created by a team of 5 developers, and sometimes developers cut corners. There are miscellaneous rooms that are unreachable to the player, and you must be able to handle those scenarios.

(While the [5 developer team](https://www.theverge.com/2021/3/3/22311338/valheim-five-million-copies-sold-valve-steam-early-access-success#:~:text=The%20Swedish%20studio%20developed%20the,at%20one%20point%20last%20month.) is true, the miscellaneous rooms are not. That is purely for our story.)

**Challenge**
=============

**Overview**
------------

In this problem, you must find a path from a start room to an end room while only crossing through a limited amount of rooms. Both the start and end rooms are included in the stamina count. Some rooms will be unreachable, meaning they are a room surrounded by unavailable rooms on all sides, effectively blocked in, and some rooms will be easily reachable. Your solution must be able to handle both cases. 

You must implement the function **dungeon\_escape**. It uses the class **Dungeon** (a graph class) and its member functions to find a path used to escape your dungeon. 

_Modify the following function:_

**dungeon\_escape(dungeon: Dungeon, start: int, end: int, stamina\_limit: int) -> Tuple\[List\[int\], int\]:**

*   **dungeon: Dungeon:** The dungeon you are trying to escape
*   **start\_room: int:** The starting room of your dungeon, this integer directly correlates to an index in the adjacency\_matrix of **d****ungeon**
*   **end\_room: int:** The end room of your dungeon, this integer directly correlates to an index in the adjacency\_matrix of **dungeon**
*   **stamina\_limit: int:** The max amount of stamina you can use when trying to escape the dungeon. This is **NOT** the number of rooms you pass through, rather the number of hallways passed to get to your exit.
    *   The stamina limit does **NOT** require you to find the shortest path! You just need to find a path uses a stamina amount less than or equal to the stamina limit.
*   **Return:** A tuple where the list of integers is your path, where the integers refer to rooms in your dungeon, and an integer representing the length (stamina used) of the path
    *   Your final path **MUST** contain both the start and endpoints, one at each end of your path
        *   Ex: start = 5 and end = 12, the path must look like \[5, ...., 12\] OR \[12, ...., 5\]
    *   The stamina used is **NOT** equal to the number of rooms in your path, it is equal to the number of hallways or room connections in your final path
*   **Time Complexity:** O(R + H) where R is the number of rooms in the dungeons and H is the number of halls connecting all the rooms
*   **Space Complexity:** O(R)
    *   **NOTE:** This is only the space complexity you use to implement your solution. The space complexity of the dungeon is O(R^2) and is not counted towards your space complexity, so any object passed into this function does not count towards your final space complexity. However, if you were to make a copy of your dungeon in your solution, that would run your used space to be O(R^2) which is unacceptable. 

_Do NOT modify the following functions. You however will need to use them in your solution._

**class Dungeon:**

This class represents a dungeon object, implemented using an adjacency matrix. Rooms in the dungeon are represented as a row or column in the matrix and hallways connecting rooms are represented as a 1 value in the matrix. For example, a connection between room 0 and room 5 is represented by a 1 at index 5 in row 0 and at index 0 in row 5 (as there is no given direction between rooms, we can go from room 5 to room 0 and from room 0 to room 5).

*   **Attributes:**
    *   **adjacency\_matrix: List\[List\[int\]\]:** a matrix representing hallways between rooms
        *   Ex: a 1 at adjacency\_matrix\[5\]\[10\] indicates a hallway between rooms 5 and 10. Because Dungeons have no direction between rooms (you can walk from room 5 to room 10 and from room 10 to room 5), there should also be a 1 at adjacency\_matrix\[10\]\[5\].
*   **\_\_init\_\_(self, rooms: List\[int\], hallways: List\[Tuple\[int, int\]\]) -> None:**
    *   Constructs a Dungeon instance
    *   For the self.\_add\_connecting\_hallway(\*hall) line, the asterisk indicates [unpacking](https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/). How this works, is that the function \_add\_connecting\_hallway takes 2 parameters and I know that hall is a tuple containing two items. The asterisk indicates that you can unpack each item into its respective function parameter. i.e. the item at index 0 in the tuple becomes the first parameter of the function and the item at index 1 in the tuple becomes the second parameter of the function.
    *   **rooms: List\[int\]:** a list of all the rooms in the dungeon
        *   **Note:** the list of rooms will be a consecutive list of integers starting at 0
    *   **hallways: List\[Tuple\[int, int\]\]:** a list of tuples where the tuple represents the hallway connection between two rooms
    *   **Return:** None
*   **\_add\_connecting\_hallway(self, start\_room: int, end\_room: int) -> None:**
    *   A protected function that adds a hallway between two rooms
    *   **start\_room: int:** the first room in this hallway connection
    *   **end\_room: int:** the second room in this hallway connection
    *   **Return:** None
*   **get\_connecting\_rooms(self, current\_room: int) -> List(int):**
    *   Gets all the rooms connected to the current room
    *   **current\_room: int:** the room we are trying to find all connections too
    *   **Return:** None
*   **get\_required\_stamina(self, start\_room: int, end\_room: int) -> int:**
    *   Gets the stamina required to go from two connected rooms
    *   **start\_room: int:** the first room in this hallway connection
    *   **end\_room: int:** the second room in this hallway connection
    *   **Return:** the required stamina to go between the two rooms

**Guarantees**:

*   The start room will always be a different room from the end room
*   The start and end rooms will always be valid rooms in the dungeon
*   stamina\_limit >= 0
*   A room cannot have a pathway to itself

**Examples**:

**Ex 1:![ex1.png](https://s3.amazonaws.com/mimirplatform.production/files/fbbce083-cdc1-451e-8b64-1972a74bbec9/ex1.png)**

The adjacency matrix for example 1 would be

              0  1  2  3  4     
          0 \[\[0, 0, 0, 0, 1\]  
          1  \[0, 0, 1, 1, 1\]  
          2  \[0, 1, 0, 1, 1\]  
          3  \[0, 1, 1, 0, 1\]  
          4  \[1, 1, 1, 1, 0\]\] 

Notice how the diagonals of this matrix are all zeros since a room cannot have a loop to itself. Also, note the matrix is symmetric (its transpose is equal to itself) which means A\[i\]\[j\] = A\[j\]\[i\]!

We start at room 1 in our dungeon and want to end at room 0. Let us say we have a stamina of 10, so going from room 1 to room 0 is easily reachable with our stamina. There are also many different paths that one could take to get from room 1 to 0. 

All acceptable paths include: (1, 2, 3, 4, 0), (1, 3, 2, 4, 0), (1, 2, 4, 0), (1, 3, 4, 0), (1, 4, 0). Your returned used stamina would be 4 for paths (1, 2, 3, 4, 0) and (1, 3, 2, 4, 0), 3 for paths (1, 2, 4, 0) and (1, 3, 4, 0), and the used stamina will be 2 for path (1, 4, 0). **Recall:** the used stamina is **NOT** how many rooms you passed through, it is how many "hallways" you have passed to get from room to room.

All of the above paths have a stamina of less than 10 and are connected paths from room 1 to room 0. The above paths can also be reversed. i.e. (1, 2, 4, 0) -> (0, 4, 2, 1). Both are acceptable answers. 

**Ex 2:**

 ![ex2.png](https://s3.amazonaws.com/mimirplatform.production/files/db6d7b41-c364-4270-ae82-9803eca915a9/ex2.png)

The adjacency matrix for example 2 would be

             0  1  2  3  4  5  
         0 \[\[0, 1, 1, 0, 0, 0\]  
         1  \[1, 0, 0, 1, 0, 0\]  
         2  \[1, 0, 0, 1, 1, 0\]  
         3  \[0, 1, 1, 0, 0, 0\]  
         4  \[0, 0, 1, 0, 0, 0\]  
         5  \[0, 0, 0, 0, 0, 0\]\] 

Our start room is room 4 and our end room is room 5 and our stamina is 10. You may notice that room 5 is not connected to any rooms in our dungeon, so we cannot exit this dungeon. The return will be an empty list to represent an empty path and used stamina of 0 since we cannot exit the dungeon.

**Ex 3:** ![ex3.png](https://s3.amazonaws.com/mimirplatform.production/files/4f040ef8-4314-4790-b4ed-964a7529183a/ex3.png)

The adjacency matrix for example 3 would be

              0  1  2  3  4  5  
         0  \[\[0, 1, 1, 0, 0, 0\]  
         1   \[1, 0, 0, 1, 0, 0\]  
         2   \[1, 0, 0, 0, 1, 0\]  
         3   \[0, 1, 0, 0, 0, 1\]  
         4   \[0, 0, 1, 0, 0, 1\]  
         5   \[0, 0, 0, 1, 1, 0\]\] 

Our start room is room 0 and our end room is room 5. However, this time our stamina is 1. There is no possible path from room 0 to room 5 only passing through 1 hallway. With the current stamina, only rooms 1 or 2 could be reached as that is passing through 1 hallway. So the return will be an empty list and the used stamina will be 0 since there is no way to exit the dungeon with the given stamina.

Tips, Tricks, and Notes
=======================

*   There are many search and graph traversal algorithms. [One of them](https://neo4j.com/blog/graph-search-algorithm-basics/) might be useful for you.
*   Remember, you can return ANY path from start to finish so long as it doesn't surpass the stamina limit!
*   While the stamina limit is large for test cases where stamina is not being tested, the stamina limit may be too small if you were to loop through the same room multiple times. i.e. having a path like (0, 1, 2, 3, 1, 4). There is a cycle (1, 2, 3, 1) that does not need to be included. (0, 1, 4) could have been returned and that would be an acceptable path. So while the the found path does not have to be the shortest path, you may want to somehow keep track of which rooms you have visited so you do not create cycles in your path.
*   Your returned path does not have to be from start to finish, it could be from finish to start. As long as your path is a valid, connected path from one room to the other, it will pass the test cases. See Ex. 1.
*   Some test cases used a dungeon generator based on [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). The code used to create those dungeons are included (written by Andy Wilson).

**Submission**
==============

**Deliverables**
----------------

Be sure to upload the following deliverables in a .zip folder to Mimir by 11:59 PM Eastern Time on **Tuesday** **3/30/2021**.

Your .zip folder can contain other files (for example, description.md and tests.py), but must include (at least) the following:

    CC9.zip  
        |— CC9/  
        |— README.xml       (for coding challenge feedback)  
        |— \_\_init\_\_.py      (for proper Mimir testcase loading)  
        |— solution.py      (contains your solution source code)

**Grading**
-----------

The following 100-point rubric will be used to determine your grade on CC9:

*   Tests (65)
    *   00 - Coding Standard: \_\_/5
    *   01 - Basic: \_\_/10
    *   02 - Unreachable Exits: \_\_/15
    *   03 - Multiple Working Paths: \_\_/15
    *   04 - Comprehensive: \_\_/20
*   Manual (35)
    *   M1 - Time Complexity O(R + H): \_\_/15
    *   M2 - Space Complexity O(R): \_\_/15
    *   README.md is _completely_ filled out with (1) Name, (2) Feedback, (3) Time to Completion, (4) Citations, and (Difficulty): \_\_/5

Coding Challenge created by Jacob Caurdy and Olivia Mikola 

Dungeon generation code provided by Andy Wilson