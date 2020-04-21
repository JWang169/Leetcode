# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None 
        
        val = preorder[0]
        root = TreeNode(val)
        idx = 1 
        while idx < len(preorder) and preorder[idx] < val:
            idx += 1 
        root.left = self.bstFromPreorder(preorder[1: idx])
        root.right = self.bstFromPreorder(preorder[idx: ])
        return root 
        
        
        