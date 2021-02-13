#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

code from the EPI book
"""
import collections
class BinaryTreeNode:
    # Utility function to create new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#solution
def is_balanced_binary_tree(tree:BinaryTreeNode)-> bool:
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight',('balanced','height'))                                                    
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(balanced=True,height=-1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return left_result
        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return right_result
        is_balanced = abs(left_result.height - right_result.height) <=1
        height = max(left_result.height,right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced,height)
    return check_balanced(tree).balanced
    
"""
Balanced Tree

     1
   /   \
  2     2
 / \   / \
3   4 4   3

"""

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(2)
root.left.left = BinaryTreeNode(3)
root.left.right = BinaryTreeNode(4)
root.right.left = BinaryTreeNode(4)
root.right.right = BinaryTreeNode(3)

print(f' Is Binary tree HeightBalanced:{is_balanced_binary_tree(root)}')                                                               
                                                                                 
"""
Unbalanced Tree

        1
      /   \
     2     2
    / \   
   3   4 
  / \
 7   8

"""
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(2)
root.left.left = BinaryTreeNode(3)
root.right.left = BinaryTreeNode(4)
root.left.left.left = BinaryTreeNode(7)
root.left.left.right = BinaryTreeNode(8)

print(f' Is Binary tree HeightBalanced:{is_balanced_binary_tree(root)}')  