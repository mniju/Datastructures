# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:12:01 2021

@author: NijuMalar
"""

class ListNode:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next
        
def overlapping_no_cycle_lists(L1:[ListNode],L2:[ListNode])->[bool]:
    def list_length(L:[ListNode]):
        length=0
        while L:
            length+=1
            L=L.next
        return length
    if list_length(L1)<list_length(L2):
        L1,L2 = L2,L1
        # L1 holds the longest list
        # move first in the longest list until the remaining length of th list 
        # equals the other list
    for _ in range (list_length(L1)-list_length(L2)):
        L1=L1.next
    while L1 and L2  :
        if L1 == L2 :
            return True
        else:
            L1,L2 = L1.next,L2.next
    return False

def printList(msg, head):
 
    print(msg, end='')
    ptr = head
    while ptr:   
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print("None")
    
first = None
for i in reversed(range(1, 6)):
    first = ListNode(i, first)
 
# construct the second linked list (1 -> 2 -> 3 -> None)
second = None
for i in reversed(range(1, 4)):
    second = ListNode(i, second)
    
printList("L1: ",first)
printList("L2: ",second)

# link tail of the second list to fourth node of the first list
second.next.next.next = first.next.next.next
printList("L2-Linked: ",second)

print(overlapping_no_cycle_lists(first,second))