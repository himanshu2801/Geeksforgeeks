"""
Given two binary strings that represent value of two integers, find the product of two strings. For example, if the first bit string is “1100” and second bit string is “1010”, output should be 120.

Input:
First line consists of T test cases. Only line of every test case consists of 2 binary strings.

Output:
Single line output, print the multiplied value.

Constraints:
1<=T<=100
1<=Length of string<=100

Example:
Input:
2
1100 01
01 01
Output:
12
1
"""
t=int(input())
for i in range(t):
    s1,s2=input().split()
    i,j=0,0
    temp=len(s1)-1
    temp2=len(s2)-1
    x,y=0,0
    while i<len(s1):
        if s1[i]=="1":
            x=x+2**temp
        temp=temp-1
        i=i+1
    while j<len(s2):
        if s2[j]=="1":
            y=y+2**temp2
        j=j+1
        temp2=temp2-1
    print(x*y)
