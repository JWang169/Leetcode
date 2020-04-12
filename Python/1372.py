# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.result = 0
        
        left = self.helper(root.left, True)
        right = self.helper(root.right, False)
        return max(self.result, max(left, right))
    
    
    def helper(self, node, left):
        if not node:
            return 0
        l = self.helper(node.left, True)
        r = self.helper(node.right, False)
        self.result = max(self.result, max(l, r))
        
        if left:
            return 1 + r
        else:
            return 1 + l
            
        