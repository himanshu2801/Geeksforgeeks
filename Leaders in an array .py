"""
Given an array A of positive integers. Your task is to find the leaders in the array.

Note: An element of array is leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader. 

Example 1:

Input:
N = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements 
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.
Example 2:

Input:
N = 5
A[] = {1,2,3,4,0}
Output: 4 0
Explanation: 4 and 0 are leaders.
Your Task:
The task is to complete the function leader() which returns an array of leaders in same order as they appear in the array. The printing is automatically done by driver code.

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 107
0 <= Ai <= 107
"""
def leaders(A,N):
    lst=[]
    max = A[N-1]
    for i in range(N-1, -1, -1):
        if max == A[i] or max < A[i]:
            lst.append(A[i])
            max = A[i]
    lst.reverse()
    
    return lst
