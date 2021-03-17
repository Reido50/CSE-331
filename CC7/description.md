<h1><strong>CC7 - SS21- Combo Time</strong></h1>
<p><strong>Due: Tuesday,&nbsp; March 16th, 11:59 pm</strong></p>
<p><em><span style="font-weight: 400;">This is not a team project, do not copy someone else&rsquo;s work.</span></em></p>
<h1><strong>Introduction</strong></h1>
<p style="text-align: center;"><img src="https://s3.amazonaws.com/mimirplatform.production/files/2f6ee375-6d37-4c17-93b2-b9fe636fbac9/wonderful101.gif" alt="wonderful101.gif" width="538" height="303" /></p>
<p><span style="font-weight: 400;">As a huge action and fighting game fan, you love when you pull off a big juicy combo. Since you&rsquo;re such a big fan, you decide to create your own action game. You decide that your gimmick will be that by rewinding time, your combo will play in reverse up until the greatest, but smaller hit point in the combo is reached. You&rsquo;ve designed your combo system in a way where it is easy to take in list hit points from a combo and find the ending greatest smallest hit point to end your combo rewind attack.&nbsp;</span></p>
<p><span style="font-weight: 400;">For your revolutionary new system to work, you need to find the greatest smaller predecessor from the element in your combo hit points list. Since you are such a big fan of CSE 331 you paid good attention and think using a tree would be a good idea plus, you know them like the back of your hand. Should be no sweat!</span></p>
<h1><strong>Challenge</strong></h1>
<h2><strong>Overview</strong></h2>
<p><span style="font-weight: 400;">In this problem you will be given a list of integers. Each element of the input list should be replaced with the greatest element that is smaller than the current element </span><strong>and</strong><span style="font-weight: 400;"> is to its left. Your function will return nothing, but instead will edit the input list inplace so the element&rsquo;s greatest smaller predecessor will take its place.</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">For example, if the input list [4, 6, 3, 9, 7, 10] the output would be [None, 4, None, 6, 6, 9]. Please see the below examples for a detailed walk through of the example.&nbsp;</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">As an added twist, we will be requiring you to adhere to an</span><strong> average &amp; worst case</strong><span style="font-weight: 400;"> time complexity this time around! We </span><strong>highly</strong><span style="font-weight: 400;"> recommend that you use a BST to solve this problem because it will give you the desired average runtime. <span data-preserver-spaces="true">Please note that the BST would be&nbsp;</span><strong><span data-preserver-spaces="true">non-balancing</span></strong><span data-preserver-spaces="true">&nbsp;so,&nbsp;</span><strong><span data-preserver-spaces="true">don't worry</span></strong><span data-preserver-spaces="true">&nbsp;about the additional overhead that would be required when using/making a balancing BST.</span></span></p>
<p><span style="font-weight: 400;">The following TreeNode class is given to you</span></p>
<table style="height: 207px;" width="590">
<tbody>
<tr>
<td style="width: 584px;">
<p><strong>class TreeNode:</strong></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;def __init__(self, val: int, left: TreeNode = None, right: TreeNode = None):</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.val = val</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.left = left</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.right = right</span></p>
</td>
</tr>
</tbody>
</table>
<p><em><span style="font-weight: 400;">Modify the following function</span></em></p>
<p><strong>rewind_combo(points: List[int]) -&gt; List[Optional[int]]:</strong></p>
<ul>
<li><strong>points:</strong> List[int]: <span style="font-weight: 400;">Python integer list of size n representing hit points</span></li>
</ul>
<ul>
<li><strong>Return:</strong> A new list with the <span style="font-weight: 400;">greatest smaller predecessor for each element in the list</span></li>
</ul>
<ul>
<li><strong>Average Case Time Complexity:</strong> <span style="font-weight: 400;">O(nlogn) where n is the size of the points list</span></li>
</ul>
<ul>
<li><strong>Worst Case Time Complexity:</strong> <span style="font-weight: 400;">O(n^2) where n is the size of the points list</span></li>
</ul>
<ul>
<li><strong>Space Complexity:</strong> <span style="font-weight: 400;">O(n) where n is the size of the points list</span></li>
<li><strong><span style="font-weight: 400;"><strong>Note</strong>: You will not receive any runtime points for this function unless you meet both the average and worst case time complexities.</span></strong></li>
</ul>
<h3><strong>Guarantees</strong></h3>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">The points list will always contain integers with </span><strong>no </strong><span style="font-weight: 400;">duplicates</span></li>
</ul>
<h3><strong>Examples:</strong></h3>
<p>&nbsp;</p>
<p><strong>ORIGINAL input</strong><span style="font-weight: 400;"> = </span><span style="font-weight: 400;">[4, 6, 3, 9, 7, 10]</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">Input = [</span><strong>4</strong><span style="font-weight: 400;">, 6, 3, 9, 7, 10]</span></p>
<p><span style="font-weight: 400;">The first element of the original list has no elements to its left, which guarantees it will be replaced with </span><strong>None</strong><span style="font-weight: 400;">. So the return list should look like [<strong>None</strong>]</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">Input = [4, </span><strong>6</strong><span style="font-weight: 400;">, 3, 9, 7, 10]</span></p>
<p><span style="font-weight: 400;">The second element, 6, has one element to its left in the original list [4, 6, 3, 9, 7, 10] with a value of 4. 4 is less than 6 and is the greatest of all 1 values to its left, so the second element will be replaced with 4. The return list should now look like [None, </span><strong>4</strong><span style="font-weight: 400;">]</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">Input = [4, 6, </span><strong>3</strong><span style="font-weight: 400;">, 9, 7, 10]</span></p>
<p><span style="font-weight: 400;">The third element, 3, has two elements to its left in the original list [4, 6, 3, 9, 7, 10] with the values of 4 and 6. Neither of these values are less than 3, guaranteeing the third element will be replaced with None. The return list should now look like [None, 4, <strong>None</strong>]</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">Input = [4, 6, 3, </span><strong>9</strong><span style="font-weight: 400;">, 7, 10]</span></p>
<p><span style="font-weight: 400;">The fourth element, 9, has three elements to its left in the original list [4, 6, 3, 9, 7, 10] with the values of 4, 6 and 3. All of these values are less than 9, so the element will be replaced with the largest of the three, 6. The return list should now look like [None, 4, None, </span><strong>6</strong><span style="font-weight: 400;">]</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">Input = [4, 6, 3, 9, </span><strong>7</strong><span style="font-weight: 400;">, 10]</span></p>
<p><span style="font-weight: 400;">The fifth element, 7, has four elements to its left in the original list [4, 6, 3, 9, 7, 10] with the values of 4, 6, 3 and 9. All of these values except 9 are less than 7, so the element will be replaced with the largest of the three, 6. The return list should now look like [None, 4, None, 6, </span><strong>6</strong><span style="font-weight: 400;">]</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">Input = [4, 6, 3, 9, 7, </span><strong>10</strong><span style="font-weight: 400;">]</span></p>
<p><span style="font-weight: 400;">Finally the last element, 10, is the largest element of the list, and will be replaced with the largest value coming before it, 9. So the return list should look like [None, 4, None, 6, 6, </span><strong>9</strong><span style="font-weight: 400;">]</span></p>
<p>&nbsp;</p>
<p><span style="font-weight: 400;">Once the function is all done the returned list should look like </span><strong>[None, 4, None, 6, 6, 9].</strong></p>
<p>&nbsp;</p>
<h1><strong>Submission</strong></h1>
<p style="text-align: center;"><img src="https://s3.amazonaws.com/mimirplatform.production/files/ba568f2b-d7f9-41a3-92c3-e17e4e71cf08/wombo.gif" alt="wombo.gif" /></p>
<h2><strong>Deliverables</strong></h2>
<p><span style="font-weight: 400;">Be sure to upload the following deliverables in a .zip folder to Mimir by </span><strong>11:59PM</strong><span style="font-weight: 400;"> Eastern Time on </span><strong>Tuesday, 03/16/2021</strong><span style="font-weight: 400;">.</span></p>
<p><span style="font-weight: 400;">Your .zip folder can contain other files (for example, description.md and tests.py), but must include (at least) the following:</span></p>
<p><span style="font-weight: 400;">CC7.zip</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; CC7/</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; README.xml &nbsp; &nbsp; &nbsp; (for coding challenge feedback)</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; __init__.py&nbsp; &nbsp; &nbsp; (for proper Mimir testcase loading)</span></p>
<p><span style="font-weight: 400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&mdash; solution.py&nbsp; &nbsp; &nbsp; (contains your solution source code)</span></p>
<h2><strong>Grading</strong></h2>
<p><span style="font-weight: 400;">The following 100-point rubric will be used to determine your grade on CC7:</span></p>
<ul>
<li>Tests (65)</li>
</ul>
<ul>
<ul>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">00 - Coding Standard: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">01 - Test Basic: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">02 - Test Worst Case: __/10</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">03 - Test Best Case: __/10</span></li>
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
<li style="font-weight: 400;"><span style="font-weight: 400;">README.xml is </span><em><span style="font-weight: 400;">completely</span></em><span style="font-weight: 400;"> filled out with (1) Name, (2) Feedback, (3) Time to Completion and (4) Citations: __/5</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Time Complexity (</span><strong>average</strong><span style="font-weight: 400;"> O(nlogn), </span><strong>worst </strong><span style="font-weight: 400;">O(n^2)): __/25</span></li>
<li style="font-weight: 400;"><span style="font-weight: 400;">Space Complexity (O(n)): __/5</span></li>
</ul>
</ul>
<p>&nbsp;</p>
<h1><strong>Tips, Tricks, and Notes</strong></h1>
<ul>
<li>You must fill out doc-strings!</li>
</ul>
<ul>
<li>Please fill out README, it&rsquo;s the easiest way to get points!</li>
</ul>
<ul>
<li style="font-weight: 400;"><span style="font-weight: 400;">Think of how you can utilize BST operations to achieve the required average time complexity. Many BST operations (insert, search, etc.) run in O(h) time where h is the height of the tree. Depending on how balanced the tree is, h will be anywhere in between log(n) and n, but on average will lean towards log(n). Use this to your advantage!</span></li>
<li><span data-preserver-spaces="true">If you decide to go for the BST route, keep in mind that this tree will be non-balancing so, there is a lot less overhead when writing this because you won't have to worry about keeping the tree balanced.</span></li>
</ul>
<p>&nbsp;</p>
<p><em><span style="font-weight: 400;">Created by Zach Arnold and Andy Wilson</span></em></p>
