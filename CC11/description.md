<h1><strong>CC11 - SS21 - The Power Of Names</strong></h1>
<h1><strong>Due: Tue, 4/13 @ 11:59pm</strong></h1>
<p><em>This is not a team project, do not copy someone else&rsquo;s work.</em></p>
<h1><strong>Introduction</strong></h1>
<p><img src="https://s3.amazonaws.com/mimirplatform.production/files/f3c3d714-91ef-4ced-aa61-ea414f2e6f18/Dark-Souls-III-Screen-Shot-1.jpg" alt="DarkSouls.jpg" /></p>
<p>Recently, you bought a copy of Dark Souls. You've heard around that it's a great game, and you've been itching to give it a try. But you've been trying for the past week and you can't get past the first area! You keep dying! Enemies keep popping out of corners and walls, there's just no way you can anticipate where the next enemy is coming from. You ask your friends for help, but all they tell you is to just get good.</p>
<p>You decide it is up to you to find your own solution to revealing these enemies...</p>
<h1><strong>Challenge</strong></h1>
<h2><strong>Overview</strong></h2>
<p>In this problem, you will be given a trie of enemies and a pattern key (a string) to search for. Your function should determine which enemy names match the given key. All of the enemies will be provided in CamelCase, as will the key. The goal is to match the enemies with the provided CamelCase key.</p>
<p>Essentially, a trie represents strings in a tree-like data structure. Each node of the tree represents one character of a string, and also potentially has a link to more characters in the language you are using. For example, consider a simple trie containing the words 'apple', 'thee', 'them', 'this', and 'try'.</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s3.amazonaws.com/mimirplatform.production/files/342d8ea4-4890-4e88-b912-779de883cdc4/trie_example.png" alt="TrieGraph.png" /></p>
<p style="text-align: center;"><em>Visualization from: <a href="https://www.cs.usfca.edu/~galles/visualization/Trie.html">https://www.cs.usfca.edu/~galles/visualization/Trie.html</a></em></p>
<p>All the words starting with T share the same T node, and 'thee' and 'them' both share the T, H, and E nodes. It is important to note that each node has its own links to other nodes. For example, the E in 'apple' is not shared with the E in 'thee'. Only the prefixes are shared, which is why a trie is also called a prefix tree.</p>
<p>In some trie implementations, each node has an array of k characters (where k is the number of keys in the alphabet being represented). However, as you will see, our implementation uses a python <em>defaultdict</em> with the character as the key and the corresponding node as the value. This means that each node only contains valid children, which can be iterated/accessed in the same way as a normal dictionary.</p>
<p><em>The following functions are provided if you choose to use a Trie. You are not expected to modify them</em></p>
<p><strong>class Node:</strong></p>
<ul>
<li><strong>__init__(self) -&gt; None:</strong>
<ul>
<li><strong>children: defaultdict(node):</strong> Dictionary of child nodes. Each dictionary entry is an empty node by default.
<ul>
<li><code>node.children[char]</code> to access a child's node</li>
</ul>
</li>
<li><strong>is_end: bool:</strong> A flag to mark if this node is the end of a word</li>
<li><strong>Return:</strong> None</li>
</ul>
</li>
<li><strong>__str__(self) -&gt; str:</strong>
<ul>
<li><strong>Return</strong>: The string 'Node'</li>
</ul>
</li>
<li><strong>__repr__(self) -&gt; str:</strong>
<ul>
<li><strong>Return</strong>: The string 'Node'</li>
</ul>
</li>
</ul>
<p><strong>class Trie:</strong></p>
<ul>
<li><strong>__init__(self) -&gt; None:</strong>
<ul>
<li><strong>root: Node:</strong> The root node of this Trie</li>
<li><strong>Return:</strong> None</li>
</ul>
</li>
<li><strong>__str__(self) -&gt; str:</strong>
<ul>
<li><strong>Return</strong>: A basic string representation of the Trie</li>
</ul>
</li>
<li><strong>__repr__(self) -&gt; str:</strong>
<ul>
<li><strong>Return</strong>: A basic string representation of the Trie</li>
</ul>
</li>
<li><strong>insert(self, word: str) -&gt; None</strong>
<ul>
<li>Inserts a word into the Trie by creating a node for each character in the word</li>
<li><strong>Time Complexity: O(dm)</strong>
<ul>
<li>Where d is the size of the alphabet and m is the size of the word</li>
</ul>
</li>
<li><strong>Return:</strong> None</li>
</ul>
</li>
</ul>
<p><em>Modify the following function</em></p>
<p><strong>enemy_revealer(enemies: Trie, key: str] -&gt; List[str]</strong></p>
<ul>
<li><strong>enemies: Trie:</strong> Trie of enemy names of size n</li>
<li><strong>key: str:</strong> Key pattern string to match enemies with</li>
<li><strong>Return:</strong> New list of enemies that match the key pattern</li>
<li><strong>Time Complexity: O(ck)*</strong>
<ul>
<li>Where<br />
<ul>
<li><strong>c</strong> is the number of children of a node (usually 26), and</li>
<li><strong>k</strong> is the height of the tree</li>
</ul>
</li>
<li>* In the real world, string concatenation is O(n), but you can consider it as O(1) for this challenge. There is a way that you can achieve the same effect without incurring O(n) with each iteration (hint: list append is O(1) amortized), but it is not necessary for this challenge.</li>
</ul>
</li>
<li><strong>Space Complexity: O(n)</strong></li>
</ul>
<p><strong>Examples</strong>:</p>
<p><strong>Ex 1:</strong></p>
<p><strong>Enemies</strong> = Trie&lt;"Angel", "Banshee", "Basilisk", "ChaosBug", "Corpse"&gt;</p>
<p><strong>Key</strong> = "B"</p>
<p><strong>Output</strong> = ["Banshee", "Basilisk"]</p>
<p>Out of all the pool of possible enemies in this area, given key pattern "B", we are looking for enemies that start with the letter "B" and do not have another capital character in them. "Banshee" and "Basilisk" are the only two enemies that fit this pattern.</p>
<p><strong>Ex 2:</strong></p>
<p><strong>Enemies</strong> = Trie&lt;"Angel", "Banshee", "Basilisk", "ChaosBug", "Corpse"&gt;</p>
<p><strong>Key</strong> = "C"</p>
<p><strong>Output</strong> = ["Corpse"]</p>
<p>Out of all the pool of possible enemies in this area, given key pattern "C," we are looking for enemies that start with the letter "C" and do not have another capital character in them. "Corpse" is the only enemy that fits this pattern. "ChaosBug" is not a valid enemy. Despite it starting with the letter "C", it does not fit the pattern because it also has a "B" (a valid pattern for "ChaosBug" would be "CB").</p>
<p><strong>Ex 3:</strong></p>
<p><strong>Enemies</strong> = Trie&lt;"Banshee", "BerenikeKnight", "BlackKnight", "Butcher", "BoneWheel"&gt;</p>
<p><strong>Key</strong> = "BKn"</p>
<p><strong>Output</strong> = ["BerenikeKnight", "BlackKnight"]</p>
<p>Given key pattern "BKn", we are now looking for enemies that have two capital letters in them, "B" and "K", in that order. Additionally, the second word starting with a "K" needs to be followed by a <em>lowercase</em> "n". All the enemies in this pool start with the letter "B", but only "BerenikeKnight" and "BlackKnight" should be returned.</p>
<p><strong>Ex 4:</strong></p>
<p><strong>Enemies</strong> = Trie&lt;"DancerOfTheBorealValley", "DarkSunGwyndolin", "DarkeaterMidir", "DarkmoonSoldiers", "Darkwraith", "DarkwraithKnight", "DaughterOfCrystalKriemhild", "Deacon", "DeaconsOfTheDeep", "DeepAccursed", "Demon", "DemonCleric", "DemonFiresage", "DemonFromBelow", "DemonInPain", "DemonPrince", "DemonStatue", "DesertPyromancerZoey", "DevoutHollow", "DragonslayerArmour", "Drake", "DrakebloodKnight", "DrangKnights"&gt;</p>
<p><strong>Key</strong> = "DrK"</p>
<p><strong>Output</strong> = ["DarkwraithKnight", "DrakebloodKnight", "DrangKnights"]</p>
<p>Given key pattern "DrK", we are now looking for enemies that have two capital letters in them, "D" and "K". Additionally, the word starting with "D" needs to be followed by a lowercase "r". "DrakebloodKnight" and "DrangKnights" fit this pattern. But "DarkwraithKnight" should also be considered. Even though the lowercase "r" is not immediately after the "D", it still follows the "D".</p>
<h1>Tips, Tricks, and Notes</h1>
<ul>
<li>You <strong>must</strong> fill out docstrings to receive Coding Standard points.</li>
<li>If you choose to use a Trie, consider populating the Trie with all your enemies, then using the key to search through the Trie for valid enemies.</li>
<li>Your Trie class is included in your submission, so feel free to add functionality if you wish. Just stay in time complexity!</li>
<li>If you need some <em>epic</em> music to listen to while coding <a href="https://www.youtube.com/watch?v=epK4CBE4bB8">here is a playlist of various Dark Souls boss battle themes</a>.</li>
</ul>
<h1><strong>Submission</strong></h1>
<p><strong><img style="display: block; margin-left: auto; margin-right: auto;" src="https://s3.amazonaws.com/mimirplatform.production/files/724730f9-8704-4bb7-9ebb-12d019d3050d/BriskHardFeline-max-1mb.gif" alt="BriskHardFeline-max-1mb.gif" /></strong></p>
<h2><strong>Deliverables</strong></h2>
<p>Be sure to upload the following deliverables in a .zip folder to Mimir by 11:59 PM Eastern Time on <strong>Tuesday</strong> 4<strong>/13/2021</strong>.</p>
<p>Your .zip folder can contain other files (for example, description.md and tests.py), but must include (at least) the following:</p>
<pre><code>CC11.zip    
    |<span class="hljs-type">&mdash; CC11</span>/   
        |<span class="hljs-type">&mdash; README</span>.xml       (<span class="hljs-keyword">for</span> coding challenge feedback)        
        |<span class="hljs-type">&mdash; __init__</span>.py      (<span class="hljs-keyword">for</span> proper Mimir testcase loading)        
        |<span class="hljs-type">&mdash; solution</span>.py      (contains your solution source code)
</code></pre>
<h2><strong>Grading</strong></h2>
<p>The following 100-point rubric will be used to determine your grade on CC8:</p>
<ul>
<li>Tests (65)
<ul>
<li>00 - Coding Standard: __/5</li>
<li>01 - Single Words: __/12.5</li>
<li>02 - Prefixes: __/12.5</li>
<li>03 - Basic: __/15</li>
<li>04 - Comprehensive: __/20</li>
</ul>
</li>
<li>Manual (35)
<ul>
<li>M0 - enemy_revealer Time Ock): __/15</li>
<li>M1 - enemy_revealer Space O(n): __/15</li>
<li>README.md is <em>completely</em> filled out with (1) Name, (2) Feedback, (3) Time to Completion, (4) Citations, and (Difficulty): __/5</li>
</ul>
</li>
</ul>
<p>Coding Challenge created by Sean Nguyen and Lukas Richters</p>
