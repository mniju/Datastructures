# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:32:55 2021

@author: NijuMalar
"""

def evaluate(expression:str)->int:
    stack_results :list[int] = []
    delimiter = ','
    operators = {'+':lambda y,x: x+y,'-':lambda y,x: x-y,
                 '*':lambda y,x: x*y,'/':lambda y,x : x//y}
    
    for token in expression.split(delimiter):
        if token in operators:
            stack_results.append(
                    operators[token](stack_results.pop(),stack_results.pop()))
        else:
            stack_results.append(int(token))
    return stack_results[-1]
            

print(evaluate("4,13,5,/,+"))
