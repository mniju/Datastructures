from collections import deque
class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key  = key 
        self.left = left 
        self.right = right

def levelOrderTraversal(root:Node):
    queue = deque()
    queue.append(root)

    while queue:
        currentNode= queue.popleft()
        print(f'{currentNode.key}')
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

#Driver Code
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)

levelOrderTraversal(root)
    



