import unittest, string, math, random, cProfile
import numpy as np
from Graph import Graph, Vertex, AStarPriorityQueue, defeat_the_chonk


class GraphTests(unittest.TestCase):

    """
    Begin Vertex Tests
    """

    def test_degree(self):

        # (1) test a-->b and a-->c
        vertex = Vertex('a')
        vertex.adj['b'] = 1
        self.assertEqual(vertex.degree(), 1)
        vertex.adj['c'] = 3
        assert vertex.degree() == 2

        # (2) test a-->letter for all letters in alphabet
        vertex = Vertex('a')
        for i, char in enumerate(string.ascii_lowercase):
            self.assertEqual(i, vertex.degree())
            vertex.adj[char] = i

    def test_get_edges_vertex(self):

        # (1) test a-->b and a-->c
        vertex = Vertex('a')
        solution = {('b', 1), ('c', 2)}
        vertex.adj['b'] = 1
        vertex.adj['c'] = 2
        subject = vertex.get_edges()
        self.assertEqual(solution, subject)

        # (2) test empty case
        vertex = Vertex('a')
        solution = set()
        subject = vertex.get_edges()
        self.assertEqual(solution, subject)

        # (3) test a-->letter for all letters in alphabet
        for i, char in enumerate(string.ascii_lowercase):
            vertex.adj[char] = i
            solution.add((char, i))
        subject = vertex.get_edges()
        self.assertEqual(solution, subject)

    def test_distances(self):

        # (1) test pythagorean triple
        vertex_a = Vertex('a')
        vertex_b = Vertex('b', 3, 4)

        subject = vertex_a.euclidean_distance(vertex_b)
        self.assertEqual(5, subject)
        subject = vertex_b.euclidean_distance(vertex_a)
        self.assertEqual(5, subject)
        subject = vertex_a.taxicab_distance(vertex_b)
        self.assertEqual(7, subject)
        subject = vertex_b.taxicab_distance(vertex_a)
        self.assertEqual(7, subject)

        # (2) test linear difference
        vertex_a = Vertex('a')
        vertex_b = Vertex('b', 0, 10)

        subject = vertex_a.euclidean_distance(vertex_b)
        self.assertEqual(10, subject)
        subject = vertex_b.euclidean_distance(vertex_a)
        self.assertEqual(10, subject)
        subject = vertex_a.taxicab_distance(vertex_b)
        self.assertEqual(10, subject)
        subject = vertex_b.taxicab_distance(vertex_a)
        self.assertEqual(10, subject)

        # (3) test zero distance
        vertex_a = Vertex('a')
        vertex_b = Vertex('b')

        subject = vertex_a.euclidean_distance(vertex_b)
        self.assertEqual(0, subject)
        subject = vertex_b.euclidean_distance(vertex_a)
        self.assertEqual(0, subject)
        subject = vertex_a.taxicab_distance(vertex_b)
        self.assertEqual(0, subject)
        subject = vertex_b.taxicab_distance(vertex_a)
        self.assertEqual(0, subject)

        # (4) test floating point distance
        vertex_a = Vertex('a')
        vertex_b = Vertex('b', 5, 5)

        subject = vertex_a.euclidean_distance(vertex_b)
        self.assertAlmostEqual(5 * math.sqrt(2), subject)
        subject = vertex_b.euclidean_distance(vertex_a)
        self.assertAlmostEqual(5 * math.sqrt(2), subject)
        subject = vertex_a.taxicab_distance(vertex_b)
        self.assertEqual(10, subject)
        subject = vertex_b.taxicab_distance(vertex_a)
        self.assertEqual(10, subject)

    """
    End Vertex Tests
    """

    """
    Begin Graph Tests
    """

    def test_reset_vertices(self):

        graph = Graph()

        # (1) visit all vertices then reset
        graph.vertices['a'] = Vertex('a')
        graph.vertices['b'] = Vertex('b')

        for vertex in graph.vertices.values():
            vertex.visited = True
        graph.reset_vertices()
        for vertex in graph.vertices.values():
            self.assertFalse(vertex.visited)

    def test_get_vertex(self):

        graph = Graph()

        # (1) test basic vertex object
        vertex_a = Vertex('a')
        graph.vertices['a'] = vertex_a
        subject = graph.get_vertex('a')
        self.assertEqual(vertex_a, subject)

        # (2) test empty case
        subject = graph.get_vertex('b')
        self.assertIsNone(subject)

        # (3) test case with adjacencies
        vertex_b = Vertex('b')
        for i, char in enumerate(string.ascii_lowercase):
            vertex_b.adj[char] = i
        graph.vertices['b'] = vertex_b
        subject = graph.get_vertex('b')
        self.assertEqual(vertex_b, subject)

    def test_get_vertices(self):

        graph = Graph()
        solution = set()

        # (1) test empty graph
        subject = graph.get_vertices()
        self.assertEqual(solution, subject)

        # (2) test single vertex
        vertex = Vertex('$')
        graph.vertices['$'] = vertex
        solution.add(vertex)
        subject = graph.get_vertices()
        self.assertEqual(solution, subject)

        # (3) test multiple vertices
        graph = Graph()
        solution = set()
        for i, char in enumerate(string.ascii_lowercase):
            vertex = Vertex(char)
            graph.vertices[char] = vertex
            solution.add(vertex)
        subject = graph.get_vertices()
        self.assertEqual(solution, subject)

    def test_get_edge(self):

        graph = Graph()

        # (1) neither end vertex exists
        subject = graph.get_edge('a', 'b')
        self.assertIsNone(subject)

        # (2) one end vertex exists
        graph.vertices['a'] = Vertex('a')
        subject = graph.get_edge('a', 'b')
        self.assertIsNone(subject)

        # (3) both end vertices exist, but no edge
        graph.vertices['a'] = Vertex('a')
        graph.vertices['b'] = Vertex('b')
        subject = graph.get_edge('a', 'b')
        self.assertIsNone(subject)

        # (4) a -> b exists but b -> a does not
        graph.vertices.get('a').adj['b'] = 331
        subject = graph.get_edge('a', 'b')
        self.assertEqual(('a', 'b', 331), subject)
        subject = graph.get_edge('b', 'a')
        self.assertIsNone(subject)

        # (5) connect all vertices to center vertex and return all edges
        graph.vertices['$'] = Vertex('$')
        for i, char in enumerate(string.ascii_lowercase):
            graph.vertices[char] = Vertex(char)
            graph.vertices.get('$').adj[char] = i
        for i, char in enumerate(string.ascii_lowercase):
            subject = graph.get_edge('$', char)
            self.assertEqual(('$', char, i), subject)

    def test_get_edges(self):

        graph = Graph()

        # (1) test empty graph
        subject = graph.get_edges()
        self.assertEqual(set(), subject)

        # (2) test graph with vertices but no edges
        graph.vertices['a'] = Vertex('a')
        graph.vertices['b'] = Vertex('b')
        subject = graph.get_edges()
        self.assertEqual(set(), subject)

        # (3) test graph with one edge
        graph.vertices.get('a').adj['b'] = 331
        subject = graph.get_edges()
        self.assertEqual({('a', 'b', 331)}, subject)

        # (4) test graph with two edges
        graph = Graph()
        graph.vertices['a'] = Vertex('a')
        graph.vertices['b'] = Vertex('b')
        graph.vertices.get('a').adj['b'] = 331
        graph.vertices.get('b').adj['a'] = 1855
        subject = graph.get_edges()
        solution = {('a', 'b', 331), ('b', 'a', 1855)}
        self.assertEqual(solution, subject)

        # (5) test entire alphabet graph
        graph = Graph()
        solution = set()
        for i, char in enumerate(string.ascii_lowercase):
            graph.vertices[char] = Vertex(char)
            for j, jar in enumerate(string.ascii_lowercase):
                if i != j:
                    graph.vertices.get(char).adj[jar] = 26 * i + j
                    solution.add((char, jar, 26 * i + j))

        subject = graph.get_edges()
        self.assertEqual(solution, subject)

    def test_bfs(self):

        graph = Graph()

        # (1) test on empty graph
        subject = graph.bfs('a', 'b')
        self.assertEqual(([], 0), subject)

        # (2) test on graph missing start or dest
        graph.add_to_graph('a')
        subject = graph.bfs('a', 'b')
        self.assertEqual(([], 0), subject)
        subject = graph.bfs('b', 'a')
        self.assertEqual(([], 0), subject)

        # (3) test on graph with both vertices but no path
        graph.add_to_graph('b')
        subject = graph.bfs('a', 'b')
        self.assertEqual(([], 0), subject)

        # (4) test on single edge
        graph = Graph()
        graph.add_to_graph('a', 'b', 331)
        subject = graph.bfs('a', 'b')
        self.assertEqual((['a', 'b'], 331), subject)

        # (5) test on two edges
        graph = Graph()
        graph.add_to_graph('a', 'b', 331)
        graph.add_to_graph('b', 'c', 100)
        subject = graph.bfs('a', 'c')
        self.assertEqual((['a', 'b', 'c'], 431), subject)

        # (6) test on edge triangle and ensure one-edge path is taken
        # (bfs guarantees fewest-edge path, not least-weighted path)
        graph = Graph()
        graph.add_to_graph('a', 'b', 331)
        graph.add_to_graph('b', 'c', 100)
        graph.add_to_graph('a', 'c', 999)
        subject = graph.bfs('a', 'c')
        self.assertEqual((['a', 'c'], 999), subject)

        # (7) test on grid figure-8 and ensure fewest-edge path is taken
        graph = Graph(csv='test_csvs/bfs/7.csv')

        subject = graph.bfs('bottomleft', 'topleft')
        self.assertEqual((['bottomleft', 'midleft', 'topleft'], 2), subject)

        graph.reset_vertices()      # mark all unvisited
        subject = graph.bfs('bottomright', 'topright')
        self.assertEqual((['bottomright', 'midright', 'topright'], 2), subject)

        graph.reset_vertices()      # mark all unvisited
        subject = graph.bfs('bottomleft', 'topright')
        self.assertIn(subject[0], [['bottomleft', 'midleft', 'topleft', 'topright'],
                                   ['bottomleft', 'midleft', 'midright', 'topright'],
                                   ['bottomleft', 'bottomright', 'midright', 'topright']])
        self.assertEqual(3, subject[1])

        # (8) test on example graph from Onsay's slides, starting from vertex A
        # see bfs_graph.png
        graph = Graph(csv='test_csvs/bfs/8.csv')

        subject = graph.bfs('a', 'd')
        self.assertEqual((['a', 'b', 'd'], 4), subject)

        graph.reset_vertices()      # mark all unvisited
        subject = graph.bfs('a', 'f')
        self.assertEqual((['a', 'c', 'f'], 4), subject)

        graph.reset_vertices()      # mark all unvisited
        subject = graph.bfs('a', 'h')
        self.assertEqual((['a', 'e', 'h'], 4), subject)

        graph.reset_vertices()      # mark all unvisited
        subject = graph.bfs('a', 'g')
        self.assertEqual((['a', 'e', 'g'], 4), subject)

        graph.reset_vertices()      # mark all unvisited
        subject = graph.bfs('a', 'i')
        self.assertIn(subject[0], [['a', 'e', 'h', 'i'], ['a', 'e', 'g', 'i']])
        self.assertEqual(6, subject[1])

        # (9) test path which does not exist
        graph.reset_vertices()      # mark all unvisited
        graph.add_to_graph('z')
        subject = graph.bfs('a', 'z')
        self.assertEqual(([], 0), subject)

    def test_dfs(self):

        graph = Graph()

        # (1) test on empty graph
        subject = graph.dfs('a', 'b')
        self.assertEqual(([], 0), subject)

        # (2) test on graph missing start or dest
        graph.add_to_graph('a')
        subject = graph.dfs('a', 'b')
        self.assertEqual(([], 0), subject)
        subject = graph.dfs('b', 'a')
        self.assertEqual(([], 0), subject)

        # (3) test on graph with both vertices but no path
        graph.add_to_graph('b')
        subject = graph.dfs('a', 'b')
        self.assertEqual(([], 0), subject)

        # (4) test on single edge
        graph = Graph()
        graph.add_to_graph('a', 'b', 331)
        subject = graph.dfs('a', 'b')
        self.assertEqual((['a', 'b'], 331), subject)

        # (5) test on two edges
        graph = Graph()
        graph.add_to_graph('a', 'b', 331)
        graph.add_to_graph('b', 'c', 100)
        subject = graph.dfs('a', 'c')
        self.assertEqual((['a', 'b', 'c'], 431), subject)

        # (6) test on linear chain with backtracking distractors
        # see linear_graph.png
        graph = Graph(csv='test_csvs/dfs/6.csv')

        subject = graph.dfs('a', 'e')
        self.assertEqual((['a', 'b', 'c', 'd', 'e'], 4), subject)

        graph.reset_vertices()      # mark all unvisited
        subject = graph.dfs('e', 'a')
        self.assertEqual((['e', 'd', 'c', 'b', 'a'], 8), subject)

        # (7) test on linear chain with cycle
        # see cyclic_graph.png
        graph = Graph(csv='test_csvs/dfs/7.csv')

        subject = graph.dfs('a', 'd')
        self.assertIn(subject, [(['a', 'b', 'm', 'c', 'd'], 24),
                                (['a', 'b', 'n', 'c', 'd'], 28)])

        graph.reset_vertices()      # mark all unvisited
        subject = graph.dfs('d', 'a')
        self.assertIn(subject, [(['d', 'c', 'm', 'b', 'a'], 240),
                                (['d', 'c', 'n', 'b', 'a'], 280)])

        # (8) test path which does not exist on graph
        graph.reset_vertices()
        graph.add_to_graph('z')
        subject = graph.dfs('a', 'z')
        self.assertEqual(([], 0), subject)

    def test_detect_cycle(self):

        graph = Graph()

        # (1) test on empty graph
        self.assertFalse(graph.detect_cycle())

        # (2) 2 vertices, no cycles, no edges
        graph.add_to_graph('a', 'b')
        self.assertFalse(graph.detect_cycle())

        # (3) 2 vertices, no cycles, one edge
        graph.add_to_graph('a', 'b', 1)
        self.assertFalse(graph.detect_cycle())

        # (4) 2 vertices, one cycle
        graph.add_to_graph('b', 'a', 1)
        self.assertTrue(graph.detect_cycle())

        # (5) one vertex, one cycle
        graph = Graph()
        graph.add_to_graph('a','a', 1)
        self.assertTrue(graph.detect_cycle())

        # (6) two vertices, one cycle
        graph = Graph()
        graph.add_to_graph('a')
        graph.add_to_graph('b','b', 1)
        self.assertTrue(graph.detect_cycle())

        # (7) many vertices, several cycles
        graph = Graph()
        for id in string.ascii_lowercase:
            graph.add_to_graph(id)
        graph.add_to_graph('e', 'f', 1)
        graph.add_to_graph('f', 'g', 1)
        graph.add_to_graph('g', 'e', 1)
        graph.add_to_graph('z', 'h', 1)
        graph.add_to_graph('g', 'f', 1)
        graph.add_to_graph('z', 'a', 1)
        self.assertTrue(graph.detect_cycle())

        # (8) linked list
        graph = Graph()
        letters = list(string.ascii_lowercase)
        for i, id in enumerate(string.ascii_lowercase):
            if i+1 < len(letters):
                graph.add_to_graph(id, letters[i+1], 1)
        self.assertFalse(graph.detect_cycle())

        # (9) circular linked list
        graph.add_to_graph('z', 'a', 1)
        self.assertTrue(graph.detect_cycle())

        # (10a) big graph, no cycles
        graph = Graph()
        for i in range(200):
            for postfix in ['a', 'b', 'c', 'd']:
                graph.add_to_graph(str(i), str(i) + postfix, i)
                if postfix != 'd':
                    graph.add_to_graph(str(i) + postfix, str(i) + 'd', i)
            graph.add_to_graph(str(i), str(i+1), i)
        self.assertFalse(graph.detect_cycle())

        # (10b) big graph, one cycle
        graph.add_to_graph('124b', '33', 1)
        self.assertTrue(graph.detect_cycle())


    def test_graph_comprehensive(self):

        # construct random matrix
        random.seed(331)
        vertices = [s for s in string.ascii_lowercase]
        matrix = [[None] + vertices]
        probability = 0.1  # probability that two vertices are connected
        for i in range(1, len(matrix[0])):
            row = [matrix[0][i]]
            for j in range(1, len(matrix[0])):
                weight = (random.randint(1, 10))  # choose a random weight between 1 and 9
                connect = (random.random() < probability)  # connect if random draw in (0,1) < probability
                if i == j or not connect:  # such that p=0 never connects and p=1 always connects
                    weight = None  # do not connect vertex to self, either
                row.append(weight)
            matrix.append(row)

        # (1) test matrix2graph and graph2matrix
        graph = Graph()
        [graph.add_to_graph(letter) for letter in string.ascii_lowercase]  # prespecify order of vertices in dict
        graph.matrix2graph(matrix)
        subject = graph.graph2matrix()
        self.assertEqual(matrix, subject)

        # (2) test get_vertices by comparing certain invariants (ordering is not guaranteed under set)
        subject = graph.get_vertices()

        subject_ids = {vertex.id for vertex in subject}
        solution_ids = {letter for letter in string.ascii_lowercase}
        self.assertEqual(solution_ids, subject_ids)

        subject_degrees = {}
        for vertex in subject:
            degree = vertex.degree()
            if degree in subject_degrees:
                subject_degrees[degree] += 1
            else:
                subject_degrees[degree] = 1
        solution_degrees = {2: 8, 3: 7, 6: 1, 1: 5, 4: 3, 5: 1, 0: 1}
        self.assertEqual(solution_degrees, subject_degrees)

        # (3) test get_edges
        subject = graph.get_edges()
        solution = {('a', 's', 9), ('a', 't', 8), ('a', 'z', 6), ('b', 'l', 4), ('b', 'v', 9), ('c', 'k', 10),
                    ('c', 'u', 7), ('d', 'e', 1), ('d', 'i', 10), ('e', 'o', 5), ('e', 'q', 4), ('e', 'v', 8),
                    ('f', 'j', 6), ('g', 'h', 7), ('g', 'o', 4), ('g', 'r', 10), ('h', 'd', 4), ('h', 'k', 3),
                    ('h', 'l', 10), ('j', 'b', 5), ('j', 'o', 7), ('j', 'q', 7), ('j', 'r', 3), ('j', 'w', 6),
                    ('j', 'y', 2), ('k', 'z', 3), ('l', 'g', 7), ('l', 'h', 9), ('l', 'i', 10), ('l', 'w', 6),
                    ('m', 'a', 2), ('m', 'f', 10), ('m', 'j', 3), ('n', 't', 6), ('o', 'd', 5), ('o', 'l', 9),
                    ('p', 'q', 1), ('q', 'o', 4), ('q', 'z', 7), ('r', 'c', 4), ('s', 'i', 7), ('s', 'j', 8),
                    ('s', 'k', 8), ('s', 'w', 10), ('t', 'd', 1), ('t', 'g', 2), ('t', 'q', 7), ('t', 'u', 9),
                    ('u', 'g', 8), ('u', 'y', 3), ('v', 'i', 8), ('v', 'x', 5), ('w', 'c', 3), ('w', 'd', 2),
                    ('x', 'h', 7), ('x', 'j', 4), ('x', 'u', 3), ('y', 'e', 7), ('y', 'l', 4), ('y', 'n', 3),
                    ('z', 'j', 1), ('z', 'n', 4), ('z', 'q', 7), ('z', 's', 4), ('z', 'y', 5)}
        self.assertEqual(subject, solution)

        # define helper function to check validity of bfs/dfs result
        def is_valid_path(graph, search_result):
            path, dist = search_result
            length = 0
            for i in range(len(path) - 1):
                start, end = path[i], path[i + 1]
                edge = graph.get_edge(start, end)
                if edge is None:
                    return False  # path contains some edge not in the graph
                length += edge[2]
            return length == dist  # path consists of valid edges: return whether length matches

        # (4) check bfs/dfs on all pairs of vertices in graph
        for start in vertices:
            for end in vertices:
                if start != end:
                    # (5.1) test bfs
                    subject = graph.bfs(start, end)
                    self.assertTrue(is_valid_path(graph, subject))
                    graph.reset_vertices()

                    # (5.2) test dfs
                    subject = graph.bfs(start, end)
                    self.assertTrue(is_valid_path(graph, subject))
                    graph.reset_vertices()

    def test_a_star(self):

        #=== (A) Grid graph tests ===#
        graph = Graph()

        # (1) test on nxn grid from corner to corner: should shoot diagonal
        # (shortest path is unique, so each heuristic will return the same path)
        grid_size = 5
        for x in range(grid_size):
            for y in range(grid_size):
                idx = f"{x},{y}"
                graph.vertices[idx] = Vertex(idx, x, y)
        for x in range(grid_size):
            for y in range(grid_size):
                if x < grid_size - 1:
                    graph.add_to_graph(f"{x},{y}", f"{x+1},{y}", 1)
                    graph.add_to_graph(f"{x+1},{y}", f"{x},{y}", 1)
                if y < grid_size - 1:
                    graph.add_to_graph(f"{x},{y}", f"{x},{y+1}", 1)
                    graph.add_to_graph(f"{x},{y+1}", f"{x},{y}", 1)
                if x < grid_size - 1 and y < grid_size - 1:
                    graph.add_to_graph(f"{x},{y}", f"{x+1},{y+1}", math.sqrt(2))
                    graph.add_to_graph(f"{x+1},{y+1}", f"{x},{y}", math.sqrt(2))

        for metric in [Vertex.euclidean_distance, Vertex.taxicab_distance]:
            subject = graph.a_star('0,0', '4,4', metric)
            self.assertEqual(['0,0', '1,1', '2,2', '3,3', '4,4'], subject[0])
            self.assertAlmostEqual((grid_size - 1) * math.sqrt(2), subject[1])
            graph.reset_vertices()

        # (2) test on nxn grid with penalty for shooting diagonal
        # (shortest path is not unique, so each heuristic will return a different path)
        for x in range(grid_size-1):
            for y in range(grid_size-1):
                graph.add_to_graph(f"{x},{y}", f"{x+1},{y+1}", 3)
                graph.add_to_graph(f"{x+1},{y+1}", f"{x},{y}", 3)

        subject = graph.a_star('0,0', '4,4', Vertex.euclidean_distance)
        self.assertEqual((['0,0', '1,0', '1,1', '2,1', '2,2', '3,2', '3,3', '4,3', '4,4'], 8), subject)
        graph.reset_vertices()
        subject = graph.a_star('0,0', '4,4', Vertex.taxicab_distance)
        self.assertEqual((['0,0', '1,0', '2,0', '3,0', '4,0', '4,1', '4,2', '4,3', '4,4'], 8), subject)
        graph.reset_vertices()


        #=== (B) MSU graph tests ===#
        graph = Graph(csv='test_csvs/astar/msu_graph_csv.csv')
        # now must set of coordinates for each vertex:
        positions = [(0,0), (2,0), (4,0), (6,0), (9,0), (12,0), (2,5), (6,4), (12,4), (5,9), (8,8), (12,8), (8,10), (0,2),
                     (4,2), (9,2), (9,-2), (7,6), (8,11), (14,8)]
        for index, v_id in enumerate(list(graph.vertices)):
            graph.vertices[v_id].x, graph.vertices[v_id].y = positions[index]

        for metric in [Vertex.euclidean_distance, Vertex.taxicab_distance]:

            # (3) test Breslin to Union shortest path in both directions
            # (shortest path is unique, so each heuristic will return the same path)
            subject = graph.a_star('Breslin Center', 'Union', metric)
            solution = (['Breslin Center', 'A', 'B', 'G', 'J', 'M', 'Union'], 22)
            self.assertEqual(solution, subject)
            graph.reset_vertices()

            subject = graph.a_star('Union', 'Breslin Center', metric)
            solution = (['Union', 'M', 'J', 'G', 'B', 'A', 'Breslin Center'], 22)
            self.assertEqual(solution, subject)
            graph.reset_vertices()

            # (4) test Breslin to EB shortest path - bypass slow Shaw Ln
            # (shortest path is unique, so each heuristic will return the same path)
            subject = graph.a_star('Breslin Center', 'Engineering Building', metric)
            solution = (['Breslin Center', 'A', 'B', 'G', 'H', 'D', 'E', 'Engineering Building'], 34)
            self.assertEqual(solution, subject)
            graph.reset_vertices()

            subject = graph.a_star('Engineering Building', 'Breslin Center', metric)
            solution = (['Engineering Building', 'E', 'D', 'H', 'G', 'B', 'A', 'Breslin Center'], 34)
            self.assertEqual(solution, subject)
            graph.reset_vertices()

            # (5) test EB to The Rock shortest path - bypass slow Farm Ln
            # (shortest path is unique, so each heuristic will return the same path)
            subject = graph.a_star('Engineering Building', 'The Rock', metric)
            solution = (['Engineering Building', 'E', 'D', 'H', 'G', 'J', 'K', 'L', 'The Rock'], 34)
            self.assertEqual(solution, subject)
            graph.reset_vertices()

            subject = graph.a_star('The Rock', 'Engineering Building', metric)
            solution = (['The Rock', 'L', 'K', 'J', 'G', 'H', 'D', 'E', 'Engineering Building'], 34)
            self.assertEqual(solution, subject)
            graph.reset_vertices()

            # (6) test Union to Library - despite equal path lengths, A* heuristic will always prefer search to the left
            # (both heuristics will prefer the same path)
            subject = graph.a_star('Union', 'Library', metric)
            solution = (['Union', 'M', 'J', 'K', 'Library'], 8)
            self.assertEqual(solution, subject)
            graph.reset_vertices()

            subject = graph.a_star('Library', 'Union', metric)
            solution = (['Library', 'K', 'J', 'M', 'Union'], 8)
            self.assertEqual(solution, subject)
            graph.reset_vertices()

    def test_a_star_comprehensive(self):

        #=== (C) Random graph tests ===#
        # (1) initialize vertices of Euclidean and Taxicab weighted random graphs
        random.seed(331)
        probability = 0.5                                       # probability that two vertices are connected
        e_graph, t_graph = Graph(), Graph()
        vertices = []
        for s in string.ascii_lowercase:
            x, y = random.randint(0, 100), random.randint(0, 100)
            vertex = Vertex(s, x, y)
            vertices.append(vertex)
            e_graph.vertices[s], t_graph.vertices[s] = vertex, vertex
            e_graph.size += 1
            t_graph.size += 1

        # (2) construct adjacency matrix with edges weighted by appropriate distance metric
        e_matrix = [[None] + [s for s in string.ascii_lowercase]]
        t_matrix = [[None] + [s for s in string.ascii_lowercase]]
        for i in range(1, len(e_matrix[0])):
            e_row = [e_matrix[0][i]]
            t_row = [t_matrix[0][i]]
            for j in range(1, len(e_matrix[0])):
                connect = (random.random() < probability)           # connect if random draw in (0,1) < probability
                e_weighted_dist, t_weighted_dist = None, None
                if i != j and connect:
                    e_dist = vertices[i-1].euclidean_distance(vertices[j-1])
                    t_dist = vertices[i-1].taxicab_distance(vertices[j-1])
                    weight = (random.randint(1, 10))                         # choose a random weight between 1 and 9
                    e_weighted_dist = e_dist * weight                        # create realistic weighted dist
                    t_weighted_dist = t_dist * weight                        # create realistic weighted dist
                e_row.append(e_weighted_dist)
                t_row.append(t_weighted_dist)
            e_matrix.append(e_row)
            t_matrix.append(t_row)
        e_graph.matrix2graph(e_matrix)
        t_graph.matrix2graph(t_matrix)

        # (3) define helper function to check validity of search result
        def is_valid_path(graph, search_result):
            path, dist = search_result
            length = 0
            for i in range(len(path) - 1):
                start, end = path[i], path[i + 1]
                edge = graph.get_edge(start, end)
                if edge is None:
                    return False  # path contains some edge not in the graph
                length += edge[2]
            return length == dist  # path consists of valid edges: return whether length matches

        # (4) test all 26 x 26 pairwise A* traversals across random matrix and ensure they return valid paths w/o error
        for start in vertices:
            for end in vertices:
                if start != end:
                    subject = e_graph.a_star(start.id, end.id, Vertex.euclidean_distance)
                    self.assertTrue(is_valid_path(e_graph, subject))
                    e_graph.reset_vertices()

                    subject = t_graph.a_star(start.id, end.id, Vertex.taxicab_distance)
                    self.assertTrue(is_valid_path(t_graph, subject))
                    t_graph.reset_vertices()

    def test_profile(self):

        # use this testcase to evaluate your code's performance
        # replace function call inside string with any testcase to analyze
        print(cProfile.runctx("self.test_a_star_comprehensive()", globals(), locals()))

    """
    End Graph Tests
    """

    """
    Begin AStarPriorityQueue Tests (NOT FOR MIMIR - just for local development)
    """

    def test_apq(self):

        pq = AStarPriorityQueue()

        # test basics and ensure vertices are visited when popped
        for i, char in enumerate(string.ascii_lowercase):
            pq.push(-i, Vertex(char))
        for i, char in enumerate(reversed(string.ascii_lowercase)):
            priority, vertex = pq.pop()
            assert priority == -25+i
            assert vertex.id == char
            assert vertex.visited

        # test updating and ensure vertices are visited when popped
        for i, char in enumerate(string.ascii_lowercase):
            pq.push(i, Vertex(char))
        pq.update(-1, Vertex('z'))
        pq.update(100, Vertex('a'))
        priority, vertex = pq.pop()
        assert (priority, vertex.id, vertex.visited) == (-1, 'z', True)
        for i, char in enumerate(string.ascii_lowercase):
            if char != 'a' and char != 'z':
                priority, vertex = pq.pop()
                assert (priority, vertex.id, vertex.visited) == (i, char, True)
        priority, vertex = pq.pop()
        assert (priority, vertex.id, vertex.visited) == (100, 'a', True)
        assert pq.empty()   # assert trailing vertices are popped off properly

        # test to ensure Nones are popped off of the end (see SS20 Piazza post for concerns)
        pq = AStarPriorityQueue()
        for i, char in enumerate(string.ascii_lowercase):
            pq.push(i, Vertex(char))
        for i, char in enumerate(string.ascii_lowercase):
            pq.update(-i, Vertex(char))     # will force earlier nodes to be set to None and pushed to end of list
        for i, char in enumerate(reversed(string.ascii_lowercase)):
            priority, vertex = pq.pop()
            assert priority == -25+i
            assert vertex.id == char
            assert vertex.visited
        assert pq.empty()  # assert trailing vertices are popped off properly

    """
    End AStarPriorityQueue Tests
    """
    def test_chonk(self):
        chonk = Graph(csv='chonk.csv')
        check = np.loadtxt('chonk_solution.csv', delimiter=',', dtype=float).tolist()
        assert check == defeat_the_chonk(chonk)


if __name__ == '__main__':
    unittest.main()
