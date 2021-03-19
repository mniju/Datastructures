# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:57:03 2021


"""

def square_root(k:int)->int:
    left , right = 0,k
    while left <=right:
        mid = (left+right)//2
        mid_square = mid*mid
        if mid_square <=k:
            left = mid+1
        else:
            right = mid-1
        print(f'Interval [{left},{right}]')
    return left-1


x = 101
print(f'Square root of {x} is {square_root(x)}')

'''
x =99

Interval [0,48]
Interval [0,23]
Interval [0,10]
Interval [6,10]
Interval [9,10]
Interval [10,10]
Square root of 99 is 9

x = 101
Interval [0,49]
Interval [0,23]
Interval [0,10]
Interval [6,10]
Interval [9,10]
Interval [10,10]
Interval [11,10]
Square root of 101 is 10
''' 