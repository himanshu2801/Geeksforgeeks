"""
Ishaan is given N integers in the form of an array A. He is asked to select all of these integers in any order. For selecting every integer he gets some points. He needs to maximize those points.
For every integer he selects, he gets points equal to the value of :
the selected integer * number of integers selected before the current integer (Refer example for explanation)
Help him find the maximum points he can get provided he can select every integer exactly 1 time.

Input : 
First line of input contains a single integer T denoting the number of test cases.The first line of each test case contains an integer N.The second line contains N space-separated integers denoting the array A.

Output : 
For each test case, print the required answer in a new line.

Constraints : 
1 <= T <= 100
1 <= N <= 1000
1 <= A[i] <= 1000

Example : 
Input : 
3
5
1 2 2 4 9
3
2 4 6
4
2 2 2 2
Output : 
54
16
12

Explanation : 
Case 1 : 
First he selects 1
Points : 1 * 0 (no integer selected before this)
Total Points = 0

Then he selects 2
Points : 2 * 1 (1 selected before this)
Total Points = 2

Then he selects 2
Points : 2 * 2 (1,2 selected before this)
Total Points = 6

Then he selects 4
Points : 4 * 3 (1,2,2 selected before this)
Total Points = 18

Then he selects 9
Points : 9 * 4 (1,2,2,4 selected before this)
Total Points = 54
"""
for _ in range(int(input())):
    n = int(input())
    lst = [int(x) for x in input().split()]
    lst = sorted(lst)
    sum = 0
    for i in range(1,n):
        sum += i*lst[i]
    print(sum)
        
