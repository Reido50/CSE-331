"""
Name:
CSE 331 FS20 (Onsay)
"""

import heapq
import itertools
import math
import queue
import random
import time
import csv
from typing import TypeVar, Callable, Tuple, List, Set

import matplotlib.cm as cm
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

T = TypeVar('T')
Matrix = TypeVar('Matrix')  # Adjacency Matrix
Vertex = TypeVar('Vertex')  # Vertex Class Instance
Graph = TypeVar('Graph')    # Graph Class Instance


class Vertex:
    """ Class representing a Vertex object within a Graph """

    __slots__ = ['id', 'adj', 'visited', 'x', 'y']

    def __init__(self, idx: str, x: float = 0, y: float = 0) -> None:
        """
        DO NOT MODIFY
        Initializes a Vertex
        :param idx: A unique string identifier used for hashing the vertex
        :param x: The x coordinate of this vertex (used in a_star)
        :param y: The y coordinate of this vertex (used in a_star)
        """
        self.id = idx
        self.adj = {}             # dictionary {id : weight} of outgoing edges
        self.visited = False      # boolean flag used in search algorithms
        self.x, self.y = x, y     # coordinates for use in metric computations

    def __eq__(self, other: Vertex) -> bool:
        """
        DO NOT MODIFY
        Equality operator for Graph Vertex class
        :param other: vertex to compare
        """
        if self.id != other.id:
            return False
        elif self.visited != other.visited:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex visited flags not equal: self.visited={self.visited},"
                  f" other.visited={other.visited}")
            return False
        elif self.x != other.x:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex x coords not equal: self.x={self.x}, other.x={other.x}")
            return False
        elif self.y != other.y:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex y coords not equal: self.y={self.y}, other.y={other.y}")
            return False
        elif set(self.adj.items()) != set(other.adj.items()):
            diff = set(self.adj.items()).symmetric_difference(set(other.adj.items()))
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex adj dictionaries not equal:"
                  f" symmetric diff of adjacency (k,v) pairs = {str(diff)}")
            return False
        return True

    def __repr__(self) -> str:
        """
        DO NOT MODIFY
        :return: string representing Vertex object
        """
        lst = [f"<id: '{k}', weight: {v}>" for k, v in self.adj.items()]

        return f"<id: '{self.id}'" + ", Adjacencies: " + "".join(lst) + ">"

    def __str__(self) -> str:
        """
        DO NOT MODIFY
        :return: string representing Vertex object
        """
        return repr(self)

    def __hash__(self) -> int:
        """
        DO NOT MODIFY
        Hashes Vertex into a set; used in unit tests
        :return: hash value of Vertex
        """
        return hash(self.id)

#============== Modify Vertex Methods Below ==============#

    def degree(self) -> int:
        # Return the length of the adj dictionary
        return len(self.adj)

    def get_edges(self) -> Set[Tuple[str, float]]:
        """
        Returns a set of tuples representing outgoing edges from this vertex
        :return: Set of tuples (other_id, weight). Empty if no edges
        """
        # Create set
        output = set()
        # Add tuples to output from adj dictionary
        for key in self.adj:
            output.add((key, self.adj[key]))
        # Return output (may be empty)
        return output

    def euclidean_distance(self, other: Vertex) -> float:
        """
        Calculates the euclidean distance from this vertex to another
        :param other: Vertex in which we calculate the distance to
        :return: The euclidean distance between this vertex and vertex other
        """
        # Equation for euclidean distance sqrt((x2-x1)^2 + (y2-y1)^2)
        return math.sqrt(math.pow((other.x - self.x), 2) + math.pow((other.y - self.y), 2))

    def taxicab_distance(self, other: Vertex) -> float:
        """
        Calculates the taxical distance from this vertex to another
        :param other: Vertex in which we calculate the distance to
        :return: The taxicab distance between this vertex and vertex other
        """
        # Equation for taxicab distance: abs(x2-x1) + abs(y2-y1)
        return abs(other.x - self.x) + abs(other.y - self.y)
        


class Graph:
    """ Class implementing the Graph ADT using an Adjacency Map structure """

    __slots__ = ['size', 'vertices', 'plot_show', 'plot_delay']

    def __init__(self, plt_show: bool = False, matrix: Matrix = None, csv: str = "") -> None:
        """
        DO NOT MODIFY
        Instantiates a Graph class instance
        :param: plt_show : if true, render plot when plot() is called; else, ignore calls to plot()
        :param: matrix : optional matrix parameter used for fast construction
        :param: csv : optional filepath to a csv containing a matrix
        """
        matrix = matrix if matrix else np.loadtxt(csv, delimiter=',', dtype=str).tolist() if csv else None
        self.size = 0
        self.vertices = {}

        self.plot_show = plt_show
        self.plot_delay = 0.2

        if matrix is not None:
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix)):
                    if matrix[i][j] == "None" or matrix[i][j] == "":
                        matrix[i][j] = None
                    else:
                        matrix[i][j] = float(matrix[i][j])
            self.matrix2graph(matrix)


    def __eq__(self, other: Graph) -> bool:
        """
        DO NOT MODIFY
        Overloads equality operator for Graph class
        :param other: graph to compare
        """
        if self.size != other.size or len(self.vertices) != len(other.vertices):
            print(f"Graph size not equal: self.size={self.size}, other.size={other.size}")
            return False
        else:
            for vertex_id, vertex in self.vertices.items():
                other_vertex = other.get_vertex(vertex_id)
                if other_vertex is None:
                    print(f"Vertices not equal: '{vertex_id}' not in other graph")
                    return False

                adj_set = set(vertex.adj.items())
                other_adj_set = set(other_vertex.adj.items())

                if not adj_set == other_adj_set:
                    print(f"Vertices not equal: adjacencies of '{vertex_id}' not equal")
                    print(f"Adjacency symmetric difference = "
                          f"{str(adj_set.symmetric_difference(other_adj_set))}")
                    return False
        return True

    def __repr__(self) -> str:
        """
        DO NOT MODIFY
        :return: String representation of graph for debugging
        """
        return "Size: " + str(self.size) + ", Vertices: " + str(list(self.vertices.items()))

    def __str__(self) -> str:
        """
        DO NOT MODFIY
        :return: String representation of graph for debugging
        """
        return repr(self)

    def plot(self) -> None:
        """
        DO NOT MODIFY
        Creates a plot a visual representation of the graph using matplotlib
        """
        if self.plot_show:

            # if no x, y coords are specified, place vertices on the unit circle
            for i, vertex in enumerate(self.get_vertices()):
                if vertex.x == 0 and vertex.y == 0:
                    vertex.x = math.cos(i * 2 * math.pi / self.size)
                    vertex.y = math.sin(i * 2 * math.pi / self.size)

            # show edges
            num_edges = len(self.get_edges())
            max_weight = max([edge[2] for edge in self.get_edges()]) if num_edges > 0 else 0
            colormap = cm.get_cmap('cool')
            for i, edge in enumerate(self.get_edges()):
                origin = self.get_vertex(edge[0])
                destination = self.get_vertex(edge[1])
                weight = edge[2]

                # plot edge
                arrow = patches.FancyArrowPatch((origin.x, origin.y),
                                                (destination.x, destination.y),
                                                connectionstyle="arc3,rad=.2",
                                                color=colormap(weight / max_weight),
                                                zorder=0,
                                                **dict(arrowstyle="Simple,tail_width=0.5,"
                                                                  "head_width=8,head_length=8"))
                plt.gca().add_patch(arrow)

                # label edge
                plt.text(x=(origin.x + destination.x) / 2 - (origin.x - destination.x) / 10,
                         y=(origin.y + destination.y) / 2 - (origin.y - destination.y) / 10,
                         s=weight, color=colormap(weight / max_weight))

            # show vertices
            x = np.array([vertex.x for vertex in self.get_vertices()])
            y = np.array([vertex.y for vertex in self.get_vertices()])
            labels = np.array([vertex.id for vertex in self.get_vertices()])
            colors = np.array(
                ['yellow' if vertex.visited else 'black' for vertex in self.get_vertices()])
            plt.scatter(x, y, s=40, c=colors, zorder=1)

            # plot labels
            for j, _ in enumerate(x):
                plt.text(x[j] - 0.03*max(x), y[j] - 0.03*max(y), labels[j])

            # show plot
            plt.show()
            # delay execution to enable animation
            time.sleep(self.plot_delay)

    def add_to_graph(self, start_id: str, dest_id: str = None, weight: float = 0) -> None:
        """
        Adds to graph: creates start vertex if necessary,
        an edge if specified,
        and a destination vertex if necessary to create said edge
        If edge already exists, update the weight.
        :param start_id: unique string id of starting vertex
        :param dest_id: unique string id of ending vertex
        :param weight: weight associated with edge from start -> dest
        :return: None
        """
        if self.vertices.get(start_id) is None:
            self.vertices[start_id] = Vertex(start_id)
            self.size += 1
        if dest_id is not None:
            if self.vertices.get(dest_id) is None:
                self.vertices[dest_id] = Vertex(dest_id)
                self.size += 1
            self.vertices.get(start_id).adj[dest_id] = weight

    def matrix2graph(self, matrix: Matrix) -> None:
        """
        Given an adjacency matrix, construct a graph
        matrix[i][j] will be the weight of an edge between the vertex_ids
        stored at matrix[i][0] and matrix[0][j]
        Add all vertices referenced in the adjacency matrix, but only add an
        edge if matrix[i][j] is not None
        Guaranteed that matrix will be square
        If matrix is nonempty, matrix[0][0] will be None
        :param matrix: an n x n square matrix (list of lists) representing Graph as adjacency map
        :return: None
        """
        for i in range(1, len(matrix)):         # add all vertices to begin with
            self.add_to_graph(matrix[i][0])
        for i in range(1, len(matrix)):         # go back through and add all edges
            for j in range(1, len(matrix)):
                if matrix[i][j] is not None:
                    self.add_to_graph(matrix[i][0], matrix[j][0], matrix[i][j])

    def graph2matrix(self) -> Matrix:
        """
        given a graph, creates an adjacency matrix of the type described in "construct_from_matrix"
        :return: Matrix
        """
        matrix = [[None] + [v_id for v_id in self.vertices]]
        for v_id, outgoing in self.vertices.items():
            matrix.append([v_id] + [outgoing.adj.get(v) for v in self.vertices])
        return matrix if self.size else None

    def graph2csv(self, filepath: str) -> None:
        """
        given a (non-empty) graph, creates a csv file containing data necessary to reconstruct that graph
        :param filepath: location to save CSV
        :return: None
        """
        if self.size == 0:
            return

        with open(filepath, 'w+') as graph_csv:
            csv.writer(graph_csv, delimiter=',').writerows(self.graph2matrix())

#============== Modify Graph Methods Below ==============#

    def reset_vertices(self) -> None:
        """
        Resets visited flags of all vertices within the graph
        """
        # Iterate over every vertex and set visited to False
        for id in self.vertices:
            self.vertices[id].visited = False

    def get_vertex(self, vertex_id: str) -> Vertex:
        """
        Returns the Vertex object with a given id or None if it doesn't exist
        :return: Vertex object with the id vertex_id
        """
        # Grab the Vertex from the vertices dictionary using vertex_id as the key
        return self.vertices.get(vertex_id)

    def get_vertices(self) -> Set[Vertex]:
        """
        Returns a set of all Vertex objects held in the graph
        :return: Set of all vertex objects held in the graph (could be empty)
        """
        # Create the output set
        output = set()
        # Iterate over vertices to fill the output set
        for id in self.vertices:
            output.add(self.vertices[id])
        # Return the output set
        return output

    def get_edge(self, start_id: str, dest_id: str) -> Tuple[str, str, float]:
        """
        Finds an edge connecting start_id to dest_id
        :param start_id: Starting vertex id
        :param dest_id: Destination vertex id
        :return: Edge in the form of a tuple (start_id, dest_id, weight) or None if it DNE
        """
        # Look for the starting vertex in all vertices
        start = self.vertices.get(start_id)
        if start is None:
            return None
        # Look for ending vertex in start's adjacent vertices
        end = start.adj.get(dest_id)
        if end is None:
            return None
        # Return the tuple
        return (start_id, dest_id, start.adj[dest_id])

    def get_edges(self) -> Set[Tuple[str, str, float]]:
        """
        Generates a set of all the edges in the graph
        :return: Set of tuples that represent all edges (start_id, other_id, weight)
        """
        # Create the output set
        output = set()
        # Look for edges at each vertex
        for id in self.vertices:
            for adjid in self.vertices[id].adj:
                # Add edge to the output set
                output.add((id, adjid, self.vertices[id].adj[adjid]))
        # Return the output set
        return output

    def bfs(self, start_id: str, target_id: str) -> Tuple[List[str], float]:
        """
        Perform a breadth-first search
        :param start_id: Starting vertex for BFS
        :param target_id: Ending vertex for BFS
        :return: Tuple with a list of vertex ids that were traversed and the distance travelled
        """
        # Init queue, list, distance, and history
        q = queue.SimpleQueue()
        ids = []
        dist = 0
        history = {}

        def visit(cur_id: str, prev_id: str):
            """
            Helper function for when a vertex is visited
            :param cur_id: ID of current vertex
            :param prev_id: ID of previous vertex
            """
            q.put(self.vertices[cur_id])
            self.vertices[cur_id].visited = True
            history[cur_id] = prev_id

        # Check if given ids are not valid
        if self.vertices.get(start_id) is None or self.vertices.get(target_id) is None:
            return ([], 0)
        # Visit start_id
        visit(start_id, "start")
        # Loop to do the traversal
        while not q.empty():
            # Pop top vertex
            popped = q.get()
            # Check if target_id is adjacent to popped
            if popped.adj.get(target_id) is not None:
                ids.append(target_id)
                ids.append(popped.id)
                prev = popped.id
                current = history[popped.id]
                dist += popped.adj[target_id]
                while (current != "start"):
                    ids.append(current)
                    dist += self.vertices[current].adj[prev]
                    prev = current
                    current = history[current]
                ids.reverse()
                return (ids, dist)
            # Visit each unvisited adjacent vertex of popped
            for adjs in popped.adj:
                if not self.vertices[adjs].visited:
                    visit(adjs, popped.id)
        # Target_id was not found
        return ([], 0)

    def dfs(self, start_id: str, target_id: str) -> Tuple[List[str], float]:
        """
        Performs a Depth First Search
        :param start_id: Starting vertex for DFS
        :param target_id: Ending vertex for DFS
        :return: Tuple with a list of vertex ids that were traversed and the distance travelled
        """
        
        # Check to see if invalid input
        if self.vertices.get(start_id) is None or self.vertices.get(target_id) is None:
            return ([], 0)

        # Call the inner function
        return self.dfs_inner(start_id, target_id, [])

    def dfs_inner(self, current_id: str, target_id: str, path:List[str]=[]) -> Tuple[List[str], float]:
        """
        Performs recursive work of DFS
        :param current_id: ID of current vertex
        :param target_id: ID of target vertex
        :param path: List of vertex id strings that connect start to target
        """
        # Visit the current vertex
        self.vertices[current_id].visited = True
        path.append(current_id)

        # Check if we are at target
        if current_id == target_id:
            dist = 0
            prev = None
            for current in path:
                if prev is not None:
                    dist += self.vertices[prev].adj[current]
                prev = current
            return (path, dist)

        # Visit adjacent vertices if not already visited
        initiallen = len(path)
        for adjs in self.vertices[current_id].adj:
            if not self.vertices[adjs].visited:
                tup = self.dfs_inner(adjs, target_id, path)
                if tup[0] != [] and tup[1] != 0:
                    return tup
                if len(path) != initiallen:
                    path = path[0:initiallen]
            
        # Return no path tuple
        return ([], 0)

    def detect_cycle(self) -> bool:
        """
        Detects if the graph contains a cycle using a BFS
        :return: True if the graph contains a cycle, otherwise False
        """
        result = False
        processing = {}
        for vid in self.vertices:
            if not self.vertices[vid].visited:
                if self.detect_cycle_inner(vid, processing):
                    result = True
                    break
        self.reset_vertices()
        return result
        
    def detect_cycle_inner(self, current_id: str, processing: dict) -> bool:
        """
        Performs recursive work of detect cycle
        :param current_id: ID of current vertex
        :param processing: Dictionary holding which vertex ids are being processed
        """
        # Mark as visited and processing
        self.vertices[current_id].visited = True
        processing[current_id] = True

        # Visit adjacent vertices
        for adjid in self.vertices[current_id].adj:
            if not self.vertices[adjid].visited:
                if self.detect_cycle_inner(adjid, processing):
                    return True
            elif processing.get(adjid) is not None and processing[adjid]:
                return True
        
        # Mark current vertex as not processing anymore
        processing[current_id] = False
        return False

    def a_star(self, start_id: str, target_id: str,
               metric: Callable[[Vertex, Vertex], float]) -> Tuple[List[str], float]:
        """
        Perform A* seach from one vertex to another
        :param start_id: ID of the starting index
        :param target_id: ID of the target index
        :param metric: Heuristic metric to use
        :return: Tuple containing path and distance travelled
        """
        # Init counter variables
        solution = ([], float("inf"))
        frontier = AStarPriorityQueue()
        infrontier = {}
        prev = {}

        # Fill frontier
        for vid in self.vertices:
            frontier.push(float("inf"), self.vertices[vid])

        # Check for invalid start or target
        if self.vertices.get(start_id) is None or self.vertices.get(target_id) is None:
            return ([], 0)

        # Initialize the A* Queue
        frontier.update(0, self.vertices[start_id])
        infrontier[start_id] = 0
        prev[start_id] = "start"

        # Traverse the graph using A*
        while not frontier.empty():
            # Remove the next node from frontier
            current = frontier.pop()
            # Remove the next node from infrontier
            infrontier.pop(current[1].id)
            # Add the node to the visited
            current[1].visited = True

            # Calculate dist and ids
            ids = []
            dist = 0
            if prev.get(current[1].id) and prev[current[1].id] != "start":
                previ = prev[current[1].id]
                ids.append(current[1].id)
                ids.append(previ)
                curr = prev[previ]
                dist += self.vertices[previ].adj[current[1].id]
                while (curr != "start"):
                    ids.append(curr)
                    dist += self.vertices[curr].adj[previ]
                    previ = curr
                    curr = prev[curr]
                ids.reverse()

            # Check if we made it to target node
            if current[1].id == target_id:
                if dist < solution[1]:
                    solution = (ids, dist)

            # Add all adjacent nodes to frontier with respective weights
            for adjid in current[1].adj:
                if (not self.vertices[adjid].visited) and (infrontier.get(adjid) is None):
                    g = self.vertices[current[1].id].adj[adjid] + dist
                    h = metric(self.vertices[adjid], self.vertices[target_id])
                    f = g + h
                    frontier.update(f, self.vertices[adjid])
                    infrontier[adjid] = g
                    prev[adjid] = current[1].id

        return solution

        

class AStarPriorityQueue:
    """
    Priority Queue built upon heapq module with support for priority key updates
    Created by Andrew McDonald
    Inspired by https://docs.python.org/2/library/heapq.html
    """

    __slots__ = ['data', 'locator', 'counter']

    def __init__(self) -> None:
        """
        Construct an AStarPriorityQueue object
        """
        self.data = []                        # underlying data list of priority queue
        self.locator = {}                     # dictionary to locate vertices within priority queue
        self.counter = itertools.count()      # used to break ties in prioritization

    def __repr__(self) -> str:
        """
        Represent AStarPriorityQueue as a string
        :return: string representation of AStarPriorityQueue object
        """
        lst = [f"[{priority}, {vertex}], " if vertex is not None else "" for
               priority, count, vertex in self.data]
        return "".join(lst)[:-1]

    def __str__(self) -> str:
        """
        Represent AStarPriorityQueue as a string
        :return: string representation of AStarPriorityQueue object
        """
        return repr(self)

    def empty(self) -> bool:
        """
        Determine whether priority queue is empty
        :return: True if queue is empty, else false
        """
        return len(self.data) == 0

    def push(self, priority: float, vertex: Vertex) -> None:
        """
        Push a vertex onto the priority queue with a given priority
        :param priority: priority key upon which to order vertex
        :param vertex: Vertex object to be stored in the priority queue
        :return: None
        """
        # list is stored by reference, so updating will update all refs
        node = [priority, next(self.counter), vertex]
        self.locator[vertex.id] = node
        heapq.heappush(self.data, node)

    def pop(self) -> Tuple[float, Vertex]:
        """
        Remove and return the (priority, vertex) tuple with lowest priority key
        :return: (priority, vertex) tuple where priority is key,
        and vertex is Vertex object stored in priority queue
        """
        vertex = None
        while vertex is None:
            # keep popping until we have valid entry
            priority, count, vertex = heapq.heappop(self.data)
        del self.locator[vertex.id]            # remove from locator dict
        vertex.visited = True                  # indicate that this vertex was visited
        while len(self.data) > 0 and self.data[0][2] is None:
            heapq.heappop(self.data)          # delete trailing Nones
        return priority, vertex

    def update(self, new_priority: float, vertex: Vertex) -> None:
        """
        Update given Vertex object in the priority queue to have new priority
        :param new_priority: new priority on which to order vertex
        :param vertex: Vertex object for which priority is to be updated
        :return: None
        """
        node = self.locator.pop(vertex.id)      # delete from dictionary
        node[-1] = None                         # invalidate old node
        self.push(new_priority, vertex)         # push new node

# Extra Credit Problem
def defeat_the_chonk(chonk: Graph) -> List[List[float]]:
    pass
