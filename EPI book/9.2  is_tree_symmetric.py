
class BinaryTreeNode:
 
    # Utility function to create new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_symmetric(tree:BinaryTreeNode)->bool:
    def check_symmetric(subtree_0,subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return(subtree_0.data == subtree_1.data
            and check_symmetric(subtree_0.left,subtree_1.right)
            and check_symmetric(subtree_0.right,subtree_1.left))
        return False
    return not tree or check_symmetric(tree.left,tree.right)

# Drivercode
#https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/
"""
Symmetric Tree

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

print(f' Is Binary tree symmetric:{is_symmetric(root)}')

"""
Non Symmetric Tree

    1
   / \
  2   2
   \   \
   3    3
"""
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(2)
root.left.right = BinaryTreeNode(3)
root.right.right = BinaryTreeNode(3)

print(f' Is Binary tree symmetric:{is_symmetric(root)}')