# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.isValid = True
        self.helper(root)
        return self.isValid
        
        
    def helper(self, root):
        if not root:
            # min child, max child
            return None, None
        
        lmin, lmax = self.helper(root.left)
        rmin, rmax = self.helper(root.right)
        if lmax and root.val <= lmax:
            self.isValid = False
            return None, None 
        if rmin and root.val >= rmin:
            self.isValid = False
            return None, None
        
        mi = lmin if lmin else root.val 
        ma = rmax if rmax else root.val 
        return mi, ma