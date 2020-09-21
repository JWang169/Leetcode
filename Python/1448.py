# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        premax = -sys.maxsize
        self.res = 0
        self.search(root, premax)
        return self.res
    
    def search(self, node, premax):
        if not node:
            return 
        if node.val >= premax:
            self.res += 1 
        premax = max(premax, node.val)
        self.search(node.left, premax)
        self.search(node.right, premax)
        
        
        