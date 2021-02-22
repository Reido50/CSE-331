<p><strong>CC5 - SS21- In the Guardian&rsquo;s Gaze</strong></p>
<p><strong>Due: Tuesday,&nbsp; February 23th, 11:59 pm</strong></p>
<p><em><span style="font-weight: 400;">This is not a team project, do not copy someone else&rsquo;s work.</span></em></p>
<h1><strong>Introduction</strong></h1>
<p><strong><img src="https://lh3.googleusercontent.com/uP_OlV5cP-g10FSO4vBCrR1H2LW1xoJ1s0NXUk3AT-Z6nw2d56YuKA6hreVsIE-BXz3KaLoNBW8tfmgGxCmcI3UO-dwBbf7rWap5QWOPigksoCl7DBYVXqOz8I-nH-4vlOgRJXLC" /></strong></p>
<p><span style="font-weight: 400;">You&rsquo;ve been eagerly awaiting the sequel to the hit Nintendo Switch game The Legend of Zelda: Breath of the Wild, but you haven&rsquo;t heard anything about it since its announcement way back in June 2019. To fill the Zelda shaped void in your life you decide to create your own version of the game. You decide to bring back all of the classic enemies from the first game bokoblins, lynels, and of course the guardians.&nbsp;</span></p>
<p><span style="font-weight: 400;">You&rsquo;re currently working on the areas where the guardians live and, you want to make sure there is enough cover for Link to hide but also not too much where the player can easily avoid the guardian&rsquo;s sight. Your guardians work by sending a raycast out from their eye and if the ray hits Link then he&rsquo;s been spotted and the guardians goes on the attack, however the guardian can&rsquo;t see through walls. So if there is a tall wall it will block all smaller walls behind it. Also because of a bug in your code the guardian can only look up so if Link is on a wall lower than the guardian it won&rsquo;t see him. You don&rsquo;t feel like fixing it right now so you claim &ldquo;<em>It&rsquo;s not a bug. It&rsquo;s a feature</em>&rdquo; and try to design your area&rsquo;s accordingly. Instead of going around each area and testing out how many spots exist where the guardian can see you decide to put all of the area&rsquo;s wall heights into a list and create a program that will return the number of walls that can be seen when standing on top of each wall. Since you are a student who loves 331 so much, you decide to use a stack to solve this problem because it seems like a fun challenge. You also heard that you can use a Python-list as a stack by using the pop() function. Neat!</span></p>
<h1><strong>Challenge</strong></h1>
<h2><strong>Overview</strong></h2>
<p><span style="font-weight: 400;">In this coding challenge you will create a function that takes in a list of wall heights and returns a list of how many walls can be seen at each index. The walls list is a python-list of integers and each number represents the height of the wall. While standing on a wall you can only see walls that are taller than the current wall you&rsquo;re standing on and aren&rsquo;t blocked by taller walls. So if you're standing on a wall of height 6 and there are three walls in front of you of height 10, 9 and 24 you&rsquo;ll only be able to see the walls of height 10 and 24 since the wall of height 10 obscures the wall of height 9.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">For example if given the list [2, 1, 3, 4, 1, 5] starting from the first index the wall has a height of 2 so you can see the walls of height 3, 4, 5 so that means you can see 3 walls. At the second index the wall has a height of 1 so you can see walls of height 2, 3, 4, 5 so you can see 4 walls. At the third index the wall has a height of 3 so you can see the walls of height 4 and 5 so you see 2 walls. At the fourth index the wall has a height of 4 so you can see the wall of height 5 and you only see 1 wall. At the fifth index you can see the walls of heights 4 and 5 so you can only see 2 walls. Finally at the 5 index you can&rsquo;t see any other walls since you are standing on the tallest wall. The returned list will be [3, 4, 2, 1, 2, 0].</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">It is recommended that you use a stack to try and solve this problem so you can achieve the required runtime. There is not need to create your own stack class you can just use a <a href="https://www.geeksforgeeks.org/stack-and-queues-in-python/" target="_blank" rel="noopener noreferrer">Python-list as a stack</a>.</span></p>
<p><em><span style="font-weight: 400;">Modify the following functions</span></em></p>
<p><strong>check_walls_cover(walls: List[int]) -&gt; List[int]</strong></p>
<ul>
<li style="font-weight: 400;"><strong>walls: List[int]</strong><span style="font-weight: 400;">: The python integer list of size n that represents height of the wall</span></li>
<li style="font-weight: 400;"><strong>Return:</strong><span style="font-weight: 400;"> The python integer list consists of results compute as describe</span></li>
<li style="font-weight: 400;"><strong>Time Complexity:</strong><span style="font-weight: 400;"> O(n) where n is the size of walls&rsquo; list</span></li>
<li style="font-weight: 400;"><strong>Space Complexity:</strong><span style="font-weight: 400;"> O(n) where n is the size of walls&rsquo; list</span></li>
</ul>
<p>&nbsp;</p>
<h4><strong>Guarantees</strong></h4>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">The height of the walls is either zero or positive number</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Test Case is generate as guarantees</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">No more guarantee for coding challenge 5</span></li>
</ul>
<h4><strong>Examples:</strong></h4>
<p>&nbsp;</p>
<p><strong>walls_list</strong><span style="font-weight: 400;"> = [5, 2, 1, 10, 8, 4, 11]</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">At the first index, you stand on a wall of height 5. You can clearly see two walls with height 10 and 11, respectively. Then, two will be on the first place of the result&rsquo;s list.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">At the second index, you stand on a wall of height 2. You can clearly see three walls with height 5 on the left and 10 and 11 on the right. Then, three will be on the second index of the result&rsquo;s list.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">At the third index, you stand on a wall of height 1. You can clearly see fours walls with height 2 and 5 on the left and 10 and 11 on the right. Then, four will be on the third index of the result&rsquo;s list.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">At the fourth index, you stand on a wall of height 10. You can clearly see one wall with height 11. Then, one will be on the fourth index of the result&rsquo;s list.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">At the fifth index, you stand on a wall of height 8. You can clearly see two walls with height 10 on the left and 11 on the right. Then, two will be on the fifth index of the result&rsquo;s list.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">At the sixth index, you stand on a wall of height 4. You can clearly see three walls with height 8 and 10 on the left and 11 on the right. Then, three will be on the sixth index of the result&rsquo;s list.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">Finally, you stand on the last wall of height 11. You cannot see any wall around. Then, placing the zero on the last index of the result&rsquo;s list.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">After operating through the list, your function will return [2, 3, 4, 1, 2, 3, 0].</span></p>
<h1><strong>Submission</strong></h1>
<p><img src="https://lh5.googleusercontent.com/lPWQLQ6vAFBWmd8LMPuBZL9rOHPhcUF_mLhJM-02FnjWTaiF-_EB9PdtCfsqlmPBG0w6hYLPgd4VsDxRMZy1ecImoDTYQ_uWQaFTLD2q" width="576" height="324" /></p>
<h2><strong>Deliverables</strong></h2>
<p><span style="font-weight: 400;">Be sure to upload the following deliverables in a .zip folder to Mimir by </span><strong>11:59PM</strong><span style="font-weight: 400;"> Eastern Time on </span><strong>Tuesday, 02/23/2021</strong><span style="font-weight: 400;">.</span></p>
<p><span style="font-weight: 400;">Your .zip folder can contain other files (for example, description.md and tests.py), but must include (at least) the following:</span></p>
<p><span style="font-weight: 400;">CC5.zip</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; CC5/</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; README.xml &nbsp; &nbsp; &nbsp; (for coding challenge feedback)</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; __init__.py&nbsp; &nbsp; &nbsp; (for proper Mimir testcase loading)</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; solution.py&nbsp; &nbsp; &nbsp; (contains your solution source code)</span></p>
<h2><span style="font-weight: 400;">Grading</span></h2>
<p><span style="font-weight: 400;">The following 100-point rubric will be used to determine your grade on CC4:</span></p>
<ul>
<li>Tests (65)</li>
</ul>
<ul>
<ul>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">00 - Coding Standard: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">01 - Test Basic: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">02 - Test Only Increasing: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">03 - Test Only Decreasing: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">04 - Test Small Comprehensive: __/15</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">05 - Test Large Comprehensive: __/20</span></li>
</ul>
</ul>
</ul>
<ul>
<li>Manual (35)</li>
</ul>
<ul>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">README.md is </span><em><span style="font-weight: 400;">completely</span></em><span style="font-weight: 400;"> filled out with (1) Name, (2) Feedback, (3) Time to Completion and (4) Citations: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time Complexity (O(n)): __/15</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Space Complexity (O(n)): __/15</span></li>
</ul>
</ul>
<p>&nbsp;</p>
<h1><span style="font-weight: 400;">Tips, Tricks, and Notes</span></h1>
<ul>
<li><strong>You must fill out doc-strings!</strong></li>
</ul>
<ul>
<li><strong>Please fill out README, it&rsquo;s the easiest way to get points!</strong></li>
<li>You can use Python list as stack</li>
</ul>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Additional data structures other than Python List are <strong>not allowed</strong>.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">List append() operates in O(1)</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">List pop() (when used on the last element in a list) operates in O(1)</span></li>
</ul>
<p><br /><br /></p>
<p><em><span style="font-weight: 400;">Created by Bank Tanawan and Andy Wilson</span></em></p>
<p><br /><br /></p>