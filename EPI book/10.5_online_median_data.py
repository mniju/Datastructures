from typing import List, Iterator
import heapq,itertools,math

def compute_online_median(sequence:Iterator[int])->List[float]:
    '''
    https://www.youtube.com/watch?v=EcNbRjEcb14
    Book soln : https://github.com/adnanaziz/EPIJudge/blob/master/epi_judge_python_solutions/online_median.py
    Divide the input to two halves 
    One heap to store the 1st half and another to store 2nd half.
    We need the max val in the first Half and the min val  in the second half to 
    find the median.
    (a) use max heap for first half ( use negative elemnts to use the default min heap)
    (b) use min heap for second half

    '''
    left_max_heap = []
    right_min_heap =[]
    result =[]
    for x in sequence:
        if right_min_heap and left_max_heap:
             if x >right_min_heap[0] :
                     # Incoming new element , Find the Heap to insert .
                     # is it bigger than the starting elemnt of the right heap
                     # then it should go left
                     heapq.heappush(right_min_heap,x)
                     element_to_leftheap = heapq.heappop(right_min_heap)
                     heapq.heappush(left_max_heap,-element_to_leftheap)
             else:
                 heapq.heappush(left_max_heap,-x)
        else:
            heapq.heappush(left_max_heap,-x)
        if len(left_max_heap)>len(right_min_heap):
            max_element = -heapq.heappop(left_max_heap)
            heapq.heappush(right_min_heap,max_element)
        result.append(0.5*(-left_max_heap[0]+right_min_heap[0]) if len(right_min_heap)== len(left_max_heap) else right_min_heap[0])
    return result

#Driver code

sequence_input = iter([1,0,3,5,2,0,1])
print(compute_online_median(sequence_input))

'''
left_max_heap : []
right_min_heap: [1]
---------------------------------
left_max_heap : [0]
right_min_heap: [1]
---------------------------------
left_max_heap : [0]
right_min_heap: [1, 3]
---------------------------------
left_max_heap : [-1, 0]
right_min_heap: [3, 5]
---------------------------------
left_max_heap : [-1, 0]
right_min_heap: [2, 5, 3]
---------------------------------
left_max_heap : [-1, 0, 0]
right_min_heap: [2, 5, 3]
---------------------------------
left_max_heap : [-1, 0, 0]
right_min_heap: [1, 2, 3, 5]
---------------------------------
Output : [1, 0.5, 1, 2.0, 2, 1.5, 1]
'''

