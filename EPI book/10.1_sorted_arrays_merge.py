from typing import List
import heapq

'''
Nice video Tutorial fom BackToSWE:
 https://www.youtube.com/watch?v=ptYUCjfNhJY&list=LL&index=1
'''

def merge_sorted_arrays(sorted_arrays:List[List[int]])->List[int]:
    min_heap: List[Tuple[int,int]] = []
    # Build a an  iterator for each list within the List
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]
    '''
    1. Add the first element in each list to the Heap - Tuple(save the element and the List-(index) which it belongs)
    2. pop the smallest from the heap and add to the result list
    3 remember the list from which the elemnt we poped belongs as we need to add the 
     next elemnt  again
    4. pick the next elemnent from the list (identified in previous step ) and add to heap
    '''
    for i,list_iter in enumerate(sorted_arrays_iters):
        first_element = next(list_iter,None)
        if first_element is not None:
            # step(1)
            heapq.heappush(min_heap,(first_element,i))
    result =[]
    #steps 2 to 4
    while min_heap:
       small_element,element_in_list_index = heapq.heappop(min_heap)
       result.append(small_element)
       next_element_in_list = next(sorted_arrays_iters[element_in_list_index],None)
       if next_element_in_list is not None:
           heapq.heappush(min_heap,(next_element_in_list,element_in_list_index))
    return result

        

#Driver Code

sortedArrays = [[3,5,7],[0,6],[0,6,28],[0,0,3,5,6,6,7,28]]
print(merge_sorted_arrays(sortedArrays))
#output : [0, 0, 0, 0, 3, 3, 5, 5, 6, 6, 6, 6, 7, 7, 28, 28]
