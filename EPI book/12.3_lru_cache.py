'''
Implement an LRU cache to store  the book prices for each ISBN

We need the folllowing additonal functionality in LRU
1. Insert : if an ISBN isalready present, insert should not update the price.But should update the 
ISBN to be the most recent entry.
2. Lookup:given an iSBN reurn the corresponding price , if the elemeny is not present, reurn -1.
if the elemeny is present , update that entry t o be the most recent used isbn
3. Erase:reove the soecified isbn and corresponding value froom the list.
return true if isbn present, otherwise return flase

'''
import collections

class LruCache:
    def __init__(self,capacity:int)->None:
        self._isbn_price_table = collections.OrderedDict[int,int]= collections.OrderedDict()
        self._caapcity = capacity
    
    def lookup(self,isbn:int)->int:
        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn) # item is present , now pop it out 
        #push item . Ordered list maintains the element entry similiar to Queue
        self._isbn_price_table[isbn]=price # this item will be moved to top of the recent acessed list

    def insert(self,isbn:int,price:int)->None:
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif self._caapcity == len(self._isbn_price_table):
            '''
            The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
            The pairs are returned in LIFO order if last is true or FIFO order if false.
            '''
            self._isbn_price_table.popitem(last =False) # Enforce FIFO order
        self._isbn_price_table[isbn] = price
    
    def erase (self,isbn:int)->bool:
        #dictionary.pop(key[, default])
        return self._isbn_price_table.pop(isbn,None) is not None
