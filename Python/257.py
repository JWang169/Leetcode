# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        paths = []
        for child in (left + right):
            paths.append(str(root.val) + "->" + child)
        if not paths:
            paths.append(str(root.val))
        return paths
