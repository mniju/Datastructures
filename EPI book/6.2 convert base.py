# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:08:25 2020

@author: NijuMalar
"""
import functools

def convert_base(num_as_string:str,b1:int,b2:int)->str:
    def convert_from_base(num_as_int,base):
            return ('' if num_as_int==0 else \
                    convert_from_base(num_as_int//base,base)+ string.hexdigits[num_as_int % base].upper())
    is_negative = num_as_string[0]=='-'
    num_as_int =  functools.reduce(lambda runningsum,c: runningsum*b1 + string.hexdigits.index(c.lower()),num_as_string[is_negative:],0)
    return ('-' if is_negative else '')+('0'if num_as_int ==0 else convert_from_base(num_as_int,b2))

print(convert_from_base(3,2))
print(convert_base('615',7,2))