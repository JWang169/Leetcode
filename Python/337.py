# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        res0, res1 = self.dfs(root)
        return max(res0, res1)
        
    def dfs(self, root):
        # return two results:
        # 1. do not rob current root
        # 2. rob current root
        if not root:
            return 0, 0
        
        l0, l1 = self.dfs(root.left)
        r0, r1 = self.dfs(root.right)
        res0 = max(l0, l1) + max(r0, r1)
        res1 = l0 + r0 + root.val
        return res0, res1
        