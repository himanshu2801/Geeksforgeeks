"""
Given an array arr[] of N non-negative integers representing the height of blocks at index i as Ai where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
The structure is like below:
|  |
|_|
We can trap 2 units of water in the middle gap.



Example 1:

Input:
N = 4
arr[] = {7,4,0,9}
Output: 10
Explanation: Water trapped by the 
block of height 4 is 3 units, block 
of height 0 is 7 units. So, the 
total unit of water trapped is 
10 units.
Example 2:

Input:
N = 3
arr[] = {6,9,9}
Output: 0
Explanation: No water will be trapped.
Your Task:
The task is to complete the function trappingWater() which returns the total amount of water that can be trapped.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
3 <= N <= 107
0 <= Ai <= 108
"""

def trappingWater(arr,n):
    left = []
    right = []
    max = arr[0]
    for i in range(n):
        if max <= arr[i]:
            max = arr[i]
        left.append(max)
    max = arr[n-1]
    for i in range(n-1, -1, -1):
        if max <= arr[i]:
            max = arr[i]
        right.append(max)
    sum = 0
    right.reverse()
    for i in range(n):
        x = min(left[i], right[i]) - arr[i]
        if x > 0:
            sum = sum + x
    return sum
