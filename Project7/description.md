<h1>Project 7 - Priority Queues &amp; Heaps</h1>
<p><strong>Due:&nbsp; Friday, April 2nd @ 11:59pm</strong></p>
<p><em>This is not a team project. Do not copy someone else's work.</em></p>
<h2>Description</h2>
<p><strong>Fig A: Priority Queue</strong></p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://www.techiedelight.com/wp-content/uploads/2016/11/Min-Heap.png" alt="Introduction to Priority Queues using Binary Heaps - Techie Delight" width="509" height="327" /></p>
<p>&nbsp;</p>
<p><strong>Fig B: Min-Heap and Max-Heap</strong></p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s3.amazonaws.com/mimirplatform.production/files/e508eda0-bedf-415c-8b7f-9fe1ada32f74/heaps.PNG" alt="heaps.PNG" width="604" height="242" /></p>
<p>&nbsp;</p>
<p>For this project, you will build a priority queue that is implemented as both a binary min-heap and binary max-heap. It will default to a min-heap. Essentially, a priority queue is a min-heap or max-heap, but instead of ordering itself based on value, it orders itself based on priority. You will then use this priority queue to implement a max-heap. The min-heap is taken care of for you, and is based on your max-heap implementation. As in, if your max-heap is correct, your min-heap will be too.</p>
<p><span style="text-decoration: underline;">Min-heaps</span> are a data structure that is a complete tree satisfying the heap property: Every child node must be larger than or equal to it's parent. This means the smallest node is always at the root of the tree. <span style="text-decoration: underline;">Max-heaps</span> are the same as min-heaps, with a different heap property: Every child node must be smaller than or equal to it's parent. This means the largest node is always at the root of the tree.</p>
<p>You will be using these two data structures to implement the priority queue, which is a complete tree with nodes having a key-value pair. The key denotes the node's priority, and value denotes the data the node holds. For a min-heap, the node with the smallest priority will always be at the root of the tree, and vice versa for the max heap.</p>
<p>The priority queue will use a list to store data. Despite the underlying data structure using a list, it can be represented as a tree (Fig. A). The list will hold MinNodes or MaxNodes (which you will implement). The node's ordering in the list determines the tree hierarchy: root is at index 0. Its left child is at index 1, and the right child at index 2. Etc.</p>
<h2>Assignment Overview + Clarification of Classes</h2>
<p>First, you will implement MinNode and MaxNode classes.</p>
<p><strong>MinNode vs MaxNode:</strong></p>
<blockquote>
<p><strong>MinNode:</strong></p>
<ul>
<li>Is a PriorityNode - has a priority and value.<br />
<ul>
<li>Despite the name, this class would be used within a priority queue that uses a min-heap, not within a normal min-heap. Normal min-heaps do not need nodes typically.</li>
</ul>
</li>
<li>Smaller numbers signify higher priority. Thus, nodes with smaller priorities and values are higher in the priority queue.</li>
</ul>
<p><strong>MaxNode:</strong></p>
<ul>
<li>Is a PriorityNode - has a priority and value.
<ul>
<li>Despite the name, this class would be used within a priority queue that uses a max-heap, not within a normal max-heap.</li>
</ul>
</li>
<li>Larger numbers signify higher priority. Thus, nodes with larger priorities and values are higher in the priority queue.</li>
</ul>
</blockquote>
<p>A PriorityNode has a priority and a value. The value is the node's data, while the priority is used to determine the node's ordering in the priority queue. MinNodes and MaxNodes are PriorityNodes - they have a priority and a value - but they change how the node is sorted within the priority queue. They do this by overriding the <span style="font-family: 'courier new', courier, monospace;">__lt__</span> and <span style="font-family: 'courier new', courier, monospace;">__gt__<span style="font-family: geomanist, sans-serif;"> magic functions.</span></span></p>
<p><span style="font-family: 'courier new', courier, monospace;"><span style="font-family: geomanist, sans-serif;">Both of these nodes are to be used within a priority queue. A MinNode is used to satisfy the min-heap property, and a MaxNode is used to satisfy the max-heap property. This is done so that the priority queue can be implemented as both a min-heap or max-heap simply by changing the type of node it uses (MinNode vs MaxNode).<br /></span></span></p>
<p>A MinNode wants lower priority nodes to be higher in the priority queue (children greater than the parent). A MaxNode wants to be sorted so that higher priority nodes will be higher in the priority queue (children less than parent). <span style="text-decoration: underline;">If the priorities are the same, the ordering is based on the value of each node - as in the value will act as the priority. If the node's have the same priority and value, then the nodes are already in the proper order relative to each other.</span></p>
<p>Next, you will be implementing a priority queue as a min-heap and max-heap, but with PriorityNodes (MinNode and MaxNode). You will then be implementing class MaxHeap, which will alter how values are pushed and popped from the heap (from the priority queue). It uses a PriorityQueue.&nbsp; You do not have to implement MinHeap. This is done for you, and will work if you properly implement MaxHeap.</p>
<p><strong><a href="https://anmolsehgal.medium.com/heap-vs-priority-queues-vs-queues-b03398312c87">Heaps vs Priority Queue:</a><br /></strong></p>
<blockquote>
<p><strong>Heaps:</strong></p>
<ul>
<li>Is either a complete tree satisfying the min-heap or a max-heap properties<br />
<ul>
<li>Values are pushed onto the "heap"</li>
</ul>
</li>
<li>Common implementation's use a list to store values
<ul>
<li>The list is known as the "heap"</li>
</ul>
</li>
<li>Does not typically use nodes, but rather just the values. We use Nodes where priority = value</li>
<li>Order is determined by the values</li>
</ul>
<p><strong>Priority Queue:</strong></p>
<ul>
<li>Complete tree implemented as either a min-heap, a max-heap, or both<br />
<ul>
<li>Uses a min-heap or max-heap to push Nodes onto the "heap"</li>
</ul>
</li>
<li>Common implementation's use a list to store values.
<ul>
<li>The list is known as the "heap"</li>
</ul>
</li>
<li>Uses nodes to keep track of a priority and a value (data)</li>
<li>Order is determined by the node's priorities. (If priorities are the same, common implementations sort on value, which was added first, or arbitrary (undefined). We use value as the second condition for ordering)</li>
</ul>
</blockquote>
<p>PriorityQueue will take a parameter at initialization (<span style="font-family: 'courier new', courier, monospace;">is_min</span>) to determine whether it uses/is a min-heap or a max-heap. This parameter determines if a MinNode (min-heap) or a MaxNode (max-heap) should be used within the priority queue. The priority queue pushes priorities and values onto the heap by creating MinNodes and MaxNodes and pushing those to the heap (both are PriorityNodes, just with different behavior based on <span style="font-family: 'courier new', courier, monospace;">__lt__</span> and <span style="font-family: 'courier new', courier, monospace;">__gt__</span>).&nbsp;</p>
<p>The MaxHeap will use a PriorityQueue, initializing the priority queue to act as a MaxHeap. MaxHeap does not use priorities. To do properly push onto the PriorityQueue, values should be pushed in a way that ignores priority. When popping from the MaxHeap, it will not return a node, just the value that was pushed onto the heap to begin with. Peeking at the heap will also need to return a value instead of a node. Essentially, the MaxHeap is abstracting away (hiding) the priority aspect of PriorityQueue.</p>
<h2>Assignment Specifications</h2>
<h3>Node classes:</h3>
<div>PriorityNode (Do Not Modify)</div>
<div>| ---- MinNode (Implement)</div>
<div>| ---- MaxNode (Implement)</div>
<blockquote>
<div><strong>class PriorityNode:</strong></div>
<div>
<ul>
<li>Implementation of a Priority Node - a Heap Node with a Priority</li>
</ul>
</div>
<div><em>DO NOT MODIFY the following attributes/functions</em></div>
<div>
<ul>
<li><strong>Attributes</strong>
<ul>
<li><strong>priority</strong>: Node's priority - determines its ordering in the priority queue.</li>
<li><strong>value:</strong> Node's value - Data associated with node. Can be anything. <span style="font-family: 'courier new', courier, monospace;">Int, float, dict, str,</span> or another object.</li>
</ul>
</li>
<li><a href="https://rszalski.github.io/magicmethods/"><strong>__init__(self, Priority: Any, val: Any)</strong></a>
<ul>
<li>Abstract function - you are not able to initialize a PriorityNode. Instead you must initialize the subclasses below (MaxNode and MinNode)</li>
<li><strong>priority</strong>: Priority to be stored in the node</li>
<li><strong>value</strong>: Data to be stored in the node</li>
</ul>
</li>
<li><a href="https://rszalski.github.io/magicmethods/"><strong>__str__(self) -&gt; str and __repr__(self) -&gt; str</strong></a>
<ul>
<li>This method is inherited by MinNode and MaxNode. Hence, they are use this as their __str__ method.</li>
<li>Represents nodes as a string in the form &lt;priority_of_node, value_data_held_by_node&gt;. <span class="frontend-shared-components-CodeHighlight-___CodeHighlight__code-highlight___YBGmv  ">Thus, <code>&lt;1, 10&gt;</code> indicates a Min or Max node object with a priority of 1 holding a value of 10 as an integer, whereas <code>&lt;1, None&gt;</code> indicates a node with a priority of 1 holding a value of <code>None</code>.</span></li>
<li>Note that Python will automatically invoke this function when using printing a <code>Node</code> to the console, and PyCharm will automatically invoke this function when displaying a <code>Node</code> in the debugger.</li>
<li>Call this with <code>str(node)</code> (rather than <code>node.__str__()</code>).</li>
<li><strong>Returns</strong>: str</li>
</ul>
</li>
<li><a href="https://rszalski.github.io/magicmethods/"><strong>__eq__(self, other: "PriorityNode") -&gt; bool</strong></a>
<ul>
<li>Equality comparator for when priority nodes are equal</li>
<li><strong>other</strong>: second node to compare self to</li>
<li><strong>Returns</strong>: True if the nodes are equal, False if otherwise</li>
</ul>
</li>
</ul>
</div>
<div>&nbsp;</div>
<div><strong>class MaxNode:</strong></div>
<div>
<ul>
<li>Implementation of a priority node for a priority queue max-heap.Nodes with higher priority values are at the top of the priority queue.</li>
<li><strong>Will help to implement MinNode first</strong>.</li>
</ul>
</div>
<div><em>DO NOT MODIFY the following attributes/functions</em></div>
<div>
<ul>
<li><strong>Attributes</strong>
<ul>
<li><strong>priority</strong>: Node's priority - determines its ordering in the priority queue.</li>
<li><strong>value:</strong> Node's value - Data associated with node. Can be anything. <span style="font-family: 'courier new', courier, monospace;">Int, float, dict, str,</span> or another object.</li>
</ul>
</li>
<li><strong>__init__(self, Priority: Any, val: Any)</strong>
<ul>
<li>Upcalls to PriorityNode constructor. Constructs a MaxNode.</li>
<li>Object constructor - this function is called when initializing an instance of this class. Create a MaxNode by doing:
<ul>
<li>node = MaxNode(priority, value)</li>
</ul>
</li>
<li><strong>priority</strong>: Priority to be stored in the node</li>
<li><strong>value</strong>: Data to be stored in the node</li>
</ul>
</li>
</ul>
</div>
<div><span class="frontend-shared-components-CodeHighlight-___CodeHighlight__code-highlight___YBGmv  "><em>IMPLEMENT the following functions</em></span></div>
<div>
<ul>
<li><a href="https://rszalski.github.io/magicmethods/"><strong>__lt__(self, other: "PriorityNode") -&gt; bool</strong></a>
<ul>
<li>Less than comparator. Determines if <strong>self </strong>is&nbsp;greater than <strong>other</strong> node, and thus should be sorted <span style="text-decoration: underline;">lower</span> than <strong>other</strong> node in priority queue.</li>
<li>Defines behavior for the less-than operator "&lt;". Compare nodes by doing:
<ul>
<li>node1 &lt; node2</li>
</ul>
</li>
<li><span style="text-decoration: underline;">Tip</span>: Because PriorityQueue defaults to a min-heap, this function does the opposite of what is expected from a __lt__ function. Read below:</li>
<li>To implement this properly, it should return the opposite of what is expected from __lt__ / the opposite as MinNode. As in, if <strong>self</strong> is less than <strong>other</strong>, this function should return false.<br />
<ul>
<li>Less means that self has a priority lower in magnitude than other, or if the priorities are the same, self has a lower value than other. If this is the case, return False.</li>
<li>Examples:
<ul>
<li>node &lt;5, 1&gt;&nbsp; is greater than node &lt;2, 2&gt; because priority 5 is greater than priority 2. Thus, return True.</li>
<li>node &lt;1, 5&gt;&nbsp; is greater than node &lt;1, 2&gt; because the priorities are the same and value 5 is greater than value 2. Thus return True.</li>
<li>node &lt;1, 1&gt; is not greater than node &lt;1, 1&gt; because they have equal priorities and values.</li>
</ul>
</li>
</ul>
</li>
<li><strong>other</strong>: node to compare self to<strong><br /></strong></li>
<li><strong>Returns</strong>: bool - False if <strong>self</strong> is less than <strong>other</strong>, True if <strong>self</strong> is greater than <strong>other</strong></li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><a href="https://rszalski.github.io/magicmethods/"><strong>__gt__(self, other: "PriorityNode") -&gt; bool</strong></a></li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li>Greater than comparator. Determines if <strong>self</strong> node is less than <strong>other</strong> node, and thus should be sorted <span style="text-decoration: underline;">higher</span> than <strong>other</strong> node in priority queue.</li>
<li>Defines behavior for the greater-than operator "&gt;". Compare nodes by doing:
<ul>
<li>node1 &gt; node2</li>
</ul>
</li>
<li><u>Tip</u>: Because PriorityQueue defaults to a min-heap, this function does the opposite of what is expected from a __gt__ function. Read below:</li>
<li>To implement this properly, it should return the opposite of what is expected from __gt__ / the opposite as MinNode. As in, if <strong>self</strong> is greater than <strong>other</strong>, this function should return false.
<ul>
<li>Greater means that self has a priority greater in magnitude than other, or if the priorities are the same, self has a greater value than other. If this is the case, return False.</li>
<li>Examples:
<ul>
<li>node &lt;1, 1&gt;&nbsp; is less than node &lt;2, 2&gt; because priority 1 is less than priority 2. Thus, return True.</li>
<li>node &lt;1, 1&gt;&nbsp; is less than node &lt;1, 2&gt; because the priorities are the same and value 1 is less than value 2. Thus return True.</li>
<li>node &lt;1, 1&gt; is not less than node &lt;1, 1&gt; because they have equal priorities and values.</li>
</ul>
</li>
</ul>
</li>
<li><strong>other</strong>: node to compare self to<strong><br /></strong></li>
<li><strong>Returns</strong>: bool - False if <strong>self</strong> is greater than <strong>other</strong>, True if <strong>self</strong> is less than <strong>other</strong></li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
</ul>
</div>
<div>&nbsp;</div>
<div><strong>class MinNode:</strong></div>
<div>
<ul>
<li>Implementation of a priority node for a priority queue min-heap.Nodes with lower priority values are at the top of the priority queue.</li>
</ul>
</div>
<div><em>DO NOT MODIFY the following attributes/functions</em></div>
<div>
<ul>
<li><strong>Attributes</strong>
<ul>
<li><strong>priority</strong>: Node's priority - determines its ordering in the priority queue.</li>
<li><strong>value:</strong> Node's value - Data associated with node. Can be anything. <span style="font-family: 'courier new', courier, monospace;">Int, float, dict, str,</span> or another object.</li>
</ul>
</li>
</ul>
<ul>
<li><strong>__init__(self, Priority: Any, val: Any)</strong>
<ul>
<li>Upcalls to PriorityNode constructor. Constructs a MinNode.</li>
<li><strong>priority</strong>: Priority to be stored in the node</li>
<li><strong>value</strong>: Data to be stored in the node</li>
</ul>
</li>
</ul>
</div>
<div><span class="frontend-shared-components-CodeHighlight-___CodeHighlight__code-highlight___YBGmv  "><em>IMPLEMENT the following functions</em></span></div>
<div>
<ul>
<li><strong>__lt__(self, other: "PriorityNode") -&gt; bool</strong><br />
<ul>
<li>Less than comparator. Determines if <strong>self</strong> node is less than <strong>other</strong> node, and thus should be sorted <span style="text-decoration: underline;">higher</span> than <strong>other</strong> node in priority queue.</li>
<li>Defines behavior for the less-than operator "&lt;". Compare nodes by doing:
<ul>
<li>node1 &lt; node2</li>
</ul>
</li>
<li>Less means that self has a priority lower in magnitude than other, or if the priorities are the same, self has a lower value than other. If this is the case, the function returns true.
<ul>
<li>Examples:
<ul>
<li>node &lt;1, 1&gt;&nbsp; is less than node &lt;2, 2&gt; because priority 1 is less than priority 2. Thus, return True.</li>
<li>node &lt;1, 1&gt;&nbsp; is less than node &lt;1, 2&gt; because the priorities are the same and value 1 is less than value 2. Thus return True.</li>
<li>node &lt;1, 1&gt; is not less than node &lt;1, 1&gt; because they have equal priorities and values.</li>
</ul>
</li>
</ul>
</li>
<li><strong>other</strong>: node to compare self to<strong><br /></strong></li>
<li><strong>Returns</strong>: bool - True if <strong>self</strong> is less than <strong>other</strong>, False is <strong>self</strong> is greater than <strong>other</strong></li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>__gt__(self, other: "PriorityNode") -&gt; bool</strong>
<ul>
<li>Greater than comparator. Determines if <strong>self</strong> node is greater than <strong>other</strong> node, and thus should be sorted <span style="text-decoration: underline;">lower</span> than <strong>other</strong> node in priority queue.</li>
<li>Defines behavior for the greater-than operator "&gt;". Compare nodes by doing:
<ul>
<li>node1 &gt; node2</li>
</ul>
</li>
<li>Greater means that self has a priority higher in magnitude than other, or if the priorities are the same, self has a higher value than other. If this is the case, the function returns true.
<ul>
<li>Examples:
<ul>
<li>node &lt;5, 1&gt;&nbsp; is greater than node &lt;2, 2&gt; because priority 5 is greater than priority 2. Thus, return True.</li>
<li>node &lt;1, 5&gt;&nbsp; is greater than node &lt;1, 2&gt; because the priorities are the same and value 5 is greater than value 2. Thus return True.</li>
<li>node &lt;1, 1&gt; is not greater than node &lt;1, 1&gt; because they have equal priorities and values.</li>
</ul>
</li>
</ul>
</li>
<li><strong>other</strong>: node to compare self to<strong><br /></strong></li>
<li><strong>Returns</strong>: bool - True if <strong>self</strong> is greater than <strong>other</strong>, False if <strong>other</strong> is less than <strong>other</strong></li>
<li>Time Complexity: O(1)</li>
</ul>
</li>
</ul>
</div>
<ul>
<li style="list-style-type: none;">
<ul>
<li>
<div>Space Complexity: O(1)</div>
</li>
</ul>
</li>
</ul>
</blockquote>
<h3>Priority Queue/ Heap Classes:</h3>
<div>PriorityQueue (Implement)</div>
<div>MaxHeap (Implement)</div>
<div>| ---- MinHeap (Do Not Modify)</div>
<blockquote>
<div><strong>class PriorityQueue:</strong></div>
<div>
<ul>
<li>Implementation of a priority queue - the highest/lowest priority elements are at the front (root). Can act as a min or max-heap.</li>
</ul>
</div>
<div><em>DO NOT MODIFY the following attributes/functions</em></div>
<div>
<ul>
<li><strong>Attributes</strong>
<ul>
<li><strong>_data</strong>: List that holds all nodes on heap</li>
<li><strong>_is_min</strong>: Bool - True if priority queue is a min-heap, False if max-heap</li>
</ul>
</li>
<li><strong>__init__(self, is_min: bool = True)</strong>
<ul>
<li>Constructs the priority queue</li>
<li><strong>Is_min</strong>: If the priority queue acts as a priority min or max-heap.</li>
</ul>
</li>
<li><strong>__str__(self) -&gt; str and __repr__(self) -&gt; str<br /></strong>
<ul>
<li>Represents the priority queue as a string</li>
<li>Call this with <code>str(pqueue)</code> (rather than <code>pqueue.__str__()</code>).</li>
<li><strong>Returns</strong>: str - string representation of the heap</li>
<li>Time Complexity: O(N)</li>
<li>Space Complexity: O(N)</li>
</ul>
</li>
<li><strong>to_tree_str(self) -&gt; str</strong>
<ul>
<li>Represents the priority queue as a string in the format of a tree:</li>
<li>Example:<br />
<ul>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; root</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; /&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; left_child &nbsp; &nbsp;&nbsp; right_child</li>
</ul>
</li>
<li><strong>Returns</strong>: str - String to print</li>
<li>Time Complexity: O(N)</li>
<li>Space Complexity: O(N)</li>
</ul>
</li>
<li><strong>is_min_heap(self) -&gt; bool</strong>
<ul>
<li>Check if priority queue is a min or a max-heap</li>
<li><strong>Returns</strong>: True if min-heap, False if max-heap</li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
</ul>
</div>
<div><span class="frontend-shared-components-CodeHighlight-___CodeHighlight__code-highlight___YBGmv  "><em>IMPLEMENT the following functions</em></span></div>
<div>
<ul>
<li><a href="https://rszalski.github.io/magicmethods/"><strong> __len__(self) -&gt; int</strong></a>
<ul>
<li>Determine the amount of nodes on the heap</li>
<li>Call this with <code>len(pqueue)</code> (rather than <code>pqueue.__len__()</code>).</li>
<li><strong>Returns</strong>: The amount of nodes in the priority queue.</li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>empty(self) -&gt; bool</strong>
<ul>
<li>Public method</li>
<li>Checks if the heap is empty</li>
<li><strong>Returns</strong>: bool - True if Empty, else False</li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>peek(self) -&gt; PriorityNode<br /></strong>
<ul>
<li>Public method</li>
<li>Gets the root node (min or max node)</li>
<li><strong>Returns</strong>: MinNode or MaxNode - None if heap is empty, else root node</li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>get_left_child_index(self, index: int) -&gt; int</strong><br />
<ul>
<li>Gets the specified parent node's left child index</li>
<li><strong>Index</strong>: Index of parent node</li>
<li><strong>Returns</strong>: Index of left child or None if it does not exist (invalid)</li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>get_right_child_index(self, index: int) -&gt; int</strong>
<ul>
<li>Desc: Gets the specified parent node's right child index</li>
<li><strong>Index</strong>: Index of parent node</li>
<li><strong>Returns</strong>: Index of right child or None if it does not exist (invalid)</li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>get_parent_index(self, index: int) -&gt; int</strong>
<ul>
<li>Gets the specified child node's parent index</li>
<li><strong>Index</strong>: Index of child node</li>
<li><strong>Returns</strong>: Index of parent or None if does not exist (root)</li>
<li>Time Complexity: O(1)</li>
<li>Spacestring representation of the heap Complexity: O(1)</li>
</ul>
</li>
<li><strong>push (self, priority: Any, val: Any) -&gt; None</strong>
<ul>
<li>Public method</li>
<li>Inserts a node with the specified priority/value pair onto the heap</li>
<li>Hint: Use one of the percolate functions here</li>
<li><strong>Priority</strong>: Node's priority</li>
<li><strong>Val</strong>: Node's value</li>
<li><strong>Returns</strong>: None</li>
<li>Time Complexity: O(log[N])*</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>pop(self) -&gt; PriorityNode<br /></strong>
<ul>
<li>Public method</li>
<li>Removes the top priority node from heap (min or max element)</li>
<li>Hint: Use one of the percolate functions here</li>
<li><strong>Returns</strong>: MinNode or MaxNode - The root node of the heap (min or max element)</li>
<li>Time Complexity: O(log(N))*</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>get_minmax_child_index(self, index: int) -&gt; int</strong>
<ul>
<li>Gets the specified parent's min (min-heap) or max (max-heap) child index</li>
<li><strong>Index</strong>: Index of parent element</li>
<li><strong>Returns</strong>: Index of min child (if min-heap) or max child (if max-heap) or None if invalid</li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>percolate_up(self, index: int) -&gt; None</strong>
<ul>
<li>Moves a node in the queue/heap up to its correct position (level in the tree).</li>
<li><strong>Index</strong>: Index of node to be percolated up</li>
<li><strong>Returns</strong>: None</li>
<li>Time Complexity: O(log(N))</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>percolate_down(self, index: int) -&gt; None</strong>
<ul>
<li>Moves a node in the queue/heap down to its correct position (level in the tree).</li>
</ul>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<ul>
<li><strong>Index</strong>: Index of node to be percolated down</li>
<li>Returns: None</li>
<li>Time Complexity: O(log(N))</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
</ul>
</div>
<div>&nbsp;</div>
<div><strong>class MaxHeap</strong>:</div>
<div>
<ul>
<li>Implementation of a max-heap - &nbsp;the highest value is at the front (root).</li>
<li>Initializes a PriorityQueue with is_min set to False.</li>
<li>Uses the priority queue to satisfy the min heap properties by initializing the priority queue as a max-heap, and then using value as both the priority and value.</li>
</ul>
</div>
<div><em>DO NOT MODIFY the following attributes/functions</em></div>
<div>
<ul>
<li><strong>Attributes</strong>
<ul>
<li><strong>_pqueue</strong>: PriorityQueue to use as a MaxHeap</li>
</ul>
</li>
<li><strong>__init__(self)<br /></strong>
<ul>
<li>Constructs the max-heap</li>
<li>Upcalls PriorityQueue constructor with _is_min set to False</li>
</ul>
</li>
<li><strong>__str__(self) -&gt; str and __repr__(self) -&gt; str</strong>
<ul>
<li>Represents the max-heap as a string</li>
<li>Call this with <code>str(maxheap)</code> (rather than <code>maxheap.__str__()</code>).</li>
<li><strong>Returns</strong>: str - String representation of the heap</li>
<li>Time Complexity: O(N)</li>
<li>Space Complexity: O(N)</li>
</ul>
</li>
<li><strong>to_tree_str(self) -&gt; str</strong>
<ul>
<li>Represents the priority queue as a string in the format of a tree:</li>
<li>Example:<br />
<ul>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; root</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; /&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \</li>
<li>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; left_child &nbsp; &nbsp;&nbsp; right_child</li>
</ul>
</li>
<li><strong>Returns</strong>: str - String to print</li>
<li>Time Complexity: O(N)</li>
<li>Space Complexity: O(N)</li>
</ul>
</li>
<li><strong>__len__(self) -&gt; int</strong><br />
<ul>
<li>Determine the amount of nodes on the heap</li>
<li>Call this with <code>len(maxheap)</code> (rather than <code>maxheap.__len__()</code>).</li>
<li><strong>Returns</strong>: The amount of nodes in the priority queue.</li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>empty(self) -&gt; bool</strong>
<ul>
<li>Public method</li>
<li>Checks if the heap is empty</li>
<li><strong>Returns</strong>: bool - True if Empty, else False</li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
</ul>
</div>
<div><span class="frontend-shared-components-CodeHighlight-___CodeHighlight__code-highlight___YBGmv  "><em>IMPLEMENT the following functions</em></span></div>
<div>
<ul>
<li><strong>peek(self) -&gt; Any</strong>
<ul>
<li>Public method</li>
<li>Gets the max element's value (root node's value)</li>
<li><strong>You may not access private member variables of PriorityQueue. Doing so will result in a 0 for this function and any related testcases manual or otherwise.<br /></strong></li>
<li><strong>Returns</strong>: None if heap is empty, else root's value</li>
<li>Time Complexity: O(1)</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>push (self, Val: Any) -&gt; None</strong>
<ul>
<li>Public method</li>
<li>Inserts a node with the specified value onto the heap</li>
<li><strong>You may not access private member variables of PriorityQueue</strong>. <strong>Doing so will result in a 0 for this function and any related testcases manual or otherwise.</strong></li>
<li><strong>Val</strong>: Node's value</li>
<li><strong>Returns</strong>: None</li>
<li>Time Complexity: O(log[N])*</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
<li><strong>pop(self) -&gt; Any</strong>
<ul>
<li>Public method</li>
<li>Removes the max element from the heap</li>
<li><strong>You may not access private member variables of PriorityQueue. Doing so will result in a 0 for this function and any related testcases manual or otherwise.</strong></li>
<li><strong>Returns</strong>: Value of max element</li>
<li>Time Complexity: O(log(N))*</li>
<li>Space Complexity: O(1)</li>
</ul>
</li>
</ul>
</div>
<div>&nbsp;</div>
<div><strong>class MinHeap(MaxHeap)</strong>:</div>
<div>
<ul>
<li>Implementation of a max-heap - &nbsp;the highest value is at the front (root).</li>
<li>Initializes a PriorityQueue with is_min set to True.</li>
<li>Inherits from MaxHeap because it uses the same exact functions, but instead has a priority queue with a min-heap.</li>
</ul>
</div>
<div><em>DO NOT MODIFY the following attributes/functions</em></div>
<div>
<ul>
<li><strong>Attributes</strong>
<ul>
<li><strong>_pqueue</strong>: PriorityQueue to use as a MinHeap</li>
</ul>
</li>
<li><strong>__init__(self)<br /></strong>
<ul>
<li>Constructs the max-heap</li>
<li>Upcalls PriorityQueue constructor with _is_min set to False</li>
</ul>
</li>
<li><strong>__str__(self) -&gt; str and __repr__(self) -&gt; str</strong><strong><br /></strong>
<ul>
<li>Represents the max-heap as a string</li>
<li>Call this with <code>str(maxheap)</code> (rather than <code>maxheap.__str__()</code>).</li>
<li><strong>Returns</strong>: str - String representation of the heap</li>
<li>Time Complexity: O(N)</li>
<li>Space Complexity: O(N)</li>
</ul>
</li>
</ul>
</div>
</blockquote>
<p><a href="https://medium.com/@satorusasozaki/amortized-time-in-the-time-complexity-of-an-algorithm-6dd9a5d38045">*Amortized Time Complexity</a></p>
<h3>Heap Sort:</h3>
<p>Heap sort is an algorithm that sorts using a Binary Heap data structure. The root node of a heap is guaranteed to be the next smallest element (min-heap) or next largest element (max-heap) which is a useful property for sorting a list.</p>
<blockquote>
<div><strong>heap_sort(array: List[Any]) -&gt; None</strong></div>
<ul>
<li>
<div>Sort array in-place using heap sort algorithm w/ max-heap</div>
<div>
<ul>
<li>You are not allowed to create a new list and append values onto it. You must modify the original array (in-place).</li>
<li><strong>CREATING A NEW LIST WILL RESULT IN ZERO POINTS FOR THIS FUNCTION (ITS TEST CASES AND THE MANUAL GRADING)</strong></li>
</ul>
</div>
</li>
<li>
<div><strong>You may not access private member variables of PriorityQueue, MinHeap, or MaxHeap. Doing so will result result in a 0 points for this function's test case.<br /></strong></div>
</li>
<li>
<div><strong>Array</strong>: List to be sorted</div>
</li>
<li>
<div><strong>Returns</strong>: None</div>
</li>
<li>
<div>Time Complexity: O(Nlog(N))</div>
</li>
<li>
<div>Space Complexity: O(N) for MaxHeap only, you are not allowed to create a list.</div>
</li>
</ul>
</blockquote>
<h2>Application Problem</h2>
<p>Angelo wants to determine how project difficulty changes throughout the semester. To do this, he wants to review all student feedback in real-time so he can determine the course's difficulty in realtime, and at any previous point in the semester.</p>
<p>Course difficulty is measured by the median amount of time student's spend on the projects. If students spend more time on a project, the median will be higher, and one can assume the project is more difficult. The median is used because it is less affected by outliers. The amount of time student's spend on a project is recorded every time they submit their README feedback.</p>
<p>You are being tasked with writing this program. You need to calculate and record the median at every point in time - AKA every time a student submits their README feedback. This will allow for Angelo to graph course difficulty over time.</p>
<p>You are given a list of values to read in one by one. Find an efficient way to keep track of the median after each value is read in. Return this as a list of medians in the order calculated.</p>
<p>The median of a list of values is defined as the middle number after sorting them in order. If the there is an odd number of values the median is the average of the middle two numbers.</p>
<p><span style="text-decoration: underline;">Example</span>:</p>
<p>current_medians( [2, 8, 35, 9] ) -&gt; [2, 5, 8, 8.5]</p>
<ul>
<li>As each number from the data was read in, a median of current data was calculated and added to the return list.</li>
<li>After 2 was read in, the median was 2</li>
<li>After 8 was read in, the median was 5 because the median of 2 and 8 is 5</li>
<li>After 35 was read in, the median was 8 because the median of 2, 8, and 35 is 8</li>
<li>And so on....</li>
</ul>
<blockquote>
<div><strong>current_medians(array: List[int]) -&gt; List[int]</strong></div>
<div>
<ul>
<li><strong>Must use PriorityQueue, MinHeap, and/or MaxHeap. Failure to do so will result in a zero for this function.</strong></li>
<li><strong>You may not access private member variables of PriorityQueue, MinHeap, or MaxHeap.</strong></li>
<li><strong>You may not use heap_sort.</strong></li>
<li><strong>Array</strong>: A list of <em>numeric values</em></li>
<li><strong>Returns</strong>: List of current medians in order data was read in</li>
<li>Time Complexity: O(Nlog(N))
<ul>
<li>N is the number of values in all lists</li>
<li><strong>Function must strictly be of the given time complexity</strong></li>
</ul>
</li>
<li>Space Complexity: O(N]</li>
</ul>
</div>
</blockquote>
<h2>Turning It In/ Deliverables</h2>
<p>Be sure to upload the following deliverables in a .zip folder to Mimir by 11:59p ET on Friday, April 2nd.</p>
<pre><code>Project7.zip
    |<span class="hljs-type">&mdash; Project7</span>/<br />        |<span class="hljs-type">&mdash; __init__</span>.py        (<span class="hljs-keyword">for</span> proper Mimir testcase loading)<br />        |<span class="hljs-type">&mdash; README</span>.xml         (<span class="hljs-keyword">for</span> project feedback)<br />        |<span class="hljs-type">&mdash; PriorityQueue</span>.py   (your solution source code for pqueues, heaps, application)<br />        |<span class="hljs-type">&mdash; PriorityNode</span>.py    (your solution source code for min and max node)
</code></pre>
<ul>
<li>__init__.py, a python3 file.</li>
<li>PriorityQueue.py, a python3 file.</li>
<li>PriorityNode.py, a python3 file.</li>
<li>README.xml, a text file that includes:
<ul>
<li>Your name</li>
<li>Feedback on the project</li>
<li>How long it took to complete</li>
<li>Project difficulty</li>
<li>A list of any external resources that you used, especially websites (make sure to include the URLs) and which function you used this information for. Please note that you can not use outside resources to solve the entire project, or use outside sources for multiple functions that leads to the solution of the project, then you are submitting someone else's work not yours. Outside sources use should not be used for more than one function, and it should not be more than few lines of code to solve that function.&nbsp; Please note that there is no penalty for using the programming codes shared by Onsay in Lectures and posted on D2L.</li>
</ul>
</li>
</ul>
<h2>Assignment Notes</h2>
<ul>
<li>
<p>No use of the module heapq allowed.</p>
</li>
<li>
<p>You must write docstrings for every completed function.</p>
</li>
<li>
<p><strong>The only containers allowed are lists to be used in the Application Problem and heap_sort functions.</strong></p>
</li>
<li>
<p>You may not access member variables with leading underscores outside their class.</p>
</li>
<li>
<p>Methods/attributes with leading underscores cannot be called outside of the class definition.</p>
</li>
<li>
<p>Keys and values can be ints, strings, or floats.</p>
</li>
<li>
<p>String methods are provided for debugging purposes.</p>
</li>
<li>
<p>Some heaps start at an index of one. However, for this assignment, indexing will start at index zero, just like normal lists.</p>
</li>
</ul>
<p><strong>Using/doing any of the following will result in a 0 for the function/class/assignment:</strong></p>
<ul>
<li>
<p>heapq module</p>
</li>
<li>
<p>sorted()</p>
</li>
<li>
<p>Initializing a list in heap_sort (besides the list that is initialized within MaxHeap)</p>
</li>
</ul>
<h2>Important Resources</h2>
<ul>
<li><a href="https://medium.com/python-features/magic-methods-demystified-3c9e93144bf7">Magic Methods</a></li>
<li><a href="https://www.programiz.com/python-programming/inheritance">Inheritance overview</a>:
<ul>
<li>Base classes + inheritance</li>
<li>Extending base class with new methods</li>
<li>Method overriding of base class methods</li>
</ul>
</li>
<li><a href="https://www.programiz.com/python-programming/methods/built-in/super">super():</a>
<ul>
<li>Used to upcall in base classes.</li>
</ul>
</li>
<li><a href="https://medium.com/@satorusasozaki/amortized-time-in-the-time-complexity-of-an-algorithm-6dd9a5d38045">Amortized Time Complexity</a></li>
</ul>
<h2>Rubric/ Grading</h2>
<ul>
<li>
<div>Tests(70)
<ul>
<li><strong>Coding Standard: &nbsp;</strong> &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; __/5</li>
<li>
<p><span style="font-family: geomanist, sans-serif;"><strong><code>MinNode &amp; MaxNode:</code> (2)</strong></span></p>
<ul>
<li>Min/Max Nodes: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; __/2</li>
</ul>
</li>
</ul>
</div>
</li>
</ul>
<ul>
<li style="list-style-type: none;">
<div>
<ul>
<li><strong>PriorityQueue: (40)</strong>
<ul>
<li>Simple: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; __/1</li>
<li>Left/Right Child Index: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; __/1</li>
<li>Parent &amp; Min/Max Child Index: __/1</li>
<li>Percolate Up: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/4</li>
<li>Percolate Down: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; __/4</li>
<li>Push: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; __/2</li>
<li>Push Comprehensive: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; __/6</li>
<li>Pop: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/2</li>
<li>Pop Comprehensive: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; __/6</li>
<li>Comprehensive: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; __/8</li>
</ul>
</li>
<li><strong>MaxHeap: (3)</strong>
<ul>
<li>MaxHeap: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/3</li>
</ul>
</li>
<li><strong>HeapSort: (5)</strong>
<ul>
<li>HeapSort: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/5</li>
</ul>
</li>
<li><strong>Current Medians: (15)</strong><br />
<ul>
<li>Simple: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; __/2</li>
<li>Current Medians: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; __/5</li>
<li>Comprehensive: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/8</li>
</ul>
</li>
</ul>
</div>
</li>
<li>
<div>Manual (30)</div>
<ul>
<li>
<div><strong>Time Complexity: (15)</strong></div>
<div>
<ul>
<li>&nbsp;__len__, empty, peek &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/1 (All or nothing)</li>
<li>get_left_child_index &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; __/0.5</li>
<li>get_right_child_index &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; __/0.5</li>
<li>get_parent_index &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/0.5</li>
<li>get_minmax_child_index &nbsp; &nbsp;&nbsp;&nbsp; __/0.5</li>
<li>percolate_up &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/1</li>
<li>percolate_down &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/1</li>
<li>pop&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/2</li>
<li>push&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/2</li>
<li>heap_sort&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; __/3</li>
<li>current_medians&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; __/3</li>
</ul>
</div>
</li>
<li>
<div><strong>Space Complexity: (10)</strong></div>
<div>
<ul>
<li>All non-listed methods* &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/2&nbsp; (All or nothing)</li>
<li>pop&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; __/1</li>
<li>push&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; __/1</li>
<li>heap_sort&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; __/3</li>
<li>current_medians&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; __/3</li>
</ul>
</div>
</li>
<li>
<div><span class="frontend-shared-components-CodeHighlight-___CodeHighlight__code-highlight___YBGmv  "><code><strong>README.xml</strong></code> is completely filled out with (1) Name, (2) Feedback, (3) Difficulty, (4) Time to Completion, (5) Citations: __/5</span></div>
</li>
</ul>
</li>
</ul>
<p><span class="frontend-shared-components-CodeHighlight-___CodeHighlight__code-highlight___YBGmv  ">* __len__, empty, peek, get_left_child_index, get_right_child_index, get_parent_index, get_minmax_child_index.</span></p>
<p>This project was created by Angelo Savich and Zach Arnold. The application is based on Zosha Korzecke's PriorityQueues &amp; Heaps application problem.</p>