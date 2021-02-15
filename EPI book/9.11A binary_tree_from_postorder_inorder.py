# solution from Book

from typing import List

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

#build the subtree
# Hint the last elemnt is the root
def binary_tree_from_preorder_inorder(postorder:List[int],inorder:List[int])->BinaryTreeNode:
    #Hash table for the sequence from inorder
    node_to_inorder_idx = {data:i for i,data in enumerate(inorder)}
    def binary_tree_from_postorder_inorder_helper(postorder_start,postorder_end,inorder_start,inorder_end):
        if postorder_end <= postorder_start or inorder_end <= inorder_start:
            return None
        inorder_root_index = node_to_inorder_idx[postorder[postorder_end-1]]
        left_subtree_size = inorder_root_index- inorder_start
        return BinaryTreeNode(
            postorder[postorder_end-1],

            binary_tree_from_postorder_inorder_helper(
                postorder_start,postorder_start+left_subtree_size,
                inorder_start,inorder_root_index),

            binary_tree_from_postorder_inorder_helper(
                postorder_start+left_subtree_size,postorder_end-1,
                inorder_root_index+1,inorder_end))

    return  binary_tree_from_postorder_inorder_helper(postorder_start=0,
                                                     postorder_end=len(postorder),
                                                     inorder_start =0,
                                                     inorder_end= len(inorder))  
        

#Driver Code and Helper Functions
#https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
def prInorder(node):
 
    if (node == None):
        return
         
    prInorder(node.left)
    print(node.data, end = " ")
    prInorder(node.right)

def prPostorder(node):
 
    if (node == None):
        return
         
    prInorder(node.left)
    prInorder(node.right)
    print(node.data, end = " ")
    

'''
Book Figure 9.5

     H
   /   \
  B     C
 / \   / \
F   E     D
   / \   / \
  A         G
 / \       / \
          I
          
'''


inorder = [ 'F','B','A','E','H','C','D','I','G'] 
preorder = ['H','B','F','E','A','C','D','G','I']
postorder = ['F','B','A','E','C','D','I','G','H']

constructed_tree = binary_tree_from_preorder_inorder(postorder,inorder)
prPostorder(constructed_tree)