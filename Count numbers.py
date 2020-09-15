"""
question...
Given a number N, count the numbers from 1 to N that don’t contain digit 3 in their decimal representation.
 

Example 1:

Input:
N = 5
Output:
4
Explanation:
From 1 - 5, only 3 contains
3 in its decimal representation
so output is 4
Example 2:

Input:
N = 25
Output:
22
Explanation:
In between 1 to 25,
3,13,23 contain 3 in their
decimal representaion so 
output is 25 - 3 = 22

Your Task:
You don't need to read input or print anything. Your task is to complete the function count() which takes an integer N as input parameter and returns an integer, the total count of numbers from 1 to N that don’t contain digit 3 in their decimal representation.
 

Expected Time Complexity: O(log N)
Expected Space Complexity: O(1)
 

Constraints:
0 <= N <= 500
"""
class Solution:
    def count (self, N):
        swap=0
        n=N
        if N>299 and N<400:
            N=299
            n=N
        if N<100:
            if N<30:
                swap=N//10
                temp=N%10
                if  temp>2:
                    swap=swap+1
                return n-swap
            elif N>29 and N<40:
                swap=N//10
                swap=swap+N%10
                return n-swap-1
            else:
                swap=9+N//10
                if N%10>2:
                    swap=swap+1
                return n-swap
        elif N>99 and N<300:
            temp=N//100
            swap=19*temp
            N=N%100
            if N<30:
                swap=swap+N//10
                if N%10>2:
                    swap=swap+1
                return n-swap
            elif N>29 and N<40:
                swap=swap+N//10 + N%10
                return n-swap-1
            else:
                swap=swap + 9 + N//10
                if N%10>2:
                    swap=swap+1
                return n-swap
        else:
            temp=N//100
            swap=19*temp
            N=N%100
            if N<30:
                swap=swap+N//10
                if N%10>2:
                    swap=swap+1
                return n-swap-81
            elif N>29 and N<40:
                swap=swap+N//10 + N%10
                return n-swap-1-81
            else:
                swap=swap + 9 + N//10
                if N%10>2:
                    swap=swap+1
                return n-swap-81
