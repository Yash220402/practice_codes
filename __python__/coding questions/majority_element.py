"""
MAJORITY ELEMENT

Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example :
Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
"""

# @param A : tuple of integers
# @return an integer
import math

def majorityElement(A):
    d = {}
    for i in range(len(A)):
        if A[i] not in d:
            d[A[i]] = 1
        else:
            d[A[i]] += 1
    return sorted(d, """function to sort according to values""")

if __name__ == "__main__":
    A = [2, 1, 2]
    print(majorityElement(A))