from collections import deque 
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.queue = deque()
        if root:
            self.inorder(root)
    
    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        self.queue.append(root)
        if root.right:
            self.inorder(root.right)

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        while self.queue:
            return True 
    """
    @return: return next node
    """
    def next(self):
        # write your code here
        return self.queue.popleft()