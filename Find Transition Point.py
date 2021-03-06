"""
You are given a sorted array containing only numbers 0 and 1. Find the transition point efficiently. The transition point is a point where "0" ends and "1" begins (0 based indexing).
Note that, if there is no "1" exists, print -1.
Note that, in case of all 1s print 0.

Example 1:

Input:
N = 5
C[] = {0,0,0,1,1}
Output: 3
Explanation: position 3 is 0 and next
one is 1, so answer is 3.
Example 2:

Input:
N = 4
C[] = {0,0,0,0}
Output: -1
Explanation: Since, there is no "1",so
the answer is -1.
Your Task:
The task is to complete the function transitionPoint() that takes array and N as input and returns the value of the position where "0" ends and "1" begins.

Expected Time Complexity: O(LogN).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 500000
0 ≤ C[i] ≤ 1
"""
def transitionPoint(arr, n):
    if 1 not in arr:
        return -1
    elif 0 not in arr:
        return 0
    else:
        return arr.index(1)
