# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        1. find the last node of left
        2. save the right node
        3. lastLeft.right = root.right
        4. root.right = root.left
        5. root.left = None
        """
        if not root:
            return None
        lastLeft = self.flatten(root.left)
        lastRight = self.flatten(root.right)
        if lastLeft:
            lastLeft.right = root.right 
            root.right = root.left
            root.left = None 
        return lastRight or lastLeft or root
    

