
#Merge two sorted arrays
'''
Given two sote arrays in it , if one aray has sufficient empty space at the end, the
it can be used to store the combines spacr of both the arrays in the sorted order.
A = [3,13,17,-,-,-,-,-], B = [3,7,11,19] , this can be merged as [3,3,7,11,13,17,19,-]

Write  a program for this .
Assume the first array has sufficient empty spaces.

'''
#Soln
'''
We will fill the forst array from the end, entry at m+n-1
m - valid entries in the first array .
n - valid entries in the second array
we start moving from the last valid element in both the elements and move backward.

'''
from typing import List

def merge_two_sorted_arrays(A:List[int],m:int,B:List[int],n:int)->None:
    a,b,write_index = m-1, n-1, m+n-1
    while a>=0 and b>=0:
        # In the worst case, b will be 0 and a still not yet 0
        # as we are moving backwards in a
        if A[a]>B[b]:
            A[write_index] = A[a]
            a-=1
        else:
            A[write_index]= B[b]
            b-=1
        write_index-=1
    #if still some index pending in B
    while b>=0:
        A[write_index]= B[b]
        b-=1
        write_index-=1

#Driver code
A = [3,13,17,0,0,0,0,0]
B = [3,7,11,19]
merge_two_sorted_arrays(A,3,B,4)
print(A)
#[3, 3, 7, 11, 13, 17, 19, 0]