<p><strong>Due: Tuesday, April 20th @ 11:59pm</strong></p>
<p><em>This is not a team project, do not copy someone else&rsquo;s work.</em></p>
<h1><strong>Introduction</strong></h1>
<p><img class="HiaYvf-SmKAyb" src="https://lh4.googleusercontent.com/T5WhWO1bqCNgLBwonX9kvSrW79TPssE-EpoCxVSbBiRf2BJNaV5Q-jbEnhKIjNnP6yTr7aDA7JYW6pI4oowPTEnnXjHd0a9fiEsq-zIP9pPnbojmIKcWm3DC7jghP1nToM3mobpK" /></p>
<p><strong>Previously on "I Love You Colonel Sanders!"...</strong></p>
<p>After the wild success of the dating simulator &rdquo;I Love You Colonel Sanders!&rdquo; letters have been pouring in asking for more. Fans have been asking the big questions like &ldquo;What&rsquo;s The Colonel doing now?&rdquo; and &ldquo;Will we ever learn the nameless student&rsquo;s name?&rdquo;</p>
<p>KFC has decided to create a sequel to satisfy the hungry fans&rsquo; appetites. &ldquo;I Love You Colonel Sanders! 2: 12 Herbs and Spices&rdquo; promises to be bigger and better with more characters, branching dialogue paths, and deeper and richer character development. The development studio has hired&nbsp;<strong>you</strong>&nbsp;to create a more robust dialogue system.</p>
<p>Of course, you were able to oblige them without much trouble.</p>
<p>(Thank you Bank and Andy!!)</p>
<p><strong>Three months later...</strong></p>
<p>&ldquo;I Love You Colonel Sanders! 2: 12 Herbs and Spices&rdquo; was an even greater success than the first. You were promoted, and given your own corner office with a view on the twelfth floor. To thank the game's loyal fans, the higher-ups have asked you to make a DLC, featuring never-before-seen finger-lickin' fun! Soon after you begin development, however, you realize that your dialog engine is rather inefficient, since it poorly concatenates strings...</p>
<p>&nbsp;</p>
<h1><strong>Challenge</strong></h1>
<h2><strong>Overview</strong></h2>
<p>You will create a function that takes a list of strings and determines the best way to concatenate them. String concatenation is typically an expensive operation. Since strings are immutable, a concatenation of two strings requires a copy of each character in the string to form the new string. So, to optimize the concatenation process, you should look to <em>minimize the number of copies</em>. For example:</p>
<p><img src="https://s3.amazonaws.com/mimirplatform.production/files/5adc0abb-c52e-4dd0-b548-96e0e5f2e76b/example.png" alt="example.png" /></p>
<p>This challenge is designed to use <em>dynamic programming</em>. Dynamic programming increases runtime performance by storing values for "subproblems." A classic example is to <a href="https://medium.com/geekculture/how-to-solve-fibonacci-sequence-using-dynamic-programming-b7cd784ee10d" target="_blank" rel="noopener noreferrer">calculate the nth Fibonacci number</a>. Essentially, the dynamic approach stores previously calculated values, so that if you request the n + 1 Fibonacci number after asking for the nth, the calculation uses the previously stored value of n and n-1 to calculate n+1 without doing all the same work we already did.</p>
<p>Consider building some form of records to store calculations of how many copies each pair of strings result in when concatenated.</p>
<p><img src="https://s3.amazonaws.com/mimirplatform.production/files/d28639d3-c859-4e93-9215-e092774bc503/memoize.png" alt="memoize.png" /></p>
<p><em>Modify the following function</em></p>
<p><strong>colonel_concat(dialogue: List[str]) -&gt; Int</strong></p>
<ul>
<li><strong>dialogue:</strong> The list of strings to concatenate. You must preserve the "word" that would be concatenated together (see example 2).</li>
<li><strong>Output:</strong> Minimum number of copies to concatenate the string.</li>
<li><strong>Time Complexity: O(n^3)</strong>
<ul>
<li>n is the size of the input list</li>
<li>A naive approach to this problem is O(2^n)!</li>
</ul>
</li>
<li><strong>Space Complexity: O(n^2)</strong></li>
<li>You are allowed to use Lists and Dictionaries for this challenge.</li>
</ul>
<p>&nbsp;</p>
<h4><strong>Examples:</strong></h4>
<p><em>Ex. 1:</em></p>
<p><strong>dialogue:</strong> ['aaa', 'aa', 'a']</p>
<p><strong>Output:</strong> 9. The ideal concatenation for this string is <strong>'aaa' + ('aa' + 'a')</strong>. 'aa' + 'a' requires 3 copies, meaning that 'aaa' + 'aaa' is another 6 copies, resulting in a total of 9 string copies for this concatenation.</p>
<p>&nbsp;</p>
<p><em>Ex. 2:</em></p>
<p><strong>dialogue: </strong>['a', 'bbbb', 'c']</p>
<p><strong>Output:&nbsp;</strong>11. This is an example of a string where the "word" results in an inefficient concatenation. The resulting word has to be 'abbbbc', even though this doesn't represent the minimum number of copies for the concatenation. If this was the ideal case, where order did not matter, the optimal solution would be ('a' + 'c') + 'bbbb'. However, in all cases, <em><strong>ORDER MUST BE PRESERVED</strong></em> when determining the number of string copies.</p>
<p>&nbsp;</p>
<h1><strong>Submission</strong></h1>
<p><img class="HiaYvf-SmKAyb" src="https://lh6.googleusercontent.com/l_p-MNP7onFeq3VVsMVQLUenFOw8Nu_sk_xn3_focIyVRmaEFCESc58df2fX6vgS2D3zgDYyUB4Dudu0eaFSqCAeTm0nOtz4fSKeZYy5cMZRbYhZsjSAbq57Gfj-p3uKit2FZVOi" /></p>
<h2><strong>Deliverables</strong></h2>
<p>Be sure to upload the following deliverables in a .zip folder to Mimir by&nbsp;<strong>11:59PM</strong>&nbsp;Eastern Time on&nbsp;<strong>Tuesday, 04/20/2021</strong>.</p>
<p>Your .zip folder can contain other files (for example, description.md and tests.py), but must include (at least) the following:</p>
<pre>CC12.zip<br /> &nbsp;&nbsp;&nbsp;|&mdash; CC12/<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; README.xml &nbsp; &nbsp; &nbsp; (for coding challenge feedback)<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; __init__.py&nbsp; &nbsp; &nbsp; (for proper Mimir testcase loading)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; solution.py&nbsp; &nbsp; &nbsp; (contains your solution source code)</pre>
<h2><strong>Grading</strong></h2>
<p>The following 100-point rubric will be used to determine your grade on CC12:</p>
<ul>
<li>Tests (70)
<ul>
<li>00 - Coding Standard: __/5</li>
<li>01 - Test Basic: __/10</li>
<li>02 - Test Intermediate: __/15</li>
<li>03 - Test Large: _/20</li>
<li>04 - Test Comprehensive: __/20</li>
</ul>
</li>
<li>Manual (30)
<ul>
<li>README.md is <em>completely</em> filled out with (1) Name, (2) Feedback, (3) Time to Completion, (4) Citations, and (Difficulty): __/5</li>
<li>M0 - colonel_concat Time O[n^3): __/15</li>
<li>M1 - colonel_concat Space O(n^2): __/10</li>
</ul>
</li>
</ul>
<p>&nbsp;</p>
<h1><strong>Tips, Tricks, and Notes</strong></h1>
<ul>
<li>Remember that order must be preserved when determining the minimum number of string copies.</li>
<li>This problem is best solved by applying the practices of dynamic programming.</li>
</ul>
<p>Created by Andrew Haas, Sean Nguyen, and Lukas Richters</p>