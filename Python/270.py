# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return None 
        res = root.val
        node = root 
        while node:
            if node.val == target:
                return node.val
            if abs(res - target) > abs(node.val - target):
                res = node.val 
            if node.val < target:
                node = node.right
            else:
                node = node.left 
        return res 