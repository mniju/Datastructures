# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:01:13 2021

@author: NijuMalar
"""

class Queue:
    
    SCALE_FACTOR =2 
    
    def __init__(self,capacity:int)->None:
        self._entries =[0]*capacity
        self._head = self._tail = self._num_queue_elements=0
        
    def enqueue(self,x:int)->None:
        if self._num_queue_elements == len(self._entries):
            # Needs resize
            self._entries = self._entries[self._head:] + self._entries[:self._head]
            self._entries += [0] * (Queue.SCALE_FACTOR*len(self._entries)-len(self._entries))
            self._head,self._tail = 0,self. 
            
        self._entries[self._tail] = x
        self._tail = (self._tail +1) % len(self._entries)
        self._num_queue_elements +=1
        
    def dequeue(self)->int:
        x = self._entries[self._head]
        self._num_queue_elements -=1
        self._head = (self._head +1) % len(self._entries)
        return x
    

TestQ = Queue(10)
for i in range(0,20):
    TestQ.enqueue(i)

for _ in range(20):
    print(TestQ.dequeue())


    