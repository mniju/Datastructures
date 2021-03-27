'''
Write a program to test of the letters from the string 
ca n be permutes to palindrome

eg) edified can be permuted to deified
'''

'''
1. mom : Palindrome of odd length , one char has odd count.
2. rotator Palindrome of even length , all char has even count.

- So at most there can be be one char with a frequency of odd count if its chars ar palindrome
( 1 for odd length and 0 for even length str)
'''
import collections

def can_form_palindrome(s:str)->bool:
    return sum(v%2 for v in collections.Counter(s).values())<=1


#Drivercode

s = 'edified'
print(can_form_palindrome(s))