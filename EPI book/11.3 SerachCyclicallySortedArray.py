# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:43:35 2021

Search a cyclically sorted Array

eg) [378,478,550,631,103,203,220,234,279,368]


"""

from typing import List

def search_smallest(A:List[int])->int:
    left,right = 0,len(A)-1
    while left < right:
        mid = (left+right)//2
        if A[mid]<A[right]:
            right = mid
        else:
            left = mid+1
    return left

A=[378,478,550,631,103,203,220,234,279,368]
print(f'Smallest value in A: {A[search_smallest(A)]}')
#Smallest value in A: 103