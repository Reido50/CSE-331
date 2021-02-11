<h1><strong>CC3 - SS21- Salmon Run <em>Profreshional</em></strong></h1>
<p><strong>Due: Tuesday, February 9th, 11:59 pm</strong></p>
<p><em>This is not a team project, do not copy someone else&rsquo;s work.</em></p>
<h1><strong>Introduction</strong></h1>
<p><img class="HiaYvf-SmKAyb" src="https://lh6.googleusercontent.com/bd-6as5aYfBJiJFLW0wqAQ9JenTGJj2KMxNLGbHn8npvdqWWI8CFcW271QNeaYItTF5UG5cvQFr_WhNlDe4UGpLhAIXt9dUujxsh_44zm0ZPoRd4qMoa9ZvdKLCTcmwKY0A7RKs7" /><br /><br /></p>
<p><span style="font-weight: 400;">As an avid Splatoon 2: Salmon Run player you feel the randomly matched online teammates you&rsquo;re getting aren&rsquo;t quite up to snuff. So you create a bot that will learn to play Salmon Run by itself so you won&rsquo;t have to rely on real human teammates. For your bot, you&rsquo;re tracking how many salmonids it defeats before dying. You want to find out which iteration of your bot did the best and you know that the best bot iteration will be the one where the kill count changes from increasing to decreasing.&nbsp;</span></p>
<p><span style="font-weight: 400;">Instead of going through all of the data by hand, you decide to create a program that will do it for you so you can participate in this weekend&rsquo;s Splatfest. Since you recently learned about recursion you decide to write your function recursively for more practice.</span></p>
<h1><strong>Challenge</strong></h1>
<h2><strong>Overview</strong></h2>
<p><span style="font-weight: 400;">For this challenge you will be making a </span><strong>recursive</strong><span style="font-weight: 400;"> function that will find the point in a list where it stops increasing for example [1 ,2, 3, 5, 1] it stops increasing at 5 which is at </span><strong>index 4</strong><span style="font-weight: 400;"> so your function should return </span><strong>4</strong><span style="font-weight: 400;">. </span></p>
<p><span style="font-weight: 400;"><strong>Please note</strong> that for this function the index returned will be from in range 1 to n. So for the example given above the if the list stopped increasing at the beginning then 1 would be returned as the index, or if it stopped increasing at the second element then 2 would be returned, if at the third element then 3, the forth 4, and if at the fifth then 5. So essentially just add one to the list index of the element.</span></p>
<p><span style="font-weight: 400;">Your function will receive a python list of integers that represents the number of salmonids that your bot defeated.</span></p>
<p><span style="font-weight: 400;">Your goal is to find the index of the bot where the salmonid defeat count stopped increasing in the given python list.</span></p>
<p><em><span style="font-weight: 400;">Modify the following functions</span></em></p>
<p><strong>finding_best_bot( bots_list: List[int]) -&gt; int</strong></p>
<ul>
<li style="font-weight: 400;"><strong>bots_list: List[int]</strong><span style="font-weight: 400;">: The python list of integer of size n that represents the number of salmonids that your bot defeated</span></li>
<li style="font-weight: 400;"><strong>Notice that index of robot start at 1 not 0</strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">You <strong>must use the </strong></span><strong>recursive function</strong><span style="font-weight: 400;"> inside the finding_best_bot, it&rsquo;s the inner function</span></li>
<li style="font-weight: 400;"><strong>Return:</strong><span style="font-weight: 400;"> An integer that represents </span><span style="font-weight: 400;">the bot&rsquo;s index where the salmonid defeat count stopped increasing in the given python list, in the other words, the last bot where defeat count increased.</span></li>
<li style="font-weight: 400;"><strong>Time Complexity:</strong><span style="font-weight: 400;"> O(log(n)) where n is the size of bots_list</span></li>
</ul>
<h4><strong>Guarantees</strong></h4>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">bots_list is generated carefully; so, that it always has increasing order before decreasing order. If the increasing sequence doesn&rsquo;t exist in the bots_list, it will start with a decreasing sequence.</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">The integer inside bots_list <strong>is always positive</strong></span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Each number will either increase or decrease from the previous one. In the other words, <strong>ai &lt; aj or ai &gt; aj, where i &lt; j, 0 &lt;= i &lt; j &lt; n, i and j are index of actual list</strong></span></li>
</ul>
<h4><strong>Examples:</strong></h4>
<p><strong>Ex 1:</strong></p>
<p><strong>bots_list</strong><span style="font-weight: 400;"> = [1, 2, 3, 20, 1]</span></p>
<p><span style="font-weight: 400;">[<strong>1</strong></span><strong>, 2</strong><span style="font-weight: 400;">, 3, 20, 1]</span></p>
<p><span style="font-weight: 400;">Starting at index 1 we see that the value here is 1 and the value at the next index is 2. 2 is greater than 1 so we&rsquo;ll continue iteration through this list.&nbsp;</span></p>
<p><span style="font-weight: 400;">[1, </span><strong>2, 3</strong><span style="font-weight: 400;">, 20, 1]</span></p>
<p><span style="font-weight: 400;">Next the value at index 2 is 2 and the value at the next index is 3. 3 is greater than 2 so we&rsquo;ll continue iterating.&nbsp;</span></p>
<p><span style="font-weight: 400;">[1, 2, </span><strong>3, 20</strong><span style="font-weight: 400;">, 1]</span></p>
<p><span style="font-weight: 400;">Next the value at index 3 is 3 and the value at the next index is 20. 20 is greater than 3 so we&rsquo;ll continue on because we have not found the index where the list stops increasing.&nbsp;</span></p>
<p><span style="font-weight: 400;">[1, 2, 3, </span><strong>20, 1</strong><span style="font-weight: 400;">]</span></p>
<p><span style="font-weight: 400;">Next the value at index 4 is 20 and the value at the next index is 1. 1 is less than 20 so we&rsquo;ve found the index where the list stops increasing. The 20 is located at index 4 so the function will return 4.</span></p>
<p><strong>Return</strong><span style="font-weight: 400;">: 4</span></p>
<p>&nbsp;</p>
<p><strong>Ex 2:</strong></p>
<p><strong>bots_list</strong><span style="font-weight: 400;"> = [1, 10, 20, 5, 1]</span></p>
<p><span style="font-weight: 400;">[</span><strong>1, 10</strong><span style="font-weight: 400;">, 20, 5, 1]</span></p>
<p><span style="font-weight: 400;">Starting at index 1 we see that the value here is 1 and the value at the next index is 10. 10 is greater than 0 so we&rsquo;ll continue iteration through this list.&nbsp;</span></p>
<p><span style="font-weight: 400;">[1, </span><strong>10, 20</strong><span style="font-weight: 400;">, 5, 1]</span></p>
<p><span style="font-weight: 400;">Next the value at index 2 is 10 and the value at the next index is 20. 20 is greater than 10 so we&rsquo;ll continue iterating.&nbsp;</span></p>
<p><span style="font-weight: 400;">[1, 10,</span><strong> 20, 5</strong><span style="font-weight: 400;">, 1]</span></p>
<p><span style="font-weight: 400;">Next the value at index 3 is 20 and the value at the next index is 5. 5 is less than 20 so we&rsquo;ve found the index where the list stops increasing. The 20 is located at index 3 so the function will return 3.</span></p>
<p><strong>Return</strong><span style="font-weight: 400;">: 3</span></p>
<p>&nbsp;</p>
<h1><strong>Submission</strong></h1>
<p><img class="HiaYvf-SmKAyb" src="https://lh5.googleusercontent.com/fw8KUsT2k010jTULDk5_lG5eAmxoMzNxO02vOvh3eLBfo8ENHt2Y2Cy40xcNwvPXgh_vODoDhX0FSngC45WITMdKqUp_-2QVbL050sdh" width="670" height="377" /></p>
<h2><strong>Deliverables</strong></h2>
<p><span style="font-weight: 400;">Be sure to upload the following deliverables in a .zip folder to Mimir by </span><strong>11:59PM</strong><span style="font-weight: 400;"> Eastern Time on </span><strong>Tuesday, 02/09/2021</strong><span style="font-weight: 400;">.</span></p>
<p><span style="font-weight: 400;">Your .zip folder can contain other files (for example, description.md and tests.py), but must include (at least) the following:</span></p>
<p><span style="font-weight: 400;">CC3.zip</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; CC3/</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; README.xml &nbsp; &nbsp; &nbsp; (for coding challenge feedback)</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; __init__.py&nbsp; &nbsp; &nbsp; (for proper Mimir testcase loading)</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; solution.py&nbsp; &nbsp; &nbsp; (contains your solution source code)</span></p>
<h2><strong>Grading</strong></h2>
<p><span style="font-weight: 400;">The following 100-point rubric will be used to determine your grade on CC3:</span></p>
<ul>
<li><strong>Tests (75)</strong></li>
<ul>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">00 - Coding Standard: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">01 - Test Basic: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">02 - Test All Increasing List: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">03 - Test All Decreasing List: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">04 - Test Comprehensive Small: __/20</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">05 - Test Comprehensive Large: __/20</span></li>
</ul>
</ul>
<li><strong>Manual (25)</strong></li>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">README.md is </span><em><span style="font-weight: 400;">completely</span></em><span style="font-weight: 400;"> filled out with (1) Name, (2) Feedback, (3) Time to Completion and (4) Citations: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time Complexity (O(log(n)): __/20</span></li>
</ul>
</ul>
<p>&nbsp;</p>
<h1><strong>Tips, Tricks, and Notes</strong></h1>
<ul>
<li><strong><em>You must fill out docstrings</em></strong></li>
<li><strong><em>You must remove REPLACE in README, and put appropriate text on each section</em></strong></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Only inner function is required to use recursively</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">You must not use any additional data structure</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Hint: Think of how the value change from one index to another</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Hint: Think of a </span><a href="https://www.geeksforgeeks.org/binary-search/"><span style="font-weight: 400;">binary search</span></a><span style="font-weight: 400;">, make sure you understand how it work</span></li>
</ul>
<h2><strong>Fun Addition</strong></h2>
<ul>
<li><span style="font-weight: 400;">It can be fun to have some themed music to listen to while working so here's some music from the Splatoon series. It's fantastic! Here's my favorite <a href="https://youtu.be/1LpLirdVEk4" target="_blank" rel="noopener noreferrer">song</a>. Playlists: <a href="https://youtube.com/playlist?list=PLyyBMVVhBOc3VkRqPKdqx1eL4F2ymapDM" target="_blank" rel="noopener noreferrer">Splatoon</a> <a href="https://youtube.com/playlist?list=PL47vq3g0IDNLeuHpylQuKRUZA1h5U1iso" target="_blank" rel="noopener noreferrer">Splatoon 2</a></span></li>
</ul>
<p><span style="font-weight: 400;">Created by Bank Premsri and Andy Wilson</span></p>