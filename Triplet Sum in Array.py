"""
Given an array and an integer K. Find if there's a triplet in the array which sums up to the given integer K. 
 

Example 1:

Input: N = 6, K = 13
arr[] = [1 4 45 6 10 8]
Output: true
Explanation: The triplet {1, 4, 8} in 
the array sums up to 13.
Example 2:

Input: N = 5, K = 10
arr[] = [1 2 4 3 6]
Output: true
Explanation: The triplet {1, 3, 6} in 
the array sums up to 10.

Your Task:
You don't need to read input or print anything. Your task is to complete the function find3Numbers() which takes the array arr[], the size of the array (N) and the sum (X) as inputs and returns True if there exists a triplet in the array arr[] which sums up to X and False otherwise.

Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 103
1 ≤ A[i] ≤ 105
"""
def find3Numbers(arr, N, X):
    arr = sorted(arr)
    for i in range(N-2):
        l=i+1
        r=N-1
        while l<r:
            if arr[i] + arr[l] + arr[r] == X:
                return 1
            elif arr[i] + arr[l] + arr[r] < X:
                l = l + 1
            else:
                r = r - 1
    return 0
