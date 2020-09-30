"""
Now, as you're familiar with operating on arrays, let's do an intricate task. Here, we'll do swapping of array elements.

Given an array A of N positive integers. The task is to swap every ith element of the array with (i+2)th element.

Note: When passing array to function, we basically pass the reference to the array. More details here. We'll learn more about pointers and references in the next module.

Input:
First line of input contains number of testcase T. For each testcase, there will be two lines, first of which contains size of array N and next line contains N space seperated positive integers.

Output:
For each testcase, print the modified array.

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= Ai <= 106

User Task:
Your task is to complete the function swapElements(), which should swap each ith element with (i+2)th element. No need to print or return the array.

Example:
Input:
1
5
1 2 3 4 5

Output:
3 4 5 2 1

Explanation:
Testcase 1: Swapping 1 and 3, makes the array 3 2 1 4 5. Now, swapping 2 and 4, makes the array 3 4 1 2 5. Again, swapping 1 and 5, makes the array 3 4 5 2 1.
"""
void swapElements(int arr[], int sizeof_array){
    for(int i=0;i<sizeof_array-2;i++){
        int swap=arr[i+2];
        arr[i+2]=arr[i];
        arr[i]=swap;
    }
    
}
