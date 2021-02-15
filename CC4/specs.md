<p><strong>CC4 - SS21- A Challenger Approaches</strong></p>
<p><strong>Due: Tuesday,&nbsp; February 16th, 11:59 pm</strong></p>
<p><em><span style="font-weight: 400;">This is not a team project, do not copy someone else&rsquo;s work.</span></em></p>
<h1><strong>Introduction</strong></h1>
<p><img class="HiaYvf-SmKAyb" src="https://lh4.googleusercontent.com/dol_oB2LrfdRhn8xzWYJpVfl0EmawaB6HjxWMqbqdNyc1tyaUC8WrL3i2iXs_iRt2ZX6lE3ZG5YCmnwh4EnDwoZffc-cuhKCV4LQxm3rRX8kqA1Ut0oJSB5OesXcZ_ErFjsUxBix" /></p>
<p><span style="font-weight: 400;">As an avid Smash Ultimate player, you know that its online matchmaking is mediocre at best. Your opponents vary wildly: one moment you have a three-stock, 1 v. 1, no-items final destination match and the next you&rsquo;re in a 4-player, items on, smash-meter-on ruleset on the 75 m stage. This is bad and you know it can be much better. Knowing that Nintendo probably isn&rsquo;t going to fix this, you decide to take matters into your own hands and start making a better matchmaker yourself.</span></p>
<p><span style="font-weight: 400;">It&rsquo;s a big job, so you decide to start by matching players of similar skill levels. You think a good way to accomplish this is to look at how many stocks they got in their last game and check within a range to see how many players with a similar stock number are available. Being a good 331 student, you think it would be neat to try to use sorting or binary search to solve this problem. You also know it would be a good idea to read the rest of the coding challenge specs for more hints.</span></p>
<h1><strong>Challenge</strong></h1>
<h2><strong>Overview</strong></h2>
<p>In this problem you will be given a list of integers representing the number of stocks each player took in their last match, and an integer representing how wide the range to check should be. Using those given variables, your goal is to find the number of players within the created range for each player.&nbsp;</p>
<p>For example, suppose the given list is [5, 1, 3, 1] and the range variable is 2. The first player to work with is at index 0. They took 5 stocks in their last match. The range to check will be 2 above 5 so 7 and 2 below 5 so 3. Our range would then be [(5-2), (5+2)] or [3, 7] inclusive on both ends. In the given list there is only one value, 3, within that inclusive range so there is only 1 matchup available for the player at index 0. For a more in-depth example, check the later examples.</p>
<p>Your goal is to return a list with the number of available opponents for each player. The above example's return list would be [1, 2, 3, 2].</p>
<p><strong>Note:</strong> A <strong>stock</strong> is a term used in Smash Brothers it can be thought of as the same as a life in other video games.</p>
<p><em><span style="font-weight: 400;">Modify the following functions</span></em></p>
<p><strong>challenger_finder(numbers: List[int], k: int) -&gt; List[int]</strong></p>
<ul>
<li><strong>stocks_list: List[int]</strong><span style="font-weight: 400;">: A Python list of length n, containing integers, that represents the stocks taken in each player's last match. Each index represents a player.</span></li>
<li><strong>k: int: <span style="font-weight: 400;">Integer indicating the range that will be used to determine all available opponents for each player</span></strong></li>
<li style="font-weight: 400;"><strong>Return:</strong><span style="font-weight: 400;"> A Python list of length n, containing integers, consisting of the number of available opponents for each player.</span></li>
<li style="font-weight: 400;"><strong>Time Complexity:</strong><span style="font-weight: 400;"><em> O(nlog(n))</em> where <em>n</em> is the number of players</span></li>
</ul>
<h4><strong>Guarantees</strong></h4>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">The range, k, is <strong>nonnegative </strong>(either positive or zero)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">The </span><strong>stocks_list</strong><span style="font-weight: 400;"> may contain any integer, negative, positive, and zero</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">The </span><strong>stocks_list</strong><span style="font-weight: 400;"> may contain duplicate stocks number</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Each test case is generated as guaranteed</span></li>
</ul>
<p>&nbsp;</p>
<h4><strong>Examples:</strong></h4>
<p><strong>Ex 1:</strong></p>
<p><strong>stocks_list </strong><span style="font-weight: 400;">= [5, 1, 3, 2]</span></p>
<p><strong>k =</strong><span style="font-weight: 400;"> 1</span></p>
<p><span style="font-weight: 400;">The first player&rsquo;s stock is 5 from index 0, [</span><strong>5</strong><span style="font-weight: 400;">, 1, 3, 2], and the range is 1. The range to check possible opponents will be 1 below 5 and 1 above 5. Therefore, the range should be [5 - 1, 5 + 1] or [4, 6], inclusive on both sides. In the given list, there is no value within that finding range, [4, 6],excluding this player. Thus, </span><strong>no one</strong><span style="font-weight: 400;"> will match up with this player, and a&nbsp;<strong>0</strong> should be placed at index 0 in the return list.</span></p>
<p><span style="font-weight: 400;">The second player&rsquo;s stock is 1 from index 1, [5, </span><strong>1</strong><span style="font-weight: 400;">, 3, 2], and the range is 1. The range to check possible opponents will be 1 below 1 and 1 above 1. Therefore, the range should be [1 - 1, 1 + 1] or [0, 2], inclusive on both sides. In the given list, there is one value within that finding range, [0, 2], excluding this player. Thus, only </span><strong>one</strong><span style="font-weight: 400;"> player will match up with this playe</span><span style="font-weight: 400;">r, and a&nbsp;<strong>1</strong> should be placed at index 1 in the return list.</span></p>
<p><span style="font-weight: 400;">The third player&rsquo;s stock is 3 from index 2, [5, 1, </span><strong>3</strong><span style="font-weight: 400;">, 2], and the range is 1. The range to check possible opponents will be 1 below 3 and 1 above 3. Therefore, the range should be [3 - 1, 3 + 1] or [2, 4], inclusive on both sides. In the given list, there is one value within that finding range, [2, 4], excluding this player. Thus, only </span><strong>one</strong><span style="font-weight: 400;"> player will match up with this player,</span><span style="font-weight: 400;"> and a <strong>1</strong> should be placed at index 2 in the return list.</span></p>
<p><span style="font-weight: 400;">The last player&rsquo;s stock is 2 from index 3, [5, 1, 3, </span><strong>2</strong><span style="font-weight: 400;">], and the range is 1. The range to check possible opponents will be 1 below 2 and 1 above 2. Therefore, the range should be [2 - 1, 2 + 1] or [1, 3], inclusive on both sides. In the given list, there are two values within that finding range, [1, 3], excluding this player. Thus, </span><strong>two</strong><span style="font-weight: 400;"> players will match up with this playe</span><span style="font-weight: 400;">r, and a <strong>2</strong> should be placed at index 3 in the return list.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">According to the above results, the return list of numbers of possible opponents of each player will be <strong>[0, 1, 1, 2]</strong></span></p>
<p>&nbsp;</p>
<p><strong>Ex 2:</strong></p>
<p><strong>stocks_list </strong><span style="font-weight: 400;">= [40, 22, 30, 20]</span></p>
<p><strong>k =</strong><span style="font-weight: 400;"> 5</span></p>
<p><span style="font-weight: 400;">The first player&rsquo;s stock is 40 from index 0, [</span><strong>40</strong><span style="font-weight: 400;">, 22, 30, 20], and the range is 5. The range to check possible opponents will be 5 below 40 and 5 above 40. Therefore, the range should be [40 - 5, 40 + 5] or [35, 45], inclusive on both sides. In the given list, there is no value within that finding range, [35, 45],excluding this player. Thus, </span><strong>no one</strong><span style="font-weight: 400;"> will match up with this playe</span><span style="font-weight: 400;">r, and a&nbsp;<strong>0</strong> should be placed at index 0 in the return list.</span></p>
<p><span style="font-weight: 400;">The second player&rsquo;s stock is 22 from index 1, [40, </span><strong>22</strong><span style="font-weight: 400;">, 30, 20], and the range is 5. The range to check possible opponents will be 5 below 22 and 5 above 22. Therefore, the range should be [22 - 5, 22 + 5] or [17, 27], inclusive on both sides. In the given list, there is one value within that finding range, [17, 29], excluding this player. Thus, only </span><strong>one</strong><span style="font-weight: 400;"> player will match up with this playe</span><span style="font-weight: 400;">r, and a <strong>1</strong> should be placed at index 1 in the return list.</span></p>
<p><span style="font-weight: 400;">The third player&rsquo;s stock is 30 from index 2, [40, 22, </span><strong>30</strong><span style="font-weight: 400;">, 20], and the range is 5. The range to check possible opponents will be 5 below 30 and 5 above 30. Therefore, the range should be [30 - 5, 30 + 5] or [25, 35], inclusive on both sides. In the given list, there is no value within that finding range, [25, 35],excluding this player. Thus, </span><strong>no one</strong><span style="font-weight: 400;"> will match up with this playe</span><span style="font-weight: 400;">r, and a&nbsp;<strong>0</strong> should be placed at index 2 in the return list.</span></p>
<p><span style="font-weight: 400;">The last player&rsquo;s stock is 20 from index 3, [40, 22, 30, </span><strong>20</strong><span style="font-weight: 400;">], and the range is 5. The range to check possible opponents will be 5 below 20 and 5 above 20. Therefore, the range should be [20 - 5, 20 + 5] or [15, 25], inclusive on both sides. In the given list, there is one within that finding range, [15, 25], excluding this player. Thus, </span><strong>one</strong><span style="font-weight: 400;"> player will match up with this player</span><span style="font-weight: 400;">, and a <strong>1</strong> should be placed at index 3 in the return list.</span></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">According to the above results, the return list of numbers of possible opponents of each player will be <strong>[0, 1, 0, 1]</strong></span></p>
<p><br /><br /></p>
<h1><strong>Submission</strong></h1>
<p><img src="https://lh5.googleusercontent.com/yhikfAyWOkvvSNtloUt6oHIuyx-7YYYqcGsAJVMqKgsB1426WOCmIi1m28QfPYkE4GlwC5vC3ebj_bnwGAotBbqAmdt11wxK_UdPRgmm" width="640" height="360" /></p>
<h2><strong>Deliverables</strong></h2>
<p><span style="font-weight: 400;">Be sure to upload the following deliverables in a .zip folder to Mimir by </span><strong>11:59PM</strong><span style="font-weight: 400;"> Eastern Time on </span><strong>Tuesday, 02/16/2021</strong><span style="font-weight: 400;">. Note that&nbsp;<strong>both CC3 and CC4 are due on Tuesday, 02/16/2021</strong> due to the extension of CC3 resulting from Exam 1.</span></p>
<p><span style="font-weight: 400;">Your .zip folder can contain other files (for example, description.md and tests.py), but must include (at least) the following:</span></p>
<pre><span style="font-weight: 400;">CC4.zip</span><br /><span style="font-weight: 400;"> &nbsp;&nbsp;&nbsp;|&mdash; CC4/</span><br /><span style="font-weight: 400;"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; README.xml &nbsp; &nbsp; &nbsp; (for coding challenge feedback)</span><br /><span style="font-weight: 400;"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; __init__.py&nbsp; &nbsp; &nbsp; (for proper Mimir testcase loading)</span><br /><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; solution.py&nbsp; &nbsp; &nbsp; (contains your solution source code)</span></pre>
<h2><span style="font-weight: 400;">Grading</span></h2>
<p><span style="font-weight: 400;">The following 100-point rubric will be used to determine your grade on CC4:</span></p>
<ul>
<li><strong>Tests (75)</strong>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">00 - Coding Standard: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">01 - Test Basic: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">02 - Test Cover Whole: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">03 - Test Cover Only One: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">04 - Test Small Case Comprehensive: __/20</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">05 - Test Large Case Comprehensive: __/20</span></li>
</ul>
</li>
</ul>
<ul>
<li><strong>Manual (25)</strong></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">README.md is </span><em><span style="font-weight: 400;">completely</span></em><span style="font-weight: 400;"> filled out with (1) Name, (2) Feedback, (3) Time to Completion and (4) Citations: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time Complexity (O(nlog(n)): __/20</span></li>
</ul>
</ul>
<h1><span style="font-weight: 400;">Tips, Tricks, and Notes</span></h1>
<ul>
<li><strong>You must fill out docstrings to receive coding standard points.</strong></li>
<li><span style="font-weight: bold;">Please fill out your README: it&rsquo;s the easiest way to get points!</span></li>
<li>Try to start with an O(n^2) approach and improving your algorithm</li>
<li>Consider using sorting, sliding window, binary search, or combination of these to reduce time complexity</li>
<li>Consider a way to change the location of numbers (i.e., sort) while maintaining a reference to the location (index) in the list at which they were originally located.&nbsp;</li>
</ul>
<p>&nbsp;</p>
<p><em>Created by Bank Premsri and Andy Wilson</em></p>