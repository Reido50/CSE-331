<h1><span style="font-weight: 400;">Project 2: Recursion</span></h1>
<p><strong>Due: Friday, February 5th, 11:59 pm</strong></p>
<p><em><span style="font-weight: 400;">This is not a team project, do not copy someone else&rsquo;s work.</span></em></p>
<p><em><span style="font-weight: 400;"><img src="https://s3.amazonaws.com/mimirplatform.production/files/8e6e1569-c5a4-4899-bfde-f18550508648/cover.jpg" alt="cover.jpg" /></span></em></p>
<p><a href="https://en.wikipedia.org/wiki/Recursion_(computer_science)">Recursion</a> is a fundamental technique to apply to problems in computer science. Recursion allows us to explore structures of <a href="https://en.wikipedia.org/wiki/Structural_induction">arbitrary depth</a>, to solve problems by <a href="https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm">dividing them into smaller sub-problems</a>, and more. One of the most popular techniques for use in technical interviews, recursion is inescapable in the study of data structures and algorithms.</p>
<h2>Assignment Overview</h2>
<p><span style="font-weight: 400;">In this project, you will be implementing recursive functions for a singly linked list. Like <a href="../09a00c06-dd1b-4999-9636-7051c2549291" target="_blank" rel="noopener noreferrer">Project 0B</a>, each node contains a value, and a reference to the next node. There are two recursion approaches that we use in this project. Some functions will have a corresponding inner function that will be recursive, while other functions will themselves be recursive. Every function you implement should utilize</span><strong> RECURSION. </strong>In functions that utilize an inner function, this recursion will take place within the inner function. For more explonation, check out the specification document for <a href="../ee0a231e-d815-44d4-812b-b8a093b2e9f9" target="_blank" rel="noopener noreferrer">CC2</a>, where we defined inner functions.</p>
<h2>Assignment Notes</h2>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">You are required to add and complete the docstrings for each function. They should be in the exact same format as project 1. This should include at least a one-sentence description of the function, all parameters, and what the function returns. Please see Project 1 DLL.py &nbsp;for reference on how to complete docstrings for each function.</span></li>
<li style="font-weight: 400;"><strong>All of your functions must be recursive.</strong><span style="font-weight: 400;"> You will lose </span><strong>all</strong><span style="font-weight: 400;"> points related to the function if it is not recursive.&nbsp;</span>
<ul>
<li style="font-weight: 400;"><strong>MORE SIMPLY PUT: YOU MAY NOT USE ANY `FOR` OR `WHILE` LOOPS IN THIS PROJECT!</strong></li>
</ul>
</li>
<li style="font-weight: 400;"><strong>Do not use additional data structures</strong><span style="font-weight: 400;">, such as lists or strings, unless specified otherwise. You will lose </span><strong>all</strong><span style="font-weight: 400;"> points relating to the function if you do.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">In addition to the Mimir testing, you will also be graded on the <strong>time </strong>performance of your functions. Take note of the time complexity requirement for each function.</span></li>
<li style="font-weight: 400;"><strong>No hardcoding</strong> <strong>testcases</strong>. If you do this, you will lose <strong>all</strong> points for the function.</li>
</ul>
<h2>Assignment Specifications</h2>
<p><span style="font-family: geomanist, sans-serif;"><strong>class Node:</strong></span></p>
<p><em><strong><span style="font-family: geomanist, sans-serif;">Do not </span></strong><span style="font-family: geomanist, sans-serif;"><strong>modify</strong> this class</span></em></p>
<ul>
<li style="font-weight: 400;"><strong><span style="font-family: 'courier new', courier, monospace;">Attributes:</span></strong>
<ul>
<li style="font-weight: 400;"><strong><span style="font-family: 'courier new', courier, monospace;">value: </span></strong><span style="font-family: 'courier new', courier, monospace;"><span style="font-family: geomanist, sans-serif;">Value stored in a <span style="font-family: 'courier new', courier, monospace;">Node</span></span></span></li>
<li style="font-weight: 400;"><strong><span style="font-family: 'courier new', courier, monospace;"><span style="font-family: geomanist, sans-serif;"><span style="font-family: 'courier new', courier, monospace;">next:&nbsp;</span></span></span></strong><span style="font-family: 'courier new', courier, monospace;"><span style="font-family: geomanist, sans-serif;"><span style="font-family: 'courier new', courier, monospace;"><span style="font-family: geomanist, sans-serif;">Reference to the following&nbsp;<span style="font-family: 'courier new', courier, monospace;">Node <span style="font-family: geomanist, sans-serif;">(May be <span style="font-family: 'courier new', courier, monospace;">N</span><span style="font-family: 'courier new', courier, monospace;">one<span style="font-family: geomanist, sans-serif;">)</span></span></span></span></span></span></span></span></li>
</ul>
</li>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>__init__(self, value: T, next: Node = None) -&gt; None:</strong></span>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">This function initializes a node with a given value and next reference, pointing to the next Node in the list.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;">self.value</span> - the value of the Node.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;">self.next</span> - the next Node in the list, default value is None</span></li>
</ul>
</li>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>__repr__(self) -&gt; str:</strong></span>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">A node is represented in string form as &lsquo;value&rsquo;.</span></li>
</ul>
</li>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>__str__(self) -&gt; str:</strong></span>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">A node is represented in string form as &lsquo;value&rsquo;. Use <span style="font-family: 'courier new', courier, monospace;">str(node)</span> to make it a string.</span></li>
</ul>
</li>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>__eq__(self, other: Node) -&gt; bool:</strong></span>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">This function compares two Nodes.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;">other</span> - the right-hand operand of the &ldquo;==&rdquo;</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Returns either <span style="font-family: 'courier new', courier, monospace;">True</span> or <span style="font-family: 'courier new', courier, monospace;">False</span></span></li>
</ul>
</li>
</ul>
<p><strong>class RecursiveSinglyLinkedList:</strong></p>
<p><em><strong>Do not modify</strong> the following attributes/methods</em></p>
<ul>
<li style="font-weight: 400;"><strong><span style="font-family: 'courier new', courier, monospace;">Attributes:</span></strong>
<ul>
<li style="font-weight: 400;"><strong><span style="font-family: 'courier new', courier, monospace;">head:</span></strong><span style="font-family: 'courier new', courier, monospace;"><span style="font-family: geomanist, sans-serif;"> The first Node in the linked list</span> <span style="font-family: geomanist, sans-serif;">(</span><span style="font-family: geomanist, sans-serif;">M</span><span style="font-family: geomanist, sans-serif;">ay be</span> None<span style="font-family: geomanist, sans-serif;">)</span></span></li>
</ul>
</li>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>__init__(self) -&gt; None:</strong></span>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">This function initializes a RecursivelySinglyLinkedList</span></li>
</ul>
</li>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>__repr__(self) -&gt; str:</strong></span>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">A string representation of the list.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">For this to work, you must have completed&nbsp;<span style="font-family: 'courier new', courier, monospace;">to_string</span></span></li>
</ul>
</li>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>__eq__(self, other: Node) -&gt; bool:</strong></span>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">This function compares two RecursiveSinglyLinkLists.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">other - the right-hand operand of the &ldquo;==&rdquo;</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Returns either <span style="font-family: 'courier new', courier, monospace;">True</span> or <span style="font-family: 'courier new', courier, monospace;">False</span></span></li>
</ul>
</li>
</ul>
<p><span style="font-weight: 400;">You must implement the following functions in </span><strong>SLL.py</strong><span style="font-weight: 400;">. Take note of the specified return values, input parameters, and time complexity requirements. </span><strong>Do not change the function signatures.</strong></p>
<ul>
<li style="font-weight: 400;"><strong><span style="font-family: 'courier new', courier, monospace;">to_string(self, curr: Node) -&gt; str:</span></strong></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Generate and return a string representation of the list, starting at head </span><span style="font-family: 'courier new', courier, monospace;"><strong>curr</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">The values should be separated by a &ldquo; --&gt; &ldquo; (a space followed by two hyphens, a greater than symbol, and then another space)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Return an empty string if there are no nodes in the list.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">You are allowed to use strings in this function.</span></li>
<li><strong>This function must be recursive</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(n<sup>2</sup></em></span><span style="font-weight: 400;"><em>)</em>, due to the run time of string concatenation in python.</span></li>
</ul>
<li style="font-weight: 400;"><strong><span style="font-family: 'courier new', courier, monospace;">length(self, curr: Node) -&gt; str:</span></strong></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Determines the number of nodes in the list starting with head </span><span style="font-family: 'courier new', courier, monospace;"><strong>curr</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">If the list is empty, it has a length of 0.</span></li>
<li><strong>This function must be recursive</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(n)</em></span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>sum_list(self, curr: Node) -&gt; T:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Calculates and returns the sum of the values in the list starting with head </span><span style="font-family: 'courier new', courier, monospace;"><strong>curr</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">If the list is empty, it has a sum of 0.</span></li>
<li><strong>This function must be recursive</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(n)</em></span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>push(self, value: T) -&gt; None:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Insert the given </span><span style="font-family: 'courier new', courier, monospace;"><strong>value</strong></span><span style="font-weight: 400;"> into the linked list</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">The value should be inserted at the end of the list</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Return the starting node of the linked list</span></li>
<li style="font-weight: 400;"><strong>Must call <span style="font-family: 'courier new', courier, monospace;">push_inner</span></strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(n)</em></span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>push_inner(curr: Node) -&gt; None:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">This is a helper function for </span><span style="font-family: 'courier new', courier, monospace;"><strong>push</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Insert the given </span><span style="font-family: 'courier new', courier, monospace;"><strong>value</strong></span><span style="font-weight: 400;"> (from </span><span style="font-family: 'courier new', courier, monospace;"><strong>push</strong></span><span style="font-weight: 400;">) into the linked list that has head </span><span style="font-family: 'courier new', courier, monospace;"><strong>curr</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">The value should be inserted at the end of the list</span></li>
<li><strong>This function must be recursive</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity O(n)</span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>remove(self, value: T) -&gt; None:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Remove the first node in the list with the given </span><span style="font-family: 'courier new', courier, monospace;"><em>value</em></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">If the value doesn&rsquo;t exist, do not change the linked list</span></li>
<li style="font-weight: 400;"><strong>Must call <span style="font-family: 'courier new', courier, monospace;">remove_inner</span></strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(n)</em></span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>remove_inner(curr: Node) -&gt; Node:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">This is a helper function for </span><span style="font-family: 'courier new', courier, monospace;"><strong>remove</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Remove the first node in the list with the given </span><span style="font-family: 'courier new', courier, monospace;"><strong>value </strong></span><span style="font-weight: 400;">(from </span><span style="font-family: 'courier new', courier, monospace;"><strong>remove</strong></span><span style="font-weight: 400;">) </span><span style="font-weight: 400;">starting at head </span><span style="font-family: 'courier new', courier, monospace;"><strong>curr</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">If the value doesn&rsquo;t exist, do not change the linked list</span></li>
<li><strong>This function must be recursive</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity O(n)</span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>remove_all(self, value: T) -&gt; None:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Remove all nodes in the list with the given </span><span style="font-family: 'courier new', courier, monospace;"><strong>value</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">If the value doesn&rsquo;t exist, do not change the linked list</span></li>
<li style="font-weight: 400;"><strong>Must call <span style="font-family: 'courier new', courier, monospace;">remove_all_inner</span></strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(n)</em></span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>remove_all_inner(curr: Node) -&gt; Node:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">This is a helper function for </span><span style="font-family: 'courier new', courier, monospace;"><strong>remove_all</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Remove all nodes in the list with the given </span><span style="font-family: 'courier new', courier, monospace;"><strong>value </strong></span><span style="font-weight: 400;">(from </span><span style="font-family: 'courier new', courier, monospace;"><strong>remove_all</strong></span><span style="font-weight: 400;">) starting at head </span><span style="font-family: 'courier new', courier, monospace;"><strong>curr</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">If the value doesn&rsquo;t exist, do not change the linked list</span></li>
<li><strong>This function must be recursive</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(n)</em></span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>search(self, value: T) -&gt; bool:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Looks for </span><span style="font-family: 'courier new', courier, monospace;"><strong>value </strong></span><span style="font-weight: 400;">in the list</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Returns True if the value is in the list and False if it is not in the list</span></li>
<li style="font-weight: 400;"><strong>Must call <span style="font-family: 'courier new', courier, monospace;">search_inner</span></strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(n)</em></span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>search_inner(curr: Node) -&gt; bool:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">This is a helper function for </span><span style="font-family: 'courier new', courier, monospace;"><strong>search</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Looks for </span><span style="font-family: 'courier new', courier, monospace;"><strong>value </strong></span><span style="font-weight: 400;">(from <span style="font-family: 'courier new', courier, monospace;"><strong>search</strong></span></span><span style="font-weight: 400;">) in the list starting with head </span><span style="font-family: 'courier new', courier, monospace;"><strong>curr</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Returns True if the value is in the list and False if it is not in the list</span></li>
<li><strong>This function must be recursive</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity O(n)</span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>count(self, value: T) -&gt; int:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Counts and returns how many times the given </span><span style="font-family: 'courier new', courier, monospace;"><strong>value</strong></span><span style="font-weight: 400;"> occurs in the list</span></li>
<li style="font-weight: 400;"><strong>Must call <span style="font-family: 'courier new', courier, monospace;">count_inner</span></strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(n)</em></span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>count_inner(curr: Node) -&gt; int:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">This is a helper function for </span><span style="font-family: 'courier new', courier, monospace;"><strong>count</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Counts and returns how many times the given </span><span style="font-family: 'courier new', courier, monospace;"><strong>value</strong></span><span style="font-weight: 400;"> (from </span><span style="font-family: 'courier new', courier, monospace;"><strong>count</strong></span><span style="font-weight: 400;">) occurs in the list starting at head </span><span style="font-family: 'courier new', courier, monospace;"><strong>curr</strong></span></li>
<li><strong>This function must be recursive</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(n)</em></span></li>
</ul>
<li style="font-weight: 400;"><span style="font-family: 'courier new', courier, monospace;"><strong>reverse(self, curr: Node) -&gt; Node:</strong></span></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Given a list starting with head </span><span style="font-family: 'courier new', courier, monospace;"><strong>curr</strong></span><span style="font-weight: 400;">, reverse this list.&nbsp;</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Return the head of the reversed list.</span></li>
<li><strong>This function must be recursive</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(n)</em></span></li>
</ul>
</ul>
<h2><strong>Application Problem:&nbsp;</strong></h2>
<p><strong><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s3.amazonaws.com/mimirplatform.production/files/225fee6d-f9a9-4ec8-bc4c-2f29cecf34bb/animal-crossing-new-horizons-guide-gulliver-item-craft-robot-hero.original.jpg" alt="animal-crossing-new-horizons-guide-gulliver-item-craft-robot-hero.original.jpg" /></strong></p>
<p><span style="font-weight: 400;">In this application problem, you are an adorable character from the game </span><em><span style="font-weight: 400;">Animal Crossing</span></em><span style="font-weight: 400;">. An important part of the game is <em>crafting: </em>putting different ingredients together to create a new item. While crafting, it is quite tedious to remember all of your different recipes and to check that you are carrying the right ingredients. So, to speed up this process, you will need to write a function that checks your <strong><em>pockets</em></strong> for the ingredients necessary to craft an item, given by a <strong><em>recipe</em></strong>. </span></p>
<p><span style="font-weight: 400;">You have decided to store the recipes and your pocket contents as linked lists, where each ingredient is one <span style="font-family: geomanist, sans-serif;">Node</span>. Your function must determine if you are carrying all of the recipe ingredients in your pockets. That is, your function must determine if every element in the<strong>&nbsp;</strong><em><strong>recipe</strong>&nbsp;</em>list is in the&nbsp;<strong><em>pocket</em></strong> list. This includes having the correct number of a specific ingredient. If a recipe calls for two (or more) of the same ingredient, <em>at least</em> that many ingredients must be present in the pockets list.</span></p>
<p><span style="font-weight: 400;">If you determine a recipe is able to be crafted, remove the ingredients used to craft it from the&nbsp;<em><strong>pockets</strong></em><em>&nbsp;</em>list. If the recipe is not able to be crafted, leave&nbsp;<em><strong>pockets</strong></em><strong>&nbsp;</strong>unchanged.</span></p>
<p><span style="font-weight: 400;">To do this, you will implement one function:</span></p>
<ul>
<li><strong><span style="font-family: 'courier new', courier, monospace;">crafting(recipe: RecursiveSinglyLinkList, pockets: RecursiveSinglyLinkList)-&gt; bool</span></strong></li>
</ul>
<ul>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Given two linked lists, </span><span style="font-family: 'courier new', courier, monospace;"><strong>recipe </strong></span><span style="font-weight: 400;">and </span><span style="font-family: 'courier new', courier, monospace;"><strong>pockets</strong></span><span style="font-weight: 400;">, determine if the values in the </span><span style="font-family: 'courier new', courier, monospace;"><strong>recipe </strong></span><span style="font-weight: 400;">list are contained in the </span><span style="font-family: 'courier new', courier, monospace;"><strong>pockets</strong></span><span style="font-weight: 400;"> list.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">If&nbsp;<strong>all</strong>&nbsp;the values in <span style="font-family: 'courier new', courier, monospace;"><strong>recipe&nbsp;</strong><span style="font-family: geomanist, sans-serif;">are present in&nbsp;<span style="font-family: 'courier new', courier, monospace;"><strong>pockets</strong><span style="font-family: geomanist, sans-serif;">, they will be consumed, and therefore must be removed from <span style="font-family: 'courier new', courier, monospace;"><strong>pockets.</strong></span></span></span></span></span></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Return <span style="font-family: 'courier new', courier, monospace;">True</span> if the pockets contain enough ingredients to complete the recipe, <span style="font-family: 'courier new', courier, monospace;">False</span> otherwise.</span></li>
<li style="font-weight: 400;"><strong>This function must be recursive - NO `FOR` or `WHILE` loops are allowed.</strong></li>
<li style="font-weight: 400;"><strong>You may not use any additional data structures other than linked lists in this function</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time complexity: <em>O(rp)*</em></span></li>
</ul>
</ul>
<p><span style="font-weight: 400;">* Where <strong><em>r</em></strong> is the number of elements in the recipe and <strong><em>p</em></strong> is the number of elements in your pockets.</span></p>
<p><strong>Examples:</strong></p>
<p><span style="font-weight: 400;">Ex1.&nbsp;</span></p>
<p><span style="font-weight: 400;">recipe = <strong>wood</strong> --&gt; <strong>wood</strong> --&gt; <strong>clay</strong></span></p>
<p><span style="font-weight: 400;">pockets = apple --&gt; <strong>wood</strong> --&gt; <strong>clay</strong> --&gt; <strong>wood</strong></span></p>
<p><span style="font-weight: 400;">Returns: <span style="font-family: 'courier new', courier, monospace;">True</span>, because each element in the recipe list is present in the pockets list.</span></p>
<p>pockets, after function call = apple</p>
<p><span style="font-weight: 400;">Ex2.</span></p>
<p><span style="font-weight: 400;">recipe = <strong>sand dollar</strong> --&gt; <strong>sea snail</strong> --&gt; <strong>gold nugget</strong> --&gt; <strong>gold nugget</strong></span></p>
<p><span style="font-weight: 400;">pockets = wood --&gt; <strong>sand dollar</strong> --&gt; <strong>gold nugget</strong> --&gt; <strong>sea snail</strong> --&gt; clay --&gt; bamboo piece</span></p>
<p><span style="font-weight: 400;">Returns: <span style="font-family: 'courier new', courier, monospace;">False</span>, because the recipe requires two golden nuggets, but you only have one in your pokets.</span></p>
<p><span style="font-weight: 400;">pockets, after function call = wood --&gt; <strong>sand dollar</strong> --&gt; <strong>gold nugget</strong> --&gt; <strong>sea snail</strong> --&gt; clay --&gt; bamboo piece</span></p>
<p><strong>Submission</strong></p>
<h4><strong>Deliverables</strong></h4>
<p><span style="font-weight: 400;">Be sure to upload the following deliverables in a .zip folder to Mimir by 11:59p ET on Friday, January 29th.</span></p>
<p><span style="font-weight: 400;">Project2.zip</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; Project2/</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; README.xml&nbsp; &nbsp; &nbsp; (for project feedback)</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; __init__.py &nbsp; &nbsp; (for proper Mimir testcase loading)</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; SLL.py&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; (contains your solution source code)</span></p>
<p>&nbsp;</p>
<p><strong>Grading</strong></p>
<ul>
<li>Tests (72)</li>
<li>Manual (28)
<ul>
<li><code>README.xml</code> is completely filled out with (1) Name, (2) Feedback, (3) Time to Completion and (4) Citations: __/2</li>
<li><span style="font-family: 'courier new', courier, monospace;">to_string, length, sum_list <span style="font-family: geomanist, sans-serif;">Time Complexity __/3</span></span></li>
<li><span style="font-family: 'courier new', courier, monospace;">push <span style="font-family: geomanist, sans-serif;">Time Complexity __/3</span></span></li>
<li><span style="font-family: 'courier new', courier, monospace;">remove <span style="font-family: geomanist, sans-serif;">Time Complexity __/3</span></span></li>
<li><span style="font-family: 'courier new', courier, monospace;">remove_all <span style="font-family: geomanist, sans-serif;">Time Complexity __/3</span></span></li>
<li><span style="font-family: 'courier new', courier, monospace;">search <span style="font-family: geomanist, sans-serif;">Time Complexity __/3</span></span></li>
<li><span style="font-family: 'courier new', courier, monospace;">count <span style="font-family: geomanist, sans-serif;">Time Complexity __/3</span></span></li>
<li><span style="font-family: 'courier new', courier, monospace;">reverse <span style="font-family: geomanist, sans-serif;">Time Complexity __/3</span></span></li>
<li><span style="font-family: 'courier new', courier, monospace;">crafting <span style="font-family: geomanist, sans-serif;">Time Complexity __/5</span></span></li>
</ul>
</li>
</ul>
<h2><span style="font-family: 'courier new', courier, monospace;"><span style="font-family: geomanist, sans-serif;">Fun Aside</span></span></h2>
<ul>
<li><span style="font-family: 'courier new', courier, monospace;"><span style="font-family: geomanist, sans-serif;">Here's some calm/relaxing Animal Crossing music to work to <a href="https://youtu.be/d3YC-bxZXVY" target="_blank" rel="noopener noreferrer">remix 1</a>, <a href="https://youtu.be/Lnkl1SwErpM" target="_blank" rel="noopener noreferrer">remix 2,</a> <a href="https://youtu.be/-enSOKMeT_U" target="_blank" rel="noopener noreferrer">comp</a></span></span></li>
</ul>
<p>Created by Andy Wilson, Lukas Richter, and Andrew Haas</p>