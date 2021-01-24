# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:56:12 2020

@author: NijuMalar
"""

def binary_addition(Bs: str,Bt:str)->str:
    max_len = max(len(Bs),len(Bt))
    Bs = Bs.zfill(max_len)
    Bt = Bt.zfill(max_len)
    carry =0
    addition= []

    
    for i in reversed(range(0,max_len)):
        result  = (int(Bs[i]) + int(Bt[i]) + carry) %2 
        carry = (int(Bs[i]) + int(Bt[i]) + carry) // 2 
        addition.append(str(result))
    # Add the final carry over 
    if carry:
        addition.append(str(carry))
    return ''.join(addition [::-1])
 
b1 ="10"
b2 = "1001"
print(binary_addition(b1,b2))

