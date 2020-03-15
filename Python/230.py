# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.result = None 
        self.inorder(root, k)
        return self.result 
        
        
    def inorder(self, root, k):
        if not root:
            return 
        self.inorder(root.left, k)
        self.count += 1 
        if self.count == k:
            self.result = root.val
            return 
        self.inorder(root.right, k)