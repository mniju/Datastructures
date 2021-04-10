'''
Input  = [-4,-1],[0,2],[3,6],[7,9],[11,12],[14,17]
Added interval = [1,8]
Result = [-4,-1],[0,9],[11,12],[14,17]

'''
from typing import List
import collections

Interval = collections.namedtuple('Interval',('left','right'))
def add_interval(A:List[Interval],NewInterval:Interval)->List[Interval]:
    i =0
    result = []
    while i < len(A) and NewInterval.left > A[i].right :
        #until we find the first intersetion with new interval
        result.append(A[i])
        i+=1
    #print(f'NewIntervalright {NewInterval.right},A_left{A[i].left}')
    
    # found the first interval in range
    #now merge the new interval     
    while i<len(A) and NewInterval.right >= A[i].left:
        NewInterval = Interval(min(NewInterval.left,A[i].left),max(A[i].right,NewInterval.right)) 
        i+=1
   
    return result + [NewInterval] + A[i:]

#Driver code

i1 = Interval(-4,-1)
i2 = Interval(0,2)
i3 = Interval(3,6)
i4 = Interval(7,9)
i5 = Interval(11,12)
i6 = Interval(14,17)

NewElm = Interval(1,8)

print(add_interval ([i1,i2,i3,i4,i5,i6],NewElm))

'''
[Interval(left=-4, right=-1), Interval(left=0, right=9), Interval(left=11, right=12), 
Interval(left=14, right=17)]
'''