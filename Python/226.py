# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        queue = deque([root])
        result = root 
        while queue:
            root = queue.popleft()
            if root.left and root.right:
                queue.append(root.left)
                queue.append(root.right)
                root.left, root.right = root.right, root.left
            elif root.left:
                queue.append(root.left)
                root.right = root.left
                root.left = None 
            elif root.right:
                queue.append(root.right)
                root.left = root.right
                root.right = None 
        return result