# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        # left is bst, right is bst, leftMax < root and rightMin > root
        self.result = 0
        self.helper(root)    
        return self.result        
        
    
    def helper(self, root):
        """
        @return maxVal: max, -sys.maxsize
        @return minVal: min, sys.maxsize
        @return size: size of subtree
        """
        if not root:
            return None, None, 0, True
        
        left = self.helper(root.left)
        right = self.helper(root.right)
                
        if left[3] == False or right[3] == False:
            return 0, 0, 1, False
        
        if left[0] and left[0] >= root.val:
            return 0, 0, 1, False
        if right[1] and right[1] <= root.val: 
            return 0, 0, 1, False
        
        size = 1
        size = size + right[2] + left[2]
        ma = right[0] or root.val
        mi = left[1] or root.val
        self.result = max(self.result, size)
        return ma, mi, size, True
