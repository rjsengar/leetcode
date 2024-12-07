<h2><a href="https://www.geeksforgeeks.org/problems/subsets-1613027340/1">Subsets</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an array <strong><code>arr</code></strong> of distinct positive integers, your task is to find all its subsets. The subsets should be returned in lexicographical order.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [1, 2, 3]
<strong>Output: </strong>[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
<strong>Explanation: <br></strong>The subsets of [1, 2, 3] in lexicographical order are:
[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [1, 2]
<strong>Output: </strong>[[], [1], [1, 2], [2]]
<strong>Explanation:</strong>
The subsets of [1, 2] in lexicographical order are:
[], [1], [1, 2], [2]</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> arr[] = [10]
<strong>Output: </strong>[[], [10]]
<strong>Explanation: </strong>For the array with a single element <code>[10]</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">, the subsets are </span><code>[]</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;"> and </span><code>[10]</code><span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">.</span></span></pre>
<div><span style="font-size: 14pt;"><strong>Constraints :</strong></span></div>
<div><span style="font-size: 14pt;">1 &lt;= arr.size() &lt;= 15</span></div>
<div><span style="font-size: 14pt;">1 &lt;= arr[i] &lt;=10<sup>4</sup></span></div></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Recursion</code>&nbsp;<code>Backtracking</code>&nbsp;<code>Algorithms</code>&nbsp;