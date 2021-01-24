# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:39:13 2020

@author: NijuMalar
"""

def int_to_string(x:int)-> str:
    int_to_string,negative_num =[],False
    if x<0:
        x,negative_num = -x,True
    while True:
        int_to_string.append(chr(ord('0')+ x % 10))
        x //=10# Goto the next decimal place
        #print(int_to_string)
        if x ==0:
            break
    return ('-' if negative_num else '')+''.join(reversed(int_to_string))


import functools
def string_to_int(s:str)->int:
    
    return (-1 if s[0]== '-' else 1)*\
    functools.reduce(lambda running_sum,c:running_sum*10+string.digits.index(c),s[s[0]in '+-':],0)
    
print(string_to_int(int_to_string(401)))