'''
Write a program that  tales as input a BST and an integer k and 
returns the k largest elements in the BST in decreasing order
'''
from typing import List

class BstNode():
    def __init__(self,data=None,left=None,right=None):
        self.data =data
        self.left = left
        self.right = right


def find_k_largest_in_bst(tree:BstNode,k:int)->List[int]:
    def find_k_largest_in_bst_helper(tree):
        # perform reverse inorder traversal
        if tree and (len(k_largest_elements)<k):
            # Traverse the right side of the Tree first
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements)<k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)
    
    k_largest_elements:List[int]=[]
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements

