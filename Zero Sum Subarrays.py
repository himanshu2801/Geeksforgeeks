"""
You are given an array A of size N. You need to print the total count of sub-arrays having their sum equal to 0.

Example 1:

Input:
N = 6
A[] = {0,0,5,5,0,0}
Output: 6
Explanation: The 6 subarrays are [0], [0],
[0], [0], [0 0], and [0 0].
Example 2:

Input:
N = 10
A[] = {6,-1,-3,4,-2,2,4,6,-12,-7}
Output: 4
Explanation: The 4 subarrays are [-1 -3 4]
[-2 2], [2 4 6 -12], and [-1 -3 4 -2 2]
Your Task:
Complete findSubarray function that takes array and its size as arguments and returns the total count of sub-arrays with 0 sum. The printing is done by the driver code.

Constraints:    
1<= N <= 107
-1010 <= Ai <= 1010

Expected Time Complexity : O(NlogN)
Expected Auxilliary Space : O(N)
"""
def findSubArrays(arr,n):
    sum = 0
    count = 0
    lst = {}
    for i in range(n):
        sum = sum + arr[i]
        if sum == 0:
            count = count + 1
        if sum in lst:
            count += lst[sum]
            lst[sum] = lst[sum] + 1
        if sum not in lst:
            lst[sum]=1
    return count
