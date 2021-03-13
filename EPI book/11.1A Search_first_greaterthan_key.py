
'''
Design an efficient algorithm that takes a sorted array 
and a key and finds the index of teh first elemnt greater than that key
'''



from typing import List

def search_first_of_greaterthan_k(A:List[int],k:int)->int:
    left,right = 0,len(A)-1
    while left <= right:
        mid = (left+right)//2
        if A[mid]>k:
            right = mid-1
            if A[mid-1]<k:
                # The A[mid-1] is less than k
                #Also,we know value at A[mid] is greater than k 
                #so we return m
                return mid
        elif A[mid]==k:
            if A[mid+1]>A[mid]:
                return mid+1 
            left = mid+1
        else:
            left = mid+1
    return 0

#Driver code
'''
A = [-14,-10,2,108,108,243,285,285,285,401]
k = 285 ,
Return 9

--
A = [-14,-10,2,108,108,243,285,285,285,401]
k = -13 ,
Return 1
'''


A = [-14,-10,2,108,108,243,285,285,285,401]
print(search_first_of_greaterthan_k(A,285))
#9
print(search_first_of_greaterthan_k(A,-13))
#1