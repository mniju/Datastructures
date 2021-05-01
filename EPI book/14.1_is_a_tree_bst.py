from collections import deque
from collections import namedtuple
class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key  = key 
        self.left = left 
        self.right = right
    
def check_bst(tree:Node)->bool:
    Nodes_with_limits = collections.namedtuple('Nodes_with_limits',('node','lowerlimit','higherlimit'))
    Queue_with_Nodes = collections.deque([Nodes_with_limits(tree,float('-inf'),float('inf'))])
    
    while Queue_with_Nodes:
        subtree = Queue_with_Nodes.popleft()
        if subtree.lowerlimit<=subtree.node.data<=subtree.higherlimit:
            Queue_with_Nodes.extend(subtree.node.left,subtree.lowerlimit,subtree.node.data)
            Queue_with_Nodes.extend(subtree.node.right,subtree.node.data,subtree.higherlimit)
        else:
            return False
    return True