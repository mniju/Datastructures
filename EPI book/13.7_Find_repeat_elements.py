# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:13:04 2021
Find the element that is duplicate and missing 

In a an array one of the elemnet is present and the other is missing#

Find both the repeat element and the missing element 

eg) [2,1,3,3,4,6,0]
In this array the mising element is 5 and the dupicate is 3

We need to fnd this.

So going to the XOR operation.

1. Find XOR of the given array 

2. Find the XOR of the expected array(0- len(A))

3. step1 result XOR Step2 result gives a value - from which we get the 
least bit (kth bit) of the missing number is set  High

4. Look for the elements whose least kth bit is set in A

XOR All

5. Look for the elements whose least kth bit is set in array(0-range(len(A)))
XOR All

6. XOR the results from Step4 or step5

7.The result will be the duplicate ior missing one

8.Based on findings in step7 , find the other one.



"""

from typing import List
 
def find_repeat_elements(A:List[int])->List[int]:
    mask_data = 0
    for i,v in enumerate(A):
        mask_data ^=i^v
    # get the highst set bit from mask_data
    differ_bit = mask_data &(~(mask_data-1))
    mask_data_bit = 0
    for i,v in enumerate (A):
        if differ_bit &i:
            mask_data_bit ^=i
        if differ_bit&v:
            mask_data_bit ^=v
    
    print(f'maskdata:{mask_data}')
    if mask_data in A:
        return [mask_data_bit,mask_data^mask_data_bit]
    else:
        return [mask_data_bit^mask_data,mask_data_bit]
    
A = [2,1,3,3,4,6,0]
print(find_repeat_elements(A))
        
        

    
    
