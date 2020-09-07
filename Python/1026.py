# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root, root.val, root.val)
        
    def dfs(self, root, ma, mi):
        if not root:
            return ma - mi
        ma = max(root.val, ma)
        mi = min(root.val, mi)
        return max(self.dfs(root.left, ma, mi), self.dfs(root.right, ma, mi))