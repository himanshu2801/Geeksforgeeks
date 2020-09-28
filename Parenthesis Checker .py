"""
Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

Input:
The first line of input contains an integer T denoting the number of test cases.  Each test case consists of a string of expression, in a separate line.

Output:
Print 'balanced' without quotes if the pair of parenthesis is balanced else print 'not balanced' in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ |s| ≤ 105

Example:
Input:
3
{([])}
()
([]

Output:
balanced
balanced
not balanced
"""
t=int(input())
// First Solution
"""for i in range(t):
    s=input()
    if "[)" in s or "[}" in s:
        print("not balanced")
    elif "{]" in s or "{)" in s:
        print("not balanced")
    elif "(]" in s or "(}" in s:
        print("not balanced")
    elif len(s)%2!=0:
        print("not balanced")
    else:
        print("balanced")"""
// Second Solution
for i in range(t):
    top=-1
    lst=[]
    s=input()
    for j in range(len(s)):
        if s[j]=='{' or s[j]=="[" or s[j]=="(":
            lst.append(s[j])
            top=top+1
        elif top!=-1 and (s[j]=="}" or s[j]=="]" or s[j]==")"):
            if s[j]==")" and lst[top]=="(":
                lst.pop(top)
                top=top-1
            elif s[j]=="]" and lst[top]=="[":
                lst.pop(top)
                top=top-1
            elif s[j]=="}" and lst[top]=="{":
                lst.pop(top)
                top=top-1
            else:
                print("not balanced")
                break
    if len(lst)!=0:
        print("not balanced")
    else:
        print("balanced")
    
