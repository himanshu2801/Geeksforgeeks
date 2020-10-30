"""
Given an array of size N containing 0s, 1s, and 2s; sort the array in ascending order.

Input:
First line of input contains number of testcases T. For each testcase, there will be two lines, first of which will contain N. The second lines contains the elements of the array.

Output: 
Print sorted array.

Your Task:
Complete the function sort012() that takes array and n and sorts the array in place. 

Constraints: 
1 <= T <= 50
1 <= N <= 10^5
0 <= A[i] <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0

Output:
0 0 1 2 2
0 0 1

Explanation:
Testcase 1: After segragating the 0s, 1s and 2s, we have 0 0 1 2 2 which shown in the output.
"""
def sort012(arr,n):
    count0=arr.count(0)
    count1=arr.count(1)
    count2=arr.count(2)
    i=0
    while count0!=0:
       arr[i]=0
       count0=count0-1
       i=i+1
    while count1!=0:
       arr[i]=1
       count1=count1-1
       i=i+1
    while count2!=0:
       arr[i]=2
       count2=count2-1
       i=i+1