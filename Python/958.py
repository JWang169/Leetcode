# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True 
        depthRoot, isPerfect, iscomplete = self.depth(root)
        return iscomplete
        
        
    def depth(self, root):
        if not root:
            return 0, True, True 
        depthLeft, perfectLeft, compLeft = self.depth(root.left)
        depthRight, perfectRight, compRight = self.depth(root.right)
        if perfectLeft and perfectRight and depthLeft == depthRight:
            isPerfect = True
        else:
            isPerfect = False 
        if perfectLeft and compRight and depthLeft >= depthRight and depthLeft - depthRight <= 1:
            isComplete = True
        elif perfectRight and compLeft and depthLeft - depthRight == 1:
            isComplete = True
        else:
            isComplete = False 
        return max(depthLeft, depthRight) + 1, isPerfect, isComplete
        
        
        