"""
An array A containing heights of building was given. Its a rainy season. Calculate the amount of water collected between all the buildings.

 

Histograms with no space in between
Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, N is the number of buildings. The second line of each test case contains N input H[i],height of buildings.

Output:
Print the amount of water collected between all the buildings.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 103
1 ≤ H[i] ≤ 103

Example:
Input:
1
6
1 5 3 7 4 2

Output:
2

Explanation:
Testcase 1: Water are trapped by block at index 2 (0-based indexing) only and can trap 2 units of water.
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

for _ in range(int(input())):
    n = int(input())
    lst = [int(x) for x in input().split()]
    print(trappingWater(lst, n))

