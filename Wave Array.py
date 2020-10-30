"""
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it. In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5..... (considering the increasing lexicographical order).

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 2 1 4 3 5
Explanation: Array elements after 
sorting it in wave form are 
2 1 4 3 5.
 

Example 2:

Input:
N = 6
arr[] = {2,4,7,8,9,10}
Output: 4 2 8 7 10 9
Explanation: Array elements after 
sorting it in wave form are 
4 2 8 7 10 9.
Your Task:
The task is to complete the function convertToWave() which converts the given array to wave array.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).


Constraints:
1 ≤ N ≤ 106
0 ≤ A[i] ≤107
"""


def convertToWave(a, n):
    for i in range(1,n):
        if i%2==0:
            if a[i-1]>a[i]:
                a[i-1], a[i] = a[i], a[i-1]
        else:
            if a[i-1]<a[i]:
                a[i-1], a[i] = a[i], a[i-1]
    return a
