Project 8: Graphs
=================

**Due: Friday,April 16th @ 11:59pm**

*This is not a team project, do not copy someone else’s work.*

*Project based on constributions by Andrew Haas, Andrew McDonald,
Tanawan Premsri, and Andy Wilson*

 

Assignment Overview
-------------------

Graphs are particularly useful data structures for modeling connections
and relationships among objects. In fact, you've likely used an
application which relies on graphical modeling today - a few examples
include

-   **Facebook / Twitter / Instagram**
    -   Users are modeled as vertices storing posts, photos, videos,
        etc.
    -   Edges are modeled as "friendships," "followers," "likes,"
        "favorites," etc. 
-   **Google / Apple / Bing Maps**
    -   Intersections, cities, and other points of interest are modeled
        by vertices
    -   Road segments between intersections are modeled by weighted
        edges, where weights represent the relative speed/traffic of the
        road segment

You will be implementing a directed, weighted Graph ADT using the
**adjacency map** design, in which a graph object consists of a map
(ordered dictionary) of vertices, and each vertex holds its own map
(ordered dictionary) of adjacent vertices, i.e. vertices to which that
vertex is connected by an outgoing edge.

In some ways, this project also serves as a capstone to the course- in
completing it one utilizes recursion, queues, two dimensional arrays,
hash maps, dynamic programming, and more. You may also notice that
trees, linked lists, and even heaps are special cases of the general
graph structure, and that many graph algorithms can be applied to these
earlier structures without modification. To highlight this inheritance,
consider the inorder traversal algorithm we applied to AVL trees -
really, it was nothing more than a graph depth first search with a
tendancy to go left before right.

The goal of this project is to introduce the versatile and flexible
nature of graphs, along with the operations and search algorithms which
make them so useful.

![got\_graph.png](https://s3.amazonaws.com/mimirplatform.production/files/aea24196-db6a-46f0-9008-3ff19b7d29c7/got_graph.png)

 

Assignment Notes
----------------

-   A plotting function is provided to help you visualize the
    progression of various search algorithms
    -   Be sure to read the specs explaining **plot()**
    -   If you don't want to use it, just comment out the related import
        statements and **plot()** function
-   Python allows representation of the value infinity using
    **float('inf')**
-   No negative edge weights will ever be added to the graph
    -   All edge weights are numeric values greater than or equal to
        zero
-   Time complexities are specified in terms of **V** and **E**, where
    **V** represents the number of vertices in the graph and **E**
    represents the number of edges in a graph
    -   Recall that E is bounded above by **V**\^2; a graph has **E** =
        **V**\^2 edges if and only if every vertex is connected to every
        other vertex
-   Recall that **list.insert(0, element) **and **list.pop(0) **are both
    *O(N)* calls on a Python list
    -   Recall that python's 'lists' are not lists in the more common
        sense of the word: linked lists. They are dynamically managed
        tuples, stored in memory as contiguous arrays of pointers to
        elements elsewhere in memory. This allows indexing into a 'list'
        in constant time. The downside of this, however, is that adding
        to a python 'list' at a specific index, *i,*requires shifting
        the pointer to every element past *i *by one in the underlying
        array: a linear operation.
    -   Be careful when implementing **bfs, dfs** and the Application
        Problem to ensure you do not break time complexity by popping or
        inserting from the front of a list when reconstructing a path
    -   Instead of inserting into / popping from the front of the list,
        simply append to or pop from the end, then reverse the list
        *once* at the end
        -   If you have N calls to **list.insert(0, element)**, that is
            *O(N\^2)*
        -   If you instead have N calls to **list.append(element)**,
            followed by a single call to **list.reverse()**, that is
            *O(N)*
        -   Both methods will result in the same list being constructed,
            but the second is far more efficient

Assignment Specifications
-------------------------

### class Vertex: 

Represents a vertex object, the building block of a graph.

***DO NOT MODIFY the following attributes/functions***

-   **Attributes**
    -   **id:**A string used to uniquely identify a vertex
    -   **adj: **A dictionary of type **{other\_id : number}**which
        represents the connections of a vertex to other vertices;
        existence of an entry with key **other\_i****d* ***indicates
        connection from this vertex to the vertex with id
        **other\_id**by an edge with weight **number**
        -   Note that as of Python 3.7, [insertion
            ordering](https://stackoverflow.com/a/57072435) in normal
            dictionaries is guaranteed and ensures traversals will
            select the next neighbor to visit deterministically
    -   **visited:** A boolean flag used in search algorithms to
        indicate that the vertex has been visited
    -   **x:** The x-position of a vertex (used in Application Problem)
        (defaults to zero)
    -   **y: **The y-position of a vertex (used in Application Problem)
        (defaults to zero)
-   **\_\_init\_\_(self, idx: str, x: float=0, y: float=0) -\> None:**\
    -   Constructs a Vertex object
-   **\_\_eq\_\_(self, other: Vertex) -\> bool:**
    -   Compares this vertex for equality with another vertex
-   **\_\_repr\_\_(self) -\> str:**
    -   Represents the vertex as a string for debugging
-   **\_\_str\_\_(self) -\> str:**
    -   Represents the vertex as a string for debugging
-   **\_\_hash\_\_(self) -\> int:**
    -   Allows the vertex to be hashed into a set; used in unit tests

***IMPLEMENT the following functions***

-   **degree(self) -\> int:**
    -   Returns the number of outgoing edges from this vertex; i.e., the
        outgoing degree of this vertex
    -   *Time Complexity: O(1)*
    -   *Space Complexity: O(1)*
-   **get\_edges(self) -\> Set[Tuple[str, float]]:**
    -   Returns a **set** of tuples representing outgoing edges from
        this vertex
    -   Edges are represented as tuples **(other\_id,
        weight)**** **where 
        -   **other\_id** is the unique string id of the destination
            vertex
        -   **weight** is the weight of the edge connecting this vertex
            to the other vertex
    -   Returns an empty set if this vertex has no outgoing edges
    -   *Time Complexity: O(degV)*
    -   *Space Complexity: O(degV)*
-   **euclidean\_distance(self, other: Vertex) -\> float:**
    -   Returns the [euclidean
        distance](http://rosalind.info/glossary/euclidean-distance/)
        [based on two dimensional coordinates] between this vertex and
        vertex **other**
    -   Used in Application problem
    -   *Time Complexity: O(1)*
    -   *Space Complexity: O(1)*
-   **taxicab\_distance(self, other: Vertex) -\> float:**
    -   Returns the [taxicab
        distance](https://en.wikipedia.org/wiki/Taxicab_geometry) [based
        on two dimensional coordinates] between this vertex and vertex
        **other**
    -   Used in Application problem
    -   *Time Complexity: O(1)*
    -   *Space Complexity: O(1)*

### class Graph: 

Represents a graph object

***DO NOT MODIFY the following attributes/functions***

-   **Attributes**
    -   **size: **The number of vertices in the graph
    -   **vertices:** A dictionary of type **{id : Vertex}** storing the
        vertices of the graph, where **id** represents the unique string
        id of a **Vertex **object
        -   Note that as of Python 3.7, [insertion
            ordering](https://stackoverflow.com/a/57072435) in normal
            dictionaries is guaranteed and ensures
            **get\_edges(self)**and **get\_vertices(self)** will return
            deterministically ordered lists
    -   **plot\_show**: If true, calls to **plot()** display a rendering
        of the graph in matplotlib; if false, all calls to **plot()**
        are ignored (see **plot()** below)
    -   **plot\_delay**: Length of delay in **plot() **(see **plot()**
        below)
-   **\_\_init\_\_(self, plt\_show: bool=False) -\> None:**\
    -   Constructs a Graph object
    -   Sets **self.plot\_show** to False by default
-   **\_\_eq\_\_(self, other: Graph) -\> bool:**
    -   Compares this graph for equality with another graph
-   **\_\_repr\_\_(self) -\> str:**
    -   Represents the graph as a string for debugging
-   **\_\_str\_\_(self) -\> str:**
    -   Represents the graph as a string for debugging
-   **add\_to\_graph(self, start\_id: str, dest\_id: str=None, weight:
    float=0) -\> float:**
    -   Adds a vertex / vertices / edge to the graph
        -   Adds a vertex with id **start\_id** to the graph if no such
            vertex exists
        -   Adds a vertex with id **dest\_id**to the graph if no such
            vertex exists and **dest\_id** is not None
        -   Adds an edge with weight **weight** if **dest\_id** is not
            None
    -   If a vertex with id **start\_id** or **dest\_id **already exists
        in the graph, this function will not overwrite that vertex with
        a new one
    -   If an edge already exists from vertex with id **start\_id** to
        vertex with id **dest\_id**, this function will overwrite the
        weight of that edge
-   **matrix2graph(self, matrix: Matrix) -\> None:**
    -   Constructs a graph from a given adjacency matrix representation
    -   **matrix**is guaranteed to be a square 2D list (i.e. list of
        lists where \# rows = \# columns), of size **[V+1]**x **[V+1]**
        -   **matrix[0][0] **is None
        -   The first row and first column of **matrix** hold string ids
            of vertices to be added to the graph and are symmetric, i.e.
            **matrix[i][0] = matrix[0][i]**for i = 1, ..., n 
        -   **matrix[i][j]** is None if no edge exists from the
            vertex **matrix[i][0] **to the vertex **matrix[0][j] **
        -   **matrix[i][j] **is a **number**if an edge exists from the
            vertex **matrix[i][0] **to the vertex **matrix[0][j] **with
            weight **number**
-   **graph2matrix(self) -\> None:**
    -   Constructs and returns an adjacency matrix from a graph
    -   The output matches the format of matrices described in
        **matrix2graph**
    -   If the graph is empty, returns **None**
-   **graph2csv(self, filepath: str) -\> None:**
    -   Encodes the graph (if non-empty) in a csv file at the given
        location

***USE the following function however you'd like***

-   **plot(self) -\> None:**
    -   Renders a visual representation of the graph using matplotlib
        and displays graphic in PyCharm
        -   [Follow this tutorial to install matplotlib and numpy if you
            do not have
            them](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html),
            or follow the tooltip auto-suggested by PyCharm
    -   Provided for use in debugging
    -   If you call this in your searches and **self.****plot\_show** is
        true, the search process will be animated in successive plot
        renderings (with time between frames controlled by
        **self.plot\_delay**)
    -   Not tested in any testcases
        -   All testcase graphs are constructed with **self.plot\_show**
            set to False
    -   If vertices have (x,y) coordinates specified, they will be
        plotted at those locations
    -   If vertices do not have (x,y) coordinates specified, they will
        be plotted at a random point on the unit circle
    -   To install the necessary packages (matplotlib and numpy), follow
        the auto-suggestions provided by PyCharm
    -   Vertices and edges are labeled; edges are color-coded by weight
        -   If a bi-directional edge exists between vertices, two
            color-coded weights will be displayed

![sample\_plot.png](https://s3.amazonaws.com/mimirplatform.production/files/0aec2496-150a-4b85-b86f-142f235fe4ba/sample_plot.png)

***IMPLEMENT the following functions***

-   **reset\_vertices(self) -\> None:**
    -   Resets visited flags of all vertices within the graph
    -   Used in unit tests to reset graph between searches
    -   *Time Complexity: O(V)*
    -   *Space Complexity: O(V)*
-   **get\_vertex(self, vertex\_id: str) -\> Vertex:**\
    -   Returns the Vertex object with id **vertex\_id **if it exists in
        the graph
    -   Returns None if no vertex with unique id **vertex\_id** exists
    -   *Time Complexity: O(1)*
    -   *Space Complexity: O(1)*
-   **get\_vertices(self) -\> Set[Vertex]:**\
    -   Returns a **set**of all Vertex objects held in the graph
    -   Returns an empty set if no vertices are held in the graph
    -   *Time Complexity: O(V)*
    -   *Space Complexity: O(V)*
-   **get\_edge(self, start\_id: str, dest\_id: str) -\> Tuple[str, str,
    float]:**\
    -   Returns the edge connecting the vertex with id **start\_id** to
        the vertex with id **dest\_id** in a tuple of the
        form **(start\_id, dest\_id, weight)**
    -   If the edge or either of the associated vertices does not exist
        in the graph, returns **None**
    -   *Time Complexity: O(1)*
    -   *Space Complexity: O(1)*
-   **get\_edges(self) -\> Set[Tuple[str, str, float]]:**
    -   Returns a **set**of tuples representing all edges within the
        graph
    -   Edges are represented as tuples **(start\_id, other\_id,
        weight)**** **where 
        -   **start\_id** is the unique string id of the starting vertex
        -   **other\_id** is the unique string id of the destination
            vertex
        -   **weight** is the weight of the edge connecting the starting
            vertex to the destination vertex
    -   Retuns an empty set if the graph is empty
    -   *Time Complexity: O(V+E)*
    -   *Space Complexity: O(E)*
-   **bfs(self, start\_id: str, target\_id: str) -\> Tuple[List[str],
    float]:**
    -   Perform a breadth-first search beginning at vertex with
        id **start\_id** and terminating at vertex with id **end\_id**
    -   As you explore from each vertex, iterate over neighbors
        using **vertex.adj **(not vertex.get\_edges()) to ensure
        neighbors are visited in proper order
    -   Returns tuple of the form **([path], distance)** where
        -   **[path]** is a list of vertex id strings beginning
            with **start\_id**, terminating with **end\_id**, and
            including the ids of all intermediate vertices connecting
            the two
        -   **distance** is the sum of the weights of the edges along
            the **[path]** travelled
    -   If no path exists from vertex with id **start\_id **to vertex
        with **end\_id**or if one of the vertices does not
        exist, returns tuple **([],0)**
    -   Guaranteed that **start\_id != target\_id** (since that would be
        a trivial path)
    -   Because our adjacency maps use [insertion
        ordering](https://stackoverflow.com/a/57072435), neighbors will
        be visited in a deterministic order, and thus you do not need to
        worry about the order in which you visit neighbor vertices at
        the same depth
    -   Use the
        [SimpleQueue](https://docs.python.org/3/library/queue.html)
        class to guarantee O(1) pushes and pops on queue
    -   *Time Complexity: O(V+E)*
    -   *Space Complexity: O(V)*
-   **dfs(self, start\_id: str, target\_id: str) -\> Tuple[List[str],
    float]:**
    -   Wrapper function for **dfs\_inner**, which MUST BE CALLED within
        this function
        -   The majority of the work of dfs should be done in
            **dfs\_inner**
        -   This function makes it simpler for client code to call for a
            dfs
        -   This function makes it possible to avoid inserting vertex
            ids at the front of the path list on path reconstruction,
            which leads to suboptimal performance (see Assignment Notes)
            -   Hint: construct the path in reverse order in
                **dfs\_inner**, then reverse the path in this function
                to optimize time complexity
    -   Hint: call **dfs\_inner** with **current\_id** as
        **start\_id, **then reverse the path here and return it
    -   *Time Complexity: O(V+E)  (including calls to dfs\_inner)*
    -   *Space Complexity: O(V)  (including calls to dfs\_inner)*
-   **dfs\_inner(self, current\_id: str, target\_id: str, path:
    List[str]=[]) -\> Tuple[List[str], float]**
    -   Performs the recursive work of depth-first search by searching
        for a path from vertex with id **current\_id** to vertex with
        id **target\_id**
    -   **MUST BE RECURSIVE**
    -   As you explore from each vertex, iterate over neighbors
        using **vertex.adj **(not vertex.get\_edges()) to ensure
        neighbors are visited in proper order
    -   Returns tuple of the form **([path], distance)** where
        -   **[path]** is a list of vertex id strings beginning
            with **start\_id**, terminating with **end\_id**, and
            including the ids of all intermediate vertices connecting
            the two
        -   **distance** is the sum of the weights of the edges along
            the **[path]** travelled
    -   If no path exists from vertex with id **current\_id**to vertex
        with**target\_id**or if one of the vertices does not
        exist, returns tuple **([],0)**
    -   Guaranteed that **start\_id != target\_id** (since that would be
        a trivial path)
    -   Because our adjacency maps use [insertion
        ordering](https://stackoverflow.com/a/57072435), neighbors will
        be visited in a deterministic order, and thus you do not need to
        worry about the order in which you visit neighbor vertices
    -   *Time Complexity: O(V+E)*
    -   *Space Complexity: O(V)*
-   **detect\_cycle(self) -\> bool:**
    -   returns **True **if graph contains a cycle, otherwise
        returns **False**
    -   Be careful with time and space complexity, they are easy to
        violate here
    -   The testcase should give a good idea of what constitutes a cycle
        and what does not
    -   *Time Complexity: **O(V+E)*
    -   *Space Complexity: O(V)*

Application Problem
-------------------

In response to the COVID-19 outbreak, you've been tasked with designing
the pathfinding algorithm of an [autonomous delivery vehicle which will
be used to carry food, medicine, and other essential supplies to the
front lines of infected
areas.](https://spectrum.ieee.org/automaton/robotics/robotics-hardware/robots-helping-to-fight-coronavirus-outbreak)

Rapid delivery is essential to ensure the health of patients and medical
workers; depth-first and breadth-first search won't cut it. In fact,
even Dijkstra's algorithm falls short of your high performance
standards.

Your only option is to implement [A\*
Search](https://en.wikipedia.org/wiki/A*_search_algorithm) (A-Star
Search), an algorithm that accounts for both straight-line and
along-edge distance to find the shortest path in fewer iterations.
Unlike [Dijkstra's
algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), A\*
will tend to avoid searching vertices that are close but in the wrong
direction ([gif from this
video](https://www.youtube.com/watch?v=g024lzsknDo)).

![AStarGif.gif](https://s3.amazonaws.com/mimirplatform.production/files/002f64b5-cafa-4531-8dc8-e56f0e0de6e6/AStarGif.gif)

### What is A\* Search?

Instead of searching the "next closest" vertex as is done in Dijkstra's
algorithm, A\* Search picks the vertex which is "next closest to the
goal" by weighting vertices more cleverly.

Recall that in Dijkstra's algorithm, vertices are stored in a priority
queue with a priority key equal to the current shortest path to that
vertex. If we denote the current shortest path to a vertex **v**
by **g(v)**, then on each iteration of Dijkstra's algorithm, we search
on the vertex with **min(g(v)).**

A\* search takes the same approach to selecting the next vertex, but
instead of setting the priority key of a vertex equal to **g(v)** and
selecting **min(g(v))**, it uses the value **f(v)**, and selects the
vertex with **min(f(v))** where

 

**f(v) = g(v) + h(v)**

**       = current\_shortest\_path\_to\_v +
estimated\_distance\_between\_v\_and\_target**

 

### In English, Please....

A\* Search prioritizes vertices **v**to search based on the
value **f(v)**, which is the sum of

-   **g(v)**, or the current shortest known path to vertex **v**, and
-   **h(v)**, which is the estimated (Euclidean or Taxicab) distance
    between the vertex **v** and the target vertex you're searching for

The result is that A\* prioritizes vertices to search that (1) are
*close to the origin along a known path* AND which (2) are *in the right
direction towards the target. *Vertices with a small **g(v) **are *close
to the origin along a known path *and vertices with a small **h(v)**are
*in the right direction towards the target**,***so we pick vertices with
the smallest sum of these two values.

[We strongly recommend you watch this video to build your intuition
behind A\* Search!](https://www.youtube.com/watch?v=ySN5Wnu88nE)

[A\* is extremely versatile. Here we use Euclidean and Taxicab distances
to prioritize certain directions of search, but note that any
[metric](https://en.wikipedia.org/wiki/Metric_(mathematics)#Definition)
**h(v, target)** could be used should need arise. See
[here](http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html)
for more information on situations where different metrics may be
practical.]

### Your Task

Implement A\* Search on your Graph ADT according to the following
specifications

-   **a\_star(self, start\_id, target\_id, metric)**
    -   Perform a A\* search beginning at vertex with id **start\_id**
        and terminating at vertex with id **end\_id**
    -   As you explore from each vertex, iterate over neighbors
        using **vertex.adj **(not vertex.get\_edges()) to ensure
        neighbors are visited in proper order
    -   Use the **metric** parameter to estimate h(v), the remaining
        distance, at each vertex
        -   This is a callable parameter and will always
            be **Vertex.euclidean\_distance **or **Vertex.taxicab\_distance**
    -   Returns tuple of the form **([path], distance)** where
        -   **[path]** is a list of vertex id strings beginning
            with **start\_id**, terminating with **end\_id**, and
            including the ids of all intermediate vertices connecting
            the two
        -   **distance** is the sum of the weights of the edges along
            the **[path]** travelled
    -   If no path exists from vertex with id **start\_id **to vertex
        with **end\_id**or if one of the vertices does not
        exist, returns tuple **([],0)**
    -   Guaranteed that **start\_id != target\_id** (since that would be
        a trivial path)
    -   Recall that vertices are prioritized in increasing order
        of **f(v) = g(v) + h(v)**, where
        -   **g(v) **is the shortest known path to this vertex
        -   **h(v) **is the Euclidean distance from **v** to the target
            vertex
    -   Use the given AStarPriorityQueue class to simplify priority key
        updates in search priority queue
    -   **Implementations of this function which do not utilize the
        heuristic metric will not receive any credit, visible and hidden
        testcases included.**
        -   **Do not simply implement Dijkstra's Algorithm**
    -   *Time Complexity: O(V+E)*
    -   *Space Complexity: O(V)*

To simplify the operation of updating a priority key in your search
priority queue, use the following given class.

### class AStarPriorityQueue:

*DO NOT MODIFY the following attributes/functions*

-   **Attributes**
    -   **data:**Underlying data list of priority queue
    -   **locator:** Dictionary to locate vertices within the priority
        queue
    -   **counter:**Used to break ties between vertices
-   **\_\_init\_\_(self)**\
    -   Constructs an AStarPriorityQueue object
-   **\_\_repr\_\_(self)**
    -   Represents the priority queue as a string for debugging
-   **\_\_str\_\_(self)**
    -   Represents the priority queue as a string for debugging
-   **empty(self)**
    -   Returns boolean indicating whether priority queue is empty
-   **push(self, priority, vertex)**\
    -   Push the **vertex**object onto the priority queue with a
        given **priority** key
    -   This priority queue has been specially designed to hold Vertex
        objects as values ranked by priority keys; be sure you push
        Vertex objects and NOT vertex id strings onto the queue
-   **pop(self)**\
    -   Visit, remove, and return the Vertex object with highest
        priority (i.e. lowest priority key) as a **(priority,
        vertex) **tuple
-   **update(self, new\_priority, vertex)**
    -   Update the priority of the **vertex**object in the queue to have
        a **new\_priority**

### Example

To test your algorithm's performance, you use it to find optimal paths
between locations on MSU's campus according to the graph depicted below.
Note that the function **build\_msu\_graph(self)** has been provided to
you in your **testcases.py** file.

![msu\_map.png](https://s3.amazonaws.com/mimirplatform.production/files/e54e78f3-0b7d-437c-9abc-95bd384cb32d/msu_map.png)

![a\_star\_plot.png](https://s3.amazonaws.com/mimirplatform.production/files/1330b9ef-ca73-45fc-bc58-e163872b6106/a_star_plot.png)

-   **a\_star('Breslin Center', 'Union')** would return
    -   (['Breslin Center', 'A', 'B', 'G', 'J', 'M', 'Union'], 22)
    -   This finds the same optimal path as Dijkstra
-   **a\_star('Breslin Center', 'Engineering Building')** would return
    -   (['Breslin Center', 'A', 'B', 'G', 'H', 'D', 'E', 'Engineering
        Building'], 34)
    -   This path bypasses the heavy-traffic Shaw Lane and finds the
        optimal path (note that BFS would stay on Shaw Lane for a
        sub-optimal path length of 36
-   **a\_star('Union', 'Library') **would return
    -   (['Union', 'M', 'J', 'K', 'Library'], 8)
    -   Although two equally-optimal paths exist, A\* chooses the one
        that's closer to the straight line connecting the Union to the
        Library

Extra Credit Problem:
---------------------

...Coming soon - Check for an update Tuesday, Apr 6th. Get ready for a
challenge. 

Submission:
-----------

### Deliverables:

Be sure to upload the following deliverables in a .zip folder to Mimir
by 11:59pm EST, on Friday April 16th.

Your .zip folder can contain other files (for example, description.md
and tests.py), but must include (at least) the following:

``` {.code-line}
|- Project8.zip
    |— Project8/
        |— README.xml       (for project feedback)
        |— __init__.py      (for proper Mimir testcase loading)
        |— Graph.py         (contains your solution source code)
```

### Grading

-   Tests (68)
-   Manual (32)
    -   README (2)
        -   M1: README completely filled out                           
                      \_\_/2
    -   Time & Space Complexity (32) 
        -   M2 -**degree, get\_edges, distances, reset\_vertices     
             **\_\_/3
        -   M3 - **get\_vertex, get\_vertices, get\_edge, get\_edges** 
            \_\_/3
        -   M4 - **bfs                                                 
                                             **\_\_/6
        -   M5 -**dfs**                                                 
                                           \_\_/6
        -   M6 - **detect\_cycle                                       
                                     **\_\_/6
        -   M7 - **a\_star                                             
                                           **\_\_/6

-   Extra Credit (15)
    -   Tests:                                                         
                                                \_\_/15

 
