Project 6: Hash Tables
======================

**Due: Friday, March 19th @ 11:59p ET**

*This is not a team project. Do not copy someone else’s work.*

Assignment Overview
-------------------

Hash Tables are a very powerful data structure that are best known for
their ability to insert, delete, and lookup in O(1) time. This allows
them to be very powerful in storing data that needs to be accessed
quickly. Other data structures we have explored, such as Linked Lists
(O(n) lookup and deletion) and AVL Trees (log(n) lookup, insertion, and
deletion) lack that O(1) ability accross the board. 

![hashtables.PNG](https://s3.amazonaws.com/mimirplatform.production/files/e5b39502-fcd4-4eee-9a6b-e61ca0327114/hashtables.PNG)

A lot of you may already be familiar with the concept of hash tables, as
they are implemented in Python as dictionaries and C++ as unordered
maps.

In this project, you will be implementing a Hash Table from scratch in
Python and applying it to an application problem.

Assignment Notes
----------------

1.  ***The use of a Python dictionary results in a grade of 0 for the
    project!*** 
2.  In addition,**the only python container/collection type you can use
    is the built in list class** (no sets, linked lists, queues, etc.)
3.  We are going to have you use many of pythons built in "magic
    methods" in this project. **A *magic method* is one that has the two
    underscores** on the front and the back, such as \_\_len\_\_. In
    this project, ***these "magic methods" won't be doing much, they
    will call the other protected methods that you write!***
4.  So, what are "protected methods"? ***Protected methods* are methods
    prefaced with a single underscore, such as a function called
    "\_insert".** Protected methods are meant to **only be called inside
    other functions in the class**. This is Pythons way of implementing
    the C++ equivilant of "public" and "private" - protected methods
    meant to be treated as private!
5.  Building on the above point, **all attributes/functions that are
    protected** **(that is, leading with an underscore) *should not be
    called outside of your class***, which means they should not be
    accessed in your application problem!
6.  ***Use of \_insert(), \_delete(), \_get(), and \_grow() is STRICTLY
    FORBIDDEN in the application!!!***
7.  We have very small test cases for the \_insert(), \_get(), and
    \_delete() functions. The purpose is to make sure you split the work
    between the magic and hidden methods appropriately. The majority of
    the testing will take place in the magic method implementations!
8.  A few guarentees:
    1.  Capacity will not grow past \~1000
    2.  All keys will be of type string

Here is an table that shows how private methods and magic methods relate
to each other:

![magic.PNG](https://s3.amazonaws.com/mimirplatform.production/files/72216a8d-525e-4c27-90e0-7a7f2df06b72/magic.PNG)

Assignment Specifications
-------------------------

#### class HashNode:

*DO NOT MODIFY the following attributes/functions*

-   **Attributes**
    -   **key: str:** The key of the hash node (this is what is used in
        hashing)
    -   **value: T:** Value being held in the node. Note that this may
        be any type, such as a `str`, `int`, `float`, `dict`, or a more
        complex object.
    -   **deleted: bool:** Whether or not the node has been deleted.
-   **\_\_init\_\_(self, key: str, value: T, deleted: bool = False) -\>
    None**
    -   Constructs a hash node.
    -   **key: str:** The key of the hash node.
    -   **value: T:** Value being held in the node.
    -   **deleted: bool:** Whether or not the node has been deleted.
        Defaults to false.
    -   **Returns:** `None`.
-   **\_\_str\_\_(self) -\> str** and **\_\_repr\_\_(self) -\> str**
    -   Represents the `Node` as a string.
    -   **Returns:** `str` representation of node
-   **\_\_eq\_\_(self, other: HashNode) -\> bool**
    -   Compares to see if two hash nodes are equal
    -   **other: HashNode:** The HashNode we are comparing against
    -   **Returns:** `bool `stating whether or not they are equal
-   **\_\_iadd\_\_(self, other: T) -\> bool**
    -   Adds to the value of the current HashNode
    -   **other: T:** The value we are adding to our current value
    -   **Returns:** `None`

#### class HashTable:

*DO NOT MODIFY the following attributes/functions*

-   **Attributes**
    -   **capacity: int:** Capacity of the hash table.
    -   **size: int:** Current number of nodes in the hash table.
    -   **table: List:** This is where the actual data for our hash
        table is stored
    -   **prime\_index: int:** Current index of the prime numbers we are
        using in \_hash\_2()
-   **primes**
    -   This is a list of all the prime numbers, from 2 until 1000, used
        for \_hash\_2(). This is a ***class attribute***, so it is
        **accesed by HashTable.primes, NOT self.primes()!**
-   **\_\_init\_\_(self, capacity: int = 8) -\> None**
    -   Construct an empty hash table, with the capacity as specified in
        the input
    -   capacity: int: 
    -   **Returns:** `None`.
-   **\_\_str\_\_(self) -\> str** and **\_\_repr\_\_(self) -\> str**
    -   Represents the `HashTable` as a string.
    -   **Returns:** `str`.
-   **\_\_eq\_\_(self, other: HashTable) -\> bool**
    -   Checks if two HashTables are equal
    -   **other: HashTable:** the hashtable we are comparing against
    -   **Returns**: `bool `stating whether or not they are equal
-   **\_hash\_1(self, key: str) -\> int**
    -   The first of the two hash functions used to turn a key into a
        bin number
    -   **key: str:** key we are hashing
    -   **Returns:** int that is the bin number
-   **\_hash\_2(self, key: str) -\> in**t
    -   The second of the two hash functions used to turn a key into a
        bin number. This hash function acts as the tie breaker.
    -   **key: str**: key we are hashing
    -   **Returns:** int that is the bin number

*IMPLEMENT the following functions*

-   **\_\_len\_\_(self) -\> int**
    -   Getter for the size (that, is, the number of elements) in the
        HashTable
    -   *Time Complexity: O(1)*
    -   *Space Complexity: O(1)*
    -   **Returns:** int that is size of hash table
-   **\_\_setitem\_\_(self, key: str, value: T) -\> None**
    -   Sets the value with an associated key in the HashTable
        -   ***This should be a short, \~1 line function***- the
            majority of the work should be done in the \_insert()
            method!
    -   *Time Complexity: O(1)\**
    -   *Space Complexity: O(1)\**
    -   **key: str:**The key we are hashing
    -   **value: T:**The associated value we are storing
    -   **Returns:** None
-   **\_\_getitem\_\_(self, key: str) -\> T**
    -   Looks up the value with an associated key in the HashTable
        -   **If the key does not exist in the table, raise a
            *KeyError* **
        -   ***This should be a short, \~3 line function***- the
            majority of the work should be done in the \_get() method!
    -   *Time Complexity: O(1)\**
    -   *Space Complexity: O(1)*
    -   **key: str:**The key we are seraching for the associated value
        of
    -   **Returns:** The value with an associated Key
-   **\_\_delitem\_\_(self, key: str) -\> None**
    -   Deletes the value with an associated key in the HashTable
        -   **If the key does not exist in the table, raise a
            *KeyError* **
        -   ***This should be a short, \~3 line function***- the
            majority of the work should be done in the \_get() and
            \_delete() methods!
    -   *Time Complexity: O(1)\**
    -   *Space Complexity: O(1)*
    -   **key: str:**The key we are deleting the associated value of
    -   **Returns:** None
-   **\_\_contains\_\_(self, key: str) -\> bool**
    -   Determines if a node with the key denoted by the parameter
        exists in the table
        -   ***This should be a short, \~3 line function***- the
            majority of the work should be done in the \_get() method!
    -   *Time Complexity: O(1)\**
    -   *Space Complexity: O(1)*
    -   **key: str:**The key we are checking to be a part of the hash
        table
    -   **Returns:** None
-   **hash(self, key: str, inserting: bool = False) -\> int**\
    -   Given a key string return an index in the hash table.
    -   Should implement double hashing.\
        -   If the key exists in the hash table, return the index of the
            existing HashNode
        -   If the key does not exist in the hash table, return the
            index of the next available empty position in the hash
            table.
            -   Collision resolution should implement double hashing
                with hash1 as the initial hash and hash2 as the step
                size
        -   Note - There are 2 possibilities when hashing for an index:
            -   When inserting a node into the hash table we want to
                insert into the next available bin. \
            -   When performing a lookup/deletion in the hash table we
                want to continue until we either find the proper
                HashNode or until we reach a bin that has never held a
                value. This is to preserve the collison resolution
                methodology.
            -   The inserting parameter should be used to differentiate
                between these two cases.
    -   *Time Complexity: O(1)\**
    -   *Space Complexity: O(1)*
    -   **key: str:** The key being used in our hash function
    -   **inserting: bool:** Whether or not we are doing an insertion.
        Important for the reasons described above.
    -   **Returns:** int that is the bin we hashed into
-   **\_insert(self, key: str, value: T) -\> None**
    -   Use the key and value parameters to add a HashNode to the hash
        table.\
        -   If the key exists, overwrite the existing value
        -   In the event that inserting causes the table to have a load
            factor of 0.5 or greater you must grow the table to double
            the existing capacity.
    -   *Time Complexity: O(1)\**
    -   *Space Complexity: O(1)\**
    -   **key: str:**The key associated with the value we are storing
    -   **value: T:**The associated value we are storing
    -   **Returns:** None
-   **\_get(self, key: str) -\> HashNode**
    -   Find the HashNode with the given key in the hash table.\
        -   If the element does not exist, return None
    -   *Time Complexity: O(1)\**
    -   *Space Complexity: O(1)*
    -   **key: str:**The key we looking up
    -   **Returns:** HashNode with the key we looked up
-   **\_delete(self, key: str) -\> None**
    -   Removes the HashNode with the given key from the hash table .
        -   If the node is found assign its key and value to None, and
            set the deleted flag to True
    -   *Time Complexity: O(1)\**
    -   *Space Complexity: O(1)*
    -   **key: str:**The key of the Node we are looking to delete
    -   **Returns:** None
-   **\_grow(self) -\> None**
    -   Double the capacity of the existing hash table.
        -   Do **NOT**rehash deleted HashNodes
        -   Must update self.prime\_index, the value of
            self.prime\_index should be the **index** of the largest
            prime **smaller** than self.capacity in the HashTable.primes
            tuple.\
    -   *Time Complexity: O(N)*
    -   *Space Complexity: O(N)*
    -   **Returns:** None
-   **update(self, pairs: List[Tuple[str, T]] = []) -\> None**
    -   Updates the hash table using an iterable of key value pairs
        -   If the value already exists, update it, otherwise enter it
            into the table\
    -   *Time Complexity: O(M)\*, where M is length of pairs*
    -   *Space Complexity: O(M)*
    -   **pairs:** **List[Tuple[str, T]]****: **list of tuples (key,
        value) being updated
    -   **Returns:** None
-   **keys(self) -\> List[str]**
    -   Makes a list that contains all of the keys in the table
        -   Order does not matter!
    -   *Time Complexity: O(N)\**
    -   *Space Complexity: O(N)*
    -   **Returns:** List of the keys
-   **values(self) -\> List[T]**
    -   Makes a list that contains all of the values in the table
        -   Order does not matter!
    -   *Time Complexity: O(N)\**
    -   *Space Complexity: O(N)*
    -   **Returns:** List of the values
-   **items(self) -\> List[Tuple[str,T]]**
    -   Makes a list that contains all of the keys in the table
        -   Order does not matter!
    -   *Time Complexity: O(N)\**
    -   *Space Complexity: O(N)*
    -   **Returns:** List of Tuples of the form (key, value)
-   **clear(self) -\> None**
    -   Should clear the table of HashNodes completely, in essence a
        reset of the table
        -   Should not modify capacity
        -   **Notice the O(1) space complexity - *this must be done in
            place!***
    -   *Time Complexity: O(N)*
    -   *Space Complexity: O(1)*
    -   **Returns:** None

\**Amortized Complexity*

Application: CATA Bus Data
--------------------------

The CATA schedulers have noticed that the busses are becoming less
efficient.  To combat this problem, they've tasked you with tracking
users in the CATA system and their commute times.  CATA would like to be
able to log the enter and exit times at bus stops around campus and get
the average travel time between any two stops.

Your job is to create a data structure that can be queried to get the
average travel time between two stations. 

**Your class will be instantiated with the following call:**

cata\_data = CataData()

**Example 1**

cata\_data.enter("Ian", "Wilson", 1)

cata\_data.enter("Max", "Wilson", 1)

cata\_data.exit("Ian", "Akers", 4)

cata\_data.exit("Max", "Akers", 6)

 

After this series of function calls, querying the CataData object with
cata\_data.get\_average("Wilson", "Akers") should return 4.  There are
two trips from Wilson to Akers in the system.  It took Ian a time of 3
and it took Max a time of 5.  (3 + 5) / 2 = 4

 

**Example 2**

 

cata\_data.enter("Ian", "Engineering", 0)

cata\_data.enter("Max", "Chemistry", 7)

cata\_data.exit("Ian", "Chemistry", 1)

cata\_data.enter("Ian", "Chemistry", 4)

cata\_data.exit("Ian", "Wells", 6)

cata\_data.enter("Ian", "Wells", 8)

cata\_data.exit("Ian", "Wilson", 10)

cata\_data.exit("Max", "Wells", 12)

 

cata\_data.get\_average("Chemistry", "Wells") = 3.5

cata\_data.get\_average("Engineering", "Chemistry") = 1

 

**Notes:**

-   If an id that was never in the system exits the system, nothing
    should be tracked (think of this as people who sneak onto the bus. 
    There is no scan in, but they are scanned out.  Since there is no
    record of their origin, we cannot obtain any meaningful data from
    this)
-   If the system is queried for two stations for which there isn't a
    trip yet, the get\_average function should return 0.0
-   If an id that is currently in the system enters again, use the new
    origin station (think of this as a miss of the user's last exit
    scan)

 

**class CataData: **

-   **\_\_init\_\_(self):**
    -   **Design your data structure here**
-   **enter(self, id, origin, time) -\> None**
    -   Notes that a rider, identified by "id", is on a bus.  This rider
        is starting from station "origin" at a time of "time"
    -   Time complexity: O(1)
    -   **Return:** None
-   **exit(self, id, dest, time) -\> None**\
    -   Notes that a rider, identified by "id", is no longer on a bus. 
        This rider has gotten off at station "dest" at a time of "time"
    -   Time complexity: O(1)
    -   **Return:** None
-   **get\_average(self, origin, dest) -\> float**\
    -   Gets the average travel time of users riding CATA busses from
        origin to dest.
    -   Time complexity: O(1)
    -   **Return:** None

**Every operation must be in constant time: O(1)\
The space of the data structure must be: O(n\^2) where n is the amount
of bus stops in the system.\
You must use at least one HashTable(), but you can use as many as you
want provided it's O(n\^2) space.\
REMEMBER THAT HASHTABLE VALUES CAN BE ANY TYPE\
*****Use of \_insert(), \_delete(), \_get(), and \_grow() is STRICTLY
FORBIDDEN in the application!!!***

Submission
----------

#### Deliverables

Be sure to upload the following deliverables in a .zip folder to Mimir
by 11:59p ET on Friday, March 19th.

    Project6.zip
        |— Project6/
            |— README.xml      (for project feedback)
            |— __init__.py     (for proper Mimir testcase loading)
            |— hashtable.py    (contains your solution source code)

#### Grading

-   Tests (60)
    -   Coding Standard: \_\_/2
    -   hashtable: \_\_/43
        -   hash: \_\_/7
        -   \_insert: \_\_/1
        -   \_get: \_\_/1
        -   \_delete: \_\_/1
        -   \_\_len\_\_: \_\_/1
        -   \_\_setitem\_\_: \_\_/4
        -   \_\_getitem\_\_: \_\_/4
        -   \_\_delitem\_\_: \_\_/4
        -   \_\_contains\_\_: \_\_/2
        -   update: \_\_/3
        -   keys/values/items: \_\_/5
        -   clear: \_\_/2
        -   comprehensive: \_\_/8
    -   CataData: \_\_/15
        -   application: \_\_/5
        -   application larger: \_\_/10
-   Manual (40)
    -   `README.xml` is completely filled out with (1) NetID, (2)
        Feedback, (3) Time to Completion and (4) Citations: \_\_/2
    -   hashtable time/space: \_\_/30
        -   hash: \_\_/4
        -   \_\_len\_\_: \_\_/1
        -   \_\_setitem\_\_: \_\_/4
        -   \_\_getitem\_\_: \_\_/4
        -   \_\_delitem\_\_: \_\_/4
        -   \_\_contains\_\_: \_\_/3
        -   \_grow: \_\_/4
        -   update: \_\_/2
        -   keys/values/items: \_\_/2
        -   clear: \_\_/2
    -   CataData time/space: \_\_/8

Appendix
--------

#### Authors

Project authored by Ian Barber and Max Huang

Adapted from the work of Brandon Field and Yash Vesikar
