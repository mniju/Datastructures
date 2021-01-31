# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:22:10 2020

@author: NijuMalar
"""

def is_palindrome(s:str)-> bool:
    return all (s[i]==s[~i] for i in range(len(s)//2))

print(is_palindrome("madam"))