class BstNode():
    def __init__(self,data=None,left=None,right=None):
        self.data =data
        self.left = left
        self.right = right

from typing import Optional
from typing import List

def build_min_height_bst_from_sorted_array(A:List[int])->Optional[BstNode]:
    def build_min_height_bst_from_sorted_subarry(start, end):
        if start>=end:
            return None
        mid = (start+end)//2
        return BstNode(A[mid],
        build_min_height_bst_from_sorted_subarry(start,mid),
        build_min_height_bst_from_sorted_subarry(mid+1,end))
    return build_min_height_bst_from_sorted_subarry(0,len(A))