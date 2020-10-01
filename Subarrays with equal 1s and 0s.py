"""
Given an array containing 0s and 1s. Find the number of subarrays having equal number of 0s and 1s.

Example 1:

Input:
N = 7
A[] = {1,0,0,1,0,1,1}
Output: 8
Explanation: The index range for the 8 
sub-arrays are: (0, 1), (2, 3), (0, 3), (3, 4), 
(4, 5) ,(2, 5), (0, 5), (1, 6)
Example 2:

Input:
N = 5
A[] = {1,1,1,1,0}
Output: 1
Explanation: The index range for the 
subarray is (3,4).
Your Task:
You don't need to read input or print anything. Your task is to complete the function countSubarrWithEqualZeroAndOne() which takes the array arr[] and the size of the array as inputs and returns the number of subarrays with equal number of 0s and 1s.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 106
0 <= A[i] <= 1

"""
def countSubarrWithEqualZeroAndOne(arr, N):
    lst=[]
    for i in arr:
        if i==0:
            lst.append(-1)
        else:
            lst.append(1)
    count=0
    sum=0
    h={}
    for j in lst:
        sum=sum+j
        if sum==0:
            count=count+1
        if sum in h.keys():
            count=count+h[sum]
            h[sum]=h[sum]+1
        else:
            h[sum]=1
    return count
