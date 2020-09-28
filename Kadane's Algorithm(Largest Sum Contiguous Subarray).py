"""
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
1 ≤ T ≤ 110
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Example:
Input
2
5
1 2 3 -2 5
4
-1 -2 -3 -4
Output
9
-1

Explanation:
Testcase 1: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.
"""
t=int(input())
for i in range(t):
    x=int(input())
    l=0
    lst=[int(x) for x in input().split()]
    for j in lst:
        if j>0:
            l=l+1
            break
    if l==0:
        print(max(lst))
    else:
        max1=0
        max_end=0
        sum1=0
        for j in range(len(lst)):
            max_end=max_end+lst[j]
            if max_end<0:
                max_end=0
            if max1<max_end:
                max1=max_end
        print(max1)
