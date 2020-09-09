# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        nums = list()
        nodes = deque([(root, 0)])
        res = 0
        while nodes:
            node, prev = nodes.popleft()
            cur = node.val
            if not node.left and not node.right:
                res += prev * 2 + cur 
            if node.left:
                nodes.append((node.left, prev * 2 + cur))
            if node.right:
                nodes.append((node.right, prev * 2 + cur))
        return res 