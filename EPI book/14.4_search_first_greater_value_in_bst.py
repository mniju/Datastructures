class BstNode():
    def __init__(self,data=None,left=None,right=None):
        self.data =data
        self.left = left
        self.right = right

from typing import Optional

def find_lca(tree:BstNode,s:BstNode,b:BstNode)->Optional[BstNode]:
    #Use the binary search tree property
    while s.data > tree.data or b.data <tree.data:
        while  s.data>tree.data:
            # value freater than the current node .search in the right 
            tree = tree.right
        while b.data <tree.data:
            #search in the left
            tree = tree.left
    return tree
   