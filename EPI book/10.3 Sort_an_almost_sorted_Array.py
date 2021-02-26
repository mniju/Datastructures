from typing import List, Iterator
import heapq
import itertools


def sort_k_sorted_list(k_sorted_list:Iterator[int],k:int)->List[int]:
    
    minheap:List[int] =[]
    #First batch of k items
    for x in itertools.islice(k_sorted_list,k):
        heapq.heappush(minheap,x)

    result = []
    for x in k_sorted_list:
        #Get the smallest value
        # push the new elemnet in heap and pop the minimal element out
        result.append(heapq.heappushpop(minheap,x))

    while minheap:
        #Get the remaining elements
        result.append(heapq.heappop(minheap))
        
    return result

#driver code
almost_sorted= [3,-1,2,6,4,5,8 ]
print(sort_k_sorted_list(iter(almost_sorted),2))




