
'''
Design an efficient algorithm that takes a sorted array 
and a key and finds the index of teh first elemnt greater than that key
'''



from typing import List

def interval_enclosing_k(A:List[int],k:int)->int:
    L =search_first_of_k(A,k)
    U= search_last_of_k(A,k)
    return [L,U]


def search_first_of_k(A:List[int],k:int)->int:
    left,right,result = 0,len(A)-1,-1
    while left <= right:
        mid = (left+right)//2
        if A[mid]>k:
            right = mid-1
        elif A[mid]==k:
            result =mid
            right = mid-1
        else:
            left = mid+1
    return result

def search_last_of_k(A:List[int],k:int)->int:
    left,right,result = 0,len(A)-1,-1
    while left <= right:
        mid = (left+right)//2
        if A[mid]>k:
            right = mid-1
        elif A[mid]==k:
            result =mid
            left = mid+1
        else:
            left = mid+1
    return result

#Driver code
'''
A = [1,2,2,4,4,4,7,11,11,13]
k = 11 ,
Return [7,8]

--
A = [1,2,2,4,4,4,7,11,11,13]
k = 4 ,
Return [3,5]
'''


A = [1,2,2,4,4,4,7,11,11,13]
print(interval_enclosing_k(A,11))
#[7, 8]
print(interval_enclosing_k(A,4))
#[3, 5]
print(interval_enclosing_k(A,44))
#[-1, -1]