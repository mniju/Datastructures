# -*- coding: utf-8 -*-
"""
Design an algorithm to find the kth largest element in an array

eg) if A = [3,2,1,5,4]
A[3] =5 is the first largest element (k=1)
A[0] is the third largest element (k=3)
--
The input array may have duplicates too 
eg) A = [3,2,5,3,5]
"""
from typing import List
import random
import operator

def find_kth_largest(k:int,A:List[int])->int:
    
    def find_kth(comp):
    
        def partition_around_pivot(left,right,pivot_index):
            pivot_value = A[pivot_index]
            new_pivot_index = left
            A[pivot_index],A[right] = A[right],A[pivot_index]
            print(A)
            for i in range(left,right):
                if comp(A[i],pivot_value):
                    #Move the lesser elemnts to the left
                    A[i],A[new_pivot_index] = A[new_pivot_index],A[i]
                    new_pivot_index +=1
            A[right],A[new_pivot_index] = A[new_pivot_index],A[right]
            return new_pivot_index
            
        left , right = 0, len(A)-1
        
        while left<=right:
            pivot_index = random.randint(left,right)
            print(pivot_index)
            new_pivot_index = partition_around_pivot(left,right,pivot_index)
            if new_pivot_index == k-1:
                return A[new_pivot_index]
            elif new_pivot_index < k-1:
                left = new_pivot_index+1
            else:
                right = new_pivot_index - 1
                
    return find_kth(operator.gt)
            
            
 #Drivercode#
A = [3,2,1,5,0]
k = 2 # 3rd largest element

print(f'The kth largest element is {find_kth_largest(k,A)}' )        