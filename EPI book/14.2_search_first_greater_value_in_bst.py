class BstNode():
    def __init__(self,data=None,left=None,right=None):
        self.data =data
        self.left = left
        self.right = right

from typing import Optional

def find_first_greater_than_k(tree:BstNode,k:int)->Optional[BstNode]:
    subtree, first_subtree_so_far = tree ,None
    while subtree:
        if subtree.data >k:
            first_subtree_so_far,subtree = subtree,subtree.left
        else:
            subtree = subtree.right
    return first_subtree_so_far

