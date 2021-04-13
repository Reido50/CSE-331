<h1><strong>CC10 - SS21 - Dungeons, Dungeons, and More Dungeons</strong></h1>
<p><strong>Due: Tuesday, April 6th, 11:59 pm</strong></p>
<p><em><span style="font-weight: 400;">This is not a team project, do not copy someone else&rsquo;s work.</span></em></p>
<h1><strong>Introduction</strong></h1>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s3.amazonaws.com/mimirplatform.production/files/9ff62ece-4b02-4523-8ec6-76fc2b9fc381/00-featured-zelda-dungeons.jpeg" alt="00-featured-zelda-dungeons.jpeg" width="592" height="276" /></p>
<p><span style="font-weight: 400;">You are an aspiring game developer who loves playing adventure games, especially the Legend of Zelda series. After completing last week&rsquo;s coding challenge, you are inspired to try and create your own adventure game.</span></p>
<p><span style="font-weight: 400;"> Since you are new to game design, you decide to skip creating a player controller and dive right into creating your dungeons. Sadly, you&rsquo;re stuck at home right now, and can&rsquo;t have your friends playtest your dungeons. So, you decide to create a program that will judge whether or not your dungeons are good. This may not be the best idea, but you do what you can.</span></p>
<p><span style="font-weight: 400;">You&rsquo;re using an undirected graph to represent your dungeons, with vertices representing each room of the dungeon, and edges representing the connecting halls. From your vast amount of dungeon experience, you boil a good dungeon down to one thing: a non-linear design. This means that a good dungeon will have paths that lead back to rooms you&rsquo;ve already been to. </span></p>
<p><span style="font-weight: 400;">All the dungeons in the game are contained in the Game class, which holds a graph. Each dungeon is a subgraph of the Game graph that isn't connected to other subgraphs. Thus, a Game graph may contain several dungeons, each being a subgraph disconnected from other dungeons. </span></p>
<p><span style="font-weight: 400;">Your program will need to process all of the dungeons (subgraphs) in the Game graph. With CSE 331 being one of your favorite classes ever, you know that Professor Onsay has provided all the information you&rsquo;ll need to solve this. Should be a piece of cake!</span></p>
<h1><strong>Challenge</strong></h1>
<h2><strong>Overview</strong></h2>
<p><span style="font-weight: 400;">In this coding challenge, you will be creating a function that can (i) traverse a graph made up of smaller subgraphs (dungeons) and (ii) determine if each subgraph (dungeon) has paths that loop back to an already visited vertex. If a given subgraph (dungeon) has a path that loops back to an already visited vertex, that will be considered a good subgraph (dungeon). The function should return a count of how many good subgraphs (dungeons) the Game graph as a whole contains.</span></p>
<p><span style="font-weight: 400;">You will be implementing the </span><strong>count_good_dungeons</strong><span style="font-weight: 400;"> function that takes in a variable, </span><strong>game</strong><span style="font-weight: 400;">, containing a graph object holding all of the subgraphs (dungeons) in the game that you will be crawling. This function will return an integer that is equal to the count of how many of its subgraphs (dungeons) contain paths that loop back on themselves.</span></p>
<p><span style="font-weight: 400;">You are provided a premade Game class that is implemented using an adjacency list. The Game graph is made up of room nodes and that class is also provided. These classes and their functions can be found in the game.py file.</span></p>
<p><em><span style="font-weight: 400;">Modify the following function</span></em></p>
<p><strong>count_good_dungeons(game: Graph) -&gt; int</strong></p>
<ul>
<li><strong>game: Graph:</strong> <span style="font-weight: 400;">A graph that stores the subgraphs (dungeons) to check. Note that this graph may contain multiple separate subgraphs (dungeons).</span></li>
</ul>
<ul>
<li><strong>Return:</strong> <span style="font-weight: 400;">An integer that represents the count of how many good dungeons were found</span></li>
</ul>
<ul>
<li><strong>Time Complexity:</strong> <span style="font-weight: 400;"><strong>O(V + H))</strong> where V is the number of vertices in the graph and H is the number of hallways or edges in the graph</span></li>
</ul>
<ul>
<li><strong>Space Complexity:</strong> <span style="font-weight: 400;"><strong>O(V)</strong> where V is the number of vertices in the graph</span></li>
</ul>
<p>&nbsp;</p>
<p><em><span style="font-weight: 400;">Do </span></em><strong><em>NOT</em></strong><em><span style="font-weight: 400;"> modify the following functions. You will, however, need to use them in your solution.</span></em></p>
<p><strong>class Room:</strong></p>
<p><span style="font-weight: 400;">This class represents a room in a dungeon. It functions as a node/vertex in a graph and contains a <strong>room_id</strong> and a list of the rooms adjacent to it. It contains a function that will add adjacent rooms.</span></p>
<ul>
<li style="font-weight: 400;"><strong>Attributes:</strong></li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li>room_id: Any Hashable Type: <span style="font-weight: 400;">The identifying value of the room typically will be a string or an int, but could be anything. As long as it&rsquo;s hashable</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li>adjacent_rooms: List[Room]: <span style="font-weight: 400;">A list of adjacent room objects</span></li>
</ul>
</li>
</ul>
<ul>
<li style="font-weight: 400;"><strong>__init__(self, name: Any Hashable Type) -&gt; None:</strong>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Constructs a room object with the given name as the room_id</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>room_id: Any Hashable Type:</strong> <span style="font-weight: 400;">The identifying value of the room typically will be a string or an int, but could be anything. As long as it&rsquo;s hashable</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>adjacent_rooms: List[Room]:</strong> <span style="font-weight: 400;">A list of adjacent room objects</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>_adj_rooms_set: Set[ room_id]:</strong><span style="font-weight: 400;"> A set of adjacent room ideas. This is a private variable and should NOT be accessed outside of this class.</span></li>
<li><strong style="background-color: transparent; font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';">Return:</strong><span style="font-weight: 400;"> None</span></li>
</ul>
</li>
</ul>
<ul>
<li><strong>add_adjacent(self, adj_node: Room) -&gt; bool:</strong></li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">If the given node is not already in the room&rsquo;s adjacent rooms list then it will be added and True will be returned. Otherwise, it will not be added and False will be returned</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>adj_node: Room:</strong><span style="font-weight: 400;"> The room object to add to the room&rsquo;s adjacent list</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>Return:</strong><span style="font-weight: 400;"> A boolean representing whether or not the room could be added to adjacent list</span></li>
</ul>
</li>
</ul>
<p><strong>class Game:</strong></p>
<p><span style="font-weight: 400;">This class represents a graph implemented using an adjacency list and contains all of the rooms in the game. Rooms connect with one another to form dungeons. Note that you may not be able to travel from one node across the graph to another because each dungeon is a &ldquo;subgraph&rdquo; in the overall game graph. This class contains the functions <strong>add_to_game</strong> and <strong>add_hallway</strong>.</span></p>
<ul>
<li style="font-weight: 400;"><strong>Attributes:</strong></li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li>rooms: List[Room]:<span style="font-weight: 400;"> A list of all the room objects in the game.</span></li>
</ul>
</li>
</ul>
<ul>
<li style="font-weight: 400;"><strong>__init__(self) -&gt; None:</strong>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">This function will initialize a Game object and take in nothing as input</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>rooms: List[Room]:</strong><span style="font-weight: 400;"> A list of all the room objects in the game.</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>_rooms_set: Set[room_id]:</strong><span style="font-weight: 400;"> A set containing the id&rsquo;s of all the rooms in the game. This is a private variable and should NOT be accessed outside of the Game class.</span></li>
<li><strong style="background-color: transparent; font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';">Return:</strong><span style="font-weight: 400;"> None</span></li>
</ul>
</li>
</ul>
<ul>
<li><strong>add_to_game(self, room_id) -&gt; bool:</strong></li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Creates and adds a new room to the game with the provided room_id. Will return True if the room_id already exists in the game, False otherwise.</span></li>
<li style="font-weight: 400;"><strong>room_id: Any Hashable Type:</strong><span style="font-weight: 400;"> The value that will be used to create and identify the the new room</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>Return</strong>:<span style="font-weight: 400;"> A bool representing whether or not the room could be added to the game&rsquo;s room list.</span></li>
</ul>
</li>
</ul>
<ul>
<li><strong>add_hallway(self, start: room_id, end: room_id) -&gt; bool:</strong></li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">This function will add a hallway between the rooms with the given room_ids. If the hallway between the rooms could be created True will be returned, otherwise False will be returned.</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>room1: room_id:</strong> <span style="font-weight: 400;">The room_id of the first node to create the hallway to.&nbsp;</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>room2: room_id:</strong><span style="font-weight: 400;"> The room_id of the second node to create the hallway to.</span></li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>Return:</strong><span style="font-weight: 400;"> A bool representing whether or not a hallway could be added connecting room1 and room2.</span></li>
</ul>
</li>
</ul>
<h4><strong>Guarantees</strong></h4>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">No two rooms will have the same room_id; all room_ids will be </span><strong>unique</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">A room will never have a hallway directly to itself. For example: Room(A) can </span><strong>not</strong><span style="font-weight: 400;"> be adjacent to Room(A)</span></li>
</ul>
<h4><strong>Examples:</strong></h4>
<p>&nbsp;</p>
<p><span style="font-weight: 400;"><strong>Ex1:</strong> Empty. No Dungeons</span></p>
<p><img src="https://s3.amazonaws.com/mimirplatform.production/files/dd59388e-5534-4063-a6bf-dba55ab5fd30/graph1_empty.png" alt="graph1_empty.png" width="294" height="175" /></p>
<p><span style="font-weight: 400;">There are no rooms in this game, so the returned good dungeon count should be 0.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;"><strong>Ex 2</strong>: Three Rooms Not Connected. Three Dungeons.</span></p>
<p><img src="https://s3.amazonaws.com/mimirplatform.production/files/aa684c41-d480-4e40-ae55-b54e248a4347/graph4.png" alt="graph4.png" width="299" height="178" /></p>
<p><span style="font-weight: 400;">Three rooms exist in the game; however they are not connected so they comprise three separate dungeons. Since there are no hallways to create a path that leads back to a node, the good dungeon count is 0.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;"><strong>Ex 3:</strong> Three Rooms. Rooms A and B are connected and Rooms B and C are connected. One Dungeon.</span></p>
<p><img src="https://s3.amazonaws.com/mimirplatform.production/files/6f320f81-ef28-4f9c-9a02-dd85fbc88662/graph6.png" alt="graph6.png" width="290" height="173" /></p>
<p><span style="font-weight: 400;">Three rooms exist in the game, and since they are all connected in some way, one dungeon exists. However, a Path going from one node to another does not create a path that loops back. So, the returned good dungeon count is 0.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;"><strong>Ex 4:</strong> Three Rooms. A is connected to B, B is connected to C, and C is connected to A. One Dungeon.</span></p>
<p><span style="font-weight: 400;"><img src="https://s3.amazonaws.com/mimirplatform.production/files/b7159a59-478b-4f42-8787-17d7bc16d3c0/graph7.png" alt="graph7.png" width="305" height="181" /></span></p>
<p><span style="font-weight: 400;">Three rooms exist in the game, and since they are all connected in some way, one dungeon exists. A path that will come back to a room that already exists in the path can be found, so the good dungeon count is 1.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;"><strong>Ex 5:</strong> Five Rooms. A is connected to B, B is connected to C, and C is connected to A. D is connected to E. 2 Dungeons</span></p>
<p><span style="font-weight: 400;"><img src="https://s3.amazonaws.com/mimirplatform.production/files/c59109ea-27b4-4065-8262-e43e81a8a1db/graph8.png" alt="graph8.png" width="306" height="183" /></span></p>
<p><span style="font-weight: 400;">Five rooms exist in the game. Rooms A, B, and C connect to form a dungeon, and nodes D and E are connected to form a dungeon. However, dungeon ABC doesn&rsquo;t connect to dungeon DE, so two dungeons exist in this game. In dungeon ABC, a path that will come back to a room that already exists in the path can be found, so the good dungeon count is incremented to 1. However, in dungeon DE, the only paths are E-&gt;D and D-&gt;E, so no path comes back to a dungeon already in the path. The good dungeon counter stays at 1, and 1 is returned.</span></p>
<p>&nbsp;</p>
<h1><strong>Submission</strong></h1>
<p style="text-align: center;"><img src="https://s3.amazonaws.com/mimirplatform.production/files/d41109f1-542a-43ef-91b3-21ed49f3ced7/dampe.jpeg" alt="dampe.jpeg" width="362" height="296" /></p>
<h2><strong>Deliverables</strong></h2>
<p><span style="font-weight: 400;">Be sure to upload the following deliverables in a .zip folder to Mimir by </span><strong>11:59PM</strong><span style="font-weight: 400;"> Eastern Time on </span><strong>Tuesday, 04/13/2021</strong><span style="font-weight: 400;">.</span></p>
<p><span style="font-weight: 400;">Your .zip folder can contain other files (for example, description.md and tests.py), but must include (at least) the following:</span></p>
<pre><span style="font-weight: 400;">CC10.zip</span><br /><span style="font-weight: 400;"> &nbsp;&nbsp;&nbsp;|&mdash; CC10/</span><br /><span style="font-weight: 400;"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; README.xml &nbsp; &nbsp; &nbsp; (for coding challenge feedback)</span><br /><span style="font-weight: 400;"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; __init__.py&nbsp; &nbsp; &nbsp; (for proper Mimir testcase loading)</span><br /><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; solution.py&nbsp; &nbsp; &nbsp; (contains your solution source code)</span></pre>
<h2><span style="font-weight: 400;">Grading</span></h2>
<p><span style="font-weight: 400;">The following 100-point rubric will be used to determine your grade on CC10:</span></p>
<ul>
<li>Tests (65)</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">00 - Coding Standard: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">01 - Test Basic: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">02 - Test Good Dungeons: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">03 - Test Bad Dungeons: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">04 - Test Complex Dungeons: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">05 - Test Comprehensive: __/25</span></li>
</ul>
</li>
</ul>
<ul>
<li>Manual (35)</li>
</ul>
<ul>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">README.md is </span><em><span style="font-weight: 400;">completely</span></em><span style="font-weight: 400;"> filled out with (1) Name, (2) Feedback, (3) Time to Completion and (4) Citations: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time Complexity (O(V + H)): __/15</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Space Complexity (O(V)): __/15</span></li>
</ul>
</ul>
<p>&nbsp;</p>
<h1><span style="font-weight: 400;">Tips, Tricks, and Notes</span></h1>
<ul>
<li>You must fill out doc-strings!</li>
</ul>
<ul>
<li>Please fill out README, it&rsquo;s the easiest way to get points!</li>
<li>This coding challenge is essentially two separate problems put together. Try to solve each individually, then combine them together. This will help greatly with compartmentalizing the conceptualization.
<ol>
<li>Finding how many dungeons exist within your game</li>
<li>Finding whether or not there exists a room with a path of hallways back to itself in a dungeon</li>
</ol>
</li>
</ul>
<ul>
<li>Hint<span style="font-weight: 400;">: A small reward for reading all the way down here. Think about the algorithms you&rsquo;ve learned in class and see if there are any that are particularly good at crawling an undirected graph.</span></li>
</ul>
<ul>
<li>Also here&rsquo;s some Zelda music to listen to while working on this if you need more lots of great music from the Legend of Zelda series exists given them a look! Here&rsquo;s some of my favorites This is an awesome cover of <a style="font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; font-weight: 400;" href="https://youtu.be/VQnIRwEQER8" target="_blank" rel="noopener noreferrer">Farewell King Hyrule</a><span style="font-weight: 400;"> from Wind Waker, </span><a style="font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; font-weight: 400;" href="https://youtube.com/playlist?list=PLC5AE6E1EEA630D30" target="_blank" rel="noopener noreferrer">Skyward Sword OST</a><span style="font-weight: 400;"> (</span><a style="font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; font-weight: 400;" href="https://youtu.be/5xD1FAOJI84" target="_blank" rel="noopener noreferrer">Goose&rsquo;s Theme</a><span style="font-weight: 400;"> is my favorite here), </span><a style="font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; font-weight: 400;" href="https://youtube.com/playlist?list=PLwDEuPBgBi4NDcdlZrA-LCU7j-aUXzm_k" target="_blank" rel="noopener noreferrer">Breath of the Wild OST</a><span style="font-weight: 400;"> (My favorite here is the </span><a style="font-family: Geomanist, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; font-weight: 400;" href="https://youtu.be/GA3H8Ws8b3Q" target="_blank" rel="noopener noreferrer">Hyrule Castle Theme</a><span style="font-weight: 400;">)</span></li>
</ul>
<p><em><span style="font-weight: 400;">Created by Zach Arnold and Andy Wilson</span></em></p>