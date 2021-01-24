#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:00:56 2020

@author: niju
"""
from typing import List

def buysellstock(A: List[float]) -> float:
    minbuyprice = A[0] # inf also works
    profit = -10000 # zero also works
    for price in A:
        if price < minbuyprice:
            minbuyprice = price
        profit_today = price - minbuyprice
        if profit_today > profit:
            profit = profit_today
    return profit
                
A = [310,315,275,295,260,270,290,230,255,250]
print(buysellstock(A))

# BOOK example
def buy_and_sell_stock_once(prices:List[float])->float:
    min_price_so_far,max_profit = float('inf'),0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        min_price_so_far = min(price,min_price_so_far)
        max_profit = max(max_profit_sell_today,max_profit)
    return max_profit

A = [310,315,275,295,260,270,290,230,255,250]
print(buy_and_sell_stock_once(A))

#Write a program that takes an array of integers and finds the length 
#of longest subarray whose entries are equal

def length_longest_subarray(A: List [int])->int:
   subarray_element,max_subarray_length,subarray_length = float('inf'),0,0
   print(A)
   for element in A:
       if element == subarray_element:
           subarray_length+=1
       else:
           subarray_element = element
           subarray_length =1
       max_subarray_length = max(subarray_length,max_subarray_length)
       '''
       print('-----------------------')
       print('loop Element:',element)
       print('current Element:',subarray_element)
       print('current count:',subarray_length)
       print('-----------------------')
       '''
   return max_subarray_length

Z = [2,2,3,3,3,3,3,3,4,5,5,6,6,7,9,9,9,9,0]
print(length_longest_subarray(Z))