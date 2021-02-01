# **CC2 - SS21- Bill’s PC**

**Due: Tuseday, February 2th, 11:59 pm**

_This is not a team project, do not copy someone else’s work._

# **Introduction**

![pokemon_pc.jpg](https://s3.amazonaws.com/mimirplatform.production/files/5eed942a-0398-4790-91c0-12064d85a635/pokemon_pc.jpg)

<span style="font-weight: 400;">Bill, a man known to all trainers in the Johto region, is looking for new people to help refine his pokemon storage system. He is the original creator of the system used to store excess Pokémon. His system allows trainers to easily store their Pokemon that won’t fit in their team and has enabled them to strive to “Catch’em Alll”.  </span>

<span style="font-weight: 400;">Bill has hired you to help him update his original storage system for a new region. Given that you recently started CSE 331 you decided to use a Doubly Linked List as your base data structure.</span>

# **Challenge**

## **Overview**

<span style="font-weight: 400;">You will create a function pokemon_machine that will utilize the provided DLL class. Your function should be able to add, remove, and swap pokemon in the pokemons DLL.</span>

<span style="font-weight: 400;">Your function will receive two lists,</span> <span style="font-weight: 400;">**pokemons** and **orders**. The **pokemons** list will hold a list of pokemon names represented as strings. This list will be edited **in-place** by your function, which means you are not to declare any additional lists in your function . And the **orders** list is a list of tuples. </span>

<span style="font-weight: 400;">The possible tuples are **add, remove, and swap**.</span>

<span style="font-weight: 400;">The **add** tuple will look as follows (“add”, integer index to insert the pokemon at, pokemon name) so an example would be (“add”, 37, “vulpix”).</span>

<span style="font-weight: 400;">The **remove** tuple will look as follows (“remove”, integer index of the pokemon that is to be removed) so an example would be (“remove”, 2).</span>

<span style="font-weight: 400;">And the **swap** tuple will look as follows (“swap”, integer index of the first pokemon to be swapped, integer index of the second pokemon to be swapped) so an example would be (“swap”, 37, 157).</span>

<span style="font-weight: 400;">Your goal is to use the orders list to edit the pokemons list using its list of commands. The edited pokemons list will then be returned from the function as a python list (use the linked_list_to_list function given in the DLL class).</span>

## Assignment Specifications

**Class DLLNode:**

_<span style="font-weight: 400;">DO NOT MODIFY the following attributes/functions</span>_

<span style="font-weight: 400;">This is doubly linked list node for providing you the linked list </span>

*   **Attributes**

*   **val: T**<span style="font-weight: 400;">: Value held by this node.</span> <span style="font-weight: 400;">Note that this may be any type, such as a</span> <span style="font-weight: 400;">str</span><span style="font-weight: 400;">,</span> <span style="font-weight: 400;">int</span><span style="font-weight: 400;">,</span> <span style="font-weight: 400;">float</span><span style="font-weight: 400;">,</span> <span style="font-weight: 400;">dict</span><span style="font-weight: 400;">, or a more complex object.</span>
*   **nxt : DLLNode**<span style="font-weight: 400;">:  Reference to the node that come after this node (may be None)</span>
*   **prev: DLLNode**<span style="font-weight: 400;">: Reference to the node that come before this node (may be None)</span>

*   **__init__(self, value: T, next: Node = None, prev: Node = None) -> None**

*   <span style="font-weight: 400;">Initialize doubly linked list node</span>
*   **val: T**<span style="font-weight: 400;">: Value held by this node.</span> <span style="font-weight: 400;">Note that this may be any type, such as a</span> <span style="font-weight: 400;">str</span><span style="font-weight: 400;">,</span> <span style="font-weight: 400;">int</span><span style="font-weight: 400;">,</span> <span style="font-weight: 400;">float</span><span style="font-weight: 400;">,</span> <span style="font-weight: 400;">dict</span><span style="font-weight: 400;">, or a more complex object.</span>
*   **nxt : DLLNode**<span style="font-weight: 400;">:  Reference to the node that come after this node (may be None)</span>
*   **prev: DLLNode**<span style="font-weight: 400;">: Reference to the node that come before this node (may be None)</span>
*   **return:** <span style="font-weight: 400;">None</span>

*   **__str__(self) -> str** <span style="font-weight: 400;">and</span> **__repr__(self) -> str**

*   <span style="font-weight: 400;">Represents the Doubly Linked List Node as string</span>
*   <span style="font-weight: 400;">This function might help you debug in Pycharm since it automatically calls this function to show the class for you</span>
*   **return:** <span style="font-weight: 400;">string representing the node</span>

**Class LinkedList:**

_<span style="font-weight: 400;">DO NOT MODIFY the following attributes/functions</span>_

<span style="font-weight: 400;">This is doubly linked list class will help you create the pokemon PC</span>

*   **Attributes**

*   *   **head: DLLNode**<span style="font-weight: 400;">: The head of doubly linked list  </span>
    *   **tail: DLLNode**<span style="font-weight: 400;">:  The tail of doubly linked list</span>
*   **__init__(self, value: T, next: Node = None, prev: Node = None) -> None**
    *   <span style="font-weight: 400;">Initialize doubly linked list</span>
    *   **container: List[T]**<span style="font-weight: 400;">: Container that contain the elements that will store in linked list</span>
    *   <span style="font-weight: 400;">To reduce bug and error of linked list head, this function constructs the None node to be the header node. The rest of linked list data will push after this node.</span> **Note** <span style="font-weight: 400;">that this node cannot be removed.</span>
    *   <span style="font-weight: 400;">If container is not None, this class will automatically generate the linked list that contains every element in the container.</span>
    *   **return:** <span style="font-weight: 400;">None</span>

*   **__str__(self) -> str** <span style="font-weight: 400;">and</span> **__repr__(self) -> str**
    *   <span style="font-weight: 400;">Represent Doubly Linked List Node as string</span>
    *   <span style="font-weight: 400;">This function might help you debug in Pycharm since it automatically calls this function to show the class for you</span>
    *   **return:** <span style="font-weight: 400;">string represented entire linked list</span>

_Modify the following functions and attributes_

**Solution File**

<span style="text-decoration: underline;">**_Warning: Do not convert  the LinkedList to a build-in python list. If you do that, you will lose all the points!_**</span>

*   <pre>**pokemon_machine(pokemon: LinkedList, orders: List[Tuple]) -> LinkedList:**</pre>

*   *   **pokemon: LinkedList**<span style="font-weight: 400;">**:** The first input is a linked list of strings representing pokemon’s name that are initially stored in the PC</span>

*   *   **orders: List[Tuple]**<span style="font-weight: 400;">: The second input is a python list of three possible commands used  to modify the PC</span>
        *   <span style="font-weight: 400;">The first command is for adding pokemon. This command is a tuple of length 3, where</span> 
            *   <span style="font-weight: 400;">Index 0 is a string, “add”</span>
            *   <span style="font-weight: 400;">Index 1 is an integer representing the position to put the new pokemon</span>
            *   <span style="font-weight: 400;">Index 2 is string represented the name of new pokemon</span>
            *   **Must call add_pokemon**
        *   <span style="font-weight: 400;">The second command is for removing pokemon. This command is a tuple of length 2, where</span>
            *   <span style="font-weight: 400;">Index 0 is a string, “remove”</span>
            *   <span style="font-weight: 400;">Index 1 an integer representing the position to remove pokemon from PC</span>
            *   **Must call remove_pokemon**
        *   <span style="font-weight: 400;">The last possible command is for swapping pokemons. This command is a tuple of length 3, where</span>
            *   <span style="font-weight: 400;">Index 0 is a string, “swap”</span>
            *   <span style="font-weight: 400;">Index 1 an integer representing the position of the first pokemon to swap</span>
            *   <span style="font-weight: 400;">Index 2 an integer representing the position of the second pokemon to swap</span>
            *   **Must call swap_pokemon**

*   *   <span style="font-weight: 400;">**Return:** A linked list of strings represents the current pokemons within the PC in the right order.</span>
    *   <span style="font-weight: 400;">**Time Complexity:** O(op). Where o is the length of the orders list and p is the length of the pokemon list</span>
*   **add_pokemon(cur_node: DLLnode, add_pokemon: str) -> None**
    *   <span style="font-weight: 400;">This is the **inner function** inside pokemon_machine.</span>
    *   <span style="font-weight: 400;">This function will add pokemon after the current node</span>
    *   **cur_node: str: **Current node to add the next pokemon after this node
    *   **add_pokemon: str:** Name of pokemon to add
    *   <span style="font-weight: 400;">**Return:** None</span>
    *   <span style="font-weight: 400;">**Time Complexity:** O(1)</span>
*   **remove_pokemon(cur_node: DLLnode) -> None**
    *   <span style="font-weight: 400;">This is the **inner function** inside pokemon_machine.</span>
    *   <span style="font-weight: 400;">This function will remove pokemon at the current node</span>
    *   **cur_node:** Current node to add the next pokemon after this node
    *   <span style="font-weight: 400;">Return: None</span>
    *   <span style="font-weight: 400;">Time Complexity: O(1)</span>
*   **swap_pokemon(first_node: DLLnode, second_node: DLLnode) -> None**
    *   <span style="font-weight: 400;">This is the **inner function** inside pokemon_machine.</span>
    *   <span style="font-weight: 400;">This function will swap pokemon between the first node and the second node</span>
    *   **first_node: DLLnode: **The first node to swap
    *   **second_node: DLLnode:** The second node to swap
    *   <span style="font-weight: 400;">return: None</span>
    *   <span style="font-weight: 400;">Time Complexity: O(1)</span>

#### **Guarantees**

*   <span style="font-weight: 400;">Every order is correct and the index of nearby orders will be closed to others.</span>

*   <span style="font-weight: 400;">The index of adding order is in the range of 0 to length of current list</span>
*   <span style="font-weight: 400;">The indexs of removing order and  swapping order is always less than the length of current list</span>

#### **Examples:**

_<span style="font-weight: 400;">Ex. 1:</span>_

**_pokemons:_** <span style="font-weight: 400;">["Charizard", "Bulbasaur", "Venusaur"]</span>

**_orders:_** <span style="font-weight: 400;">[("add", 1, "Mew"), ("add", 2, "Mew-Two"), ("remove", 3)]</span>

**Order 1**<span style="font-weight: 400;">: The first order in the list  [</span>**("add", 1, "Mew"),** <span style="font-weight: 400;">("add", 2, "Mew-Two"), ("remove", 3)] wants you to</span> **add Mew** <span style="font-weight: 400;">into the index 1\. This will add Mew after Charizard</span>

**List after this process**<span style="font-weight: 400;">: ["Charizard", “Mew”, "Bulbasaur", "Venusaur"]</span>

**Order 2**<span style="font-weight: 400;">: The second order in the list  [("add", 1, "Mew")</span>**,** **("add", 2, "Mew-Two")**<span style="font-weight: 400;">, ("remove", 3)] wants you to</span> **add Mew-Two** <span style="font-weight: 400;">into the index 2\. This will add Mew-Two after Mew</span>

**List after this process**<span style="font-weight: 400;">: ["Charizard", “Mew”, “Mew-Two”, "Bulbasaur", "Venusaur"]</span>

<span style="font-weight: 400;">Order 3: The third order in the list [("add", 1, "Mew")</span>**,** <span style="font-weight: 400;">("add", 2, "Mew-Two"),</span> **("remove", 3)**<span style="font-weight: 400;">] wants you to</span> **remove index 3 pokemon** <span style="font-weight: 400;">out of the list. This will remove Bulbasaur out of the list</span>

**List after this process**<span style="font-weight: 400;">: ["Charizard", “Mew”, “Mew-Two”, "Venusaur"]</span>

<span style="font-weight: 400;">After doing all the order, the PC contains ["Charizard", “Mew”, “Mew-Two”, "Venusaur"]</span>

_<span style="font-weight: 400;">Ex. 2:</span>_

**_pokemons:_** <span style="font-weight: 400;">["Kyogre", "Groudon", "Rayguaza"]</span>

**_orders:_**<span style="font-weight: 400;">[("swap", 0, 2), ("remove", 0), ("add", 0, "Pikachu")]</span>

**Order 1**<span style="font-weight: 400;">: The first order in the list [</span>**("swap", 0, 2)**<span style="font-weight: 400;">, ("remove", 0), ("add", 0, "Pikachu")] wants you to</span> **swap** <span style="font-weight: 400;">two pokemons</span> **between index 0 and index 2**<span style="font-weight: 400;">. This will swap Kyogre and Rayguaza.</span>

**List after this process**<span style="font-weight: 400;">: ["Rayguaza", "Groudon", "Kyogre"]</span>

**Order 2**<span style="font-weight: 400;">: The first order in the list [("swap", 0, 2),</span> **("remove", 0)**<span style="font-weight: 400;">, ("add", 0, "Pikachu")] wants you to</span> **remove index 0 pokemon** <span style="font-weight: 400;">out of the list. This will remove Rayguaza out of the list</span>

**List after this process**<span style="font-weight: 400;">: ["Groudon", "Kyogre"]</span>

<span style="font-weight: 400;">Order 3: The third order in the list   [("swap", 0, 2), ("remove", 0),</span> **("add", 0, "Pikachu")**<span style="font-weight: 400;">] wants you to</span> **add Pikachu** <span style="font-weight: 400;">into the index 0\. This will add Pikachu in the front of the list</span>

**List after this process**<span style="font-weight: 400;">: [“Pikachu”, "Groudon", "Kyogre"]</span>

<span style="font-weight: 400;">After doing all the order, the PC contains [“Pikachu”, "Groudon", "Kyogre"]</span>

# **Submission**

![Red_on_computer.png](https://s3.amazonaws.com/mimirplatform.production/files/6c41b8e0-2ad4-4e21-bb39-4eeddcab7990/Red_on_computer.png)

## **Deliverables**

<span style="font-weight: 400;">Be sure to upload the following deliverables in a .zip folder to Mimir by</span> **11:59PM** <span style="font-weight: 400;">Eastern Time on</span> **Tuesday, 02/02/2021**<span style="font-weight: 400;">.</span>

<span style="font-weight: 400;">Your .zip folder can contain other files (for example, description.md and tests.py), but must include (at least) the following:</span>

<span style="font-weight: 400;">CC2.zip</span>

<span style="font-weight: 400;">    |— CC2/</span>

<span style="font-weight: 400;">        |— README.xml       (for coding challenge feedback)</span>

<span style="font-weight: 400;">        |— __init__.py      (for proper Mimir testcase loading)</span>

<span style="font-weight: 400;">        |— linked_list.py   (contains linked list functions)</span>

<span style="font-weight: 400;">        |— pokedex.csv</span> <span style="font-weight: 400;">    (contains the detail of every pokemon)</span>

<span style="font-weight: 400;">        |— solution.py      (contains your solution source code)</span>

## **Grading**

<span style="font-weight: 400;">The following 100-point rubric will be used to determine your grade on CC2:</span>

*   <span style="font-weight: 400;">Tests (77)</span>

*   <span style="font-weight: 400;">00 - Coding Standard: __/5</span>
*   <span style="font-weight: 400;">01 - Test Add: __/5</span>
*   <span style="font-weight: 400;">02 - Test Remove: __/5</span>
*   <span style="font-weight: 400;">03 - Test Swap: _/5</span>
*   <span style="font-weight: 400;">04 - Test Example: __/17</span>
*   <span style="font-weight: 400;">05 - Test Small Case Comprehensive: __/20</span>
*   <span style="font-weight: 400;">06 - Test Large Case Comprehensive: __/20</span>

*   <span style="font-weight: 400;">Manual (23)</span>

*   <span style="font-weight: 400;">README.md is</span> _<span style="font-weight: 400;">completely</span>_ <span style="font-weight: 400;">filled out with (1) Name, (2) Feedback, (3) Time to Completion and (4) Citations: __/3</span>
*   <span style="font-weight: 400;">Time complexity for pokemon_machine __/5</span>
*   <span style="font-weight: 400;">Time complexity for add_pokemon __/5</span>
*   <span style="font-weight: 400;">Time complexity for remove_pokemon __/5</span>
*   <span style="font-weight: 400;">Time complexity for swap_pokemon __/5</span>

# **Tips, Tricks, and Notes**

*   <span style="font-weight: 400;">Nearby orders will have the index near each other which reduces the runtime of Linked List solution. In the other words, Linked List is really helpful for this type of problem</span>
*   <span style="font-weight: 400;">If you confuse about Linked List structure, you may need a piece of paper to draw them and write code from that. Yes, I did this sometimes.</span>
*   _<span style="font-weight: 400;">Here's some Pokemon music to get you in the spirit while working on this [Qumu remixes](https://youtube.com/playlist?list=PL0PCz_ViBzWbwm9QSz4zHADEsvkJp7fLu) and [route music](https://youtu.be/XVDNonuvo08)</span>_

Created by Bank Premsri and Andy Wilson