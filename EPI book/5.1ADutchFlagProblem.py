#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 18:33:14 2020


Dutch flag variant.
Assuming the keys take one of the three key values,
re order the array so that the objects with same key appear together.
"""
from typing import List

def reorder(A: List[int]) -> None:
    # three key values .The enumerated vales are 0,1,2
    # Can consider the pivot as 1

    key_zero,key_one,key_two =0,0,len(A)-1
    pivot_value = 1 # Lets keep the middle one as pivot
    while key_one < key_two:
        # Just to make sure we are done with elower and middlepythin 
        if A[key_one] < pivot_value:
            A[key_zero],A[key_one] = A[key_one],A[key_zero]
            key_zero ,key_one = key_zero+1,key_one+1
            
        elif A[key_one] == pivot_value:
            key_one += 1 
        else:
            
            A[key_two],A[key_one] = A[key_one],A[key_two]
            key_two -= 1
            

A = [2,1,1,0,2,0,1,2,2,0,1]
reorder(A)
print(A)
#[0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]



def booleanreorder(A: List[bool])-> None:
    false_index, true_index= 0,len(A)-1
    while false_index<true_index:
        if A[false_index]==False:
            false_index+=1
        else: 
            A[false_index],A[true_index] = A[true_index],A[false_index]
            true_index-=1
         
Z = [True,False,True,True,False,True]
booleanreorder(Z)
print(Z)
#[False, False, True, True, True, True]


def fourkeyvaluesreorder(A: List[int])->None:
    key_zero,key_one,key_two,key_three =0,0,len(A)-1,len(A)-1
    #First do a 3 way reorder. This will order the first two
    # leaving the last one to be ordered again.
    pivot_value = 1 # Lets keep the middle one as pivot
    while key_one < key_two:
        # Just to make sure we are done with elower and middle
        if A[key_one] < pivot_value:
            A[key_zero],A[key_one] = A[key_one],A[key_zero]
            key_zero ,key_one = key_zero+1,key_one+1
            
        elif A[key_one] == pivot_value:
            key_one += 1 
        else:
            
            A[key_two],A[key_one] = A[key_one],A[key_two]
            key_two -= 1
            #print('keytwo:',key_two)

    # The last two (2 and 3)are together , 
    #run again to reorder them (similiar to boolean reorder)
    smaller = 2
    while key_two<key_three:
        if A[key_two]== smaller:
            key_two+=1
        else:
            A[key_two],A[key_three]= A[key_three],A[key_two]
            key_three-=1
            

B = [0,1,2,3,3,2,0,3,2,1,3,0,1,0,3]     
fourkeyvaluesreorder(B)
print(B)
#[0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3]

