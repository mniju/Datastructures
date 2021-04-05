'''
Write a program that takes two sorted arrays , and returns a new arrray containing elements 
that are present in both the input arrays
The input may have duplicate entroes , but the the output array must be free of duplicates
eg) A = <2,3,3,5,5,6,7,7,8,12>; B = <5,5,6,8,8,9,10,10>, the output is <5,6,8>
'''
#Soln from Book #
'''
Traverse through both the arrays parallely in inreasing order (index) , at each iteration if the array elements are same
(and not added previusly ) then 
add them to the Interesection list 

else, incement the index in the array with smaller element
Time complexity O(m+n)
'''
from typing import List

def intersect_two_sorted_arrays(A:List[int],B:List[int])->List[int]:
    a_idx,b_idx , intersection_A_B = 0,0,[]
    while a_idx < len(A) and b_idx <len(B):
        if A[a_idx]==B[b_idx] and A[a_idx] !=A[a_idx-1]:
            intersection_A_B.append(A[a_idx])
            a_idx+=1
            b_idx+=1
        elif A[a_idx]<B[b_idx]:
            a_idx+=1
        else: # A[a_idx]>B[b_idx]
            b_idx+=1
    return intersection_A_B

#Driver code
A = [2,3,3,5,5,6,7,7,8,12]
B = [5,5,6,8,8,9,10,10]
print(intersect_two_sorted_arrays(A,B))
