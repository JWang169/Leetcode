"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys 
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        if not root:
            return 0
        self.minSum = sys.maxsize
        self.result = root
        self.helper(root)
        return self.result
        
        
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        curSum = left + right + root.val 
        if curSum < self.minSum:
            self.result = root
            self.minSum = curSum
        return curSum