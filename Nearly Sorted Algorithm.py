"""
Given an array of n elements, where each element is at most k away from its target position. The task is to print array in sorted form.

Input:
First line consists of T test cases. First line of every test case consists of two integers N and K, denoting number of elements in array and at most k positions away from its target position respectively. Second line of every test case consists of elements of array.

Output:
Single line output to print the sorted array.

Constraints:
1<=T<=100
1<=N<=100
1<=K<=N

Example:
Input:
2
3 3
2 1 3
6 3
2 6 3 12 56 8
Output:
1 2 3
2 3 6 8 12 56
"""
t=int(input())
for i in range(t):
    x,y=input().split()
    x=int(x)
    y=int(y)
    lst=[int(x) for x in input().split()]
    lst=sorted(lst)
    for j in lst:
        print(j , end=' ')
    print("")
